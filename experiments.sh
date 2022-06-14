#!/bin/bash
for a in {4..100}
do
  for i in {0..9}
    do
      echo carrousel_1/${a}a_${i}.scen
      now=$(date)
      echo "$now"
      timeout 180 python3 ColoredMain.py carrousel_1.graph carrousel_1/${a}a_${i}.scen 4
    done
done
