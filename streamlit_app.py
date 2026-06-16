import streamlit as st
import tempfile
import os

from src.speech_to_text import audio_to_text
from src.summarizer import generate_notes

st.set_page_config(
    page_title="Lecture Voice To Notes Generator",
    layout="wide"
)

st.title("🎤 Lecture Voice To Notes Generator")

uploaded_file = st.file_uploader(
    "Upload Lecture Audio",
    type=["wav", "mp3", "m4a"]
)

if uploaded_file is not None:

    st.success("Audio uploaded successfully!")

    # Save uploaded audio temporarily
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=os.path.splitext(uploaded_file.name)[1]
    ) as tmp_file:

        tmp_file.write(uploaded_file.read())
        temp_audio_path = tmp_file.name

    st.write("Temporary File:")
    st.code(temp_audio_path)

    if st.button("Generate Notes"):

        with st.spinner("Converting Speech To Text..."):

            transcript = audio_to_text(temp_audio_path)

        st.subheader("Transcript")

        st.text_area(
            "Transcript",
            transcript,
            height=250
        )

        with st.spinner("Generating Notes..."):

            notes = generate_notes(transcript)

        st.subheader("Generated Notes")

        st.text_area(
            "Notes",
            notes,
            height=250
        )

        os.remove(temp_audio_path)