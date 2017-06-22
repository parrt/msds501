import numpy as np
import sounddevice as sd

import soundfile as sf
data, samplerate = sf.read('../../data/sound/Kiss.aiff')
#data, samplerate = sf.read('../../data/sound/ahhh.wav')
print data
data *= 100
print data
sd.play(data, samplerate)
sd.wait()
