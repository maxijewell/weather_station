#!/bin/bash

echo Starting the weather python script...
sleep 30
while true
do
  python /home/pi/Weather_station/juliestemp.py
  sleep 1800
done
