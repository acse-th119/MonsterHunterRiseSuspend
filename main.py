# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import subprocess
from pynput.keyboard import GlobalHotKeys
import time
def on_activate_h():
    # subprocess.call('start C:\Games\ps_pause\pssuspend.exe MonsterHunterRise.exe')
    subprocess.call('cmd /c start pssuspend.exe MonsterHunterRise.exe')
    print('<ctrl>+<alt>+h pressed')

def on_activate_i():
    subprocess.call('cmd /c start pssuspend.exe -r MonsterHunterRise.exe')
    print('<ctrl>+<alt>+i pressed')

# Press the green button in the gutter to run the script.

with GlobalHotKeys({
    '<ctrl>+<alt>+h': on_activate_h,
    '<ctrl>+<alt>+i': on_activate_i}) as h:
    h.join()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
