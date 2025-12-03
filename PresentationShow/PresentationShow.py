
import time
from array import array
from time import time

import pyaudio
from pygame import mixer

from qstation import *


def start():
    ''' start the lightshow'''

    connect('172.16.0.1')
    light0_sn = 'MD2AC52400000948'
    light1_sn = 'MD2AC44400002164'
    light2_sn = 'MD1AC44400002573'

    turn_off(light0_sn)
    sleep(0.2)
    turn_off(light1_sn) 
    sleep(0.2)
    turn_off(light2_sn)
    sleep(0.7)

    
    mixer.init()
    mixer.music.load('Brazil.mp3')
    mixer.music.play()

  
    yellow = (255,255,0)
    green = (22, 100, 0)
    blue = (0, 0, 255)
    

    # array that has tuples in the form of (timeCode, sn, color)
    info_array = [(0.1, light0_sn, (0, 0, 0)),
                  #clap it up beat
                  (0.69, light0_sn, (22, 100, 0)),
                  (0.69, light1_sn, (0, 0, 0)),
                  (0.69, light2_sn, (22, 100, 0)),
                  
                  (1.17, light0_sn, (0, 0, 0)),
                  (1.17, light1_sn, (0, 0, 255)),
                  (1.17, light2_sn, (0, 0, 0)),
                  
                  (1.79, light0_sn, (22, 100, 0)),
                  (1.79, light1_sn, (0, 0, 0)),
                  (1.79, light2_sn, (22, 100, 0)),
                  
                  (2.09, light0_sn, (0, 0, 0)),
                  (2.09, light1_sn, (0, 0, 255)),
                  (2.09, light2_sn, (0, 0, 0)),
                  
                  #initiate
                  (3.0, light0_sn, (255, 225, 0)),
                  (3.3, light1_sn, (255, 225, 0)),
                  (3.6, light2_sn, (255, 225, 0)),
                  
                  (3.9, light0_sn, (0, 0, 0)),
                  (4.2, light1_sn, (0, 0, 0)),
                  (4.5, light2_sn, (0, 0, 0)),

                  #first pump
                  (5.2, light0_sn, (255, 12, 34)),
                  (5.2, light1_sn, (255, 0, 0)),
                  (5.2, light2_sn, (255, 12, 34)),
                  #blink off
                  (5.8, light0_sn, (0, 0, 0)),
                  (5.8, light1_sn, (0, 0, 0)),
                  (5.8, light2_sn, (0, 0, 0)),
                   #flash1
                  (6.0, light1_sn, (0, 0, 255)),
                  (6.2, light1_sn, (0, 0, 0)),
                  #blink on
                  (6.4, light0_sn, (255, 0, 0)),
                  (6.4, light1_sn, (255, 12, 34)),
                  (6.4, light2_sn, (255, 0, 0)),
                   #blink off
                  (7.0, light0_sn, (0, 0, 0)),
                  (7.0, light1_sn, (0, 0, 0)),
                  (7.0, light2_sn, (0, 0, 0)),
                   #flash2
                  (7.2, light0_sn, (255, 225, 0)),
                  (7.4, light0_sn, (0, 0, 0)),
                  # Change again
                  (7.6, light0_sn, (255, 0, 0)),
                  (7.6, light1_sn, (255, 165, 0)),
                  (7.6, light2_sn, (255, 12, 34)),
                   #blink off
                  (8.2, light0_sn, (0, 0, 0)),
                  (8.2, light1_sn, (0, 0, 0)),
                  (8.2, light2_sn, (0, 0, 0)),
                  #flash3
                  (8.4, light2_sn, (22, 100, 0)),
                  (8.6, light2_sn, (0, 0, 0)),
                  # second by second
                  (8.8, light0_sn, (22, 100, 0)),
                  (8.8, light1_sn, (255, 255, 0)),
                  (8.8, light2_sn, ( 0, 0, 255)),
                  #blink off
                  (9.4, light0_sn, (0, 0, 0)),
                  (9.4, light1_sn, (0, 0, 0)),
                  (9.4, light2_sn, (0, 0, 0)),
                   #flash4
                  (9.6, light1_sn, (255, 0, 0)),
                  (9.8, light1_sn, (0, 0, 0)),
                  #change one more time 
                  (10.0, light0_sn, (255, 165, 0)),
                  (10.0, light1_sn, (255, 0, 0)),
                  (10.0, light2_sn, (255, 165, 0)),
                   #last blink off
                  (10.6, light0_sn, (0, 0, 0)),
                  (10.6, light1_sn, (0, 0, 0)),
                  (10.6, light2_sn, (0, 0, 0)),
                   #last flash5
                  (10.7, light2_sn, (22, 100, 0)),
                  (10.8, light2_sn, (0, 0, 0)),
                
                    #procede as planned 
                  (11.2, light0_sn, (255, 255, 0)),
                  (11.2, light1_sn, (25, 167, 28)),
                  (11.2, light2_sn, (255, 167, 0)),
                  #taking turns 
                  (11.8, light0_sn, (0,0,0)),
                  (11.9, light1_sn, (0,0,0)),
                  (12.0, light2_sn, (0,0,0)),
                  
                  (12.4, light0_sn, (255, 165, 28)),
                  (12.5, light1_sn, (255, 0, 0)),
                  (12.6, light2_sn, (255, 255, 0)),
                  
                  (13.0, light0_sn, (0,0,0)),
                  (13.0, light1_sn, (0,0,0)),
                  (13.0, light2_sn, (0,0,0)),
                  
                  (13.3, light0_sn, (22, 100, 0)),
                  (13.3, light1_sn, (0, 0, 255)),
                  (13.3, light2_sn, (255, 255, 0)),
                  #OFF
                  (13.5, light2_sn, (0, 0, 0)),
                  (13.5, light2_sn, (0, 0, 0)),
                  (13.5, light2_sn, (0, 0, 0)),

                  #blink
                  (14.2, light0_sn, (22, 100, 0)),
                  (14.2, light1_sn, (22, 100, 0)),
                  (14.2, light2_sn, (22, 100, 0)),
                  
                  (14.5, light0_sn, (0, 0, 0)),
                  (14.5, light1_sn, (0, 0, 0)),
                  (14.5, light2_sn, (0, 0, 0)),
                  
                  #trumpets brazil flag 
                  (15.3, light0_sn, (22, 100, 0)),
                  (15.3, light1_sn, (255, 255, 0)),
                  (15.3, light2_sn, (0, 0, 255)),
                  #flag reversed 
                  (15.75, light0_sn, (0, 0, 255)),
                  (15.75, light1_sn, (255, 255, 0)),
                  (15.75, light2_sn, (22, 100, 0)),
                  # flag change again
                  (16.16, light0_sn, (255, 255, 0)),
                  (16.16, light1_sn, (22, 100, 0)),
                  (16.16, light2_sn, (0, 0, 255)),
                  
                  #off be dramatic
                  (17.0, light0_sn, (0,0,0)),
                  (17.0, light1_sn, (0,0,0)),
                  (17.0, light2_sn, (0,0,0)),
                  
                  #flashing booms 
                  (17.78, light0_sn, (green)),
                  (17.78, light1_sn, (green)),
                  (17.78, light2_sn, (green)),
                  
                  (18.00, light0_sn, (0,0,0)),
                  (18.00, light1_sn, (0,0,0)),
                  (18.00, light2_sn, (0,0,0)),
                  #next boom
                  (18.43, light0_sn, (blue)),
                  (18.43, light1_sn, (blue)),
                  (18.43, light2_sn, (blue)),
                  
                  (18.80, light0_sn, (0,0,0)),
                  (18.80, light1_sn, (0,0,0)),
                  (18.80, light2_sn, (0,0,0)),
                  
                  #3rd boom
                  (19.02, light0_sn, (yellow)),
                  (19.02, light1_sn, (yellow)),
                  (19.02, light2_sn, (yellow)),
                  
                  (19.60, light0_sn, (0,0,0)),
                  (19.60, light1_sn, (0,0,0)),
                  (19.60, light2_sn, (0,0,0)),
                  
                  #4th boom
                  (20.30, light0_sn, (blue)),
                  (20.30, light1_sn, (blue)),
                  (20.30, light2_sn, (blue)),
                  
                  (20.60, light0_sn, (0,0,0)),
                  (20.60, light1_sn, (0,0,0)),
                  (20.60, light2_sn, (0,0,0)),
                  
                  #5th
                  (20.90, light0_sn, (green)),
                  (20.90, light1_sn, (green)),
                  (20.90, light2_sn, (green)),
                  
                  (21.20, light0_sn, (0,0,0)),
                  (21.20, light1_sn, (0,0,0)),
                  (21.20, light2_sn, (0,0,0)),
                  #6th 
                  (21.55, light0_sn, (yellow)),
                  (21.55, light1_sn, (yellow)),
                  (21.55, light2_sn, (yellow)),
                  
                  (21.80, light0_sn, (0,0,0)),
                  (21.80, light1_sn, (0,0,0)),
                  (21.80, light2_sn, (0,0,0)),
                  #7th
                  (22.14 , light0_sn, (blue)),
                  (22.14 , light1_sn, (blue)),
                  (22.14 , light2_sn, (blue)),
                  
                  (22.50, light0_sn, (0,0,0)),
                  (22.50, light1_sn, (0,0,0)),
                  (22.50, light2_sn, (0,0,0)),
                  
                  #7th
                  (22.77 , light0_sn, (green)),
                  (22.77 , light1_sn, (green)),
                  (22.77 , light2_sn, (green)),
                  
                  (21.80, light0_sn, (0,0,0)),
                  (21.80, light1_sn, (0,0,0)),
                  (21.80, light2_sn, (0,0,0)),
                  
                  #8th boom blink 
                  (23.419, light0_sn, (yellow)),
                  (23.419, light1_sn, (yellow)),
                  (23.419, light2_sn, (yellow)),
                  
                  (23.70, light0_sn, (0,0,0)),
                  (23.70, light1_sn, (0,0,0)),
                  (23.70, light2_sn, (0,0,0)),
                  
                  #9th boom blink and carasel
                  (24.02, light0_sn, (255, 0, 0)),
                  (24.12, light1_sn, (252, 3, 202)),
                  (24.22, light2_sn, (yellow)),
                  
                  (24.52, light0_sn, (0,0,0)),
                  (24.62, light1_sn, (0,0,0)),
                  (24.72, light2_sn, (0,0,0)),
                  # embark on switching!
                  (25.82, light0_sn, (green)),
                  (25.82, light1_sn, (yellow)),
                  (25.82, light2_sn, (blue)),
                  #lights 2 and 3 take turns 
                  (25.93, light0_sn, (yellow)),
                  (25.93, light1_sn, (green)),
                  (25.93, light2_sn, (blue)),
                  #switch 
                  (26.53, light0_sn, (green)),
                  (26.53, light1_sn, (yellow)),
                  (26.53, light2_sn, (blue)),
                  #tiny voice synth on off
                  (26.64, light2_sn, (0,0,0)),
                  (26.83, light2_sn, (blue)),
                  (26.94, light2_sn, (0,0,0)), 
                   #switch again
                  (27.15, light0_sn, (yellow)),
                  (27.15, light1_sn, (green)),
                  (27.15, light2_sn, (blue)),
                  #switch one more time 
                  (28.25, light0_sn, (green)),
                  (28.25, light1_sn, (yellow)),
                  (28.25, light2_sn, (blue)),
                  #off
                  (28.45, light0_sn, (0,0,0)),
                  (28.55, light1_sn, (0,0,0)),
                  (28.65, light2_sn, (0,0,0)),
                  #each bulb counts start
                  (29.02, light0_sn, (yellow)),
                  (29.12, light1_sn, (green)),
                  (29.22, light2_sn, (blue)),
                  #action between 
                  (29.72, light0_sn, (0,0,0)),
                  (29.82, light1_sn, (0,0,0)),
                  (29.92, light2_sn, (0,0,0)),
                   #each bulb counts end 
                  (30.052, light0_sn, (green)),
                  (30.152, light1_sn, (yellow)),
                  (30.252, light2_sn, (blue)),
                  #pump taking turns 
                  (30.904, light0_sn, (0,0,0)),
                  (30.904, light1_sn, (blue)),
                  (30.904, light2_sn, (0,0,0)),
                  #again
                  (31.535, light0_sn, (yellow)),
                  (31.535, light1_sn, (0,0,0)),
                  (31.535, light2_sn, (green)),
                  #again
                  (32.165, light0_sn, (0,0,0)),
                  (32.165, light1_sn, (yellow)),
                  (32.165, light2_sn, (0,0,0)),
                  #again
                  (32.766, light0_sn, (green)),
                  (32.766, light1_sn, (0,0,0)),
                  (32.766, light2_sn, (blue)),
                  # i'll say when to stop 
                  (33.397, light0_sn, (0,0,0)),
                  (33.397, light1_sn, (green)),
                  (33.397, light2_sn, (0,0,0)),
                  #repeat
                  (34.042, light0_sn, (yellow)),
                  (34.042, light1_sn, (0,0,0)),
                  (34.042, light2_sn, (blue)),
                  #last time 
                  (34.628, light0_sn, (0,0,0)),
                  (34.628, light1_sn, (yellow)),
                  (34.628, light2_sn, (0,0,0)),
                  #guitar strum stop blink
                  (35.259, light0_sn, (green)),
                  (35.259, light1_sn, (blue)),
                  (35.259, light2_sn, (yellow)),
                  
                  (35.531, light0_sn, (0,0,0)),
                  (35.531, light1_sn, (0,0,0)),
                  (35.531, light2_sn, (0,0,0)),
                  #one at a time to the beat blue at last
                  (35.724, light0_sn, (0,0,0)),
                  (35.724, light1_sn, (0,0,0)),
                  (35.724, light2_sn, (blue)),
                  #green at first
                  (36.175, light0_sn, (green)),
                  (36.175, light1_sn, (0,0,0)),
                  (36.175, light2_sn, (0,0,0)),
                  #yellow at second 
                  (36.820, light0_sn, (0,0,0)),
                  (36.820, light1_sn, (yellow)),
                  (36.820, light2_sn, (0,0,0)),
                  #blue at last 
                  (37.106, light0_sn, (0,0,0)),
                  (37.106, light1_sn, (0,0,0)),
                  (37.106, light2_sn, (blue)),
                  #green at first
                  (38.247, light0_sn, (green)),
                  (38.247, light1_sn, (0,0,0)),
                  (38.247, light2_sn, (0,0,0)),
                  #yellow at second 
                  (38.698, light0_sn, (0,0,0)),
                  (38.698, light1_sn, (yellow)),
                  (38.698, light2_sn, (0,0,0)),
                  #blue at last 
                  (39.328, light0_sn, (0,0,0)),
                  (39.328, light1_sn, (0,0,0)),
                  (39.328, light2_sn, (blue)),
                  #yellow at first
                  (39.644, light0_sn, (yellow)),
                  (39.644, light1_sn, (0,0,0)),
                  (39.644, light2_sn, (0,0,0)),
                  #blue at second 
                  (40.74, light0_sn, (0,0,0)),
                  (40.74, light1_sn, (blue)),
                  (40.74, light2_sn, (0,0,0)),
                  # green at last 
                  (41.220, light0_sn, (0,0,0)),
                  (41.220, light1_sn, (0,0,0)),
                  (41.220, light2_sn, (green)),
                   #green at first
                  (41.836, light0_sn, (green)),
                  (41.836, light1_sn, (0,0,0)),
                  (41.836, light2_sn, (0,0,0)),
                  #yellow at second 
                  (42.151, light0_sn, (0,0,0)),
                  (42.151, light1_sn, (yellow)),
                  (42.151, light2_sn, (0,0,0)),
                  #blue at last 
                  (43.233, light0_sn, (0,0,0)),
                  (43.233, light1_sn, (0,0,0)),
                  (43.233, light2_sn, (blue)),
                  #yellow at first
                  (43.713, light0_sn, (yellow)),
                  (43.713, light1_sn, (0,0,0)),
                  (43.713, light2_sn, (0,0,0)),
                  #blue at second 
                  (44.329, light0_sn, (0,0,0)),
                  (44.329, light1_sn, (blue)),
                  (44.329, light2_sn, (0,0,0)),
                  # green at last 
                  (44.629, light0_sn, (green)),
                  (44.750, light1_sn, (yellow)),
                  (44.990, light2_sn, (blue)),
                  #END
                  (45.00, light0_sn, (0,0,0)),
                  (45.00, light1_sn, (0,0,0)),
                  (45.00, light2_sn, (0,0,0)),
                  ]

                  

    length = len(info_array)
    next_color = (0, 0, 0)
    next_light = light0_sn
    next_time_code = 0.0
    start_time = time()
    next_index = 1
    sleep(0.6)

    # loop to find a match between the timecode and the current time
    # set the color accordingly
    while next_index < length:
        current_time = time() - start_time
        if current_time >= next_time_code:
            set_color(next_color, next_light)
            next_change = info_array[next_index]
            next_time_code = next_change[0]
            next_light = next_change[1]
            next_color = next_change[2]
            next_index = next_index + 1

    sleep(0.7)

    # turn off the lights
    turn_off(light1_sn)
    sleep(0.2)
    turn_off(light0_sn)
    sleep(0.2)
    turn_off(light2_sn)
    mixer.music.stop()
    global endShow
    endShow = True

# the following code is taken from https://github.com/nikhiljohn10/pi-clap
# with some small modifications


# main

# global variable
global endShow
endShow = False

CHUNK = 2048
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
threshold = 1000
max_value = 0
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS, 
                rate=RATE, 
                input=True,
                frames_per_buffer=CHUNK)


print("Clap detection initialized")
while not endShow:
    data = stream.read(CHUNK)
    as_ints = array('h', data)
    max_value = max(as_ints)
    if max_value > threshold:
        print("Clapped")
        start()

stream.stop_stream()
stream.close()
p.terminate()
