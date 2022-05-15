from threading import Thread
from handlers.controllers import fps_movement, actions

def event_handler(arr: list[str]) -> None:
    while True:
        if len(arr) > 0:
            action: str = arr.pop(0)

            if action.startswith("_forward") or action.startswith("_back"):
                y_pos_thread = Thread(target=fps_movement, args=(action,))
                y_pos_thread.daemon = True
                y_pos_thread.start()
                pass
            elif action.startswith("_left") or action.startswith("_right"):
                x_pos_thread = Thread(target=fps_movement, args=(action,))
                x_pos_thread.daemon = True
                x_pos_thread.start()
                pass
            elif action.startswith("_jump") or action.startswith("_crouch"):
                annoying_thread = Thread(target=actions, args=(action,))
                annoying_thread.daemon = True
                annoying_thread.start()
                pass
            elif action.startswith("_aim") or action.startswith("_fire") or action.startswith("_drop"):
                action_thread = Thread(target=actions, args=(action,))
                action_thread.daemon = True
                action_thread.start()
                pass

            else: pass