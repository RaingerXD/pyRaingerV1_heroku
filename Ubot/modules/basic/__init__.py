from pyrogram import Client, filters
from Ubot import cmds
import os
import sys
from os import environ, execle, path, remove
from Ubot.modules.basic.help import add_command_help
from Ubotlibs import BOT_VER
from Ubotlibs.Ubot import Ubot, Devs
add_command_help = add_command_help

ADMINS = [5615921474]

BL_GCAST = [-1001755737234, -1001599474353, -1001692751821, -1001473548283, -1001459812644, -1001433238829, -1001476936696, -1001327032795, -1001294181499, -1001419516987, -1001209432070, -1001296934585, -1001481357570, -1001459701099, -1001109837870, -1001485393652, -1001354786862, -1001109500936, -1001387666944, -1001390552926, -1001752592753, -1001777428244, -1001771438298, -1001287188817, -1001812143750, -1001883961446, -1001753840975, -1001896051491, -1001578091827]


BL_UBOT = [1245451624]
DEVS = [
  5615921474,
  ]

def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Ubot"])
