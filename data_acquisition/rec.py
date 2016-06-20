from test1 import *
import time
rec = Recorder(channels=2)
with rec.open('nonblocking.wav', 'wb') as recfile2:
    recfile2.start_recording()
    time.sleep(5.0)
    recfile2.stop_recording()
