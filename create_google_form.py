from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import json
def create_google_form(full_text):
    #google forms API , getting the link
    SCOPES = ['https://www.googleapis.com/auth/forms.body']

    # Load client secrets
    with open('client_secrets.json') as secrets_file:
        secrets = json.load(secrets_file)

    # Create credentials flow
    flow = InstalledAppFlow.from_client_config(
        secrets,
        scopes=SCOPES
    )

    # Authenticate and authorize access
    credentials = flow.run_local_server(port=0)

    # Check if token file already exists
    token_path = 'token.json'
    if not credentials.valid:
        if credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_config(
                secrets,
                scopes=SCOPES
            )
            credentials = flow.run_local_server(port=0)

        # Save credentials to token file
        with open(token_path, 'w') as token_file:
            token_file.write(credentials.to_json())

    # Build Google Forms service
    service = build('forms', 'v1', credentials=credentials)

    # Request body for creating a form
    NEW_FORM = {
        "info": {
            "title": "Machine learning QUIZ",
        }
    }


    # Create the form
    response = service.forms().create(body=NEW_FORM).execute()

    # Get the form ID
    form_id = response["formId"]

    # Create a list to store question requests
    question_requests = []

    questions_text = []
    answer_options_dict = {}

    question_lines = full_text.strip().split('\n\n')
    for lines in question_lines:
        lines = lines.strip().split('\n')
        question = lines[0].lstrip('Q:').strip()
        answer_options = [option.strip() for option in lines[1:] if option.strip()]
        questions_text.append(question)
        answer_options_dict[question] = answer_options


    # Create the questions in the form
    for question, answer_options in answer_options_dict.items():
        question_body = {
            "createItem": {
                "item": {
                    "title": question,
                    "questionItem": {
                        "question": {
                            "required": True,
                            "choiceQuestion": {
                                "type": "RADIO",
                                "options": [{"value": option} for option in answer_options],
                                "shuffle": True
                            }
                        }
                    },
                },
                "location": {
                    "index": 0
                }
            }
        }
        question_requests.append(question_body)



    # Add the questions to the form
    request_body = {"requests": question_requests}
    question_setting = service.forms().batchUpdate(formId=form_id, body=request_body).execute()

    # Construct the form URL
    form_url = f"https://docs.google.com/forms/d/{form_id}/viewform"
    return form_url