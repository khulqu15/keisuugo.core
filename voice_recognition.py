import whisper
import numpy as np

class Recognizer:
    def __init__(self):
        self.model = whisper.load_model("base")

    def transcribe(self, audio_data):
        return self.model.transcribe(audio_data, fp16=False)
