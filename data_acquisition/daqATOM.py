#!/usr/bin/python -tt

from image import *
from audiorp import *
import os
import shutil

camDevID = getCamDevID()
name = raw_input("Enter name of the user: ")
nametry = name
print "Hello " + name + "!!\n"
dir_name = "/media/arpit/DAT/BlueInGrey/ProjectA.T.O.M/"+nametry
while os.path.exists(dir_name):
    resp = raw_input("dir of name "+nametry+" already exists. Add new files to this directory? [y or n]: ")
    if resp == 'n':
        nametry = raw_input("Enter name for the directory to be created: ")
        dir_name = "/media/arpit/DAT/BlueInGrey/ProjectA.T.O.M/"+nametry
    else:
        break
try:
    os.mkdir(dir_name)
except OSError, e:
    if e.errno == 17:
        pass
    else:
        print "OS error({0}): {1}".format(e.errno, e.strerror)
        exit()

dir_name_image = dir_name + "/" + nametry + "Image"
dir_name_audio = dir_name + "/" + nametry + "Audio"

try:
    os.mkdir(dir_name_image)
except OSError, e:
    if e.errno == 17:
        pass
    else:
        print "OS error({0}): {1}".format(e.errno, e.strerror)
        exit()

try:
    os.mkdir(dir_name_audio)
except OSError, e:
    if e.errno == 17:
        pass
    else:
        print "OS error({0}): {1}".format(e.errno, e.strerror)
        exit()

src_dir = os.getcwd()
time.sleep(0.5)
recFlowflag = True
while recFlowflag:
    cf = raw_input("Select Record Flow: [Press 1 for frets 0-2] [Press 2 for frets 3-5] [Press 3 for frets 6-8]: ")
    if cf == '1' or cf == '2' or cf == '3':
        recFlowflag = False
        if cf == '1':
            flowLimit = 3
            flowDefault_s = 1
            flowDefault_f = 0
        elif cf == '2':
            flowLimit = 6
            flowDefault_s = 1
            flowDefault_f = 3
        else:
            flowLimit = 9
            flowDefault_s = 1
            flowDefault_f = 6
a = raw_input("Enter String Number: [Press Enter for default] ")
b = raw_input("Enter Fret Number: [Press Enter for default] ")
if a == '':
    a = flowDefault_s
if b == '':
    b = flowDefault_f
else:
    b = int(b)
for j in range(b,flowLimit):
    for k in range(int(a),7):
        hand = "String %d, Fret %d" % (k,j)
        print "Be ready to play " + hand
        time.sleep(1)
        for i in range(1,11):
            fname = nametry+"_s%d_f%d_%d" % (k,j,i)
            fnameImage = fname+".jpg"
            fnameAudio = fname+".wav"
            if (os.path.exists(camDevID)):
                capture(fnameImage,camDevID)
            else:
                print 'Camera Error'
                exit()
            play('beep.wav')
            print "\nPlay Now"
            y = record(CHUNK,FORMAT,CHANNELS,RATE,RECORD_SECONDS)
            audioWrite(FORMAT,CHANNELS,RATE,y,fnameAudio)
            shutil.move(src_dir+"/"+fnameImage,dir_name_image)
            shutil.move(src_dir+"/"+fnameAudio,dir_name_audio)
        ready = raw_input("\nContinue? (y/n): ")
        if ready == "n":
            break
    a = '1'
    if ready == "n":
        break
print '\n*****Thank You for your participation '+name+'*****\n'
