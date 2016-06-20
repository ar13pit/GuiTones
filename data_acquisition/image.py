#!/usr/bin/python -tt

''' This program takes a snapshot using the connected USB webcam and stores it in the ATOM_Python folder.
    The program uses pygame module. The camera module is optional and thus needs to be initialised. 
'''


import time
import os
import pygame
import pygame.camera
from pygame.locals import *
    
pygame.init()
pygame.camera.init()

def getCamDevID():
    devSelect = raw_input("Use Integrated WebCam for Image capture? [y or n]: ")
    if devSelect == 'y':
        return "/dev/video0"
    else:
        flag = False
        i = 0
        while(not flag):
            i = i+1
            flag = os.path.exists("/dev/video" + str(i))
        return "/dev/video" + str(i)

def capture(filename,camDevID):
	cam = pygame.camera.Camera(camDevID,(1280,960))
	cam.start()
	time.sleep(1)    
	image = cam.get_image()
	pygame.image.save(image,filename)
	cam.stop()

def main():
    import sys
    try:
        fname = sys.argv[1]
    except IndexError:
        fname = raw_input("Enter the name of the file in the format xyz.jpg [Press Enter for Default 'Image.jpg']: ")
        if fname == '':
            fname = 'Image.jpg'
    camDevID = getCamDevID()
    capture(fname,camDevID)
    print '\n****Done!!****\n'

if __name__ == '__main__':
	main()

 
