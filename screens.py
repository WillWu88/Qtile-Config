from libqtile.config import Screen 
from libqtile import layout, bar, widget
from Xlib import display as xdisplay


from colors import *
import psutil

fullCharge_unplugged = " "
fullCharge_plugged = " "
threeqpercent = " "
twoqpercent = " "
oneqpercent = " "
batteryLow = " "
charging = " "
wpl = '/usr/share/backgrounds/mono.png'

def get_bat_icon():
    batPercent = psutil.sensors_battery().percent
    plugged = psutil.sensors_battery().power_plugged
    if plugged:
        if batPercent >=97:
            return fullCharge_plugged
        else:
            return charging
    else:
        if batPercent >= 75:
            return threeqpercent
        elif batPercent >= 40 & batPercent <= 75:
            return twoqpercent
        elif batPercent <=40 & batPercent >= 20:
            return oneqpercent
        else:
            return batteryLow

# batteryIcon = get_bat_icon()

def get_num_monitors():
    num_monitors = 0
    try:
        display = xdisplay.Display()
        screen = display.screen()
        resources = screen.root.xrandr_get_screen_resources()

        for output in resources.outputs:
            monitor = display.xrandr_get_output_info(output, resources.config_timestamp)
            preferred = False
            if hasattr(monitor, "preferred"):
                preferred = monitor.preferred
            elif hasattr(monitor, "num_preferred"):
                preferred = monitor.num_preferred
            if preferred:
                num_monitors += 1
    except Exception as e:
        # always setup at least one monitor
        return 1
    else:
        return num_monitors

num_monitors = get_num_monitors()

widget_defaults = dict(
    font='Source Code Pro',
    fontsize=12,
    padding=3,
)

extension_defaults = dict(
    font='Sauce Code Pro',
    fontsize=12,
    padding=3,
)

default_screen = Screen(top=bar.Bar(
            [
                #widget.CurrentLayoutIcon(
                #    scale = 0.9
                #),
                widget.TextBox(
                    text = "",
                    foreground = tertiaryColor2,
                    background = tertiaryColor1,
                    padding = 6,
                    fontsize = 15
                ),
                widget.Spacer(
                    length = 5,
                ),
                widget.GroupBox(
                    inactive = tertiaryColor2,
                    active = tertiaryColor2,
                    fontsize = 11,
                    margin_y = 3,
                    margin_x = 0,
                    padding_y = 5,
                    padding_x = 2,
                    borderwidth = 3,
                    this_current_screen_border = tertiaryColor2,
                    this_screen_border = tertiaryColor2,
                    other_current_screen_border = secondaryColor,
                    other_screen_border = secondaryColor,
                    highlight_color = primaryColor,
                    highlight_method = "line",
                ),
                widget.TaskList(
                    txt_floating = "🗖",
                    max_title_width = 200,
                    border = primaryColor,
                    padding_y = 1,
                    borderwidth = 3,
                    highlight_method = "block",
                    icon_size = 15
                ),
                widget.Systray(),
                widget.Sep(
                    linespace = 0,
                    padding = 5,
                    foreground = tertiaryColor1,
                    background = tertiaryColor1,
                ),
                widget.TextBox(
                    "",
                    fontsize = 19.5,
                    padding = 0,
                    foreground = primaryColor,
                    background = tertiaryColor1,
                ),
                widget.Battery(
                    foreground = tertiaryColor2,
                    background = primaryColor,
                ),
                widget.TextBox(
                    "",
                    fontsize = 22,
                    padding = 0,
                    foreground = secondaryColor,
                    background = primaryColor,
                ),
                widget.TextBox(
                    "Vol:",
                    # padding = 0,
                    foreground = tertiaryColor2,
                    background = secondaryColor,
                ),
                widget.Volume(
                    # padding = 0,
                    foreground = tertiaryColor2,
                    background = secondaryColor,
                ),
                widget.TextBox(
                    "",
                    fontsize = 22,
                    padding = 0,
                    foreground = primaryColor,
                    background = secondaryColor,
                ),
                widget.Clock(
                    format='%Y-%m-%d %a %I:%M %p',
                    background = primaryColor,
                ),
                widget.TextBox(
                    "",
                    fontsize = 22,
                    padding = 0,
                    foreground = secondaryColor,
                    background = primaryColor,
                ),
                widget.CurrentLayout(
                    background = secondaryColor,
                )
                # widget.TextBox(
                #     "",
                #     fontsize = 22,
                #     padding = 0,
                #     foreground = bckgCyan,
                #     background = bckgPurple,
                # ),
            ],
            24,
            background = tertiaryColor1,
            gap = 7,
        ),
        # bottom = bar.Gap(7),
        # right = bar.Gap(7),
        # left = bar.Gap(7),
        wallpaper = wpl,
        wallpaper_mode = 'fill',
    )
screens = [default_screen]
if (num_monitors == 2):
    screens.append(Screen(
        top=bar.Bar(
            [
                #widget.CurrentLayoutIcon(
                #    scale = 0.9
                #),
                widget.TextBox(
                    text = "",
                    foreground = tertiaryColor2,
                    background = tertiaryColor1,
                    # padding = 6,
                    fontsize = 15
                ),
                widget.Spacer(
                    length = 5,
                ),
                widget.GroupBox(
                    inactive = tertiaryColor2,
                    active = tertiaryColor2,
                    fontsize = 11,
                    margin_y = 3,
                    margin_x = 0,
                    padding_y = 5,
                    padding_x = 2,
                    borderwidth = 3,
                    this_current_screen_border = tertiaryColor2,
                    this_screen_border = tertiaryColor2,
                    other_current_screen_border = secondaryColor,
                    other_screen_border = secondaryColor,
                    highlight_color = primaryColor,
                    highlight_method = "line",
                ),
                widget.TaskList(
                    txt_floating = "🗖",
                    max_title_width = 200,
                    border = primaryColor,
                    padding_y = 1,
                    borderwidth = 3,
                    highlight_method = "block",
                    icon_size = 15
                ),
                widget.Systray(),
                widget.Sep(
                    linespace = 0,
                    padding = 5,
                    foreground = tertiaryColor1,
                    background = tertiaryColor1,
                ),
                widget.TextBox(
                    "",
                    fontsize = 19.5,
                    padding = 0,
                    foreground = primaryColor,
                    background = tertiaryColor1,
                ),
                widget.Battery(
                    foreground = tertiaryColor2,
                    background = primaryColor,
                ),
                widget.TextBox(
                    "",
                    fontsize = 22,
                    padding = 0,
                    foreground = secondaryColor,
                    background = primaryColor,
                ),
                widget.TextBox(
                    "Vol:",
                    # padding = 0,
                    foreground = tertiaryColor2,
                    background = secondaryColor,
                ),
                widget.Volume(
                    # padding = 0,
                    foreground = tertiaryColor2,
                    background = secondaryColor,
                ),
                widget.TextBox(
                    "",
                    fontsize = 22,
                    padding = 0,
                    foreground = primaryColor,
                    background = secondaryColor,
                ),
                widget.Clock(
                    format='%Y-%m-%d %a %I:%M %p',
                    background = primaryColor,
                ),
                widget.TextBox(
                    "",
                    fontsize = 22,
                    padding = 0,
                    foreground = secondaryColor,
                    background = primaryColor,
                ),
                widget.CurrentLayout(
                    background = secondaryColor,
                )
            ],
            24,
            background = tertiaryColor1,
        ),
        # bottom = bar.Gap(7),
        # right = bar.Gap(7),
        # left = bar.Gap(7),
        wallpaper = '/usr/share/xfce4/backdrops/xubuntu-disco.png',
        wallpaper_mode = 'fill',
    )
    )
if (num_monitors == 1) & (len(screens) == 2):
    screens = [default_screen]


