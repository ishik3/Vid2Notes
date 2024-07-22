import requests
import Functions.Transcription, Functions.NotesMaker, Functions.youtube_to_mp3, Functions.ImageScrapper, Functions.QuizGenerator
from fastapi import FastAPI
from fastapi.params import Body
import json
from fastapi.params import Body
import uvicorn
from fastapi.params import Body
import json
import re
import os
from dotenv import find_dotenv, load_dotenv 

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

gpt_k = os.getenv("gpt_k")
gemini_k = os.getenv("gemini_k")

app = FastAPI()

@app.post("/vid2notes/notes_generator")
def vid2notes(payload : dict = Body(...)):

    ytlink = payload["url"]

    title = Functions.youtube_to_mp3.youtube_mp3(ytlink)
    video_path = title
    video_file = open(video_path, "rb")

    transcript = Functions.Transcription.whisper(gpt_k, video_file)
    cleanNotes = Functions.NotesMaker.gemini(gemini_k, transcript)
    cleanNotes = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', cleanNotes)
    print("cleanNotes after removing control characters:", cleanNotes) 
    # thumbnail_url = f"http://img.youtube.com/vi/{ytlink[17:]}/2.jpg"
    thumbnail_url = Functions.ImageScrapper.image_scrapper(title)

    cleanNotes = json.loads(cleanNotes)
    cleanNotes["thumbnail_url"] = thumbnail_url
    return cleanNotes



@app.post("/vid2notes/quiz_generator/")
def quiz_generator(payload : dict = Body(...)):
    quiz = Functions.QuizGenerator.quiz_generator(gemini_k, payload["title"], payload["content"])
    print(quiz)
    quiz_json = json.loads(quiz)
    
    return quiz_json


if __name__ == "__main__" :
    app.run(debug=True)