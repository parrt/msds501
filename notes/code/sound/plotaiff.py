import aifc
import numpy
import matplotlib.pyplot as plt
from array import *

import sys
if len(sys.argv)>1:
	f = aifc.open(sys.argv[1])
else:
	print "please provide a filename"
	exit()

nsamples = f.getnframes()
params = f.getparams()
print params
shorts = f.readframes(nsamples)
signal = numpy.fromstring(shorts, numpy.short).byteswap()
f.close()

plt.figure(1)
plt.title('Kiss Signal...')
plt.plot(signal)

plt.show()
