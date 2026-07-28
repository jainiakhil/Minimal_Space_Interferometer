
import math
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

##For coarse gridding of the u-v plane so as to measure the coverage quantitatively
size12 = len(arrbu12)
size23 = len(arrbu23)
size31 = len(arrbu31)
cell = 100                      ##The size of each cell in the grid in km. The size can go below 100km for more finer grid but for some reason, the plotting in not being done as expected.

##For calculating percentage coverage of grid 
gridcount1 = 0
gridcount2 = 0
gridcount3 = 0
gridcounttot = 0

##Defining the grid as per the cell size for the plot due to satellites 1 and 2
grid = np.zeros(((32600/cell), (32600/cell)), dtype = int)

for i in range(0, size12):
    k = int(math.floor((arrbu12[i]/cell))) + (16300/cell)
    l = int(math.floor((arrbv12[i]/cell))) + (16300/cell)
    if grid[l][k] == 0:
        grid[l][k] = 1
        gridcount1 += 1
    else:
        grid[l][k] = 1

gridfig1 = plt.figure(figsize = (10,10))
grdifig1 = plt.imshow(grid, cmap = plt.cm.get_cmap('Reds', 2), origin = 'lower')
gridfig1 = plt.grid(True)
girdfig1 = plt.colorbar(ticks = [0, 1])
gridfig1 = plt.title('u-v Grid of Source %d at RA: %0.0f h %0.0f m %0.3f s and Dec: %0.0f deg %0.0f min %0.3f sec' % (nsrc, nsrahr, nsramin, nsrasec, nsdecdeg, nsdecmin, nsdecsec))
plt.xlim([0,300])
plt.ylim([0,300])
xlocs, xlabels = plt.xticks()
xlabels = [(((item)*100)-15000) for item in xlocs]
plt.xticks(xlocs, xlabels)
ylocs, ylabels = plt.yticks()
ylabels = [(((item)*100)-15000) for item in ylocs]
plt.yticks(ylocs, ylabels)
gridfig1 = plt.xlabel('u (km)')
gridfig1 = plt.ylabel('v (km)')
gridfig1 = plt.savefig('C:\Users\User\Desktop\Thesis Part 1\Tests\EPS Plots from Binary\[%s] Coverage due to Sat 1 and Sat 2 - Uniformly Weighted for 2 weeks for source at %0.0f h and %0.0f deg out of ionosphere.eps' % (sst, nsrahr, nsdecdeg), format = 'eps', bbox_inches = 'tight')

##Defining the grid as per the cell size for the plot due to satellites 2 and 3
grid = np.zeros(((32600/cell), (32600/cell)), dtype = int)

for i in range(0, size23):
    k = int(math.floor((arrbu23[i]/cell))) + (16300/cell)
    l = int(math.floor((arrbv23[i]/cell))) + (16300/cell)
    if grid[l][k] == 0:
        grid[l][k] = 1
        gridcount2 += 1
    else:
        grid[l][k] = 1

gridfig2 = plt.figure(figsize = (10,10))
grdifig2 = plt.imshow(grid, cmap = plt.cm.get_cmap('Blues', 2), origin = 'lower')
gridfig2 = plt.grid(True)
girdfig2 = plt.colorbar(ticks = [0, 1])
gridfig2 = plt.title('u-v Grid of Source %d at RA: %0.0f h %0.0f m %0.3f s and Dec: %0.0f deg %0.0f min %0.3f sec' % (nsrc, nsrahr, nsramin, nsrasec, nsdecdeg, nsdecmin, nsdecsec))
plt.xlim([0,300])
plt.ylim([0,300])
xlocs, xlabels = plt.xticks()
xlabels = [(((item)*100)-15000) for item in xlocs]
plt.xticks(xlocs, xlabels)
ylocs, ylabels = plt.yticks()
ylabels = [(((item)*100)-15000) for item in ylocs]
plt.yticks(ylocs, ylabels)
gridfig2 = plt.xlabel('u (km)')
gridfig2 = plt.ylabel('v (km)')
gridfig2 = plt.savefig('C:\Users\User\Desktop\Thesis Part 1\Tests\EPS Plots from Binary\[%s] Coverage due to Sat 2 and Sat 3 - Uniformly Weighted for 2 weeks for source at %0.0f h and %0.0f deg out of ionosphere.eps' % (sst, nsrahr, nsdecdeg), format = 'eps', bbox_inches = 'tight')

##Defining the grid as per the cell size for the plot due to satellites 3 and 1
grid = np.zeros(((32600/cell), (32600/cell)), dtype = int)

for i in range(0, size31):
    k = int(math.floor((arrbu31[i]/cell))) + (16300/cell)
    l = int(math.floor((arrbv31[i]/cell))) + (16300/cell)
    if grid[l][k] == 0:
        grid[l][k] = 1
        gridcount3 += 1
    else:
        grid[l][k] = 1

gridfig3 = plt.figure(figsize = (10,10))
grdifig3 = plt.imshow(grid, cmap = plt.cm.get_cmap('Greens', 2), origin = 'lower')
gridfig3 = plt.grid(True)
girdfig3 = plt.colorbar(ticks = [0, 1])
gridfig3 = plt.title('u-v Grid of Source %d at RA: %0.0f h %0.0f m %0.3f s and Dec: %0.0f deg %0.0f min %0.3f sec' % (nsrc, nsrahr, nsramin, nsrasec, nsdecdeg, nsdecmin, nsdecsec))
plt.xlim([0,300])
plt.ylim([0,300])
xlocs, xlabels = plt.xticks()
xlabels = [(((item)*100)-15000) for item in xlocs]
plt.xticks(xlocs, xlabels)
ylocs, ylabels = plt.yticks()
ylabels = [(((item)*100)-15000) for item in ylocs]
plt.yticks(ylocs, ylabels)
gridfig3 = plt.xlabel('u (km)')
gridfig3 = plt.ylabel('v (km)')
gridfig3 = plt.savefig('C:\Users\User\Desktop\Thesis Part 1\Tests\EPS Plots from Binary\[%s] Coverage due to Sat 3 and Sat 1 - Uniformly Weighted for 2 weeks for source at %0.0f h and %0.0f deg out of ionosphere.eps' % (sst, nsrahr, nsdecdeg), format = 'eps', bbox_inches = 'tight')

##Defining the grid as per the cell size for the plot due to all the satellites
grid = np.zeros(((32600/cell), (32600/cell)), dtype = int)

for i in range(0, size12):
    k = int(math.floor((arrbu12[i]/cell))) + (16300/cell)
    l = int(math.floor((arrbv12[i]/cell))) + (16300/cell)
    if grid[l][k] == 0:
        grid[l][k] = 1
        gridcounttot += 1
    else:
        grid[l][k] = 1

for i in range(0, size23):
    k = int(math.floor((arrbu23[i]/cell))) + (16300/cell)
    l = int(math.floor((arrbv23[i]/cell))) + (16300/cell)
    if grid[l][k] == 0:
        grid[l][k] = 1
        gridcounttot += 1
    else:
        grid[l][k] = 1

for i in range(0, size31):
    k = int(math.floor((arrbu31[i]/cell))) + (16300/cell)
    l = int(math.floor((arrbv31[i]/cell))) + (16300/cell)
    if grid[l][k] == 0:
        grid[l][k] = 1
        gridcounttot += 1
    else:
        grid[l][k] = 1

gridfig4 = plt.figure(figsize = (10,10))
grdifig4 = plt.imshow(grid, cmap = plt.cm.get_cmap('Greys', 2), origin = 'lower')
gridfig4 = plt.grid(True)
girdfig4 = plt.colorbar(ticks = [0, 1])
gridfig4 = plt.title('u-v Grid of Source %d at RA: %0.0f h %0.0f m %0.3f s and Dec: %0.0f deg %0.0f min %0.3f sec' % (nsrc, nsrahr, nsramin, nsrasec, nsdecdeg, nsdecmin, nsdecsec))
plt.xlim([0,300])
plt.ylim([0,300])
xlocs, xlabels = plt.xticks()
xlabels = [(((item)*100)-15000) for item in xlocs]
plt.xticks(xlocs, xlabels)
ylocs, ylabels = plt.yticks()
ylabels = [(((item)*100)-15000) for item in ylocs]
plt.yticks(ylocs, ylabels)
gridfig4 = plt.xlabel('u (km)')
gridfig4 = plt.ylabel('v (km)')
gridfig4 = plt.savefig('C:\Users\User\Desktop\Thesis Part 1\Tests\EPS Plots from Binary\[%s] Coverage Total - Uniformly Weighted for 2 weeks for source at %0.0f h and %0.0f deg out of ionosphere.eps' % (sst, nsrahr, nsdecdeg), format = 'eps', bbox_inches = 'tight')


print("The number of cells filled due to satellites 1 and 2: %d. Percentage coverage = %f" % (gridcount1, (gridcount1/834.69)))
print("The number of cells filled due to satellites 2 and 3: %d. Percentage coverage = %f" % (gridcount2, (gridcount2/834.69)))
print("The number of cells filled due to satellites 3 and 1: %d. Percentage coverage = %f" % (gridcount3, (gridcount3/834.69)))
print("The number of cells filled due to all three satellites: %d. Percentage coverage = %f" % (gridcounttot, gridcounttot/834.69))

##Doing 2D FFT on the grid due to all the satellites to get the dirty beam 
fftgrid = plt.figure(figsize = (10,10))
fftgrid = np.fft.ifft2(grid)
fftgrid = np.fft.fftshift(fftgrid)
fftimg = plt.imshow(np.abs(fftgrid), cmap = plt.cm.get_cmap('afmhot'), clim = [0, 0.01], origin = 'lower')
fftimg = plt.grid(False)
fftimg = plt.colorbar()
fftgrid = plt.title('Dirty Beam for Source %d at RA: %0.0f h %0.0f m %0.3f s and Dec: %0.0f deg %0.0f min %0.3f sec' % (nsrc, nsrahr, nsramin, nsrasec, nsdecdeg, nsdecmin, nsdecsec))
fftimg = plt.savefig('C:\Users\User\Desktop\Thesis Part 1\Tests\EPS Plots from Binary\[%s] Dirty Beam - Uniformly Weighted for 2 weeks for source at %0.0f h and %0.0f deg out of ionosphere.eps' % (sst, nsrahr, nsdecdeg), format = 'eps', bbox_inches = 'tight')
