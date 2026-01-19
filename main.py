from hyprpy import Hyprland
from hyprpy.utils.shell import run_or_fail
import time

trigger = "discord"

inst= Hyprland()

#while (True):
#    var = instance.get_active_window()
#    print(var.wm_class)
#    time.sleep(0.5)

def super_window(sender, **kwargs):
    print("event kwargs: ", kwargs)

    win = inst.get_active_window()
    if win.wm_class == trigger:
        print("yay")

inst.signals.activewindow.connect(super_window)

inst.watch()