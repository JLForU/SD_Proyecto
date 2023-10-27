#!/bin/bash

echo -e "\nSTARTS SHELL"

# Check if the 'javac' command is available
if ! command -v javac &> /dev/null; then
    echo "Java compiler (javac) not found. Please make sure Java Development Kit (JDK) is installed."
    exit 1
fi

# Compile all .java files in the current directory
for file in *.java; do
    if [ -f "$file" ]; then
        echo -e "\tCompiling $file..."
        javac "$file" -cp ./bin
        if [ $? -eq 0 ]; then
            echo -e "\tCompilation successful."
        else
            echo -e "\tCompilation failed for $file."
        fi
    fi
done

echo -e "ENDS SHELL"

# Execute all .class files (assuming they have a 'main' method)
#for file in *.class; do
#    if [ -f "$file" ]; then
#        echo "Executing $file..."
#        java "${file%.class}"
#    fi
#done

echo -e '\n'

java -cp ./bin Servidor

echo -e '\n'

