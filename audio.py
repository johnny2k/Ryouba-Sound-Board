#!/usr/bin/env python
""" Play a WAVE file. """

import pyaudio
import wave
import sys

def sayit(fn):
    chunk = 1024
    wf = wave.open(fn, 'rb')

    p = pyaudio.PyAudio()

# open stream
    stream = p.open(format =
    p.get_format_from_width(wf.getsampwidth()),
    channels = wf.getnchannels(),
    rate = wf.getframerate(),
    output = True)

# read data
    data = wf.readframes(chunk)

# play stream
    while data != '':
        stream.write(data)
        data = wf.readframes(chunk)

    stream.close()
    p.terminate()
