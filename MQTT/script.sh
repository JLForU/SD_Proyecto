#!/bin/bash

# Loop through all Python files in the directory.
for file in ./*.py; do
	gnome-terminal -- bash -c "python3 '$file'; bash"
done
