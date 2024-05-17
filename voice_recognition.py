import whisper
import numpy as np

class Recognizer:
    def __init__(self):
        self.model = whisper.load_model("base")

    def transcribe(self, audio_data):
        audio = whisper.load_audio(audio_data)
        audio = whisper.pad_or_trim(audio)
        mel = whisper.log_mel_spectrogram(audio).to(self.model.device)
        
        _, probs = self.model.detect_language(mel)
        language = max(probs, key=probs.get)
        print(f"Detected language: {language}")

        options = whisper.DecodingOptions()
        result = whisper.decode(self.model, mel, options)
        return result.text
