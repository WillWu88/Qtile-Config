from libqtile.config import Screen 
from libqtile import layout, bar, widget, qtile
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
wpl = '/usr/share/backgrounds/xfce/xfce-verticals.png'

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
    font = "DejaVu Sans Mono for Powerline Bold",
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
                    text = "",
                    foreground = tertiaryColor2,
                    background = tertiaryColor1,
                    padding = 6,
                    fontsize = 25,
                    mouse_callbacks = {
                        'Button1': lambda: qtile.cmd_spawn('rofi -show combi'),
                    }
                ),
                widget.Spacer(
                    length = 5,
                    **extension_defaults
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
                    txt_floating = "",
                    max_title_width = 200,
                    border = primaryColor,
                    padding_y = 1,
                    borderwidth = 3,
                    highlight_method = "block",
                    icon_size = 15,
                ),
                widget.TextBox(
                    "",
                    fontsize = 22,
                    padding = 0,
                    foreground = secondaryColor,
                    background = tertiaryColor1,
                ),
                # widget.NetGraph(
                #     mouse_callbacks = {
                #         'Button1': lambda: qtile.cmd_spawn('nm-applet'),
                #     },
                #     background = secondaryColor,
                #     type = 'line',
                # ),
                widget.Systray(
                    systray = "trayer",
                    background = secondaryColor,
                ),
                # widget.Sep(
                #     linespace = 0,
                #     padding = 5,
                #     foreground = tertiaryColor1,
                #     background = tertiaryColor1,
                # ),
                widget.TextBox(
                    "",
                    fontsize = 22,
                    padding = 0,
                    foreground = primaryColor,
                    background = secondaryColor,
                ),
                widget.Battery(
                    foreground = tertiaryColor2,
                    background = primaryColor,
                ),
                widget.TextBox(
                    "",
                    fontsize = 22,
                    padding = 0,
                    foreground = secondaryColor,
                    background = primaryColor,
                ),
                widget.TextBox(
                    "VOL:",
                    # padding = 0,
                    foreground = tertiaryColor2,
                    background = secondaryColor,
                ),
                widget.PulseVolume(
                    get_volume_cmd = "pamixer --get-volume",
                    # padding = 0,
                    foreground = tertiaryColor2,
                    background = secondaryColor,
                    volume_app = "pamixer",
                    step = 5,
                    update_interval = 0.1
                ),
                widget.TextBox(
                    "",
                    fontsize = 22,
                    padding = 0,
                    foreground = primaryColor,
                    background = secondaryColor,
                ),
                widget.Clock(
                    format='%Y-%m-%d %a %I:%M %p',
                    background = primaryColor,
                    mouse_callbacks = {
                        'Button1': lambda: qtile.cmd_spawn('galendae'),
                    }
                ),
                widget.TextBox(
                    "",
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
second_Screen = Screen(top=bar.Bar(
            [
                #widget.CurrentLayoutIcon(
                #    scale = 0.9
                #),
                widget.TextBox(
                    text = "",
                    foreground = tertiaryColor2,
                    background = tertiaryColor1,
                    padding = 6,
                    fontsize = 25,
                    mouse_callbacks = {
                        'Button1': lambda: qtile.cmd_spawn('rofi -show combi'),
                    }
                ),
                widget.Spacer(
                    length = 5,
                    **extension_defaults
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
                    txt_floating = "",
                    max_title_width = 200,
                    border = primaryColor,
                    padding_y = 1,
                    borderwidth = 3,
                    highlight_method = "block",
                    icon_size = 15,
                ),
                widget.TextBox(
                    "",
                    fontsize = 22,
                    padding = 0,
                    foreground = secondaryColor,
                    background = tertiaryColor1,
                ),
                # widget.NetGraph(
                #     mouse_callbacks = {
                #         'Button1': lambda: qtile.cmd_spawn('nm-applet'),
                #     },
                #     background = secondaryColor,
                #     type = 'line',
                # ),
                widget.Memory(
                    background = secondaryColor,

                ),
                # widget.Sep(
                #     linespace = 0,
                #     padding = 5,
                #     foreground = tertiaryColor1,
                #     background = tertiaryColor1,
                # ),
                widget.TextBox(
                    "",
                    fontsize = 22,
                    padding = 0,
                    foreground = primaryColor,
                    background = secondaryColor,
                ),
                widget.Battery(
                    foreground = tertiaryColor2,
                    background = primaryColor,
                ),
                widget.TextBox(
                    "",
                    fontsize = 22,
                    padding = 0,
                    foreground = secondaryColor,
                    background = primaryColor,
                ),
                widget.TextBox(
                    "VOL:",
                    # padding = 0,
                    foreground = tertiaryColor2,
                    background = secondaryColor,
                ),
                widget.PulseVolume(
                    get_volume_cmd = "pamixer --get-volume",
                    # padding = 0,
                    foreground = tertiaryColor2,
                    background = secondaryColor,
                    volume_app = "pamixer",
                    step = 5,
                    update_interval = 0.1
                ),
                widget.TextBox(
                    "",
                    fontsize = 22,
                    padding = 0,
                    foreground = primaryColor,
                    background = secondaryColor,
                ),
                widget.Clock(
                    format='%Y-%m-%d %a %I:%M %p',
                    background = primaryColor,
                    mouse_callbacks = {
                        'Button1': lambda: qtile.cmd_spawn('galendae'),
                    }
                ),
                widget.TextBox(
                    "",
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
    screens.append(second_Screen)
if (num_monitors == 1) & (len(screens) == 2):
    screens = [default_screen]


