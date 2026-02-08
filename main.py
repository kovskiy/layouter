from hyprpy import Hyprland
from hyprpy.utils.shell import run_or_fail
import toml
from pathlib import Path
import argparse
from logger import logger_window, logger_layout

inst = Hyprland()

config_path = Path("~/.config/layouter/config.toml").expanduser()
with config_path.open("r", encoding="utf-8") as c:
    config = toml.load(c)

user_keyboard = config['keyboards'][0]

layout = None

def switcher(sender, **kwargs):
    win = kwargs["window_class"]

    for index, windows, in config['layouts'].items():
        if win in windows:
            layout = index
            run_or_fail(["hyprctl", "switchxkblayout", f"{user_keyboard}", f"{layout}"])

log = False

parser = argparse.ArgumentParser()
parser.add_argument(
    "--debug",
    action="store_true"
)

args = parser.parse_args()
log = args.debug

if log:
    inst.signals.activewindow.connect(logger_window)
    inst.signals.activelayout.connect(logger_layout)
inst.signals.activewindow.connect(switcher)

inst.watch()
