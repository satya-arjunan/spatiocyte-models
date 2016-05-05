import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl


#http://imagej.net/Color_Image_Processing#RGB_color_merging
#https://github.com/imagej/ImageJA/blob/3ed2e1a1d785eda3c9dfdb330030aee968c242b8/src/main/java/ij/plugin/RGBStackMerge.java
#http://stackoverflow.com/questions/36429847/merging-greyscale-channels-into-a-color-composite
#http://stackoverflow.com/questions/726549/algorithm-for-additive-color-mixing-for-rgb-values

# create dummy data
#zvals = np.ones((100,100))# np.random.rand(100,100)*10-5
#zvals =  np.random.rand(10,10)*10-5
#zvals2 = np.random.rand(10,10)*10-5

zvals = np.linspace(0, 1, 8).reshape(4,2)
zvals2 = np.linspace(1, 0, 8).reshape(4,2)

# make the colormaps
cmap1 = mpl.colors.LinearSegmentedColormap.from_list('my_cmap',['#FF0000','black'],256)
cmap2 = mpl.colors.LinearSegmentedColormap.from_list('my_cmap2',['#00FF00','black'],256)

c1 = np.array(cmap1(zvals))
c2 = np.array(cmap2(zvals2))
print "c1", c1
print "c2", c2

c3 = np.clip(np.add(c1, c2), 0, 1)
print "c3", c3
#i1 = plt.pcolor(zvals, cmap=cmap1)
#pc = plt.imshow(c3, interpolation='none')
pc = plt.imshow(c3)

#pc.update_scalarmappable()
#print pc.get_facecolors()

plt.show()
