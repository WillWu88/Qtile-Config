from libqtile import layout
from colors import *

layout_param = {"border_focus": primaryColor,
                "border_normal": tertiaryColor2,
                "border_width": 3,
                "margin": 10,
               }
layouts = [
    layout.MonadTall(**layout_param),
    layout.MonadWide(**layout_param),
    layout.Stack(num_stacks=2, fair = True, **layout_param),
    layout.Stack(num_stacks=1, **layout_param),
    layout.RatioTile(**layout_param),
    layout.Floating(),
]
