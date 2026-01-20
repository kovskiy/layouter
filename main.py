from hyprpy import Hyprland
from hyprpy.utils.shell import run_or_fail

trigger = "vesktop"

inst= Hyprland()

user_keyboard = str(input("Enter your device name (you can get it using 'hyprctl devices' command!): "))

def current_layout(sender, **kwargs):
    layout = kwargs["layout_name"]
    keyboard = kwargs["keyboard_name"]

    print(f"{layout}", "+", f"{keyboard}")

def super_window(sender, **kwargs):
    win = kwargs["window_class"]

    print(f"current class is: {win}")
    if win == trigger:
        run_or_fail(["hyprctl", "switchxkblayout", f"{user_keyboard}", "2"])

inst.signals.activelayout.connect(current_layout)
inst.signals.activewindow.connect(super_window)

inst.watch()