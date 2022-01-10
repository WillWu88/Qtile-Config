# import the qtile package
from libqtile.config import Key, Group, Drag, Click
from libqtile.lazy import lazy
from libqtile import extension
from workspace import groups

# Programs and keys
browser = "firefox"
term = "alacritty"
mod = "mod4"

def backlight(action):
    def f(qtile):
        brightness = int(subprocess.run(['xbacklight', '-get'],
                                        stdout=subprocess.PIPE).stdout)
        if brightness != 1 or action != 'dec':
            if (brightness > 49 and action == 'dec') \
                                or (brightness > 39 and action == 'inc'):
                subprocess.run(['xbacklight', f'-{action}', '10',
                                '-fps', '10'])
            else:
                subprocess.run(['xbacklight', f'-{action}', '1'])
    return f

keys = [
    # Switch between windows in current stack pane
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),

    # Move windows up or down in current stack
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),

    Key([mod, "shift"], "l", lazy.layout.swap_right(),
        lazy.layout.client_to_previous()),
    Key([mod, "shift"], "h", lazy.layout.swap_left(),
        lazy.layout.client_to_next()),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next()),
    # Key(["shift"], "space", lazy.layout.previous()),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate(), lazy.layout.flip()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),

    # Resizing windows in monad layout
    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "o", lazy.layout.shrink()),
    Key([mod], "n", lazy.layout.normalize()),

    # spawn programs
    Key([mod], "Return", lazy.spawn(term)), # terminal 
    Key([mod], "BackSpace", lazy.spawn(browser)), # browser
    Key([mod], "v", lazy.spawn(term+" -e vim")), # vim
    Key([mod], "e", lazy.spawn("emacsclient -c -a emacs"), desc='emacs'),# emacs
    Key([mod, "shift"], "p", lazy.spawn(term+" -e scrot")), # screenshot
    Key([mod], "r", lazy.spawn("rofi -show combi")),
    Key([mod], "g", lazy.spawn("galendae")),


    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod, "shift"], "Tab", lazy.prev_layout()), 
    Key([mod], "w", lazy.window.kill()),

    # commands
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),

    # Audio Control
    Key([], "XF86AudioMute",
        lazy.spawn("pamixer -t")),
    Key([], "XF86AudioLowerVolume",
        lazy.spawn("pamixer -d 5")),
    Key([], "XF86AudioRaiseVolume",
        lazy.spawn("pamixer -i 5")),
    Key([], 'XF86MonBrightnessUp',   lazy.function(backlight('inc'))),
    Key([], 'XF86MonBrightnessDown', lazy.function(backlight('dec'))),
    Key([], 'XF86AudioPlay', lazy.spawn("playerctl play-pause")),
    Key([], 'XF86AudioNext', lazy.spawn("playerctl next")),
    Key([], 'XF86AudioPrev', lazy.spawn("playerctl previous")),


    # toggle window stat
    Key([mod], 'm', lazy.window.toggle_minimize()),
    Key([mod], 'f', lazy.window.toggle_floating(),),
    Key([mod], 't', lazy.window.toggle_fullscreen()),

    # shift focus between monitors
    Key([mod, "control"], 'h', lazy.prev_screen()),
    Key([mod, "control"], "l", lazy.next_screen()),

    # Commands for Floating Layout
    Key(["mod1"], "Tab", lazy.group.next_window(), lazy.window.bring_to_front()),
    Key(["mod1", "shift"], "Tab", lazy.group.prev_window(), lazy.window.bring_to_front()),
]

# Keys for switching groups
for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name,
            lazy.window.togroup(i.name, switch_group=True)),
    ])

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
]
