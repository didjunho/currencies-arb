#!/bin/bash

#function called by trap
do_this_on_ctrl_c(){
    echo "Exited the loop, there were $loopN number of loops executed !"
    date
    exit 0
}

trap 'do_this_on_ctrl_c' SIGINT

loopN=0

while true
do
    python3 get.py 
    python3 clearMem.py
    sleep 5m
done