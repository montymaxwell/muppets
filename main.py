import numpy
import cv2 as cv
import pytesseract
from PIL import ImageGrab
from threading import Thread
from pynput.keyboard import Key, Controller

# TESSERACT PATH CONFIG
pytesseract.pytesseract.tesseract_cmd = r'C:\Tesseract\tesseract.exe'

# SCREEN CAPTURE CONFIG
# --- 1080p config ---
POSX = 20
POSY = 1000
WIN_WIDTH = 560
WIN_HEIGHT = 1025
# ---  720p Config ---
# NOTE: Valorant must be windowed but maximized
# POSX = 10
# POSY = 950
# WIN_WIDTH = 490
# WIN_HEIGHT = 970

KEYBOARD = Controller()

action_queue = []
subaction_queue = []

def press(key: Key, count: int):
    for i in range(count):
        print(i)
        KEYBOARD.press(key=key)
    KEYBOARD.release(key=key)

def parser(text: str) -> str:
    arr = text.split(":")
    return arr[1].strip()

def fps_movement(commanddata: str) -> bool:
    cmd = commanddata.split(" ")
    steps = 1
    if len(cmd) >= 2:
        if cmd[1] == "forward":
            if len(cmd) == 3 and cmd[2]:
                steps = int(cmd[2])
            press('w', steps)
            return True

        elif cmd[1] == "left":
            if len(cmd) == 3 and cmd[2]:
                steps = int(cmd[2])
            press("a", steps)
            return True

        elif cmd[1] == "right":
            if len(cmd) == 3 and cmd[2]:
                steps = int(cmd[2])
            press("d", steps)
            return True

        elif cmd[1] == "back":
            if len(cmd) == 3 and cmd[2]:
                steps = int(cmd[2])
            press("s", steps)
            return True

        else: return False

def action_event():
    while True:
        if len(action_queue) > 0:
            action: str = action_queue.pop(0)
            print(action)
            fps_movement(commanddata=parser(text=action))

if __name__=='__main__':
    # action_thread = Thread(target=action_event)
    # action_thread.daemon = True
    # action_thread.start()

    last_text: str = ""
    current_text: str = ""
    while True:
        vision = ImageGrab.grab(bbox=(POSX, POSY, WIN_WIDTH, WIN_HEIGHT))
        vision = vision.convert('L')
        vision = numpy.array(vision)
        vision = cv.cvtColor(vision, cv.COLOR_RGB2BGR)
        cv.imshow("Computer Vision", vision)

        if(current_text != last_text):
            last_text = current_text
            # my setup sees (AU) instead of (All).
            if(last_text.startswith("(Team)") or last_text.startswith("(AU)")):
                if("_play" in last_text):
                        # i want to play songs through microphone
                    pass
                elif("_move" in last_text):
                    print(last_text.strip())
                    fps_movement(commanddata=parser(text=last_text.strip()))
                else: pass
            else: pass
        else:
            current_text = pytesseract.image_to_string(vision)

        if(cv.waitKey(1) == ord('q')):
            cv.destroyAllWindows()
            break