import numpy
import sounddevice as sd

fs = 44100 # sampling frequency
T = 1.5    # seconds
t = numpy.linspace(0, T, int(T*fs), endpoint=False) # time variable
y = numpy.sin(2*numpy.pi*440*t)                     # pure sine wave at 440 Hz
y2 = numpy.sin(2*numpy.pi*1000*t)                   # pure sine wave at 1000 Hz
sd.play(y+y2, fs)
sd.wait()
