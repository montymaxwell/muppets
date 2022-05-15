import time
from pynput.mouse import Button, Controller as mouse_controller
from pynput.keyboard import Key, Controller as keyboard_controller
import pydirectinput

# entire shit is deprecated, or not?
KEYBOARD = keyboard_controller()
MOUSE = mouse_controller()

# <?deprecated?> 
def press(key: Key, count: int) -> None:
    for i in range(count):
        KEYBOARD.press(key=key)
    KEYBOARD.release(key=key)

def mouse(btn: Button, count: int) -> None:
    for i in range(count):
        MOUSE.press(btn)
        MOUSE.release(btn)

def action_press(key: Key, count: int):
    for i in range(count):
        KEYBOARD.press(key=key)
        KEYBOARD.release(key=key)
        time.sleep(1)

def action_mouse(btn: Button, count: int) -> None:
    for i in range(count):
        MOUSE.press(btn)
        time.sleep(1)
        MOUSE.release(btn)

def get_steps(data: list[str]) -> int:
    if len(data) == 2 and data[1]:
        if int(data[1]) < 1000:
            return int(data[1]) * 2
        elif int(data[1]) > 5000:
            return int(data[1])
        else: return 1
# </?deprecated?>

def fps_movement(commanddata: str) -> bool:
    cmd = commanddata.split(" ")
    print(cmd)
    steps = 1
    if len(cmd) >= 1:
        if cmd[0] == "_forward":
            steps = get_steps(cmd)
            press("w", steps)
            return True

        elif cmd[0] == "_left":
            steps = get_steps(cmd)
            press("a", steps)
            return True

        elif cmd[0] == "_right":
            steps = get_steps(cmd)
            press("d", steps)
            return True

        elif cmd[0] == "_back":
            steps = get_steps(cmd)
            press("s", steps)
            return True

        else: return False

def actions(commanddata: str) -> bool:
    cmd = commanddata.split(" ")
    print(cmd)
    count = 1
    if len(cmd) >= 1:
        if cmd[0] == "_jump":
            count = get_steps(cmd)
            pydirectinput.press(keys="space", presses=count, interval=1)
            return True

        elif cmd[0] == "_crouch":
            count = get_steps(cmd)
            pydirectinput.press(keys="ctrl", presses=count, interval=1)
            return True

        elif cmd[0] == "_fire":
            count = get_steps(cmd)
            pydirectinput.press(keys="i", presses=count)
            return True

        elif cmd[0] == "_aim":
            count = get_steps(cmd)
            pydirectinput.press(keys="o", presses=count)
            return True
        
        elif cmd[0] == "_drop":
            count = get_steps(cmd)
            pydirectinput.press(keys="g", presses=count)

        elif cmd[0] == "_spike":
            count = get_steps(cmd)
            pydirectinput.press(keys="p", presses=count)
            return True

        elif cmd[0] == "_look-left":
            count = get_steps(cmd)
            pydirectinput.moveRel(yOffset=count, duration=5)
            return True

        elif cmd[0] == "_look-right":
            count = get_steps(cmd)
            pydirectinput.moveRel(xOffset=-abs(count), duration=5)
            return True

        elif cmd[0] == "_look-up":
            count = get_steps(cmd)
            pydirectinput.moveRel(yOffset=count, duration=5)
            return True

        elif cmd[0] == "_look-down":
            count = get_steps(cmd)
            pydirectinput.moveRel(yOffset=-abs(count), duration=5)
            return True


        else: return False