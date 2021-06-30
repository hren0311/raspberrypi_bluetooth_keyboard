from picap import Picap
from time import sleep
from key import Key

def main():

    picap = Picap()
    key = Key()
    
    while running:

        try:

            touch_l,release_l = picap.getData()
            key.keyInput(touch_l,release_l)
        runngin = True
        except KeyboardInterrupt:
            running = False
        sleep(0.01)

if __name__ == '__main__':
    main()