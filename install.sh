#!/bin/bash

dir="$HOME/.local/share/fonts/X11"

mkdir -p "$dir"
cp terminess-breathe.pcf.gz "$dir"
fc-cache -v | grep "$dir"
