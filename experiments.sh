#!/bin/bash
file=grid8
for a in {37..100}
do
  for i in {0..9}
    do
      echo file/${a}a_${i}.scen
      now=$(date)
      echo "$now"
      timeout 180 python3 ColoredMain.py $file.graph $file/${a}a_${i}.scen 2
    done
done
