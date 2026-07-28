
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
arrayname = "[28-02-2020 18;33;23] 4Sat u-v Array for 1 weeks for source at 0 h and 00 deg.npy"
sourcename = "[28-02-2020 18;33;23] 4Sat Source Info for 1 weeks for source at 3 h and 00 deg.npy"

##Path definition
binpath = "C:\Users\User\Desktop\Thesis Part 1\Tests\Binary Files"
fullpatharray = os.path.join(binpath, arrayname)
fullpathsource = os.path.join(binpath, sourcename)

##Load npy files
(arrbu01, arrbv01, arrbu02, arrbv02, arrbu03, arrbv03, arrbu12, arrbv12, arrbu13, arrbv13, arrbu23, arrbv23) = np.load(fullpatharray)
(nsrc, nsrahr, nsramin, nsrasec, nsdecdeg, nsdecmin, nsdecsec) = np.load(fullpathsource)

##Plot u-v graph and saving it as eps file
plt.figure(figsize = (10,10))
plt.scatter(arrbu01, arrbv01, color = 'purple', marker = 'o', s = 0.1, label = 'Baseline between Satellite 0 and Satellite 1')
plt.scatter(arrbu02, arrbv02, color = 'blue', marker = 'o', s = 0.1, label = 'Baseline between Satellite 0 and Satellite 2')
plt.scatter(arrbu03, arrbv03, color = 'green', marker = 'o', s = 0.1, label = 'Baseline between Satellite 0 and Satellite 3')
plt.scatter(arrbu12, arrbv12, color = 'yellow', marker = 'o', s = 0.1, label = 'Baseline between Satellite 1 and Satellite 2')
plt.scatter(arrbu13, arrbv13, color = 'orange', marker = 'o', s = 0.1, label = 'Baseline between Satellite 1 and Satellite 3')
plt.scatter(arrbu23, arrbv23, color = 'red', marker = 'o', s = 0.1, label = 'Baseline between Satellite 2 and Satellite 3')
plt.axis([-15000, 15000, -15000, 15000])
plt.title('u-v Plot of Source %d at RA: %0.0f h %0.0f m %0.3f s and Dec: %0.0f deg %0.0f min %0.3f sec' % (nsrc, nsrahr, nsramin, nsrasec, nsdecdeg, nsdecmin, nsdecsec))
plt.xlabel('u (km)')
plt.ylabel('v (km)')
#plt.legend()
plt.grid(True)
global save
plt.savefig('C:\Users\User\Desktop\Thesis Part 1\Tests\EPS Plots from Binary\[%s] 4Sat u-v Plot with Hermitian for 2 weeks for source at %0.0f h and %0.0f deg.eps' % (sst, nsrahr, nsdecdeg), format = 'eps')
