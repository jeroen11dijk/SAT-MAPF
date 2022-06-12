#!/bin/bash
for a in {4..70}
do
  for i in {0..9}
    do
      echo grid16_1/${a}a_${i}.scen
      now=$(date)
      echo "$now"
      timeout 180 python ColoredMain.py grid16_1.graph grid16_1/${a}a_${i}.scen 1
      now=$(date)
      echo "$now"
      timeout 180 python ColoredMain.py grid16_1.graph grid16_1/${a}a_${i}.scen 2
      now=$(date)
      echo "$now"
      timeout 180 python ColoredMain.py grid16_1.graph grid16_1/${a}a_${i}.scen 3
      now=$(date)
      echo "$now"
      timeout 180 python ColoredMain.py grid16_1.graph grid16_1/${a}a_${i}.scen 4
    done
done
