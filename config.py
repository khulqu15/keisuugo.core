from dotenv import load_dotenv
import pyaudio
import os

load_dotenv()

DEVICE_INDEX = int(os.getenv('DEVICE_INDEX', 0))
FORMAT = pyaudio.paInt16
CHANNELS = int(os.getenv('CHANNELS', 1))
RATE = int(os.getenv('RATE', 16000))
CHUNK = int(os.getenv('CHUNK', 1024))
