import os.path

from gcpy import benchmark as bmk

# Control what gets plotted
plot_conc = True
plot_emis = True
plot_jvalues = True
plot_aod = True
plot_rst = True

# Descriptions and paths
refstr = 'C48'
refdir = 'CONTROL_RUNDIR/OutputDir'
devstr = 'C34x1.4141'
devdir = 'EXPERIMENT_RUNDIR/OutputDir'

dev_sg_params={'stretch_factor': STRETCH_FACTOR, 'target_lat': TARGET_LAT, 'target_lon': TARGET_LON}

# Misc
cmpres='0.5x0.625'
plotsdir = os.path.join(devdir, '../plots')
gchp_datestr = '20160716'
gchp_hourstr = '1200'
roi_x=[-84.39-15, -84.39+15]
roi_y=[33.75-7.5, 33.75+7.5]

# Output dataset filenames
gchp_spcfile = 'GCHP.SpeciesConc.{}_{}z.nc4'.format(gchp_datestr, gchp_hourstr)
gchp_hcofile = 'GCHP.Emissions.{}_{}z.nc4'.format(gchp_datestr, gchp_hourstr)
gchp_jvfile = 'GCHP.JValues.{}_{}z.nc4'.format(gchp_datestr, gchp_hourstr)
gchp_aodfile = 'GCHP.Aerosols.{}_{}z.nc4'.format(gchp_datestr, gchp_hourstr)
gchp_rstfile = '../initial_restart_file.nc'


# Paths to output datasets
refspc = os.path.join(refdir, gchp_spcfile)
devspc = os.path.join(devdir, gchp_spcfile)

refhco = os.path.join(refdir, gchp_hcofile)
devhco = os.path.join(devdir, gchp_hcofile)

refjv  = os.path.join(refdir, gchp_jvfile)
devjv  = os.path.join(devdir, gchp_jvfile)

refaod = os.path.join(refdir, gchp_aodfile)
devaod = os.path.join(devdir, gchp_aodfile)

refrst = os.path.join(refdir, gchp_rstfile)
devrst = os.path.join(devdir, gchp_rstfile)

if plot_rst:
    # Concentration plots
    # (includes lumped species and separates by category)
    print('\n%%% Creating GCHP vs. GCHP restart file plots %%%')
    bmk.make_benchmark_conc_plots(refrst,
                                  refstr,
                                  devrst,
                                  devstr,
                                  dst=plotsdir,
                                  subdst='restart_file_comparison',
                                  overwrite=True,
                                  use_cmap_RdBu=True,
                                  is_restart_file=True,
                                  cmpres=cmpres,
                                  dev_sg_params=dev_sg_params,
                                  x_extent=roi_x,
                                  y_extent=roi_y)

if plot_conc:
    # Concentration plots
    # (includes lumped species and separates by category)
    print('\n%%% Creating GCHP vs. GCHP concentration plots %%%')
    bmk.make_benchmark_conc_plots(refspc,
                                  refstr,
                                  devspc,
                                  devstr,
                                  dst=plotsdir,
                                  overwrite=True,
                                  use_cmap_RdBu=True,
                                  cmpres=cmpres,
                                  dev_sg_params=dev_sg_params,
                                  x_extent=roi_x,
                                  y_extent=roi_y)

if plot_emis:
    # Emissions plots
    print('\n%%% Creating GCHP vs. GCHP emissions plots %%%')
    bmk.make_benchmark_emis_plots(refhco,
                                  refstr,
                                  devhco,
                                  devstr,
                                  dst=plotsdir,
                                  plot_by_benchmark_cat=True,
                                  plot_by_hco_cat=True,
                                  overwrite=True,
                                  flip_ref=True,
                                  flip_dev=True,
                                  cmpres=cmpres,
                                  dev_sg_params=dev_sg_params,
                                  x_extent=roi_x,
                                  y_extent=roi_y)

if plot_jvalues:
    # Local noon J-values plots
    print('\n%%% Creating GCHP vs. GCHP J-value plots %%%')
    bmk.make_benchmark_jvalue_plots(refjv,
                                    refstr,
                                    devjv,
                                    devstr,
                                    dst=plotsdir,
                                    overwrite=True,
                                    cmpres=cmpres,
                                    dev_sg_params=dev_sg_params,
                                    x_extent=roi_x,
                                    y_extent=roi_y,)

if plot_aod:
    # Column AOD plots
    print('\n%%% Creating GCHP vs. GCHP column AOD plots %%%')
    bmk.make_benchmark_aod_plots(refaod,
                                 refstr,
                                 devaod,
                                 devstr,
                                 dst=plotsdir,
                                 overwrite=True,
                                 cmpres=cmpres,
                                 dev_sg_params=dev_sg_params,
                                 x_extent=roi_x,
                                 y_extent=roi_y)
