import threading
import numpy as np
import argparse
from config import DEVICE_INDEX, FORMAT, CHANNELS, RATE, CHUNK
from audio_device import AudioStream, visualize_wave
from voice_recognition import Recognizer

def capture_audio(audio_stream, recognizer):
    frames = []
    while True:
        data = audio_stream.read_chunk()
        if data is None:
            break
        frames.append(data)

        audio_data = np.frombuffer(b''.join(frames), np.int16).astype(np.float32) / 32768.0
        visualize_wave(audio_data)
        result = recognizer.transcribe(audio_data)
        print("Anda Ngomong: ", result)

def transcribe_file_with_local_whisper(audio_stream, recognizer):
    result = recognizer.transcribe(audio_stream)
    print("Transkripsi dari Whisper lokal: ", result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Voice Recognition Program")
    parser.add_argument('--input', choices=['microphone', 'file'], required=True, help="Input source: 'microphone' or 'file'")
    parser.add_argument('--file', type=str, help="Path to the MP3 file (if input is 'file')")
    args = parser.parse_args()

    if args.input == 'microphone':
        audio_stream = AudioStream(device_index=DEVICE_INDEX, format=FORMAT, channels=CHANNELS, rate=RATE, chunk=CHUNK)
        recognizer = Recognizer()
        thread = threading.Thread(target=capture_audio, args=(audio_stream, recognizer))
        thread.start()
        print("Mendengarkan...")

    elif args.input == 'file':
        if not args.file:
            print("File path must be provided if input is 'file'")
            exit(1)
        audio_stream = AudioStream(file_path=args.file, chunk=CHUNK, rate=RATE)
        recognizer = Recognizer()

        play_thread = threading.Thread(target=audio_stream.play_audio)
        transcribe_thread = threading.Thread(target=transcribe_file_with_local_whisper, args=(args.file, recognizer))

        play_thread.start()
        transcribe_thread.start()

        play_thread.join()
        transcribe_thread.join()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Sistem mati:")
        audio_stream.close()
