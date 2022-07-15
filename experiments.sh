#!/bin/bash
file=carrousel_1
for a in {4..100}
do
  for i in {0..9}
    do
      echo file/${a}a_${i}.scen
      now=$(date)
      echo "$now"
      timeout 180 python3 ColoredMain.py $file.graph $file/${a}a_${i}.scen 5
      now=$(date)
      echo "$now"
      timeout 180 python3 ColoredMain.py $file.graph $file/${a}a_${i}.scen 6
    done
done
