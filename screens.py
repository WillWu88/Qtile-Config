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

batteryIcon = get_bat_icon()

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
                    text = "",
                    foreground = "#ffffff",
                    background = bckgBlue,
                    # padding = 2,
                    fontsize = 15
                ),
                widget.GroupBox(
                    inactive = gbInactive,
                    active = gbActive,
                    fontsize = 11,
                    margin_y = 3,
                    margin_x = 0,
                    padding_y = 5,
                    padding_x = 2,
                    borderwidth = 3,
                    this_current_screen_border = textNForeG,
                    this_screen_border = textNForeG,
                    other_current_screen_border = bckgPurple,
                    other_screen_border = bckgPurple,
                    highlight_color = gbHighLight,
                    highlight_method = "line",
                ),
                widget.TaskList(
                    txt_floating = "🗖",
                    max_title_width = 200,
                    border = bckgPurple,
                    padding_y = 1,
                    borderwidth = 3,
                    highlight_method = "block",
                    icon_size = 15
                ),
                widget.Systray(),
                widget.Sep(
                    linespace = 0,
                    padding = 5,
                    foreground = bckgBlue,
                    background = bckgBlue,
                ),
                widget.TextBox(
                    "",
                    fontsize = 19.5,
                    padding = 0,
                    foreground = bckgPurple,
                    background = bckgBlue,
                ),
                widget.Battery(
                    foreground = textNForeG,
                    background = bckgPurple,
                ),
                widget.TextBox(
                    "",
                    fontsize = 22,
                    padding = 0,
                    foreground = bckgCyan,
                    background = bckgPurple,
                ),
                widget.TextBox(
                    "Vol:",
                    # padding = 0,
                    foreground = textNForeG,
                    background = bckgCyan,
                ),
                widget.Volume(
                    # padding = 0,
                    foreground = textNForeG,
                    background = bckgCyan,
                ),
                widget.TextBox(
                    "",
                    fontsize = 22,
                    padding = 0,
                    foreground = bckgPurple,
                    background = bckgCyan,
                ),
                widget.Clock(
                    format='%Y-%m-%d %a %I:%M %p',
                    background = bckgPurple,
                ),
                widget.TextBox(
                    "",
                    fontsize = 22,
                    padding = 0,
                    foreground = bckgCyan,
                    background = bckgPurple,
                ),
                widget.CurrentLayout(
                    background = bckgCyan,
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
            background = bckgBlue,
            gap = 7,
        ),
        # bottom = bar.Gap(7),
        # right = bar.Gap(7),
        # left = bar.Gap(7),
        wallpaper = '/usr/share/xfce4/backdrops/xubuntu-disco.png',
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
                    text = "",
                    foreground = "#ffffff",
                    background = bckgBlue,
                    padding = 6,
                    fontsize = 15
                ),
                widget.Spacer(
                    length = 5,
                ),
                widget.GroupBox(
                    inactive = gbInactive,
                    active = gbActive,
                    fontsize = 11,
                    margin_y = 3,
                    margin_x = 0,
                    padding_y = 5,
                    padding_x = 2,
                    borderwidth = 3,
                    this_current_screen_border = gbThisScreenB,
                    this_screen_border = gbThisScreenB,
                    other_current_screen_border = gbOtherScreenB,
                    other_screen_border = gbOtherScreenB,
                    highlight_color = gbHighLight,
                    highlight_method = "line",
                ),
                widget.TaskList(
                    txt_floating = "🗖",
                    max_title_width = 200,
                    border = bckgPurple,
                    padding_y = 1,
                    borderwidth = 3,
                    highlight_method = "block",
                    icon_size = 15
                ),
                widget.Systray(),
                widget.Sep(
                    linespace = 0,
                    padding = 5,
                    foreground = bckgBlue,
                    background = bckgBlue,
                ),
                widget.TextBox(
                    "",
                    fontsize = 19.5,
                    padding = 0,
                    foreground = bckgPurple,
                    background = bckgBlue,
                ),
                widget.TextBox(
                    batteryIcon,
                    fontsize = 13,
                    foreground = textNForeG,
                    background = bckgPurple,
                ),
                # widget.Spacer(
                #     length = 3,
                #     background = bckgPurple,
                # ),
                widget.Battery(
                    # charging_char = charging,
                    # discharge_char = threeqpercent,
                    foreground = textNForeG,
                    background = bckgPurple,
                ),
                widget.TextBox(
                    "",
                    fontsize = 22,
                    padding = 0,
                    foreground = bckgCyan,
                    background = bckgPurple,
                ),
                widget.TextBox(
                    "Vol:",
                    # padding = 0,
                    foreground = textNForeG,
                    background = bckgCyan,
                ),
                widget.Volume(
                    # padding = 0,
                    foreground = textNForeG,
                    background = bckgCyan,
                ),
                widget.TextBox(
                    "",
                    fontsize = 22,
                    padding = 0,
                    foreground = bckgPurple,
                    background = bckgCyan,
                ),
                widget.Clock(
                    format='%Y-%m-%d %a %I:%M %p',
                    background = bckgPurple,
                ),
                widget.TextBox(
                    "",
                    fontsize = 22,
                    padding = 0,
                    foreground = bckgCyan,
                    background = bckgPurple,
                ),
                widget.CurrentLayout(
                    background = bckgCyan,
                )
            ],
            24,
            background = bckgBlue,
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


