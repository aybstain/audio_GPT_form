#Audio ChatGPT to Quiz Form
This project aims to generate a Google form quiz from an audio prompt using the ChatGPT model. The application utilizes the Google Forms API, speech recognition library, and web/mobile development technologies.

#Project Overview
The main functionalities of the project include:

Creating a Google Form: The create_google_form(full_text) function uses the Google Forms API to create a new form. It authenticates the user, retrieves necessary credentials, and builds the Google Forms service. The function takes the full_text parameter, which represents the full text obtained from the ChatGPT response, and creates questions and answer options based on the text. The form URL is returned upon successful creation.

Generating ChatGPT Response: The generate_gpt_response(text) function utilizes the OpenAI ChatGPT API to generate a response based on the given text. It combines the text with a predefined instruction and sends the prompt to the ChatGPT model. The response obtained contains the complete text for the form.

Speech Recognition: The speech_recognition() function uses the speech recognition library to record audio from the microphone. It adjusts the ambient noise level, records the audio until there are 3 seconds of silence or a phrase is detected, and attempts to recognize the speech using the Google Speech Recognition API.

Streamlit Application: The main() function implements a Streamlit application. It provides a user interface to initiate the recording process and display the generated form URL. The one_for_all_V3() function is called to record the audio, generate the ChatGPT response, create the Google Form, and return the recognized speech and the form URL.
