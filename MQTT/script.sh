#!/bin/bash

for file in ./monitor_*.py; do
    if [ -f "$file" ]; then
        gnome-terminal -- bash -c "python3 '$file'; bash"
    fi
done

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
