import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
from random import uniform


delay = 0.05
button = Button.left
start_stop_key = KeyCode(char='a')
stop_key = KeyCode(char='b')


class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == stop_key:
        click_thread.exit()
        listener.stop()


if __name__ == "__main__":
    mouse = Controller()
    click_thread = ClickMouse(uniform(delay-delay*0.1, delay+delay*0.1), button)
    click_thread.start()

    with Listener(on_press=on_press) as listener:
        listener.join()
