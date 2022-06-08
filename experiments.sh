#!/bin/bash
for a in {4..30}
do
  for i in {0..9}
    do
      now=$(date)
      echo "$now"
      echo grid8.graph grid8/${a}a_${i}.scen
      timeout 180 python3 ColoredMain.py grid8.graph grid8/${a}a_${i}.scen 2
    done
done
