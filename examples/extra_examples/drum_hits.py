#!/usr/bin/env python

import drumhat
import time
import pygame
import os
import glob
from blinkt import set_pixel, show

DRUM_FOLDER = "drums2"

BANK = os.path.join(os.path.dirname(__file__), DRUM_FOLDER)

pygame.mixer.init(44100, -16, 1, 512)
pygame.mixer.set_num_channels(16)

files = glob.glob(os.path.join(BANK, "*.wav"))
files.sort()

samples = [pygame.mixer.Sound(f) for f in files]

def show_all(state):
    for i in range(8):
        val = state * 255
        set_pixel(i, val, val, val)
    show()

def handle_hit(event):
    samples[event.channel].play(loops=0)
    show_all(1)
    print("You hit pad {}, playing: {}".format(event.pad,files[event.channel]))

def handle_release():
    show_all(0)

drumhat.on_hit(drumhat.PADS, handle_hit)
drumhat.on_release(drumhat.PADS, handle_release)

while True:
    time.sleep(1)