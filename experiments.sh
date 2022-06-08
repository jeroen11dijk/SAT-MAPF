#!/bin/bash
for a in {0..30}
do
  for i in {0..9}
    do
      timeout 180 python3 ColoredMain.py grid8.graph grid8/${a}a_${i}.scen 1
    done
done