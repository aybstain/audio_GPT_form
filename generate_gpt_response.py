import openai
def generate_gpt_response(text):
    openai.api_key = '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'
    instruction = "in this form Q: A) B) C) D)"
    prompt = f"{text}{instruction}"
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    
    full_text = response["choices"][0]["text"]
    print("Finished generating full_text")
    return full_text

