import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
from astropy.wcs import WCS



def axes(filename):
	image = fits.open(filename)
	proy = WCS(image[0].header)
	
	axim = plt.subplot(projection = proy)
	ax.imshow(image[0].data, origin = "lower")
	ax.coords.grid(image[0].data, grid_type = "contours", color = "white")
	