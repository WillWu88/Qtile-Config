#!/bin/zsh

# xrdb ~/.Xresources
xmodmap ~/.xmodmap #map caps to ctl
emacs --daemon #star emacs background server
nitrogen --restore # wallpaper setter
xbanish &! # mouse inhibitor
# trayer &!
# nm-applet &!
# redshift -l 38.6:90.3 -t 6500:3600 -g 0.8 -m randr -v &!
