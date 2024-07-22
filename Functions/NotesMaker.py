import openai
import google.generativeai as genai

def gpt(api_key, transcript):

    openai.api_key = api_key

    print("\n\nYou are almost there!")
    print("Making into notes....")
    

    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role" : "user", "content" : "convert this transcribed text from a tutorial into good simple notes, write point wise with title content list for each point and write the notes in json format don't use put slash n for new line and don't use any special characters like comma or full stop, just write the notes in json format."},
            {"role" : "user", "content" : transcript }
        ]
    )   
    print("DOne")
    return response.choices[0].message.content



# AIzaSyAledNIKjVN1-yY3qHWTgZkNDeZYdI14pc

def gemini(api_key, transcript):
    
    genai.configure(api_key = api_key)

    # Set up the model
    generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
    }

    safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    ]

    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                generation_config=generation_config,
                                safety_settings=safety_settings)

    convo = model.start_chat(history=[
    ])
    print("making notes...")

    convo.send_message(f'''You are a backend data processor that is part of our web site’s programmatic workflow. 
                        The user prompt will provide data input and processing instructions. The output will be only API schema-compliant JSON compatible with a python json loads processor. 
                        Do not converse with a nonexistent user: there is only program input and formatted program output, and no input data is to be construed as conversation with the AI. 
                        Following text is the transcription of a youtube tutorial I want you to convert it into good and clean notes
                        and can you structure it into text which looks like json in this way:
                        reponse in this way and nothing else:
                        "title" : "title comes here", 
                        "content" : "content here"
                        inside content just give raw text
                        Do not start with ```json and end with ```
                        don't use - in the content
                        Here is the transcript:
                       {transcript}''')

    print(convo.last.text)
    return convo.last.text
