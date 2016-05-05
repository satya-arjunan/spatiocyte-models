from matplotlib.colors import colorConverter
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

# create dummy data
#zvals = np.ones((100,100))# np.random.rand(100,100)*10-5
zvals =  np.random.rand(10,10)*10-5
zvals2 = np.random.rand(10,10)*10-5

zvals = [np.linspace(0, 1, 10)]*10
zvals2 = [np.linspace(1, 0, 10)]*10

# generate the colors for your colormap
color2 = colorConverter.to_rgba('black')

# make the colormaps
cmap1 = mpl.colors.LinearSegmentedColormap.from_list('my_cmap',['red',color2],256)
cmap2 = mpl.colors.LinearSegmentedColormap.from_list('my_cmap2',['red',color2],256)
cmap3 = mpl.colors.LinearSegmentedColormap.from_list('my_cmap3',['black','black'],256)


# create your alpha array and fill the colormap with them.
# here it is progressive, but you can create whathever you want
cmap2._init() # create the _lut array, with rgba values
alphas = np.linspace(1, 0, cmap2.N+3)
cmap2._lut[:,-1] = alphas
cmap1._init()
alphas = np.linspace(1, 0, cmap1.N+3)
cmap1._lut[:,-1] = alphas

img1 = plt.imshow(zvals2, interpolation='nearest', cmap=cmap3, origin='lower')
img3 = plt.imshow(zvals2, interpolation='nearest', cmap=cmap2, origin='lower')
img2 = plt.imshow(zvals, interpolation='nearest', cmap=cmap1, origin='lower')

plt.show()
