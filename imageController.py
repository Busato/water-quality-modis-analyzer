import xarray as xr
import geoio
import os

from pprint import pprint

path = "/home/nbm/Documentos/tcc/code/water-quality-modis-analyzer/images/"
files = "10_APR_07/"
image = (
    path
    + files
    + "MOD09GA.A2007100.h13v11.006.2015129072454-10-APR-07_MODIS_Grid_500m_2D_band_7"
    + ".tif"
)


img = geoio.GeoImage(image)
pix_x, pix_y = img.proj_to_raster(-48.4565845601195, -27.6013741190903)

result = os.popen("gdallocationinfo %s %s %s" % (image, pix_x, pix_y)).read()

pprint(result)
