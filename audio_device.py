import pyaudio
import numpy as np

class AudioStream:
    def __init__(self, device_index, format, channels, rate, chunk):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=format,
                                  channels=channels,
                                  rate=rate,
                                  input=True,
                                  input_device_index=device_index,
                                  frames_per_buffer=chunk)
        self.chunk = chunk

    def read_chunk(self):
        return self.stream.read(self.chunk)

    def close(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

def visualize_wave(data):
    max_amplitude = np.max(np.abs(data))
    scale_factor = max_amplitude / 40
    scaled_data = data / scale_factor
    wave_str = ''.join(['*' if x > 0 else '-' for x in scaled_data])
    print(wave_str)
