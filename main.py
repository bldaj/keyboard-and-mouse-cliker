from time import sleep
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

keyboard = KeyboardController()
mouse = MouseController()


def main():
    while True:
        keyboard.press(Key.up)
        keyboard.release(Key.up)
        sleep(3)

        keyboard.press(Key.down)
        keyboard.release(Key.down)
        sleep(1.5)

        mouse.press(Button.left)
        mouse.release(Button.left)


if __name__ == '__main__':
    main()
