from hyprpy import Hyprland
from hyprpy.utils.shell import run_or_fail
import toml

inst = Hyprland()

#log = True

config = toml.load('config.toml')
user_keyboard = config['keyboards'][0]

layout = None

# doesn't work for some reason? Probably i'm just stupid

#def logger(sender, **kwargs):
#    w = kwargs["window_class"]
#    l = kwargs["layout_name"]
#    k = kwargs["keyboard_name"]
#
#    if log = True:
#        print(f"current class is '{w}', layout is '{l}' and keyboard is '{k}'")

def switcher(sender, **kwargs):
    win = kwargs["window_class"]

    for index, windows, in config['layouts'].items():
        if win in windows:
            layout = index
            run_or_fail(["hyprctl", "switchxkblayout", f"{user_keyboard}", f"{layout}"])

#inst.signals.activewindow.connect(logger)
#inst.signals.activelayout.connect(logger)
inst.signals.activewindow.connect(switcher)

inst.watch()
