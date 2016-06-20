#!/usr/bin/python -tt

"""Audio Record/Play Module"""

from ctypes import *
import pyaudio
import wave
import sys

CHUNK = 2048
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 3

ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)
def py_error_handler(filename, line, function, err, fmt):
    pass
c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)

asound = cdll.LoadLibrary('libasound.so')
# Set error handler
asound.snd_lib_error_set_handler(c_error_handler)


def record(Chunk,Format,Channels,Rate,RecTime):
    p = pyaudio.PyAudio()
    stream = p.open(format=Format, channels=Channels, rate=Rate, input=True, frames_per_buffer=Chunk)
    print("* recording")
    frames = []
    for i in range(0, int(Rate / Chunk * RecTime)):
        data = stream.read(Chunk)
        frames.append(data)
    print("* done recording")
    stream.stop_stream()
    stream.close()
    p.terminate()
    return frames

def audioWrite(Format,Channels,Rate,Frames,File):
    p = pyaudio.PyAudio()
    wf = wave.open(File, 'wb')
    wf.setnchannels(Channels)
    wf.setsampwidth(p.get_sample_size(Format))
    wf.setframerate(Rate)
    wf.writeframes(b''.join(Frames))
    wf.close()
   
def play(filename):
    wf = wave.open(filename, 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(), rate=wf.getframerate(), output=True)
    data = wf.readframes(CHUNK)
    while data != '':
        stream.write(data)
        data = wf.readframes(CHUNK)
    stream.stop_stream()
    stream.close()
    p.terminate()
    
def main():
    if len(sys.argv) < 2:
        print("\nModule Records/Plays a wave file.\n\nUsage:\n%s play filename.wav\n%s record filename.wav " % (sys.argv[0],sys.argv[0]))
        sys.exit(-1)
    elif sys.argv[1] == 'record':
        if len(sys.argv) == 2:
            print("\nError! Enter filename.\n\nUsage:\n%s %s filename.wav" % (sys.argv[0],sys.argv[1]))
            sys.exit(-1)
        f = record(CHUNK,FORMAT,CHANNELS,RATE,RECORD_SECONDS)
        audioWrite(FORMAT,CHANNELS,RATE,f,sys.argv[2])
    elif sys.argv[1] == 'play':
        if len(sys.argv) == 2:
            print("\nError! Enter filename.\n\nUsage:\n%s %s filename.wav" % (sys.argv[0],sys.argv[1]))
            sys.exit(-1)
        play(sys.argv[2])
    
if __name__ == '__main__':
    main()
    
    