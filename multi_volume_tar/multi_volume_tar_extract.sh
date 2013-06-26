#!/bin/bash
# EXTRACTION SCRIPT

# save on file the initial volume number
echo 1 >number

# execute the "change-volume" script a first time
./multi_volume_tar_base x file

# multi-volume archive extraction
tar -M -F './multi_volume_tar_base x file' -xf file.tar 2>&-

# remove a spurious file
rm file.tar
