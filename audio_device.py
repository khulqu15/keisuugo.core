import pyaudio
import numpy as np
from pydub import AudioSegment
from pydub.playback import play
from pydub.utils import make_chunks

class AudioStream:
    def __init__(self, device_index=None, format=None, channels=None, rate=None, chunk=None, file_path=None):
        self.p = pyaudio.PyAudio()
        self.chunk = chunk
        if file_path:
            self.file_path = file_path
            self.audio_segment = AudioSegment.from_file(file_path, format="mp3")
            chunk_length_ms = (chunk / rate) * 1000 
            self.audio_chunks = make_chunks(self.audio_segment, chunk_length_ms)
            self.current_chunk = 0
        else:
            self.stream = self.p.open(format=format,
                                      channels=channels,
                                      rate=rate,
                                      input=True,
                                      input_device_index=device_index,
                                      frames_per_buffer=chunk)

    def read_chunk(self):
        if hasattr(self, 'stream'):
            return self.stream.read(self.chunk)
        else:
            if self.current_chunk < len(self.audio_chunks):
                chunk_data = self.audio_chunks[self.current_chunk].raw_data
                self.current_chunk += 1
                return chunk_data
            else:
                return None

    def play_audio(self):
        if hasattr(self, 'audio_segment'):
            play(self.audio_segment)

    def close(self):
        if hasattr(self, 'stream'):
            self.stream.stop_stream()
            self.stream.close()
        self.p.terminate()

def visualize_wave(data):
    max_amplitude = np.max(np.abs(data))
    scale_factor = max_amplitude / 40
    scaled_data = data / scale_factor
    wave_str = ''.join(['*' if x > 0 else '-' for x in scaled_data])
    print(wave_str)
