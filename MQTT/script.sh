#!/bin/bash

# SC
gnome-terminal -- bash -c "python3 sc.py; bash"
gnome-terminal -- bash -c "python3 hc.py; bash"

# Monitores
gnome-terminal -- bash -c "python3 monitor.py T; bash"
gnome-terminal -- bash -c "python3 monitor.py pH; bash"
gnome-terminal -- bash -c "python3 monitor.py OD; bash"

# Sensores
for file in ./sensor_*.py; do
    if [ -f "$file" ]; then
        gnome-terminal -- bash -c "python3 '$file'; bash"
    fi
done
for file in ./sensor_*.py; do
    if [ -f "$file" ]; then
        gnome-terminal -- bash -c "python3 '$file'; bash"
    fi
done
