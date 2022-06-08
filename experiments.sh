#!/bin/bash
for a in {15..30}
do
  for i in {0..3}
    do
      timeout 180 python ColoredMain.py grid8.graph grid8/${a}a_${i}.scen 1
    done
done