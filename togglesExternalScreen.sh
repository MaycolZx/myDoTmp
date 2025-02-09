#!/bin/sh
intern=HDMI2
extern=eDP1

if xrandr | grep "$extern disconnected"; then
    xrandr --output "$extern" --off --output "$intern" --auto
else
    xrandr --output "$intern" --off --output "$extern" --auto
fi
#xrandr --output HDMI2 --mode 1920x1080 --right-of eDP1
