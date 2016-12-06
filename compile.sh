#!/bin/bash

bdftopcf terminess-breathe.bdf -o terminess-breathe.pcf
gzip -k terminess-breathe.pcf
