    
from visual import *
from visual.graph import *
from math import *
import wx
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft2, ifft2
import time
import datetime
import winsound


##Timestamps
tss = time.time()
sst = datetime.datetime.fromtimestamp(tss).strftime('%d-%m-%Y %H;%M;%S')

##Defining the display window properties
w = window(width = 1500, height = 850, menus = True, title = 'System of Satellites', style = wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
scene = display(x = 15, y = 80, width = 1000, height = 750, label = 'Display Window')
scene.exit = False

##Creating buttons and sliders for input
p = w.panel
wx.StaticText(p, pos = (15,10), size = (1000,15), label = 'Visual Representation of the System', style=wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE)

def setrate(evt):
    value = slider.GetValue()

def setdefrate(evt):
    slider.SetValue(500)

def setmaxrate(evt):
    slider.SetValue(5000)

def hidewindow(evt):
    w.visible = False

def exitprogram(evt):
#    plt.figure(figsize = (10,10))
#    plt.scatter(arrbu01, arrbv01, color = 'purple', marker = 'o', s = 0.1, label = 'Baseline between Satellite 0 and Satellite 1')
#    plt.scatter(arrbu02, arrbv02, color = 'blue', marker = 'o', s = 0.1, label = 'Baseline between Satellite 0 and Satellite 2')
#    plt.scatter(arrbu03, arrbv03, color = 'green', marker = 'o', s = 0.1, label = 'Baseline between Satellite 0 and Satellite 3')
#    plt.scatter(arrbu12, arrbv12, color = 'yellow', marker = 'o', s = 0.1, label = 'Baseline between Satellite 1 and Satellite 2')
#    plt.scatter(arrbu13, arrbv13, color = 'orange', marker = 'o', s = 0.1, label = 'Baseline between Satellite 1 and Satellite 3')
#    plt.scatter(arrbu23, arrbv23, color = 'red', marker = 'o', s = 0.1, label = 'Baseline between Satellite 2 and Satellite 3')
#    plt.axis([-15000, 15000, -15000, 15000])
#    plt.title('u-v Plot of Source %d at RA: %0.0f h %0.0f m %0.3f s and Dec: %0.0f deg %0.0f min %0.3f sec' % (nsrc, nsrahr, nsramin, nsrasec, nsdecdeg, nsdecmin, nsdecsec))
#    plt.xlabel('u')
#    plt.ylabel('v')
#    #plt.legend()
#    plt.grid(True)
#    global save
#    plt.savefig('D:\Space Interferometer Project\Tests\PDF Plots from Live Run\[%s] u-v Plot %d.pdf' % (sst, save), bbox_inches = 'tight')
#    np.save('D:\Space Interferometer Project\Tests\Binary Files\[%s] u-v Array %d' % (sst, save), (arrbu01, arrbv01, arrbu02, arrbv02, arrbu03, arrbv03, arrbu12, arrbv12, arrbu13, arrbv13, arrbu23, arrbv23))
#    np.save('D:\Space Interferometer Project\Tests\Binary Files\[%s] Source Info %d' % (sst, save), (nsrc, nsrahr, nsramin, nsrasec, nsdecdeg, nsdecmin, nsdecsec))
#    save += 1
    
    print("[%s] \nThe system was shut down after running for %d seconds" % (sst, t - 1))
    print("A total of %d sources were observed" % (nsrc + 1))
    exit()

def printruntime(evt):
    print("[%s] \nThe system has been running for %d seconds" % (sst, t))

##Replotting the u-v graph using matplotlib and then saving it as a PDF
save = 0
def generatematplot(evt):
    plt.figure(figsize = (10,10))
    plt.scatter(arrbu01, arrbv01, color = 'purple', marker = 'o', s = 0.1, label = 'Baseline between Satellite 0 and Satellite 1')
    plt.scatter(arrbu02, arrbv02, color = 'blue', marker = 'o', s = 0.1, label = 'Baseline between Satellite 0 and Satellite 2')
    plt.scatter(arrbu03, arrbv03, color = 'green', marker = 'o', s = 0.1, label = 'Baseline between Satellite 0 and Satellite 3')
    plt.scatter(arrbu12, arrbv12, color = 'yellow', marker = 'o', s = 0.1, label = 'Baseline between Satellite 1 and Satellite 2')
    plt.scatter(arrbu13, arrbv13, color = 'orange', marker = 'o', s = 0.1, label = 'Baseline between Satellite 1 and Satellite 3')
    plt.scatter(arrbu23, arrbv23, color = 'red', marker = 'o', s = 0.1, label = 'Baseline between Satellite 2 and Satellite 3')
    plt.axis([-15800, 15800, -15800, 15800])
    plt.title('u-v Plot of Source %d at RA: %0.0f h %0.0f m %0.0f s and Dec: %0.0f deg %0.0f min %0.0f sec' % (nsrc, nsrahr, nsramin, nsrasec, nsdecdeg, nsdecmin, nsdecsec), fontsize = 14)
    plt.xlabel('u (km)', fontsize = 14)
    plt.ylabel('v (km)', fontsize = 14)
    plt.tick_params(labelsize = 14)
    #plt.legend()
    plt.grid(True)
    global save
    plt.savefig('D:\Space Interferometer Project\Tests\PDF Plots from Live Run\[%s] 4Sat u-v Plot with Hermitian for %d days for source at %0.0f hr and %0.0f deg.pdf' % (sst, day, nsrahr, nsdecdeg), bbox_inches = 'tight')
    np.save('D:\Space Interferometer Project\Tests\Binary Files\[%s] 4Sat u-v Array for %d days for source at %0.0f hr %0.0f deg' % (sst, day, nsrahr, nsdecdeg), (arrbu01, arrbv01, arrbu02, arrbv02, arrbu03, arrbv03, arrbu12, arrbv12, arrbu13, arrbv13, arrbu23, arrbv23))
    np.save('D:\Space Interferometer Project\Tests\Binary Files\[%s] 4Sat Source Info for %d days for source at %0.0f hr %0.0f deg' % (sst, day, nsrahr, nsdecdeg), (nsrc, nsrahr, nsramin, nsrasec, nsdecdeg, nsdecmin, nsdecsec))
    save += 1
    print("[%s] \nThe system has been running for %d seconds. Generating u-v plot..." % (sst, t - 1))

##For coarse gridding of the u-v plane so as to measure the coverage quantitatively
def pltcovergrid(evt):
    global arrbu01, arrbu02, arrbu03, arrbu12, arrbu13, arrbu23, arrbv01, arrbv02, arrbv03, arrbv12, arrbv13, arrbv23
    size01 = len(arrbu01)
    size02 = len(arrbu02)
    size03 = len(arrbu03)
    size12 = len(arrbu12)
    size13 = len(arrbu13)
    size23 = len(arrbu23)
    cell = 105                      ##The size of each cell in the grid in km. The size can go below 100km for more finer grid but for some reason, the plotting in not being done as expected.

##For calculating percentage coverage of grid 
    gridcount01 = 0
    gridcount02 = 0
    gridcount03 = 0
    gridcount12 = 0
    gridcount13 = 0
    gridcount23 = 0
    gridcounttot = 0

##Defining the grid as per the cell size for the plot due to satellites 0 and 1
    grid = np.zeros(((31500/cell), (31500/cell)), dtype = int)

    for i in range(0, size01):
        k = int(math.floor((arrbu01[i]/cell))) + (15750/cell)
        l = int(math.floor((arrbv01[i]/cell))) + (15750/cell)
        if grid[l][k] == 0:
            grid[l][k] = 1
            gridcount01 += 1
        else:
            grid[l][k] = 1

    gridfig01 = plt.figure(figsize = (10,10))
    grdifig01 = plt.imshow(grid, cmap = plt.cm.get_cmap('Purples', 2), origin = 'lower')
    gridfig01 = plt.grid(True)
    girdfig01 = plt.colorbar(ticks = [0, 1])
    gridfig1 = plt.title('u-v Grid of Source %d at RA: %0.0f h %0.0f m %0.0f s and Dec: %0.0f deg %0.0f min %0.0f sec' % (nsrc, nsrahr, nsramin, nsrasec, nsdecdeg, nsdecmin, nsdecsec), fontsize = 13)
    plt.xlim([0,300])
    plt.ylim([0,300])
    xlocs, xlabels = plt.xticks()
    xlabels = [(int(((item)*105)-15750)) for item in xlocs]
    plt.xticks(xlocs, xlabels)
    ylocs, ylabels = plt.yticks()
    ylabels = [(int(((item)*105)-15750)) for item in ylocs]
    plt.yticks(ylocs, ylabels)
    gridfig1 = plt.xlabel('u (km)', fontsize = 13)
    gridfig1 = plt.ylabel('v (km)', fontsize = 13)
    plt.tick_params(labelsize = 14)
    gridfig1 = plt.savefig('D:\Space Interferometer Project\Tests\PDF Plots from Live Run\[%s] 4Sat Coverage due to Sat 0 and Sat 1 - Uniformly Weighted for %d days for source at %0.0f h and %0.0f deg.pdf' % (sst, day, nsrahr, nsdecdeg), bbox_inches = 'tight')


##Defining the grid as per the cell size for the plot due to satellites 0 and 2
    grid = np.zeros(((31500/cell), (31500/cell)), dtype = int)

    for i in range(0, size02):
        k = int(math.floor((arrbu02[i]/cell))) + (15750/cell)
        l = int(math.floor((arrbv02[i]/cell))) + (15750/cell)
        if grid[l][k] == 0:
            grid[l][k] = 1
            gridcount02 += 1
        else:
            grid[l][k] = 1

    gridfig02 = plt.figure(figsize = (10,10))
    grdifig02 = plt.imshow(grid, cmap = plt.cm.get_cmap('Blues', 2), origin = 'lower')
    gridfig02 = plt.grid(True)
    girdfig02 = plt.colorbar(ticks = [0, 1])
    gridfig02 = plt.title('u-v Grid of Source %d at RA: %0.0f h %0.0f m %0.0f s and Dec: %0.0f deg %0.0f min %0.0f sec' % (nsrc, nsrahr, nsramin, nsrasec, nsdecdeg, nsdecmin, nsdecsec), fontsize = 13)
    plt.xlim([0,300])
    plt.ylim([0,300])
    xlocs, xlabels = plt.xticks()
    xlabels = [(int(((item)*105)-15750)) for item in xlocs]
    plt.xticks(xlocs, xlabels)
    ylocs, ylabels = plt.yticks()
    ylabels = [(int(((item)*105)-15750)) for item in ylocs]
    plt.yticks(ylocs, ylabels)
    gridfig02 = plt.xlabel('u (km)', fontsize = 13)
    gridfig02 = plt.ylabel('v (km)', fontsize = 13)
    plt.tick_params(labelsize = 14)
    gridfig20 = plt.savefig('D:\Space Interferometer Project\Tests\PDF Plots from Live Run\[%s] 4Sat Coverage due to Sat 0 and Sat 2 - Uniformly Weighted for %d days for source at %0.0f h and %0.0f deg.pdf' % (sst, day, nsrahr, nsdecdeg), bbox_inches = 'tight')


##Defining the grid as per the cell size for the plot due to satellites 0 and 3
    grid = np.zeros(((31500/cell), (31500/cell)), dtype = int)

    for i in range(0, size03):
        k = int(math.floor((arrbu03[i]/cell))) + (15750/cell)
        l = int(math.floor((arrbv03[i]/cell))) + (15750/cell)
        if grid[l][k] == 0:
            grid[l][k] = 1
            gridcount03 += 1
        else:
            grid[l][k] = 1

    gridfig03 = plt.figure(figsize = (10,10))
    grdifig03 = plt.imshow(grid, cmap = plt.cm.get_cmap('Greens', 2), origin = 'lower')
    gridfig03 = plt.grid(True)
    girdfig03 = plt.colorbar(ticks = [0, 1])
    gridfig03 = plt.title('u-v Grid of Source %d at RA: %0.0f h %0.0f m %0.0f s and Dec: %0.0f deg %0.0f min %0.0f sec' % (nsrc, nsrahr, nsramin, nsrasec, nsdecdeg, nsdecmin, nsdecsec), fontsize = 13)
    plt.xlim([0,300])
    plt.ylim([0,300])
    xlocs, xlabels = plt.xticks()
    xlabels = [(int(((item)*105)-15750)) for item in xlocs]
    plt.xticks(xlocs, xlabels)
    ylocs, ylabels = plt.yticks()
    ylabels = [(int(((item)*105)-15750)) for item in ylocs]
    plt.yticks(ylocs, ylabels)
    gridfig03 = plt.xlabel('u (km)', fontsize = 13)
    gridfig03 = plt.ylabel('v (km)', fontsize = 13)
    plt.tick_params(labelsize = 14)
    gridfig03 = plt.savefig('D:\Space Interferometer Project\Tests\PDF Plots from Live Run\[%s] 4Sat Coverage due to Sat 0 and Sat 3 - Uniformly Weighted for %d days for source at %0.0f h and %0.0f deg.pdf' % (sst, day, nsrahr, nsdecdeg), bbox_inches = 'tight')


##Defining the grid as per the cell size for the plot due to satellites 1 and 2
    grid = np.zeros(((31500/cell), (31500/cell)), dtype = int)

    for i in range(0, size12):
        k = int(math.floor((arrbu12[i]/cell))) + (15750/cell)
        l = int(math.floor((arrbv12[i]/cell))) + (15750/cell)
        if grid[l][k] == 0:
            grid[l][k] = 1
            gridcount12 += 1
        else:
            grid[l][k] = 1

    gridfig12 = plt.figure(figsize = (10,10))
    grdifig12 = plt.imshow(grid, cmap = plt.cm.get_cmap('BuPu', 2), origin = 'lower')
    gridfig12 = plt.grid(True)
    girdfig12 = plt.colorbar(ticks = [0, 1])
    gridfig12 = plt.title('u-v Grid of Source %d at RA: %0.0f h %0.0f m %0.0f s and Dec: %0.0f deg %0.0f min %0.0f sec' % (nsrc, nsrahr, nsramin, nsrasec, nsdecdeg, nsdecmin, nsdecsec), fontsize = 13)
    plt.xlim([0,300])
    plt.ylim([0,300])
    xlocs, xlabels = plt.xticks()
    xlabels = [(int(((item)*105)-15750)) for item in xlocs]
    plt.xticks(xlocs, xlabels)
    ylocs, ylabels = plt.yticks()
    ylabels = [(int(((item)*105)-15750)) for item in ylocs]
    plt.yticks(ylocs, ylabels)
    gridfig12 = plt.xlabel('u (km)', fontsize = 13)
    gridfig12 = plt.ylabel('v (km)', fontsize = 13)
    plt.tick_params(labelsize = 14)
    gridfig12 = plt.savefig('D:\Space Interferometer Project\Tests\PDF Plots from Live Run\[%s] 4Sat Coverage due to Sat 1 and Sat 2 - Uniformly Weighted for %d days for source at %0.0f h and %0.0f deg.pdf' % (sst, day, nsrahr, nsdecdeg), bbox_inches = 'tight')


##Defining the grid as per the cell size for the plot due to satellites 1 and 3
    grid = np.zeros(((31500/cell), (31500/cell)), dtype = int)

    for i in range(0, size13):
        k = int(math.floor((arrbu13[i]/cell))) + (15750/cell)
        l = int(math.floor((arrbv13[i]/cell))) + (15750/cell)
        if grid[l][k] == 0:
            grid[l][k] = 1
            gridcount13 += 1
        else:
            grid[l][k] = 1

    gridfig13 = plt.figure(figsize = (10,10))
    grdifig13 = plt.imshow(grid, cmap = plt.cm.get_cmap('Oranges', 2), origin = 'lower')
    gridfig13 = plt.grid(True)
    girdfig13 = plt.colorbar(ticks = [0, 1])
    gridfig13 = plt.title('u-v Grid of Source %d at RA: %0.0f h %0.0f m %0.0f s and Dec: %0.0f deg %0.0f min %0.0f sec' % (nsrc, nsrahr, nsramin, nsrasec, nsdecdeg, nsdecmin, nsdecsec), fontsize = 13)
    plt.xlim([0,300])
    plt.ylim([0,300])
    xlocs, xlabels = plt.xticks()
    xlabels = [(int(((item)*105)-15750)) for item in xlocs]
    plt.xticks(xlocs, xlabels)
    ylocs, ylabels = plt.yticks()
    ylabels = [(int(((item)*105)-15750)) for item in ylocs]
    plt.yticks(ylocs, ylabels)
    gridfig13 = plt.xlabel('u (km)', fontsize = 13)
    gridfig13 = plt.ylabel('v (km)', fontsize = 13)
    plt.tick_params(labelsize = 14)
    gridfig13 = plt.savefig('D:\Space Interferometer Project\Tests\PDF Plots from Live Run\[%s] 4Sat Coverage due to Sat 1 and Sat 3 - Uniformly Weighted for %d days for source at %0.0f h and %0.0f deg.pdf' % (sst, day, nsrahr, nsdecdeg), bbox_inches = 'tight')


##Defining the grid as per the cell size for the plot due to satellites 2 and 3
    grid = np.zeros(((31500/cell), (31500/cell)), dtype = int)

    for i in range(0, size23):
        k = int(math.floor((arrbu23[i]/cell))) + (15750/cell)
        l = int(math.floor((arrbv23[i]/cell))) + (15750/cell)
        if grid[l][k] == 0:
            grid[l][k] = 1
            gridcount23 += 1
        else:
            grid[l][k] = 1

    gridfig23 = plt.figure(figsize = (10,10))
    grdifig23 = plt.imshow(grid, cmap = plt.cm.get_cmap('Reds', 2), origin = 'lower')
    gridfig23 = plt.grid(True)
    girdfig23 = plt.colorbar(ticks = [0, 1])
    gridfig23 = plt.title('u-v Grid of Source %d at RA: %0.0f h %0.0f m %0.0f s and Dec: %0.0f deg %0.0f min %0.0f sec' % (nsrc, nsrahr, nsramin, nsrasec, nsdecdeg, nsdecmin, nsdecsec), fontsize = 13)
    plt.xlim([0,300])
    plt.ylim([0,300])
    xlocs, xlabels = plt.xticks()
    xlabels = [(int(((item)*105)-15750)) for item in xlocs]
    plt.xticks(xlocs, xlabels)
    ylocs, ylabels = plt.yticks()
    ylabels = [(int(((item)*105)-15750)) for item in ylocs]
    plt.yticks(ylocs, ylabels)
    gridfig23 = plt.xlabel('u (km)', fontsize = 13)
    gridfig23 = plt.ylabel('v (km)', fontsize = 13)
    plt.tick_params(labelsize = 14)
    gridfig23 = plt.savefig('D:\Space Interferometer Project\Tests\PDF Plots from Live Run\[%s] 4Sat Coverage due to Sat 2 and Sat 3 - Uniformly Weighted for %d days for source at %0.0f h and %0.0f deg.pdf' % (sst, day, nsrahr, nsdecdeg), bbox_inches = 'tight')


##Defining the grid as per the cell size for the plot due to all the satellites
    grid = np.zeros(((31500/cell), (31500/cell)), dtype = int)

    for i in range(0, size01):
        k = int(math.floor((arrbu01[i]/cell))) + (15750/cell)
        l = int(math.floor((arrbv01[i]/cell))) + (15750/cell)
        if grid[l][k] == 0:
            grid[l][k] = 1
            gridcounttot += 1
        else:
            grid[l][k] = 1

    for i in range(0, size02):
        k = int(math.floor((arrbu02[i]/cell))) + (15750/cell)
        l = int(math.floor((arrbv02[i]/cell))) + (15750/cell)
        if grid[l][k] == 0:
            grid[l][k] = 1
            gridcounttot += 1
        else:
            grid[l][k] = 1       

    for i in range(0, size03):
        k = int(math.floor((arrbu03[i]/cell))) + (15750/cell)
        l = int(math.floor((arrbv03[i]/cell))) + (15750/cell)
        if grid[l][k] == 0:
            grid[l][k] = 1
            gridcounttot += 1
        else:
            grid[l][k] = 1

    for i in range(0, size12):
        k = int(math.floor((arrbu12[i]/cell))) + (15750/cell)
        l = int(math.floor((arrbv12[i]/cell))) + (15750/cell)
        if grid[l][k] == 0:
            grid[l][k] = 1
            gridcounttot += 1
        else:
            grid[l][k] = 1    

    for i in range(0, size13):
        k = int(math.floor((arrbu13[i]/cell))) + (15750/cell)
        l = int(math.floor((arrbv13[i]/cell))) + (15750/cell)
        if grid[l][k] == 0:
            grid[l][k] = 1
            gridcounttot += 1
        else:
            grid[l][k] = 1

    for i in range(0, size23):
        k = int(math.floor((arrbu23[i]/cell))) + (15750/cell)
        l = int(math.floor((arrbv23[i]/cell))) + (15750/cell)
        if grid[l][k] == 0:
            grid[l][k] = 1
            gridcounttot += 1
        else:
            grid[l][k] = 1

    gridfigtot = plt.figure(figsize = (10,10))
    grdifigtot = plt.imshow(grid, cmap = plt.cm.get_cmap('Greys', 2), origin = 'lower')
    gridfigtot = plt.grid(True)
    girdfigtot = plt.colorbar(ticks = [0, 1])
    gridfigtot = plt.title('u-v Grid of Source %d at RA: %0.0f h %0.0f m %0.0f s and Dec: %0.0f deg %0.0f min %0.0f sec' % (nsrc, nsrahr, nsramin, nsrasec, nsdecdeg, nsdecmin, nsdecsec), fontsize = 13)
    plt.xlim([0,300])
    plt.ylim([0,300])
    xlocs, xlabels = plt.xticks()
    xlabels = [(int(((item)*105)-15750)) for item in xlocs]
    plt.xticks(xlocs, xlabels)
    ylocs, ylabels = plt.yticks()
    ylabels = [(int(((item)*105)-15750)) for item in ylocs]
    plt.yticks(ylocs, ylabels)
    gridfigtot = plt.xlabel('u (km)', fontsize = 13)
    gridfigtot = plt.ylabel('v (km)', fontsize = 13)
    plt.tick_params(labelsize = 14)
    gridfigtot = plt.savefig('D:\Space Interferometer Project\Tests\PDF Plots from Live Run\[%s] 4Sat Coverage Total - Uniformly Weighted for %d days for source at %0.0f h and %0.0f deg.pdf' % (sst, day, nsrahr, nsdecdeg), bbox_inches = 'tight')

    
    print("[%s] \nThe system has been running for %d seconds. Plotting coverage and dirty beam..." % (sst, t - 1))
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
    plt.xlim([0,300])
    plt.ylim([0,300])
    plt.tick_params(labelsize = 14)
    #plt.tick_params(labelbottom = False)
    #plt.tick_params(labelleft = False)
    fftgrid = plt.title('Dirty Beam for Source %d at RA: %0.0f h %0.0f m %0.0f s and Dec: %0.0f deg %0.0f min %0.0f sec' % (nsrc, nsrahr, nsramin, nsrasec, nsdecdeg, nsdecmin, nsdecsec))
    fftimg = plt.savefig('D:\Space Interferometer Project\Tests\PDF Plots from Live Run\[%s] 4Sat Dirty Beam - Uniformly Weighted for %d days for source at %0.0f h and %0.0f deg.pdf' % (sst, day, nsrahr, nsdecdeg), bbox_inches = 'tight')
    #print(fftgrid)


    

slider = wx.Slider(p, pos=(1050,35), size=(400,20), minValue=1, maxValue=5000)
wx.StaticText(p, pos = (1200,15), size = (1000,15), label = 'Set Rate of System')
wx.StaticText(p, pos = (1055,55), size = (15,15), label = '1')
wx.StaticText(p, pos = (1090,55), size = (25,15), label = '500')
wx.StaticText(p, pos = (1430,55), size = (30,15), label = '5000')

slider.Bind(wx.EVT_SCROLL, setrate)
slider.SetValue(500)

defrate = wx.Button(p, label = 'Set Default Rate', pos = (1140,70))
defrate.Bind(wx.EVT_BUTTON, setdefrate)

defmrate = wx.Button(p, label = 'Set Max Rate', pos = (1260,70))
defmrate.Bind(wx.EVT_BUTTON, setmaxrate)

runtime = wx.Button(p, label = 'Print Run Time', pos = (1050,710))
runtime.Bind(wx.EVT_BUTTON, printruntime)

plotcov = wx.Button(p, label = 'Plot Coverage', pos = (1050,750))
plotcov.Bind(wx.EVT_BUTTON, pltcovergrid)

exitwin = wx.Button(p, label = 'Exit Program', pos = (1375,750))
exitwin.Bind(wx.EVT_BUTTON, exitprogram)

genmatplt = wx.Button(p, label = 'Save u-v Plot', pos = (1373,710))
genmatplt.Bind(wx.EVT_BUTTON, generatematplot)


##Legend for user help
wx.StaticText(p, pos = (1050,120), size = (1000,15), label = '**Display Actions**')
wx.StaticText(p, pos = (1050,135), size = (1000,15), label = 'Right Click and move to change viewing angle')
wx.StaticText(p, pos = (1050,150), size = (1000,15), label = 'Alt + Left Click and move for zoom')
wx.StaticText(p, pos = (1050,165), size = (1000,15), label = 'Alt for pause and play. Left Click to pause for 5 seconds')
wx.StaticText(p, pos = (1050,180), size = (1000,15), label = 'Close Display Window to improve performance')

##Text boxes to input source position. Source 0 is already set
wx.StaticText(p, pos = (1050,210), size = (200,15), label = 'Input RA and Dec of Source:')

wx.StaticText(p, pos = (1050,232), size = (20,15), label = 'RA:')
rahr = wx.TextCtrl(p, pos = (1075, 230), size = (30,20), value = '0')
wx.StaticText(p, pos = (1110,232), size = (15,15), label = 'h')
ramin = wx.TextCtrl(p, pos = (1125, 230), size = (30,20), value = '0')
wx.StaticText(p, pos = (1160,232), size = (15,15), label = 'm')
rasec = wx.TextCtrl(p, pos = (1175, 230), size = (30,20), value = '0')
wx.StaticText(p, pos = (1210,232), size = (15,15), label = 's')

wx.StaticText(p, pos = (1240,232), size = (25,15), label = 'Dec:')
decdeg = wx.TextCtrl(p, pos = (1270, 230), size = (30,20), value = '0')
wx.StaticText(p, pos = (1305,232), size = (20,15), label = 'deg')
decmin = wx.TextCtrl(p, pos = (1330, 230), size = (30,20), value = '0')
wx.StaticText(p, pos = (1365,232), size = (20,15), label = 'min')
decsec = wx.TextCtrl(p, pos = (1390, 230), size = (30,20), value = '0')
wx.StaticText(p, pos = (1425,232), size = (20,15), label = 'sec')

##Text boxes to input source distance. Source 0 is already set
wx.StaticText(p, pos = (1050, 268), size = (150,20), label = 'Input Distance of Source:')
sourcedist = wx.TextCtrl(p, pos = (1200, 265), size = (90,20), value = '1000000000')
wx.StaticText(p, pos = (1295, 268), size = (20,20), label = 'AU')

##Button to update the source after input
upd = 1
nsrc = 0                            ##Number of sources surveyed
def updatesource(evt):
    global upd
    global nsrc
    upd = 1
    nsrc += 1

updatepos = wx.Button(p, label = 'Update Source', pos = (1350,270))
updatepos.Bind(wx.EVT_BUTTON, updatesource)

##Button and text box to input maximum run time
wx.StaticText(p, pos = (1230,695), size = (150,15), label = 'Max Run Time:')
maxruntime = wx.TextCtrl(p, pos = (1230, 720), size = (60,20), value = '1209600')
wx.StaticText(p, pos = (1295,722), size = (20,15), label = 'sec')

upd2 = 0
def updatemaxruntime(evt):
    global upd2
    upd2 = 1

updatemaxrt = wx.Button(p, label = 'Update Value', pos = (1225,750))
updatemaxrt.Bind(wx.EVT_BUTTON, updatemaxruntime)


##All positions and distances are measured in km. All time units are measured in seconds. All mass units are measured in kg

##The axial tilt of earth is taken to be 23.4 degrees, which is roughly the current value.
##But, as the earth is the center in this model, so instead of tilting the earth, which would have made it too complicated, the sun's position and thus, the plane of revoluton of earth has been tilted suitably.
theta = (23.4)*(pi/180)                     ##23.4 degrees in radians

sund = 146.6e6                              ##Distance of sun from earth is 146.6e6 km = 1 AU
sunx = sund*cos(theta)                      ##x-coordinate of sun after accounting for tilt
suny = sund*sin(theta)                      ##y-coordinate of sun after accounting for tilt

sat0phase = (45)*(pi/180)                   ##Initial phase of satellite 0
sat1phase = (45)*(pi/180)                   ##Initial phase of satellite 1
sat2phase = (90)*(pi/180)                   ##Initial phase of satellite 2
sat3phase = (90)*(pi/180)                   ##Initial phase of satellite 3

sat0dist = 770                              ##Distance above earth surface in km for satellite 0
sat1dist = 980                              ##Distance above earth surface in km for satellite 1
sat2dist = 1190                             ##Distance above earth surface in km for satellite 2
sat3dist = 1400                             ##Distance above earth surface in km for satellite 3


sun = sphere(pos = vector(-sunx,-suny,0), radius = 695700, material = materials.emissive, color = color.orange, opacity = 0.8)                                              ##Sun is in the 3rd quadrant initially, so x and y-coordinates are in negative
earth = sphere(pos = vector(0,0,0), radius = 6371, material = materials.earth, make_trail = True, retain = 10000, trail_type = "curve", opacity = 0.4)

sat0x = (earth.radius + sat0dist)*cos(sat0phase)                    ##x-coordinate of satellite 0 after accounting for phase
sat0z = (earth.radius + sat0dist)*sin(sat0phase)                    ##z-coordinate of satellite 0 after accounting for phase

sat1x = (earth.radius + sat1dist)*cos(sat1phase)                    ##x-coordinate of satellite 1 after accounting for phase
sat1z = (earth.radius + sat1dist)*sin(sat1phase)                    ##z-coordinate of satellite 1 after accounting for phase

sat2x = (earth.radius + sat2dist)*cos(sat2phase)                    ##x-coordinate of satellite 2 after accounting for phase
sat2y = (earth.radius + sat2dist)*sin(sat2phase)                    ##y-coordinate of satellite 2 after accounting for phase

sat3z = (earth.radius + sat3dist)*cos(sat3phase)                    ##z-coordinate of satellite 3 after accounting for phase
sat3y = (earth.radius + sat3dist)*sin(sat3phase)                    ##y-coordinate of satellite 3 after accounting for phase

sat0 = sphere(pos = vector(sat1x,0,sat1z), radius = 100, color = color.orange, make_trail = True, retain = 2000, trail_type = "curve")                        ##New satellite at a height of 429 km
sat1 = sphere(pos = vector(sat1x,0,sat1z), radius = 100, color = color.red, make_trail = True, retain = 2000, trail_type = "curve")                           ##New satellite at a height of 629 km
sat2 = sphere(pos = vector(sat2x,sat2y,0), radius = 100, color = color.blue, make_trail = True, retain = 2000, trail_type = "curve")                          ##Polar satellite at a height of 829 km
sat3 = sphere(pos = vector(0,sat3y,sat3z), radius = 100, color = color.green, make_trail = True, retain = 2000, trail_type = "curve")                         ##Polar satellite at a height of 1129 km

sunlight = local_light(pos = sun.pos, color = color.yellow)                                                                                                                 ##Sunlight simulation       

##Axis of earth and the satellites
earthaxis = cylinder(pos = vector(0,-7000,0), radius = 100, length = 14000, axis = vector(0,1,0), color = color.white, center = earth.pos, opacity = 0.5)
##sat0axis = cylinder(pos = vector(-7000/math.sqrt(3),-7000/math.sqrt(3),7000/math.sqrt(3)), radius = 50, length = 14000, axis = vector(1/math.sqrt(3),1/math.sqrt(3),-1/math.sqrt(3)), color = sat0.color, center = earth.pos)
sat0axis = cylinder(pos = vector(-3500,-7000/math.sqrt(2),3500), radius = 50, length = 14000, axis = vector(0.5,1/math.sqrt(2),-0.5), color = sat0.color, center = earth.pos)
##sat1axis = cylinder(pos = vector(7000/math.sqrt(3),-7000/math.sqrt(3),-7000/math.sqrt(3)), radius = 50, length = 14000, axis = vector(-1/math.sqrt(3),1/math.sqrt(3),1/math.sqrt(3)), color = sat1.color, center = earth.pos)
sat1axis = cylinder(pos = vector(3500,-7000/math.sqrt(2),-3500), radius = 50, length = 14000, axis = vector(-0.5,1/math.sqrt(2),0.5), color = sat1.color, center = earth.pos)
sat2axis = cylinder(pos = vector(0,0,-7000), radius = 50, length = 14000, axis = vector(0,0,1), color = sat2.color, center = earth.pos)
sat3axis = cylinder(pos = vector(-7000,0,0), radius = 50, length = 14000, axis = vector(1,0,0), color = sat3.color, center = earth.pos)

##Representational field of views of satellites
sat0field = cylinder(pos = sat0.pos, radius = 12000, opacity = 0.03, color = sat0.color)                ##Field of view/beam angle - full hemisphere for now
sat1field = cylinder(pos = sat1.pos, radius = 12000, opacity = 0.03, color = sat1.color)                ##Field of view/beam angle - full hemisphere for now
sat2field = cylinder(pos = sat2.pos, radius = 12000, opacity = 0.03, color = sat2.color)                ##Field of view/beam angle - full hemisphere for now
sat3field = cylinder(pos = sat3.pos, radius = 12000, opacity = 0.03, color = sat3.color)                ##Field of view/beam angle - full hemisphere for now


##Defining the source position on the celestial sphere. 
nsourcedist = 1.5e17                                                                                                                              ##Initial distance of the point source in km (Equal to 10^9 AU and 15800 ly)
sourcex = 0                                                                                                                                       ##Initial x-coordinate of source
sourcey = 0                                                                                                                                       ##Initial y-coordinate of source
sourcez = nsourcedist                                                                                                                             ##Initial z-coordinate of source
sourcepos = vector(sourcex,sourcey,sourcez)                                                                                                       ##Initial position of the point source on the celestial sphere.
sourcedir = cylinder(pos = earth.pos, radius = 20, length = 3e4, axis = sourcepos-earth.pos, color = color.magenta)                               ##Laser pointer pointing towards the source


sun.mass = 1.989e30                                     ##Mass of sun in kg
earth.mass = 5.982e24                                   ##Mass of earth in kg
#sat1.mass = 3e3                                         ##Mass of satellite in kg (unnecessary)
#sat2.mass = 3e3                                         ##Mass of satellite in kg (unnecessary)
#sat3.mass = 3e3                                         ##Mass of satellite in kg (unnecessary)


G = 6.674e-20                                           ##Universal gravitational constant in km^3 kg^-1 s^-2


##Calculating the initial speed of satellite based on the distance from earth's surface in km/s. v = sqrt(G*M/r)
sat0.speed = math.sqrt((G*earth.mass)/(earth.radius+sat0dist))
sat1.speed = math.sqrt((G*earth.mass)/(earth.radius+sat1dist))          
sat2.speed = math.sqrt((G*earth.mass)/(earth.radius+sat2dist))
sat3.speed = math.sqrt((G*earth.mass)/(earth.radius+sat3dist))

##Initial speed of earth around the sun in km/s
earth.speed = math.sqrt((G*sun.mass)/sund)

##Time period of the satellites based on the speed and distance from earth's surface. T = 2*pi*r/v
sat0.period = 2*pi*(earth.radius+sat0dist)/sat0.speed
sat1.period = 2*pi*(earth.radius+sat1dist)/sat1.speed
sat2.period = 2*pi*(earth.radius+sat2dist)/sat2.speed
sat3.period = 2*pi*(earth.radius+sat3dist)/sat3.speed
                  
##Direction of motion of satellite
sat0dir = (np.cross(sat0.pos, sat0axis.axis))/(np.linalg.norm(np.cross(sat0.pos, sat0axis.axis)))
sat1dir = (np.cross(sat1.pos, sat1axis.axis))/(np.linalg.norm(np.cross(sat1.pos, sat1axis.axis)))
sat2dir = (np.cross(sat2.pos, sat2axis.axis))/(np.linalg.norm(np.cross(sat2.pos, sat2axis.axis)))
sat3dir = (np.cross(sat3.pos, sat3axis.axis))/(np.linalg.norm(np.cross(sat3.pos, sat3axis.axis)))

earth.v = vector(0,0,-earth.speed)                                        ##Initial velocity of earth in km/s (at perihelion)
sat0.v = sat0.speed*sat0dir + earth.v                                     ##Initial velocity of satellite 0 in km/s
sat1.v = sat1.speed*sat1dir + earth.v                                     ##Initial velocity of satellite 1 in km/s
sat2.v = sat2.speed*sat2dir + earth.v                                     ##Initial velocity of satellite 2 in km/s
sat3.v = sat3.speed*sat3dir + earth.v                                     ##Initial velocity of satellite 3 in km/s


##Info printed at the start of the program for user
print("[%s] \nRunning the program: Test with uniformly weighted grid for coverage and dirty beam with Hermitian nature with 10 second plotting including Matplotlib without fixed celestial sphere and with constantly updating source for a 4 satellite system all corrected while avoinding ionospheric effects\n\nSatellite 0 is at a height of %0.1f km, having an initial speed of %0.3f km/s and a period of %0.3f s \nSatellite 1 is at a height of %0.1f km, having an initial speed of %0.3f km/s and a period of %0.3f s \nSatellite 2 is at a height of %0.1f km, having an initial speed of %0.3f km/s and a period of %0.3f s \nSatellite 3 is at a height of %0.1f km, having an initial speed of %0.3f km/s and a period of %0.3f s \n" % (sst, sat0dist, sat0.speed, sat0.period, sat1dist, sat1.speed, sat1.period, sat2dist, sat2.speed, sat2.period, sat3dist, sat3.speed, sat3.period))

##Tried to define functions for satellite orbits but was not working as expected. Will check later if required
#def satorbit(sat_x, sat_y, sat_z, sat_pos, sat_v):
#    r = ((sat_x-earth.x)**2 + (sat_y-earth.y)**2 + (sat_z-earth.z)**2)**0.5         ##distance between satellite and earth
#    rv = (earth.pos-sat_pos)/r                                                      ##radial vector
#    Fa = ((G*earth.mass)/r**2)*rv                                                   ##Acceleration due to graviaitonal force
#    sat_v += Fa
#    sat_pos += sat_v
#
#def satfieldfollow(satfield_pos, satfield_axis, satfield_length, sat_pos):
#    satfield_pos = sat_pos
#    satfield_axis = sat_pos-earth.pos
#    satfield_length = 50


##Commented out as not required for the moment
##For plotting the speed/position variations of satellites
#gd = gdisplay(x = 800, y = 0, width = 600, height = 600, foreground = color.black, background = color.white, xmax = 50000, xmin = 0, ymax = 7.8, ymin = 7.1)
#f1 = gcurve(color = color.red)
#f2 = gcurve(color = color.blue)
#f3 = gcurve(color = color.green)


##Defining the unit vectors for u-v plots
uunitvec = vector(0,1,0)
vunitvec = vector(0,0,1)

##Creating empty arrays to fill with the u-v values 
arrbu01 = []
arrbv01 = []
arrbu02 = []
arrbv02 = []
arrbu03 = []
arrbv03 = []
arrbu12 = []
arrbv12 = []
arrbu13 = []
arrbv13 = []
arrbu23 = []
arrbv23 = []

track = 0               ##To measure is the satellites are tracking the source or not. Not being used currently
t = 0                   ##To measure the runtime of the system
deltat = 1              ##Number of seconds per frame. Do not change it over 10, as after that the system starts to malfunction. Unless more speed is required, it is best to leave this at 1.
Nt = 10                 ##To plot the graph every N seconds
day = 0                 ##To measure runtime in days
week = 0                ##To measure runtime in weeks
month = 0               ##To measure runtime in months
tmax = 1382400          ##Default value of max run time, unless user inputs otherwise
#tsat1sun = 0
#tsat2sun = 0
#tsat3sun = 0

print("The system will run for a maximum time of %d seconds\n\n" % (tmax))


run = True

while run:
    rate(slider.GetValue())

##To pause the scene. A left click on the screen would pause the scene for 5 seconds, by default. Change sleep duration to change the pause time
    if scene.mouse.events:
        m = scene.mouse.getevent()
        if m.click == 'left':
            run = not run
            sleep(5)
            run = not run
            
    earth.rotate(angle = deltat*2*pi/(24*60*60), axis = vector(0,1,0), origin = earth.pos)                 ##For earth's rotation

#    satorbit(sat1.x, sat1.y, sat1.z, sat1.pos, sat1.v)
#    satfieldfollow(sat1field.pos, sat1field.axis, sat1field.length, sat1.pos)

##For revoluton of earth around sun
    re = ((earth.x-sun.x)**2 + (earth.y-sun.y)**2 + (earth.z-sun.z)**2)**0.5              ##Distance between earth and sun
    rve = (sun.pos-earth.pos)/re                                                          ##Radial vector
    Fae = ((G*sun.mass)/re**2)*rve                                                        ##Acceleration due to gravitaitonal force of sun
    earth.v += Fae*deltat                                                                 ##Update velocity of earth
    earth.pos += earth.v*deltat                                                           ##Update position of earth
    
    earthaxis.pos =  earth.pos + vector(0,-7000,0)                                              ##Update position of earth axis
    sat0axis.pos = earth.pos + vector(-3500,-7000/math.sqrt(2),3500)                            ##Update position of satellite 0 axis
    sat1axis.pos = earth.pos + vector(3500,-7000/math.sqrt(2),-3500)                            ##Update position of satellite 1 axis
    sat2axis.pos = earth.pos + vector(0,0,-7000)                                                ##Update position of satellite 2 axis
    sat3axis.pos = earth.pos + vector(-7000,0,0)                                                ##Update position of satellite 3 axis
    sourcedir.pos = earth.pos                                                                   ##Update starting point of laser pointer to match with centre of earth
    sourcedir.axis = sourcepos-earth.pos                                                        ##Update axis od laser pointer to always point towards source
    sourcedir.length = 3e4                                                                      ##Update length of laser pointer

    scene.center = earth.pos                                                                    ##Such that the camera would always follow the earth


##For revoluton of satellites around earth (accounting for the force due to both earth and sun)
##For satellite 0
    r0 = ((sat0.x-earth.x)**2 + (sat0.y-earth.y)**2 + (sat0.z-earth.z)**2)**0.5           ##Distance between satellite and earth
    r0s = ((sat0.x-sun.x)**2 + (sat0.y-sun.y)**2 + (sat0.z-sun.z)**2)**0.5                ##Distance between satellite and sun
    rv0 = (earth.pos-sat0.pos)/r0                                                         ##Radial vector for earth
    rv0s = (sun.pos-sat0.pos)/r0s                                                         ##Radial vector for sun
    Fa0 = ((G*earth.mass)/r0**2)*rv0                                                      ##Acceleration due to gravitaitonal force of earth
    Fa0s = ((G*sun.mass)/r0s**2)*rv0s                                                     ##Acceleration due to gravitaitonal force of sun
    Fa0net = Fa0 + Fa0s                                                                   ##Net acceleration due to gravitational force
    sat0.v += Fa0net*deltat                                                               ##Update velocity of satellite
    sat0.pos += sat0.v*deltat                                                             ##Update position of satellite
    
    sat0field.pos = sat0.pos                                                              ##Update position of satellite FoV
    sat0field.axis = sat0.pos-earth.pos                                                   ##Direction of satellite FoV axis 
    sat0field.length = 1000                                                               ##Thickness of satellite FoV. Just for the purpose of understanding the perspective
#    f0.plot(pos = (t, mag(sat0.v - earth.v)))


##For satellite 1
    r1 = ((sat1.x-earth.x)**2 + (sat1.y-earth.y)**2 + (sat1.z-earth.z)**2)**0.5           ##Distance between satellite and earth
    r1s = ((sat1.x-sun.x)**2 + (sat1.y-sun.y)**2 + (sat1.z-sun.z)**2)**0.5                ##Distance between satellite and sun
    rv1 = (earth.pos-sat1.pos)/r1                                                         ##Radial vector for earth
    rv1s = (sun.pos-sat1.pos)/r1s                                                         ##Radial vector for sun
    Fa1 = ((G*earth.mass)/r1**2)*rv1                                                      ##Acceleration due to gravitaitonal force of earth
    Fa1s = ((G*sun.mass)/r1s**2)*rv1s                                                     ##Acceleration due to gravitaitonal force of sun
    Fa1net = Fa1 + Fa1s                                                                   ##Net acceleration due to gravitational force
    sat1.v += Fa1net*deltat                                                               ##Update velocity of satellite
    sat1.pos += sat1.v*deltat                                                             ##Update position of satellite
    
    sat1field.pos = sat1.pos                                                              ##Update position of satellite FoV
    sat1field.axis = sat1.pos-earth.pos                                                   ##Direction of satellite FoV axis 
    sat1field.length = 700                                                                ##Thickness of satellite FoV. Just for the purpose of understanding the perspective
#    f1.plot(pos = (t, mag(sat1.v - earth.v)))


##For satellite 2
    r2 = ((sat2.x-earth.x)**2 + (sat2.y-earth.y)**2 + (sat2.z-earth.z)**2)**0.5           ##Distance between satellite and earth
    r2s = ((sat2.x-sun.x)**2 + (sat2.y-sun.y)**2 + (sat2.z-sun.z)**2)**0.5                ##Distance between satellite and sun
    rv2 = (earth.pos-sat2.pos)/r2                                                         ##Radial vector for earth
    rv2s = (sun.pos-sat2.pos)/r2s                                                         ##Radial vector for sun
    Fa2 = ((G*earth.mass)/r2**2)*rv2                                                      ##Acceleration due to gravitaitonal force of earth
    Fa2s = ((G*sun.mass)/r2s**2)*rv2s                                                     ##Acceleration due to gravitaitonal force of sun
    Fa2net = Fa2 + Fa2s                                                                   ##Net acceleration due to gravitational force
    sat2.v += Fa2net*deltat                                                               ##Update velocity of satellite
    sat2.pos += sat2.v*deltat                                                             ##Update position of satellite
    
    sat2field.pos = sat2.pos                                                              ##Update position of satellite FoV
    sat2field.axis = sat2.pos-earth.pos                                                   ##Direction of satellite FoV axis 
    sat2field.length = 400                                                                ##Thickness of satellite FoV. Just for the purpose of understanding the perspective
#    f2.plot(pos = (t, mag(sat2.v - earth.v)))


##For satellite 3
    r3 = ((sat3.x-earth.x)**2 + (sat3.y-earth.y)**2 + (sat3.z-earth.z)**2)**0.5           ##Distance between satellite and earth
    r3s = ((sat3.x-sun.x)**2 + (sat3.y-sun.y)**2 + (sat3.z-sun.z)**2)**0.5                ##Distance between satellite and sun
    rv3 = (earth.pos-sat3.pos)/r3                                                         ##Radial vector for earth
    rv3s = (sun.pos-sat3.pos)/r3s                                                         ##Radial vector for sun
    Fa3 = ((G*earth.mass)/r3**2)*rv3                                                      ##Acceleration due to gravitaitonal force of earth
    Fa3s = ((G*sun.mass)/r3s**2)*rv3s                                                     ##Acceleration due to gravitaitonal force of sun
    Fa3net = Fa3 + Fa3s                                                                   ##Net acceleration due to gravitational force
    sat3.v += Fa3net*deltat                                                               ##Update velocity of satellite
    sat3.pos += sat3.v*deltat                                                             ##Update position of satellite
    
    sat3field.pos = sat3.pos                                                              ##Update position of satellite FoV
    sat3field.axis = sat3.pos-earth.pos                                                   ##Direction of satellite FoV axis
    sat3field.length = 100                                                                ##Thickness of satellite FoV. Just for the purpose of understanding the perspective
#    f3.plot(pos = (t, mag(sat3.v - earth.v)))


    if (r0 <= earth.radius):
        print("[%s] \nSatellite 0 has crashed into the Earth at time %d seconds!" % (sst, t))
        break
    if (r1 <= earth.radius):
        print("[%s] \nSatellite 1 has crashed into the Earth at time %d seconds!" % (sst, t))
        break
    if (r2 <= earth.radius):
        print("[%s] \nSatellite 2 has crashed into the Earth at time %d seconds!" % (sst, t))
        break
    if (r3 <= earth.radius):
        print("[%s] \nSatellite 3 has crashed into the Earth at time %d seconds!" % (sst, t))
        break
    if (sat0.pos == sat1.pos):
        print("[%s] \nSatellite 0 has crashed with Satellite 1 at time %d seconds!" % (sst, t))
        break
    if (sat0.pos == sat2.pos):
        print("[%s] \nSatellite 0 has crashed with Satellite 2 at time %d seconds!" % (sst, t))
        break
    if (sat0.pos == sat3.pos):
        print("[%s] \nSatellite 0 has crashed with Satellite 3 at time %d seconds!" % (sst, t))
        break    
    if (sat1.pos == sat2.pos):
        print("[%s] \nSatellite 1 has crashed with Satellite 2 at time %d seconds!" % (sst, t))
        break
    if (sat1.pos == sat3.pos):
        print("[%s] \nSatellite 1 has crashed with Satellite 3 at time %d seconds!" % (sst, t))
        break
    if (sat2.pos == sat3.pos):
        print("[%s] \nSatellite 2 has crashed with Satellite 3 at time %d seconds!" % (sst, t))
        break
    if (re <= sun.radius):
        print("[%s] \nThe Earth has crashed into the Sun at time %d seconds, resulting in a cataclysmic event and thus, marking an end to life on Earth... R.I.P. Earthlings!" % (sst, t))


##Converting the equitorial coordinates into cartesian coordinates, as this system is based on that form of input only
    if upd == 1:

##Getting the values from text boxes and converting them from string to float
        srahr = rahr.GetValue()
        nsrahr = float(srahr)   
        sramin = ramin.GetValue()
        nsramin = float(sramin)
        srasec = rasec.GetValue()
        nsrasec = float(srasec)
        sdecdeg = decdeg.GetValue()
        nsdecdeg = float(sdecdeg)
        sdecmin = decmin.GetValue()
        nsdecmin = float(sdecmin)
        sdecsec = decsec.GetValue()
        nsdecsec = float(sdecsec)
        ssourcedist = sourcedist.GetValue()
        isourcedist = (float(ssourcedist))
        nsourcedist = (isourcedist)*(1.496e8)

##        ##Test
##        kzz1 = np.dot(sat0axis.axis, sourcedir.axis)/(abs(sat0axis.axis)*abs(sourcedir.axis))
##        print("%f" % (kzz1))
##        kzz2 = np.dot(sat1axis.axis, sourcedir.axis)/(abs(sat1axis.axis)*abs(sourcedir.axis))
##        print("%f" % (kzz2))
##        kzz3 = np.dot(sat2axis.axis, sourcedir.axis)/(abs(sat2axis.axis)*abs(sourcedir.axis))
##        print("%f" % (kzz3))
##        kzz4 = np.dot(sat3axis.axis, sourcedir.axis)/(abs(sat3axis.axis)*abs(sourcedir.axis))
##        print("%f" % (kzz4))

##For logging the sources observed
        print("[%s] \nSource %d \nRA: \n%0.0f h %0.0f m %0.3f s \nDec: \n%0.0f deg %0.0f min %0.3f sec \nDistance: \n%0.3f AU" % (sst, nsrc, nsrahr, nsramin, nsrasec, nsdecdeg, nsdecmin, nsdecsec, isourcedist))

##Converting from RA Dec to cartesian, centered at earth
        cal1 = ((nsrahr*15) + (nsramin*0.25) + (nsrasec*0.004166))*(pi/180)
        cal2 = ((abs(nsdecdeg) + (nsdecmin/60) + (nsdecsec/3600))* np.sign(nsdecdeg))*(pi/180)

        sourcez = ((nsourcedist*cos(cal2))*cos(cal1) - earth.z)
        sourcex = ((nsourcedist*cos(cal2))*sin(cal1) - earth.x)
        sourcey = ((nsourcedist*sin(cal2)) - earth.y)

##Updating the source position and pointing laser accordingly
        sourcepos = vector(sourcex,sourcey,sourcez)
        sourcedir.axis = sourcepos-earth.pos

##Defining u and v unit vectors such that they are perpendicular to the source direction as well as to each other
        if earthaxis.axis != sourcedir.axis:
            uunitvec = (np.cross(earthaxis.axis, sourcedir.axis))/(np.linalg.norm(np.cross(earthaxis.axis, sourcedir.axis)))
            vunitvec = (np.cross(sourcedir.axis, uunitvec))/(np.linalg.norm(np.cross(sourcedir.axis, uunitvec)))
        else:
            vunitvec = (np.cross(sat2axis.axis, sourcedir.axis))/(np.linalg.norm(np.cross(sat2axis.axis, sourcedir.axis)))
            uunitvec = (np.cross(sourcedir.axis, vunitvec))/(np.linalg.norm(np.cross(sourcedir.axis, vunitvec)))

##Replotting the u-v graph using matplotlib and then saving it as a PDF every time the source is updated
#        plt.figure(figsize = (10,10))
#        plt.scatter(arrbu01, arrbv01, color = 'purple', marker = 'o', s = 0.1, label = 'Baseline between Satellite 0 and Satellite 1')
#        plt.scatter(arrbu02, arrbv02, color = 'blue', marker = 'o', s = 0.1, label = 'Baseline between Satellite 0 and Satellite 2')
#        plt.scatter(arrbu03, arrbv03, color = 'green', marker = 'o', s = 0.1, label = 'Baseline between Satellite 0 and Satellite 3')
#        plt.scatter(arrbu12, arrbv12, color = 'yellow', marker = 'o', s = 0.1, label = 'Baseline between Satellite 1 and Satellite 2')
#        plt.scatter(arrbu13, arrbv13, color = 'orange', marker = 'o', s = 0.1, label = 'Baseline between Satellite 1 and Satellite 3')
#        plt.scatter(arrbu23, arrbv23, color = 'red', marker = 'o', s = 0.1, label = 'Baseline between Satellite 2 and Satellite 3')
#        plt.axis([-15000, 15000, -15000, 15000])
#        plt.title('u-v Plot of Source %d at RA: %0.0f h %0.0f m %0.3f s and Dec: %0.0f deg %0.0f min %0.3f sec' % (nsrc, nsrahr, nsramin, nsrasec, nsdecdeg, nsdecmin, nsdecsec))
#        plt.xlabel('u')
#        plt.ylabel('v')
#        #plt.legend()
#        plt.grid(True)
#        plt.savefig('[%s] u-v Plot %d.pdf' % (sst, save), bbox_inches = 'tight')
#        save += 1

##Emptying the arrays used to plot and save u-v plot every time the source is updated
        arrbu01 = []
        arrbv01 = []
        arrbu02 = []
        arrbv02 = []
        arrbu03 = []
        arrbv03 = []
        arrbu12 = []
        arrbv12 = []
        arrbu13 = []
        arrbv13 = []
        arrbu23 = []
        arrbv23 = []

        upd = 0
        #track = 0
        
##Recreating graph display to plot the u-v plots for all baselines whenever a new source is set
        gdisplay(x = 1050, y = 350, width = 420, height = 380, foreground = color.black, background = color.white, xmax = 15800, xmin = -15800, ymax = 15800, ymin = -15800, title = 'u-v Plot of Source %d at RA: %0.0f h %0.0f m %0.3f s and Dec: %0.0f deg %0.0f min %0.3f sec' % (nsrc, nsrahr, nsramin, nsrasec, nsdecdeg, nsdecmin, nsdecsec), xtitle = 'u', ytitle = 'v')
        fb01 = gdots(color = (0.8,0.2,0.9), size = 0.1)
        fb02 = gdots(color = (0,0,1), size = 0.1)
        fb03 = gdots(color = (0,1,0), size = 0.1)
        fb12 = gdots(color = (1,1,0), size = 0.1)
        fb13 = gdots(color = (1,0.6,0), size = 0.1)
        fb23 = gdots(color = (1,0,0), size = 0.1)


##Commented out as RA and Dec do not vary with the motion of earth in space
##Updating the pointing laser as the earth moves                
#    sourcedir.axis = sourcepos-earth.pos


##To plot u-v every N seconds
    if (t == 0) or (t%Nt == 0):
##To check whether source is within the FoV of a satellite. If the dot product between both directional vectors of satellite and source is positive, then the source is within the FoV
        sat0vis = np.dot(sat0field.axis, sourcedir.axis)
        sat1vis = np.dot(sat1field.axis, sourcedir.axis)
        sat2vis = np.dot(sat2field.axis, sourcedir.axis)
        sat3vis = np.dot(sat3field.axis, sourcedir.axis)

##To check whether sun is in the FoV of a satellite. When sun is in FoV, the satellite would be capable of collecting solar energy to power itself.
##Commented out as not required in current simulation
        #sat1sun = np.dot(sat1field.axis, (sun.pos-earth.pos))
        #sat2sun = np.dot(sat2field.axis, (sun.pos-earth.pos))
        #sat3sun = np.dot(sat3field.axis, (sun.pos-earth.pos))

##For the beam sensitivity measurement of the satellites. It is the cos of the angle between the directional vectors of satellite and the source
##Commented out as not required in current simulation
        #sat1cos = sat1vis/(abs(sat1field.axis)*abs(sourcedir.axis))
        #sat2cos = sat2vis/(abs(sat2field.axis)*abs(sourcedir.axis))
        #sat3cos = sat3vis/(abs(sat3field.axis)*abs(sourcedir.axis))

##If the source is within the FoV of atleast two of the three satellites, then tracking is started (Tracking measurement is commented out for now)
##Condition 08: +---, Condition 12: -+--, Condition 14: --+-, Condition 15: ---+, Condition 16: ---- are ignored as there would not be any baselines generated        
        if ((sat0vis > 0) and (sat1vis > 0) and (sat2vis > 0) and (sat3vis > 0)):               #Condition 01: ++++
            #track += 1
            #print(track)

            bu01 = np.dot((sat0.pos - sat1.pos),uunitvec)
            bv01 = np.dot((sat0.pos - sat1.pos),vunitvec)
            arrbu01.append(bu01)
            arrbu01.append(-bu01)
            arrbv01.append(bv01)
            arrbv01.append(-bv01)

            bu02 = np.dot((sat0.pos - sat2.pos),uunitvec)
            bv02 = np.dot((sat0.pos - sat2.pos),vunitvec)
            arrbu02.append(bu02)
            arrbu02.append(-bu02)
            arrbv02.append(bv02)
            arrbv02.append(-bv02)

            bu03 = np.dot((sat0.pos - sat3.pos),uunitvec)
            bv03 = np.dot((sat0.pos - sat3.pos),vunitvec)
            arrbu03.append(bu03)
            arrbu03.append(-bu03)
            arrbv03.append(bv03)
            arrbv03.append(-bv03)            

            bu12 = np.dot((sat1.pos - sat2.pos),uunitvec)
            bv12 = np.dot((sat1.pos - sat2.pos),vunitvec)
            arrbu12.append(bu12)
            arrbu12.append(-bu12)
            arrbv12.append(bv12)
            arrbv12.append(-bv12)

            bu13 = np.dot((sat1.pos - sat3.pos),uunitvec)
            bv13 = np.dot((sat1.pos - sat3.pos),vunitvec)
            arrbu13.append(bu13)
            arrbu13.append(-bu13)
            arrbv13.append(bv13)
            arrbv13.append(-bv13)

            bu23 = np.dot((sat2.pos - sat3.pos),uunitvec)
            bv23 = np.dot((sat2.pos - sat3.pos),vunitvec)
            arrbu23.append(bu23)
            arrbu23.append(-bu23)
            arrbv23.append(bv23)
            arrbv23.append(-bv23)

            #print(uunitvec, vunitvec)

            fb01.plot(pos = (bu01, bv01))
            fb02.plot(pos = (bu02, bv02))
            fb03.plot(pos = (bu03, bv03))
            fb12.plot(pos = (bu12, bv12))
            fb13.plot(pos = (bu13, bv13))
            fb23.plot(pos = (bu23, bv23))

            #plt.scatter(bu12,bv12,color = 'k')
            #plt.axis([-20000, 20000, -20000, 20000])
            #plt.show()
            #plt.pause(1e-20)

        elif ((sat0vis > 0) and (sat1vis > 0) and (sat2vis > 0) and (sat3vis < 0)):             #Condition 02: +++-

            bu01 = np.dot((sat0.pos - sat1.pos),uunitvec)
            bv01 = np.dot((sat0.pos - sat1.pos),vunitvec)
            arrbu01.append(bu01)
            arrbu01.append(-bu01)
            arrbv01.append(bv01)
            arrbv01.append(-bv01)

            bu02 = np.dot((sat0.pos - sat2.pos),uunitvec)
            bv02 = np.dot((sat0.pos - sat2.pos),vunitvec)
            arrbu02.append(bu02)
            arrbu02.append(-bu02)
            arrbv02.append(bv02)
            arrbv02.append(-bv02)

            bu12 = np.dot((sat1.pos - sat2.pos),uunitvec)
            bv12 = np.dot((sat1.pos - sat2.pos),vunitvec)
            arrbu12.append(bu12)
            arrbu12.append(-bu12)
            arrbv12.append(bv12)
            arrbv12.append(-bv12)

            fb01.plot(pos = (bu01, bv01))
            fb02.plot(pos = (bu02, bv02))
            fb12.plot(pos = (bu12, bv12))

        elif ((sat0vis > 0) and (sat1vis > 0) and (sat2vis < 0) and (sat3vis > 0)):             #Condition 03: ++-+

            bu01 = np.dot((sat0.pos - sat1.pos),uunitvec)
            bv01 = np.dot((sat0.pos - sat1.pos),vunitvec)
            arrbu01.append(bu01)
            arrbu01.append(-bu01)
            arrbv01.append(bv01)
            arrbv01.append(-bv01)

            bu03 = np.dot((sat0.pos - sat3.pos),uunitvec)
            bv03 = np.dot((sat0.pos - sat3.pos),vunitvec)
            arrbu03.append(bu03)
            arrbu03.append(-bu03)
            arrbv03.append(bv03)
            arrbv03.append(-bv03)   

            bu13 = np.dot((sat1.pos - sat3.pos),uunitvec)
            bv13 = np.dot((sat1.pos - sat3.pos),vunitvec)
            arrbu13.append(bu13)
            arrbu13.append(-bu13)
            arrbv13.append(bv13)
            arrbv13.append(-bv13)

            fb01.plot(pos = (bu01, bv01))
            fb03.plot(pos = (bu03, bv03))
            fb13.plot(pos = (bu13, bv13))

        elif ((sat0vis > 0) and (sat1vis > 0) and (sat2vis < 0) and (sat3vis < 0)):             #Condition 04: ++--

            bu01 = np.dot((sat0.pos - sat1.pos),uunitvec)
            bv01 = np.dot((sat0.pos - sat1.pos),vunitvec)
            arrbu01.append(bu01)
            arrbu01.append(-bu01)
            arrbv01.append(bv01)
            arrbv01.append(-bv01)

            fb01.plot(pos = (bu01, bv01))

        elif ((sat0vis > 0) and (sat1vis < 0) and (sat2vis > 0) and (sat3vis > 0)):             #Condition 05: +-++

            bu02 = np.dot((sat0.pos - sat2.pos),uunitvec)
            bv02 = np.dot((sat0.pos - sat2.pos),vunitvec)
            arrbu02.append(bu02)
            arrbu02.append(-bu02)
            arrbv02.append(bv02)
            arrbv02.append(-bv02)

            bu03 = np.dot((sat0.pos - sat3.pos),uunitvec)
            bv03 = np.dot((sat0.pos - sat3.pos),vunitvec)
            arrbu03.append(bu03)
            arrbu03.append(-bu03)
            arrbv03.append(bv03)
            arrbv03.append(-bv03)  

            bu23 = np.dot((sat2.pos - sat3.pos),uunitvec)
            bv23 = np.dot((sat2.pos - sat3.pos),vunitvec)
            arrbu23.append(bu23)
            arrbu23.append(-bu23)
            arrbv23.append(bv23)
            arrbv23.append(-bv23)

            fb02.plot(pos = (bu02, bv02))
            fb03.plot(pos = (bu03, bv03))
            fb23.plot(pos = (bu23, bv23))            

        elif ((sat0vis > 0) and (sat1vis < 0) and (sat2vis > 0) and (sat3vis < 0)):             #Condition 06: +-+-

            bu02 = np.dot((sat0.pos - sat2.pos),uunitvec)
            bv02 = np.dot((sat0.pos - sat2.pos),vunitvec)
            arrbu02.append(bu02)
            arrbu02.append(-bu02)
            arrbv02.append(bv02)
            arrbv02.append(-bv02)

            fb02.plot(pos = (bu02, bv02))

        elif ((sat0vis > 0) and (sat1vis < 0) and (sat2vis < 0) and (sat3vis > 0)):             #Condition 07: +--+

            bu03 = np.dot((sat0.pos - sat3.pos),uunitvec)
            bv03 = np.dot((sat0.pos - sat3.pos),vunitvec)
            arrbu03.append(bu03)
            arrbu03.append(-bu03)
            arrbv03.append(bv03)
            arrbv03.append(-bv03)

            fb03.plot(pos = (bu03, bv03))

        elif ((sat0vis < 0) and (sat1vis > 0) and (sat2vis > 0) and (sat3vis > 0)):             #Condition 09: -+++

            bu12 = np.dot((sat1.pos - sat2.pos),uunitvec)
            bv12 = np.dot((sat1.pos - sat2.pos),vunitvec)
            arrbu12.append(bu12)
            arrbu12.append(-bu12)
            arrbv12.append(bv12)
            arrbv12.append(-bv12)

            bu13 = np.dot((sat1.pos - sat3.pos),uunitvec)
            bv13 = np.dot((sat1.pos - sat3.pos),vunitvec)
            arrbu13.append(bu13)
            arrbu13.append(-bu13)
            arrbv13.append(bv13)
            arrbv13.append(-bv13)

            bu23 = np.dot((sat2.pos - sat3.pos),uunitvec)
            bv23 = np.dot((sat2.pos - sat3.pos),vunitvec)
            arrbu23.append(bu23)
            arrbu23.append(-bu23)
            arrbv23.append(bv23)
            arrbv23.append(-bv23)

            fb12.plot(pos = (bu12, bv12))
            fb13.plot(pos = (bu13, bv13))
            fb23.plot(pos = (bu23, bv23))

        elif ((sat0vis < 0) and (sat1vis > 0) and (sat2vis > 0) and (sat3vis < 0)):             #Condition 10: -++-

            bu12 = np.dot((sat1.pos - sat2.pos),uunitvec)
            bv12 = np.dot((sat1.pos - sat2.pos),vunitvec)
            arrbu12.append(bu12)
            arrbu12.append(-bu12)
            arrbv12.append(bv12)
            arrbv12.append(-bv12)

            fb12.plot(pos = (bu12, bv12))

        elif ((sat0vis < 0) and (sat1vis > 0) and (sat2vis < 0) and (sat3vis > 0)):             #Condition 11: -+-+

            bu13 = np.dot((sat1.pos - sat3.pos),uunitvec)
            bv13 = np.dot((sat1.pos - sat3.pos),vunitvec)
            arrbu13.append(bu13)
            arrbu13.append(-bu13)
            arrbv13.append(bv13)
            arrbv13.append(-bv13)

            fb13.plot(pos = (bu13, bv13))

        elif ((sat0vis < 0) and (sat1vis < 0) and (sat2vis > 0) and (sat3vis > 0)):             #Condition 13: --++

            bu23 = np.dot((sat2.pos - sat3.pos),uunitvec)
            bv23 = np.dot((sat2.pos - sat3.pos),vunitvec)
            arrbu23.append(bu23)
            arrbu23.append(-bu23)
            arrbv23.append(bv23)
            arrbv23.append(-bv23)

            fb23.plot(pos = (bu23, bv23))

##        if (sat1sun > 0):
##            tsat1sun += 1

##        if (t != 0) and (t%sat1.period == 0):
##            tsat1sunpercent = (tsat1sun/sat1.period)*100
##            print(tsat1sunpercent)
##            tsat1sun = 0
            
##        if (sat2sun > 0):
##            tsat2sun += 1
##            
##        if (sat3sun > 0):
##            tsat3sun += 1


    t += deltat                                                 ##Updating time after each iteration

    
    if (t%86400 == 0):
        day += 1
        print("[%s] \nThe system has been running for %d days. " % (sst, day))

    if (t%604800 == 0):
        week += 1
        print("[%s] \nThe system has been running for %d weeks" % (sst, week))

    if (t%(2.628e6) == 0):
        month += 1
        print("[%s] \nThe system has been running for %d months" % (sst, month))


##To set the maximum run time of the system, after whioh it would shut down automatically
    if upd2 == 1:
        
        upd2 = 0
        ttmax = maxruntime.GetValue()
        tmax = float(ttmax)
        print("[%s] \nThe maximum runtime of the system has been updated to %0.1f seconds" % (sst, tmax))
        
    if (t>tmax):
        print("[%s] \nThe system was stopped becasue it was set to run for a maximum time of %0.1f seconds" % (sst, tmax))
        print("The system was stopped after running for %d seconds" % (t - 1))
        winsound.Beep(3000, 3000)
        break

##Updating timestamps after every iteration
    tss = time.time()
    sst = datetime.datetime.fromtimestamp(tss).strftime('%d-%m-%Y %H;%M;%S')




