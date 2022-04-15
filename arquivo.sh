#!/bin/bash

for arq in 1 2 3 4 5; do
	touch ~/Downloads/$arq.txt
	touch -t 2201012359 ~/Downloads/$arq.txt
done


