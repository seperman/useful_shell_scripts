#!/bin/bash
# MULTI VOLUME TAR CREATION SCRIPT
# 

# save on file the initial volume number
echo 1 >number

# multi-volume archive creation
tar -ML 100000 -F './multi_volume_tar_base c file' -cf file.tar ~/Downloads/think_trac.tgz 2>&-

# execute the "change-volume" script a last time
./multi_volume_tar_base c file
