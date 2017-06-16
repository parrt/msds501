import aifc
import numpy

import sys
if len(sys.argv)>1:
        f = aifc.open(sys.argv[1])
else:
        print "please provide a filename"
        exit()

# (1, 2, 44100, 123269, 'NONE', 'not compressed') = (1 channel, 2bytes per, rate, samples, no compression)
print f.getparams()
nsamples = f.getnframes()
print "mono" if f.getnchannels()==1 else "stereo", str(nsamples)+" samples"
shorts = f.readframes(nsamples)
signal = numpy.fromstring(shorts, numpy.short).byteswap()
print signal
f.close()
