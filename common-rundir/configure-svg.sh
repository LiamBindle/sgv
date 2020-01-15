set -e 
set -x

CS_RES=48
STRETCH_FACTOR=1.0
TARGET_LAT=
TARGET_LON=
RESTART_FILE=initial_GEOSChem_rst.c48_benchmark.nc

# Fix cd command in bsub file
CWD=$(pwd)
sed -i "s#cd COMPUTE_NODE_RUNDIR#cd ${CWD}#g" run-benchmark.bsub

# Fix runConfig.sh
sed -i "s#^.*CS_RES\s*=\s*[a-zA-Z0-9\.\-\/_]*#CS_RES=${CS_RES}#g" runConfig.sh
sed -i "s#^.*INITIAL_RESTART\s*=\s*[a-zA-Z0-9\.\-\/_]*#INITIAL_RESTART=${RESTART_FILE}#g" runConfig.sh
sed -i "s/^.*STRETCH_FACTOR\s*=\s*[0-9\.\-]*/STRETCH_FACTOR=${STRETCH_FACTOR}/g" runConfig.sh
sed -i "s/^.*TARGET_LAT\s*=\s*[0-9\.\-]*/TARGET_LAT=${TARGET_LAT}/g" runConfig.sh
sed -i "s/^.*TARGET_LON\s*=\s*[0-9\.\-]*/TARGET_LON=${TARGET_LON}/g" runConfig.sh

# Run runConfig.sh
./runConfig.sh
