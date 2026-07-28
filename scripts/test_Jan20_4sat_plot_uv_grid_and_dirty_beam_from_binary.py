
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
arrayname = "[28-02-2020 18;33;23] 4Sat u-v Array for 1 weeks for source at 0 h and 00 deg.npy"
sourcename = "[28-02-2020 18;33;23] 4Sat Source Info for 1 weeks for source at 3 h and 00 deg.npy"

##Path definition
binpath = "C:\Users\User\Desktop\Thesis Part 1\Tests\Binary Files"
fullpatharray = os.path.join(binpath, arrayname)
fullpathsource = os.path.join(binpath, sourcename)

##Load npy files
(arrbu01, arrbv01, arrbu02, arrbv02, arrbu03, arrbv03, arrbu12, arrbv12, arrbu13, arrbv13, arrbu23, arrbv23) = np.load(fullpatharray)
(nsrc, nsrahr, nsramin, nsrasec, nsdecdeg, nsdecmin, nsdecsec) = np.load(fullpathsource)

##For coarse gridding of the u-v plane so as to measure the coverage quantitatively
size01 = len(arrbu01)
size02 = len(arrbu02)
size03 = len(arrbu03)
size12 = len(arrbu12)
size13 = len(arrbu13)
size23 = len(arrbu23)
cell = 100                      ##The size of each cell in the grid in km. The size can go below 100km for more finer grid but for some reason, the plotting in not being done as expected.

##For calculating percentage coverage of grid 
gridcount01 = 0
gridcount02 = 0
gridcount03 = 0
gridcount12 = 0
gridcount13 = 0
gridcount23 = 0
gridcounttot = 0

##Defining the grid as per the cell size for the plot due to satellites 0 and 1
grid = np.zeros(((30000/cell), (30000/cell)), dtype = int)

for i in range(0, size01):
    k = int(math.floor((arrbu01[i]/cell))) + (15000/cell)
    l = int(math.floor((arrbv01[i]/cell))) + (15000/cell)
    if grid[l][k] == 0:
        grid[l][k] = 1
        gridcount01 += 1
    else:
        grid[l][k] = 1

gridfig01 = plt.figure(figsize = (10,10))
grdifig01 = plt.imshow(grid, cmap = plt.cm.get_cmap('Purples', 2), origin = 'lower')
gridfig01 = plt.grid(True)
girdfig01 = plt.colorbar(ticks = [0, 1])
gridfig01 = plt.title('u-v Grid of Source %d at RA: %0.0f h %0.0f m %0.3f s and Dec: %0.0f deg %0.0f min %0.3f sec' % (nsrc, nsrahr, nsramin, nsrasec, nsdecdeg, nsdecmin, nsdecsec))
plt.xlim([0,300])
plt.ylim([0,300])
xlocs, xlabels = plt.xticks()
xlabels = [(((item)*100)-15000) for item in xlocs]
plt.xticks(xlocs, xlabels)
ylocs, ylabels = plt.yticks()
ylabels = [(((item)*100)-15000) for item in ylocs]
plt.yticks(ylocs, ylabels)
gridfig01 = plt.xlabel('u (km)')
gridfig01 = plt.ylabel('v (km)')
gridfig01 = plt.savefig('C:\Users\User\Desktop\Thesis Part 1\Tests\EPS Plots from Binary\[%s] 4Sat Coverage due to Sat 0 and Sat 1 - Uniformly Weighted for 2 weeks for source at %0.0f h and %0.0f deg.eps' % (sst, nsrahr, nsdecdeg), format = 'eps', bbox_inches = 'tight')

##Defining the grid as per the cell size for the plot due to satellites 0 and 2
grid = np.zeros(((30000/cell), (30000/cell)), dtype = int)

for i in range(0, size02):
    k = int(math.floor((arrbu02[i]/cell))) + (15000/cell)
    l = int(math.floor((arrbv02[i]/cell))) + (15000/cell)
    if grid[l][k] == 0:
        grid[l][k] = 1
        gridcount02 += 1
    else:
        grid[l][k] = 1

gridfig02 = plt.figure(figsize = (10,10))
grdifig02 = plt.imshow(grid, cmap = plt.cm.get_cmap('Blues', 2), origin = 'lower')
gridfig02 = plt.grid(True)
girdfig02 = plt.colorbar(ticks = [0, 1])
gridfig02 = plt.title('u-v Grid of Source %d at RA: %0.0f h %0.0f m %0.3f s and Dec: %0.0f deg %0.0f min %0.3f sec' % (nsrc, nsrahr, nsramin, nsrasec, nsdecdeg, nsdecmin, nsdecsec))
plt.xlim([0,300])
plt.ylim([0,300])
xlocs, xlabels = plt.xticks()
xlabels = [(((item)*100)-15000) for item in xlocs]
plt.xticks(xlocs, xlabels)
ylocs, ylabels = plt.yticks()
ylabels = [(((item)*100)-15000) for item in ylocs]
plt.yticks(ylocs, ylabels)
gridfig02 = plt.xlabel('u (km)')
gridfig02 = plt.ylabel('v (km)')
gridfig02 = plt.savefig('C:\Users\User\Desktop\Thesis Part 1\Tests\EPS Plots from Binary\[%s] 4Sat Coverage due to Sat 0 and Sat 2 - Uniformly Weighted for 2 weeks for source at %0.0f h and %0.0f deg.eps' % (sst, nsrahr, nsdecdeg), format = 'eps', bbox_inches = 'tight')

##Defining the grid as per the cell size for the plot due to satellites 0 and 3
grid = np.zeros(((30000/cell), (30000/cell)), dtype = int)

for i in range(0, size03):
    k = int(math.floor((arrbu03[i]/cell))) + (15000/cell)
    l = int(math.floor((arrbv03[i]/cell))) + (15000/cell)
    if grid[l][k] == 0:
        grid[l][k] = 1
        gridcount03 += 1
    else:
        grid[l][k] = 1

gridfig03 = plt.figure(figsize = (10,10))
grdifig03 = plt.imshow(grid, cmap = plt.cm.get_cmap('Greens', 2), origin = 'lower')
gridfig03 = plt.grid(True)
girdfig03 = plt.colorbar(ticks = [0, 1])
gridfig03 = plt.title('u-v Grid of Source %d at RA: %0.0f h %0.0f m %0.3f s and Dec: %0.0f deg %0.0f min %0.3f sec' % (nsrc, nsrahr, nsramin, nsrasec, nsdecdeg, nsdecmin, nsdecsec))
plt.xlim([0,300])
plt.ylim([0,300])
xlocs, xlabels = plt.xticks()
xlabels = [(((item)*100)-15000) for item in xlocs]
plt.xticks(xlocs, xlabels)
ylocs, ylabels = plt.yticks()
ylabels = [(((item)*100)-15000) for item in ylocs]
plt.yticks(ylocs, ylabels)
gridfig03 = plt.xlabel('u (km)')
gridfig03 = plt.ylabel('v (km)')
gridfig03 = plt.savefig('C:\Users\User\Desktop\Thesis Part 1\Tests\EPS Plots from Binary\[%s] 4Sat Coverage due to Sat 0 and Sat 3 - Uniformly Weighted for 2 weeks for source at %0.0f h and %0.0f deg.eps' % (sst, nsrahr, nsdecdeg), format = 'eps', bbox_inches = 'tight')

##Defining the grid as per the cell size for the plot due to satellites 1 and 2
grid = np.zeros(((30000/cell), (30000/cell)), dtype = int)

for i in range(0, size12):
    k = int(math.floor((arrbu12[i]/cell))) + (15000/cell)
    l = int(math.floor((arrbv12[i]/cell))) + (15000/cell)
    if grid[l][k] == 0:
        grid[l][k] = 1
        gridcount12 += 1
    else:
        grid[l][k] = 1

gridfig12 = plt.figure(figsize = (10,10))
grdifig12 = plt.imshow(grid, cmap = plt.cm.get_cmap('BuPu', 2), origin = 'lower')
gridfig12 = plt.grid(True)
girdfig12 = plt.colorbar(ticks = [0, 1])
gridfig12 = plt.title('u-v Grid of Source %d at RA: %0.0f h %0.0f m %0.3f s and Dec: %0.0f deg %0.0f min %0.3f sec' % (nsrc, nsrahr, nsramin, nsrasec, nsdecdeg, nsdecmin, nsdecsec))
plt.xlim([0,300])
plt.ylim([0,300])
xlocs, xlabels = plt.xticks()
xlabels = [(((item)*100)-15000) for item in xlocs]
plt.xticks(xlocs, xlabels)
ylocs, ylabels = plt.yticks()
ylabels = [(((item)*100)-15000) for item in ylocs]
plt.yticks(ylocs, ylabels)
gridfig12 = plt.xlabel('u (km)')
gridfig12 = plt.ylabel('v (km)')
gridfig12 = plt.savefig('C:\Users\User\Desktop\Thesis Part 1\Tests\EPS Plots from Binary\[%s] 4Sat Coverage due to Sat 1 and Sat 2 - Uniformly Weighted for 2 weeks for source at %0.0f h and %0.0f deg.eps' % (sst, nsrahr, nsdecdeg), format = 'eps', bbox_inches = 'tight')

##Defining the grid as per the cell size for the plot due to satellites 1 and 3
grid = np.zeros(((30000/cell), (30000/cell)), dtype = int)

for i in range(0, size13):
    k = int(math.floor((arrbu13[i]/cell))) + (15000/cell)
    l = int(math.floor((arrbv13[i]/cell))) + (15000/cell)
    if grid[l][k] == 0:
        grid[l][k] = 1
        gridcount13 += 1
    else:
        grid[l][k] = 1

gridfig13 = plt.figure(figsize = (10,10))
grdifig13 = plt.imshow(grid, cmap = plt.cm.get_cmap('Oranges', 2), origin = 'lower')
gridfig13 = plt.grid(True)
girdfig13 = plt.colorbar(ticks = [0, 1])
gridfig13 = plt.title('u-v Grid of Source %d at RA: %0.0f h %0.0f m %0.3f s and Dec: %0.0f deg %0.0f min %0.3f sec' % (nsrc, nsrahr, nsramin, nsrasec, nsdecdeg, nsdecmin, nsdecsec))
plt.xlim([0,300])
plt.ylim([0,300])
xlocs, xlabels = plt.xticks()
xlabels = [(((item)*100)-15000) for item in xlocs]
plt.xticks(xlocs, xlabels)
ylocs, ylabels = plt.yticks()
ylabels = [(((item)*100)-15000) for item in ylocs]
plt.yticks(ylocs, ylabels)
gridfig13 = plt.xlabel('u (km)')
gridfig13 = plt.ylabel('v (km)')
gridfig13 = plt.savefig('C:\Users\User\Desktop\Thesis Part 1\Tests\EPS Plots from Binary\[%s] 4Sat Coverage due to Sat 1 and Sat 3 - Uniformly Weighted for 2 weeks for source at %0.0f h and %0.0f deg.eps' % (sst, nsrahr, nsdecdeg), format = 'eps', bbox_inches = 'tight')

##Defining the grid as per the cell size for the plot due to satellites 2 and 3
grid = np.zeros(((30000/cell), (30000/cell)), dtype = int)

for i in range(0, size23):
    k = int(math.floor((arrbu23[i]/cell))) + (15000/cell)
    l = int(math.floor((arrbv23[i]/cell))) + (15000/cell)
    if grid[l][k] == 0:
        grid[l][k] = 1
        gridcount23 += 1
    else:
        grid[l][k] = 1

gridfig23 = plt.figure(figsize = (10,10))
grdifig23 = plt.imshow(grid, cmap = plt.cm.get_cmap('Reds', 2), origin = 'lower')
gridfig23 = plt.grid(True)
girdfig23 = plt.colorbar(ticks = [0, 1])
gridfig23 = plt.title('u-v Grid of Source %d at RA: %0.0f h %0.0f m %0.3f s and Dec: %0.0f deg %0.0f min %0.3f sec' % (nsrc, nsrahr, nsramin, nsrasec, nsdecdeg, nsdecmin, nsdecsec))
plt.xlim([0,300])
plt.ylim([0,300])
xlocs, xlabels = plt.xticks()
xlabels = [(((item)*100)-15000) for item in xlocs]
plt.xticks(xlocs, xlabels)
ylocs, ylabels = plt.yticks()
ylabels = [(((item)*100)-15000) for item in ylocs]
plt.yticks(ylocs, ylabels)
gridfig23 = plt.xlabel('u (km)')
gridfig23 = plt.ylabel('v (km)')
gridfig23 = plt.savefig('C:\Users\User\Desktop\Thesis Part 1\Tests\EPS Plots from Binary\[%s] 4Sat Coverage due to Sat 2 and Sat 3 - Uniformly Weighted for 2 weeks for source at %0.0f h and %0.0f deg.eps' % (sst, nsrahr, nsdecdeg), format = 'eps', bbox_inches = 'tight')


##Defining the grid as per the cell size for the plot due to all the satellites
grid = np.zeros(((30000/cell), (30000/cell)), dtype = int)

for i in range(0, size01):
    k = int(math.floor((arrbu01[i]/cell))) + (15000/cell)
    l = int(math.floor((arrbv01[i]/cell))) + (15000/cell)
    if grid[l][k] == 0:
        grid[l][k] = 1
        gridcounttot += 1
    else:
        grid[l][k] = 1

for i in range(0, size02):
    k = int(math.floor((arrbu02[i]/cell))) + (15000/cell)
    l = int(math.floor((arrbv02[i]/cell))) + (15000/cell)
    if grid[l][k] == 0:
        grid[l][k] = 1
        gridcounttot += 1
    else:
        grid[l][k] = 1       

for i in range(0, size03):
    k = int(math.floor((arrbu03[i]/cell))) + (15000/cell)
    l = int(math.floor((arrbv03[i]/cell))) + (15000/cell)
    if grid[l][k] == 0:
        grid[l][k] = 1
        gridcounttot += 1
    else:
        grid[l][k] = 1

for i in range(0, size12):
    k = int(math.floor((arrbu12[i]/cell))) + (15000/cell)
    l = int(math.floor((arrbv12[i]/cell))) + (15000/cell)
    if grid[l][k] == 0:
        grid[l][k] = 1
        gridcounttot += 1
    else:
        grid[l][k] = 1    

for i in range(0, size13):
    k = int(math.floor((arrbu13[i]/cell))) + (15000/cell)
    l = int(math.floor((arrbv13[i]/cell))) + (15000/cell)
    if grid[l][k] == 0:
        grid[l][k] = 1
        gridcounttot += 1
    else:
        grid[l][k] = 1

for i in range(0, size23):
    k = int(math.floor((arrbu23[i]/cell))) + (15000/cell)
    l = int(math.floor((arrbv23[i]/cell))) + (15000/cell)
    if grid[l][k] == 0:
        grid[l][k] = 1
        gridcounttot += 1
    else:
        grid[l][k] = 1

gridfigtot = plt.figure(figsize = (10,10))
grdifigtot = plt.imshow(grid, cmap = plt.cm.get_cmap('Greys', 2), origin = 'lower')
gridfigtot = plt.grid(True)
girdfigtot = plt.colorbar(ticks = [0, 1])
gridfigtot = plt.title('u-v Grid of Source %d at RA: %0.0f h %0.0f m %0.3f s and Dec: %0.0f deg %0.0f min %0.3f sec' % (nsrc, nsrahr, nsramin, nsrasec, nsdecdeg, nsdecmin, nsdecsec))
plt.xlim([0,300])
plt.ylim([0,300])
xlocs, xlabels = plt.xticks()
xlabels = [(((item)*100)-15000) for item in xlocs]
plt.xticks(xlocs, xlabels)
ylocs, ylabels = plt.yticks()
ylabels = [(((item)*100)-15000) for item in ylocs]
plt.yticks(ylocs, ylabels)
gridfigtot = plt.xlabel('u (km)')
gridfigtot = plt.ylabel('v (km)')
gridfigtot = plt.savefig('C:\Users\User\Desktop\Thesis Part 1\Tests\EPS Plots from Binary\[%s] 4Sat Coverage Total - Uniformly Weighted for 2 weeks for source at %0.0f h and %0.0f deg.eps' % (sst, nsrahr, nsdecdeg), format = 'eps', bbox_inches = 'tight')


print("The number of cells filled due to satellites 0 and 1: %d. Percentage coverage = %f" % (gridcount01, (gridcount01/706.85)))
print("The number of cells filled due to satellites 0 and 2: %d. Percentage coverage = %f" % (gridcount02, (gridcount02/706.85)))
print("The number of cells filled due to satellites 0 and 3: %d. Percentage coverage = %f" % (gridcount03, (gridcount03/706.85)))
print("The number of cells filled due to satellites 1 and 2: %d. Percentage coverage = %f" % (gridcount12, (gridcount12/706.85)))
print("The number of cells filled due to satellites 1 and 3: %d. Percentage coverage = %f" % (gridcount13, (gridcount13/706.85)))
print("The number of cells filled due to satellites 2 and 3: %d. Percentage coverage = %f" % (gridcount23, (gridcount23/706.85)))
print("The number of cells filled due to all three satellites: %d. Percentage coverage = %f" % (gridcounttot, gridcounttot/706.85))

##Doing 2D FFT on the grid due to all the satellites to get the dirty beam 
fftgrid = plt.figure(figsize = (10,10))
fftgrid = np.fft.ifft2(grid)
fftgrid = np.fft.fftshift(fftgrid)
fftimg = plt.imshow(np.abs(fftgrid), cmap = plt.cm.get_cmap('afmhot'), clim = [0, 0.01], origin = 'lower')
fftimg = plt.grid(False)
fftimg = plt.colorbar()
fftgrid = plt.title('Dirty Beam for Source %d at RA: %0.0f h %0.0f m %0.3f s and Dec: %0.0f deg %0.0f min %0.3f sec' % (nsrc, nsrahr, nsramin, nsrasec, nsdecdeg, nsdecmin, nsdecsec))
fftimg = plt.savefig('C:\Users\User\Desktop\Thesis Part 1\Tests\EPS Plots from Binary\[%s] 4Sat Dirty Beam - Uniformly Weighted for 2 weeks for source at %0.0f h and %0.0f deg.eps' % (sst, nsrahr, nsdecdeg), format = 'eps', bbox_inches = 'tight')


