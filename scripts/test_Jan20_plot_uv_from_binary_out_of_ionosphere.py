
from math import *
import numpy as np
import matplotlib.pyplot as plt
import time
import datetime
import os

##Timestamps
tss = time.time()
sst = datetime.datetime.fromtimestamp(tss).strftime('%d-%m-%Y %H;%M;%S')

##Change filename here to specify which file to load
sourcename = "[04-03-2020 19;55;24] Source Info for 2 weeks for source at 0 hr 00 deg out of ionosphere.npy"
arrayname = "[04-03-2020 19;55;24] u-v Array for 2 weeks for source at 0 hr 00 deg out of ionosphere.npy"

##Path definition
binpath = "C:\Users\User\Desktop\Thesis Part 1\Tests\Binary Files"
fullpatharray = os.path.join(binpath, arrayname)
fullpathsource = os.path.join(binpath, sourcename)

##Load npy files
(arrbu12, arrbv12, arrbu23, arrbv23, arrbu31, arrbv31) = np.load(fullpatharray)
(nsrc, nsrahr, nsramin, nsrasec, nsdecdeg, nsdecmin, nsdecsec) = np.load(fullpathsource)

##Plot u-v graph and saving it as eps file
plt.figure(figsize = (10,10))
plt.scatter(arrbu12, arrbv12, color = 'r', marker = 'o', s = 0.1, label = 'Baseline due to Satellite 1 and Satellite 2')
plt.scatter(arrbu23, arrbv23, color = 'b', marker = 'o', s = 0.1, label = 'Baseline due to Satellite 2 and Satellite 3')
plt.scatter(arrbu31, arrbv31, color = 'g', marker = 'o', s = 0.1, label = 'Baseline due to Satellite 3 and Satellite 1')
plt.axis([-16000, 16000, -16000, 16000])
plt.title('u-v Plot of Source %d at RA: %0.0f h %0.0f m %0.3f s and Dec: %0.0f deg %0.0f min %0.3f sec' % (nsrc, nsrahr, nsramin, nsrasec, nsdecdeg, nsdecmin, nsdecsec))
plt.xlabel('u (km)')
plt.ylabel('v (km)')
#plt.legend()
plt.grid(True)
plt.savefig('C:\Users\User\Desktop\Thesis Part 1\Tests\EPS Plots from Binary\[%s] u-v Plot with Hermitian for 2 weeks for source at %0.0f hr and %0.0f deg out of ionosphere.eps' % (sst, nsrahr, nsdecdeg), format = 'eps')
