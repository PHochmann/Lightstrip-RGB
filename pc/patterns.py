from update import VisualizationState
from update import RGB
import math

def setRGB(colors, pos, color):
    if (pos > 0 and pos < len(colors)):
        colors[pos] = color

colA = RGB(255, 0, 0)
colB = RGB(0, 0, 255)
total = 0
factor = 1
evenFactor = 0.5
oddFactor = 1.5
grow = 1
brightness = 1
beat_num = 0

def sectionCallback(state, section):
    state = state
    print("new section")

def barCallback(state, bar):
    global factor
    factor /= abs(factor)
    factor *= -1

def beatCallback(state, beat):
    global total
    global beat_num
    global factor
    global brightness
    total += math.pi / 2
    if beat_num % 2 == 0:
        brightness += 0.5
    beat_num += 1

def tatumCallback(state, tatum):
    state = state

def segmentCallback(state, segment):
    #print("new segment")
    state = state

def genericCallback(state, delta):
    global total
    global brightness
    totalFactor = 0
    if beat_num % 2 == 0:
        totalFactor += evenFactor
    else:
        totalFactor += oddFactor
    totalFactor *= factor
    total += delta * totalFactor
    brightness = min(brightness, 1)
    brightness *= 0.98
    for i in range(0, state.num_leds):
        ii = i / state.num_leds * math.pi
        state.colors[i] = (colA * abs(math.sin(ii + total)) + colB * abs(math.cos(ii + total))) * brightness
    for i in range(0, state.num_leds):
        state.colors[i] = RGB(int(state.colors[i].r), int(state.colors[i].g), int(state.colors[i].b))