#!/usr/bin/env sh
ifconfig | grep -w wlan0 > /dev/null
if [ $? -ne 0 ]; then
    sudo ifconfig wlan0 up
    /home/lane/pi-script/declare-IP.py
fi
