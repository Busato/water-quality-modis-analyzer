import xarray as xr
import geoio
import os

from pprint import pprint

path = "/home/nbm/Documentos/tcc/code/water-quality-modis-analyzer/images/"
files = "09_MAY_07/"
image = (
    path
    + files
    + "MOD09GA.A2007129.h13v11.006.2015130160521-09-MAY-07_MODIS_Grid_500m_2D_band_7"
    + ".tif"
)


img = geoio.GeoImage(image)
pix_x, pix_y = img.proj_to_raster(-48.4698900824481, -27.6149296999182)

result = os.popen("gdallocationinfo %s %s %s" % (image, pix_x, pix_y)).read()

pprint(result)
