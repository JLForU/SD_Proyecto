#!/bin/bash

# Check if the 'javac' command is available
if ! command -v javac &> /dev/null; then
    echo "Java compiler (javac) not found. Please make sure Java Development Kit (JDK) is installed."
    exit 1
fi

# Compile all .java files in the current directory
for file in *.java; do
    if [ -f "$file" ]; then
        echo "Compiling $file..."
        javac "$file"
        if [ $? -eq 0 ]; then
            echo "Compilation successful."
        else
            echo "Compilation failed for $file."
        fi
    fi
done

# Execute all .class files (assuming they have a 'main' method)
#for file in *.class; do
#    if [ -f "$file" ]; then
#        echo "Executing $file..."
#        java "${file%.class}"
#    fi
#done

