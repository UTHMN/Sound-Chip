import pygame
import numpy
import math

def sine_x(amp, freq, time):
    return int(round(amp * math.sin(2 * math.pi * freq * time)))

