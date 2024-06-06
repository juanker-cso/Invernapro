import os
from pathlib import Path

folder = "UI/"
for file in os.listdir(folder):
    if file.endswith(".ui"):
        name = Path(file).stem
        command = "pyside2-uic " +folder +name +".ui -o \t" +folder +name +".py"
        print(command, end="\t")
        os.popen(command)
        print("...Done")

os.popen("pyside2-rcc UI/placeholder.qrc -o placeholder_rc.py")
