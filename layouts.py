from libqtile import layout
from colors import *

layout_param = {"border_focus": borderFColor,
                "border_normal": borderNColor,
                "border_width": 3,
                "margin": 20,
               }
layouts = [
    layout.MonadTall(**layout_param),
    layout.MonadWide(**layout_param),
    layout.Stack(num_stacks=2, **layout_param),
    layout.Max(**layout_param),
    layout.Floating(),
]
