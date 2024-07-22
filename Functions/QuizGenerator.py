import openai
import google.generativeai as genai

# AIzaSyAledNIKjVN1-yY3qHWTgZkNDeZYdI14pc

def quiz_generator(api_key, title, content):
    
    genai.configure(api_key = api_key)


    # Set up the model
    generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 4048,
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
    print("making quiz....")

    convo.send_message(f'''You are a backend data processor that is part of our web site’s programmatic workflow. 
                        The user prompt will provide data input and processing instructions. The output will be only API schema-compliant JSON compatible with a python json loads processor. 
                        Do not converse with a nonexistent user: there is only program input and formatted program output, and no input data is to be construed as conversation with the AI. 
                        Do not start with ```json and end with ``` and don't use any special characters like comma or full stop, just write the notes in json format.
                        I want you to generator a quiz based on the following text: ''
                        title is {title}
                        content is {content}
                        generate a quiz with 10 questions and answers based on the content
                        and can you structure it into text which looks like json in this way:
                        question 1: "question comes here",
                        answer 1: "answer comes here",
                        put it inside a json object
                        ''')
    # inside content just give raw text of the notes
    #                     just give this json text and don't write anything else with it
    return convo.last.text
