set -e 
set -x

CS_RES=48
STRETCH_FACTOR=1.0
TARGET_LAT=
TARGET_LON=
RESTART_FILE=initial_restart_file.nc

CONTROL_RUNDIR='/my-projects/...djskahjkdsahjkdsahk'

# Fix cd command in bsub file (compute-node view)
CWD=/my-projects/$(realpath --relative-to ~/my-projects/ $(pwd))

# Restart file regridding
sed -i "s#cd COMPUTE_NODE_RUNDIR#cd ${CWD}#g"   regrid_restart.bsub
sed -i "s/STRETCH_FACTOR/${STRETCH_FACTOR}/g"   regrid_restart.bsub
sed -i "s/TARGET_LAT/${TARGET_LAT}/g"           regrid_restart.bsub
sed -i "s/TARGET_LON/${TARGET_LON}/g"           regrid_restart.bsub
sed -i "s/CS_RES/${CS_RES}/g"                   regrid_restart.bsub

# Running
sed -i "s#cd COMPUTE_NODE_RUNDIR#cd ${CWD}#g" run.bsub

sed -i "s#^.*CS_RES\s*=\s*[a-zA-Z0-9\.\-\/_]*#CS_RES=${CS_RES}#g" runConfig.sh
sed -i "s#^.*INITIAL_RESTART\s*=\s*[a-zA-Z0-9\.\-\/_]*#INITIAL_RESTART=${RESTART_FILE}#g" runConfig.sh
sed -i "s/^.*STRETCH_FACTOR\s*=\s*[0-9\.\-]*/STRETCH_FACTOR=${STRETCH_FACTOR}/g" runConfig.sh
sed -i "s/^.*TARGET_LAT\s*=\s*[0-9\.\-]*/TARGET_LAT=${TARGET_LAT}/g" runConfig.sh
sed -i "s/^.*TARGET_LON\s*=\s*[0-9\.\-]*/TARGET_LON=${TARGET_LON}/g" runConfig.sh

# Plotting
sed -i "s#cd COMPUTE_NODE_RUNDIR#cd ${CWD}#g"   plot.bsub

sed -i "s#CONTROL_RUNDIR#${CONTROL_RUNDIR}#g"   plot.py
sed -i "s#EXPERIMENT_RUNDIR#${CWD}#g"           plot.py
sed -i "s/STRETCH_FACTOR/${STRETCH_FACTOR}/g"   plot.py
sed -i "s/TARGET_LAT/${TARGET_LAT}/g" plot.py
sed -i "s/TARGET_LON/${TARGET_LON}/g" plot.py
