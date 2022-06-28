#!/bin/bash
file=combinedC
for a in {4..100}
do
  for i in {0..9}
    do
      echo file/${a}a_${i}.scen
      now=$(date)
      echo "$now"
      timeout 180 python3 CombinedMain.py $file.graph $file/${a}a_${i}.scen 4
    done
done
