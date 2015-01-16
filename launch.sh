#!/bin/bash
if [ ! -f contours ]; then
    g++ `pkg-config --cflags --libs opencv` contours.cpp -o contours
fi

exec monkeyrunner monkey.py
