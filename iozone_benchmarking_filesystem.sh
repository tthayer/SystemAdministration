#!/bin/bash
for BS in 64 128 256 512 1024 2048 4096 8192 ; do
iozone -R -b results-${BS}.xls -t 16 -r $BS -s 8g \
-i 0 -i 1 -i 2
done
