#!/bin/bash
for a in {4..100}
do
  for i in {0..9}
    do
      echo carrousel_3/${a}a_${i}.scen
      now=$(date)
      echo "$now"
      timeout 180 python3 ColoredMain.py carrousel_3.graph carrousel_3/${a}a_${i}.scen 1
      now=$(date)
      echo "$now"
      timeout 180 python3 ColoredMain.py carrousel_3.graph carrousel_3/${a}a_${i}.scen 2
      now=$(date)
      echo "$now"
      timeout 180 python3 ColoredMain.py carrousel_3.graph carrousel_3/${a}a_${i}.scen 3
      now=$(date)
      echo "$now"
      timeout 180 python3 ColoredMain.py carrousel_3.graph carrousel_3/${a}a_${i}.scen 4
    done
done
