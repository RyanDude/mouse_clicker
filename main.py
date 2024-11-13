from pynput import keyboard, mouse

mouse_control = mouse.Controller()


def on_press(key):
    try:
        if key.char == 'l':
            mouse_control.click(mouse.Button.left)
        if key.char == 'r':
            mouse_control.click(mouse.Button.right)
        if key.char == 'q':
            exit()
    except AttributeError:
        pass


''' 
if only using start() function, the main thread will run again, and the program will end
if using join(), it will wait for the listener thread to finish first, but listener thread is a dead loop
'''
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
