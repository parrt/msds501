import aifc
import numpy
import array

import sys
if len(sys.argv)>2:
        f = aifc.open(sys.argv[1])
        scaled = aifc.open(sys.argv[2], "wb")
else:
        print "please provide an input and output filename"
        exit()

params = f.getparams()
nsamples = f.getnframes()
print "mono" if f.getnchannels()==1 else "stereo", str(nsamples)+" samples"
shorts = f.readframes(nsamples)
signal = numpy.fromstring(shorts, numpy.short).byteswap() # stored big-endian, so convert
print signal
f.close()

signal *= 2
shorts = signal.byteswap().tostring()

scaled.aiff()
scaled.setparams(params)
scaled.writeframes(shorts)
scaled.close()
