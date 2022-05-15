import numpy
import cv2 as cv
import pytesseract
from PIL import ImageGrab
from multiprocessing import Process, Manager

from handlers.controllers import fps_movement
from event import event_handler

# TESSERACT PATH CONFIG
pytesseract.pytesseract.tesseract_cmd = r'C:\Tesseract\tesseract.exe'

# VALORANT CHAT SCREEN CAPTURE CONFIG
# --- 1080p config ---
POSX = 20
POSY = 1000
WIN_WIDTH = 560
WIN_HEIGHT = 1025
# ---  720p Config in 1080p Monitor ---
# NOTE: Valorant must be windowed but maximized
# POSX = 10
# POSY = 950
# WIN_WIDTH = 490
# WIN_HEIGHT = 970

def parser(text: str) -> str:
    arr = text.split(":")
    return arr[1].strip()

def action_event(action_queue: list[str]) -> None:
    while True:
        if len(action_queue) > 0:
            action: str = action_queue.pop(0)
            print(action)
            fps_movement(commanddata=parser(text=action))
            pass
        else: pass

def main(action_queue: list[str]) -> None:
    last_text: str = ""
    current_text: str = ""
    while True:
        vision = ImageGrab.grab(bbox=(POSX, POSY, WIN_WIDTH, WIN_HEIGHT))
        vision = vision.convert('L')
        vision = numpy.array(vision)
        vision = cv.cvtColor(vision, cv.COLOR_RGB2BGR)
        cv.imshow("Computer Vision", vision)

        if(current_text != last_text):
            last_text = current_text.strip()
            if("(Team)" in last_text or "(All)" in last_text or "(AU)" in last_text):
                temp = parser(last_text.strip())
                if temp.startswith("_"):
                    action_queue.append(temp)
                    pass

                # elif("_play" in last_text):
                #         # i want to play songs through the microphone but cannot. sad.
                #     pass
                pass
            else: pass
            pass
        else:
            current_text = pytesseract.image_to_string(vision)
            current_text = current_text.strip()
            pass

        if(cv.waitKey(1) == ord('q')):
            cv.destroyAllWindows()
            break

if __name__=='__main__':
    manager = Manager()
    arr = manager.list()

    p1 = Process(target=main, args=(arr,))
    p1.start()

    p2 = Process(target=event_handler, args=(arr,))
    p2.start()

    p1.join()
    p2.join()