#!/bin/bash
for a in {23..100}
do
  for i in {0..9}
    do
      echo grid16/${a}a_${i}.scen
      now=$(date)
      echo "$now"
      timeout 180 python3 ColoredMain.py grid16.graph grid16/${a}a_${i}.scen 1
      now=$(date)
      echo "$now"
      timeout 180 python3 ColoredMain.py grid16.graph grid16/${a}a_${i}.scen 2
      now=$(date)
      echo "$now"
      timeout 180 python3 ColoredMain.py grid16.graph grid16/${a}a_${i}.scen 3
    done
done
