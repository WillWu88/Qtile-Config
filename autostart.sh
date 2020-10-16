#!/bin/zsh

xrdb ~/.Xresources
xmodmap ~/.xmodmap
redshift -l 22.5:114.1 -t 6500:3600 -g 0.8 -m randr -v &!
