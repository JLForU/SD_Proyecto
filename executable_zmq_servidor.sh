#!/bin/bash

# Compile all .java files in the current directory
for file in *.java; do
    if [ -f "$file" ]; then
        # echo "Compiling $file..."
        javac -cp /usr/share/java/zmq-3.1.0.jar:/usr/share/java/jzmq-3.1.0.jar:/usr/share/java/jzmq.jar:/usr/share/java/zmq.jar:. -d bin "$file"
        # if [ $? -eq 0 ]; then
            # echo "Compilation successful."
        # else
            # echo "Compilation failed for $file."
        # fi
    fi
done

java -cp /usr/share/java/zmq-3.1.0.jar:/usr/share/java/jzmq-3.1.0.jar:/usr/share/java/jzmq.jar:/usr/share/java/zmq.jar:bin Servidor

