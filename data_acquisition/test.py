"""
PyAudio Example: Make a wire between input and output (i.e., record a
few samples and play them back immediately).

This is the callback (non-blocking) version.
"""

import pyaudio
import time
from audiorp import audioWrite

#WIDTH = 2
#CHANNELS = 2
#RATE = 44100
CHUNK = 2048
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 3

p = pyaudio.PyAudio()

def callback(in_data, frame_count, time_info, status):
    return (in_data, pyaudio.paContinue)

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                stream_callback=callback)

stream.start_stream()

frames = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
print("* done recording")
#while stream.is_active():
 #   time.sleep(0.1)

stream.stop_stream()
stream.close()
p.terminate()
fnameAudio = 'blue.wav'
audioWrite(FORMAT,CHANNELS,RATE,frames,fnameAudio)