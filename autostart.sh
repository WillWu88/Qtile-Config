#!/bin/zsh

# xrdb ~/.Xresources
xmodmap ~/.xmodmap #map caps to ctl
emacs --daemon #star emacs background server
nitrogen --restore # wallpaper setter
xbanish &! # mouse inhibitor
# trayer &!
# nm-applet &!
# redshift -l 38.6:90.3 -t 6500:3600 -g 0.8 -m randr -v &!
# polybar routine
# killall -q polybar
# echo "---" | tee -a /tmp/polybar1.log /tmp/polybar2.log
# polybar -r example | tee -a /tmp/polybar2.log & disown
# ./.config/polybar/launch.sh --pwidgets
#echo "Bars launched..."
