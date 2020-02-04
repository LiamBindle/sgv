import os
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature


plt.figure(figsize=(4, 2))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.COASTLINE, edgecolor='k', linewidth=2)

plt.gca().set_axis_off()
plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0,
            hspace = 0, wspace = 0)
plt.margins(0,0)
plt.gca().xaxis.set_major_locator(plt.NullLocator())
plt.gca().yaxis.set_major_locator(plt.NullLocator())
plt.savefig('temp.jpg', dpi=90, bbox_inches='tight', pad_inches=0)
plt.close()


# Get coastline emissions
coastlines = plt.imread('temp.jpg', format='jpeg')
coastlines = 1.2e-12 * coastlines.any(axis=-1)
coastlines = np.flip(coastlines, axis=0)
os.remove('temp.jpg')


# Set up coordinates
x = -179.5 + np.array(range(360))
y = -89.5 + np.array(range(180))
lev = np.array(range(1, 48))
time = np.array([0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334])

emission_2d = np.repeat(coastlines[None, ...], len(time), axis=0)
emission_3d = np.repeat(emission_2d[:, None, ...], len(lev), axis=1)
pasv1 = xr.DataArray(
    emission_2d,
    dims=('time', 'lat', 'lon'),
    coords={'time': time, 'lat': y, 'lon': x},
    attrs={'units': 'kg/m2/s', 'long_name': 'Diagnostic 2D coastline emission'}
)
pasv2 = xr.DataArray(
    emission_3d,
    dims=('time', 'lev', 'lat', 'lon'),
    coords={'time': time, 'lat': y, 'lon': x, 'lev': lev},
    attrs={'units': 'kg/m2/s', 'long_name': 'Diagnostic 3D coastline emission'}
)

ds = xr.Dataset({'EmisPASV1': pasv1, 'EmisPASV2': pasv2})
ds['lon'].attrs = {
    'units': 'degrees_east'
}
ds['lat'].attrs = {
    'units': 'degrees_north'
}
ds['lev'].attrs = {
    'units': 'level',
    'long_name': 'GEOS-Chem level',
    'positive': 'up'
}
ds['time'].attrs = {
    'units': 'days since 2005-01-01 00:00:00',
    'calendar': 'standard',
}
ds.attrs = {
    'description': 'Diagnostic coastline emissions for regridding problem in SGV L2',
    'history': 'Manually created by Liam Bindle on 2020-02-04'
}
print(ds)
ds.to_netcdf('diagnostic_coastline_emission.nc', unlimited_dims=['time'])





