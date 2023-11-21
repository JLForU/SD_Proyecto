#!/bin/bash

# SC
gnome-terminal -- bash -c "python3 sc.py; bash"
# HC
gnome-terminal -- bash -c "python3 hc.py; bash"

# Monitores
gnome-terminal -- bash -c "python3 monitor.py T; bash"
gnome-terminal -- bash -c "python3 monitor.py pH; bash"
gnome-terminal -- bash -c "python3 monitor.py OD; bash"

# Sensores
gnome-terminal -- bash -c "python3 sensor.py T 2 file; bash"
gnome-terminal -- bash -c "python3 sensor.py pH 2 file; bash"
gnome-terminal -- bash -c "python3 sensor.py OD 2 file; bash"
gnome-terminal -- bash -c "python3 sensor.py T 2 file; bash"
gnome-terminal -- bash -c "python3 sensor.py pH 2 file; bash"
gnome-terminal -- bash -c "python3 sensor.py OD 2 file; bash"
gnome-terminal -- bash -c "python3 sensor.py Tiempo 2 file; bash"
