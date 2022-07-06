#!/bin/bash
file=combined8
for a in {4..100}
do
  for i in {0..9}
    do
      now=$(date)
      echo "$now"
      timeout 300 python3 CombinedMain.py $file.graph $file/${a}a_${i}.scen 2
      now=$(date)
      echo "$now"
      timeout 300 python3 CombinedMain.py $file.graph $file/${a}a_${i}.scen 3
    done
done
