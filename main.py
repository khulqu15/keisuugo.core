import threading
import numpy as np
from config import DEVICE_INDEX, FORMAT, CHANNELS, RATE, CHUNK
from audio_device import AudioStream, visualize_wave
from voice_recognition import Recognizer

def capture_audio(audio_stream, recognizer):
    frames = []
    while True:
        data = audio_stream.read_chunk()
        frames.append(data)

        audio_data = np.frombuffer(b''.join(frames), np.int16).astype(np.float32) / 32768.0
        visualize_wave(audio_data)
        result = recognizer.transcribe(audio_data)
        print("Anda Ngomong: ", result['text'])

if __name__ == "__main__":
    audio_stream = AudioStream(DEVICE_INDEX, FORMAT, CHANNELS, RATE, CHUNK)
    recognizer = Recognizer()

    thread = threading.Thread(target=capture_audio, args=(audio_stream, recognizer))
    thread.start()

    print("Mendengarkan...")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Sistem mati: ")
        audio_stream.close()
