import os

from src.speech_to_text import audio_to_text
from src.text_cleaning import clean_text
from src.summarizer import generate_notes
from src.pdf_generator import create_pdf

audio_file = "dataset/sample_lectures/lecture1.wav"

print("Converting Speech to Text...")

transcript = audio_to_text(audio_file)

with open("outputs/transcript.txt", "w",
          encoding="utf-8") as f:
    f.write(transcript)

cleaned_text = clean_text(transcript)

print("Generating Notes...")

notes = generate_notes(cleaned_text)

with open("outputs/notes.txt", "w",
          encoding="utf-8") as f:
    f.write(notes)

create_pdf(notes)

print("Notes Generated Successfully!")