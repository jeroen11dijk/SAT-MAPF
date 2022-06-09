#!/bin/bash
for a in {4..30}
do
  for i in {0..9}
    do
      echo grid8/${a}a_${i}.scen
      now=$(date)
      echo "$now"
      timeout 180 python3 ColoredMain.py grid8.graph grid8/${a}a_${i}.scen 1
      now=$(date)
      echo "$now"
      timeout 180 python3 ColoredMain.py grid8.graph grid8/${a}a_${i}.scen 2
      now=$(date)
      echo "$now"
      timeout 180 python3 ColoredMain.py grid8.graph grid8/${a}a_${i}.scen 3
    done
done
