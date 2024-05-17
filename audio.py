import whisper
from pydub import AudioSegment
from pydub.playback import play

model = whisper.load_model("base")
audio = whisper.load_audio("audio.mp3")
audio = whisper.pad_or_trim(audio)
mel = whisper.log_mel_spectrogram(audio).to(model.device)
audio_segment = AudioSegment.from_file("audio.mp3", format="mp3")

_, probs = model.detect_language(mel)
print(f"Bahasa Terdeteksi: {max(probs, key=probs.get)}")

play(audio_segment)
options = whisper.DecodingOptions()
result = whisper.decode(model, mel, options)

print(f"Seorang perempuan mengatakan: {result.text}")