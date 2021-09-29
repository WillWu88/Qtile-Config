from libqtile import layout
from libqtile.config import Match
from colors import *

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(role="EventDialog"),
    Match(role="Msgcompose"),
    Match(role="Preferences"),
    Match(role="pop-up"),
    Match(role="prefwindow"),
    Match(role="task_dialog"),
    Match(wm_class='confirm'),
    Match(wm_class='dialog'),
    Match(wm_class='download'),
    Match(wm_class='error'),
    Match(wm_class='file_progress'),
    Match(wm_class='notification'),
    Match(wm_class='splash'),
    Match(wm_class='toolbar'),
    Match(wm_class='xfce4-appfinder'),
    Match(wm_class='MATLAB R2021a - academic use'),
    Match(wm_class='MATLABWindow'),
    Match(wm_class='Galendae'),
    Match(wm_class='Thunar'),
    Match(wm_class='xfce4'),
    Match(wm_class='com-yworks-A-yEd'),
    ],
    border_focus = tertiaryColor2
)
