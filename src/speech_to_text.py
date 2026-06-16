import whisper
import shutil
import os

def audio_to_text(audio_path):

    print("Audio Exists:", os.path.exists(audio_path))
    print("FFmpeg Path:", shutil.which("ffmpeg"))

    if shutil.which("ffmpeg") is None:
        raise Exception(
            "FFmpeg is not installed or not added to PATH"
        )

    model = whisper.load_model("base")

    result = model.transcribe(audio_path)

    return result["text"]