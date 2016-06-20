import pyaudio
import wave
import time
import os
import shutil
import pygame
import pygame.camera
from pygame.locals import *
    #/dev/video0 is the USB2.0 webcam
    #/dev/video1 is the integrated webcam
    #name = "Arpit"
pygame.init()
pygame.camera.init()

CHUNK = 2048
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 2
    #WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

def capture_image(filename):
	cam = pygame.camera.Camera("/dev/video4",(320,240))
	cam.start()
	image = cam.get_image()
	pygame.image.save(image,filename)
	cam.stop()

def record(Chunk,Format,Channels,Rate,Rec):
    stream = p.open(format=Format, channels=Channels, rate=Rate, input=True, frames_per_buffer=Chunk)
    print("* recording")
    frames = []
    for i in range(0, int(Rate / Chunk * Rec)):
        data = stream.read(Chunk)
        frames.append(data)
    print("* done recording")
    stream.stop_stream()
    stream.close()
    #p.terminate()
    return frames

def audioWrite(Format,Channels,Rate,Frames,File):
    wf = wave.open(File, 'wb')
    wf.setnchannels(Channels)
    wf.setsampwidth(p.get_sample_size(Format))
    wf.setframerate(Rate)
    wf.writeframes(b''.join(Frames))
    wf.close()
    
def main():
    name = raw_input("Enter name of the user: ")
    nametry = name
    print "Hello " + name + "!!\n"
    dir_name = "/media/arpit/DAT/BlueInGrey/ProjectA.T.O.M/"+nametry
    while os.path.exists(dir_name):
        print "dir of name "+nametry+" cannot be created\n"
        nametry = raw_input("Enter name for the directory to be created: ")
        dir_name = "/media/arpit/DAT/BlueInGrey/ProjectA.T.O.M/"+nametry
    os.mkdir(dir_name)
    dir_name_image = dir_name + "/" + nametry + "Image"
    dir_name_audio = dir_name + "/" + nametry + "Audio"
    os.mkdir(dir_name_image)
    os.mkdir(dir_name_audio)
    src_dir = os.getcwd()
    time.sleep(0.5)
    
    for i in range(1,17):
        hand = "Note %d" % (i)
        print "Be ready to play " + hand
        time.sleep(0.5)
        fname = nametry+"_note%d" % (i)
        fnameImage = fname+".jpg"
        fnameAudio = fname+".wav"
        capture_image(fnameImage)
        print "\nPlay Now"
        y = record(CHUNK,FORMAT,CHANNELS,RATE,RECORD_SECONDS)
        audioWrite(FORMAT,CHANNELS,RATE,y,fnameAudio)
        shutil.move(src_dir+"/"+fnameImage,dir_name_image)
        shutil.move(src_dir+"/"+fnameAudio,dir_name_audio)
    
    print '\n*****Thank You for your participation '+name+'*****\n'
    
if __name__ == '__main__':
    main()
    