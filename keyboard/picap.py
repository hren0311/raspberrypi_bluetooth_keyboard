
import MPR121
import sys

class Picap:
    touch_threshold = 40
    release_threshold = 20
    def __init__(self) -> None:
        try:
            self.sensor = MPR121.begin()
        except Exception as e:
            print (e)
            sys.exit(1)

        self.sensor.set_touch_threshold(self.touch_threshold)
        self.sensor.set_release_threshold(self.release_threshold)

    def getData(self):

        if self.sensor.touch_status_changed():
            self.sensor.update_touch_data()
            touch_l = [i for i in range(12) if self.sensor.is_new_touch(i)]
            release_l = [i for i in range(12) if self.sensor.is_new_release(i)]
            return touch_l,release_l
        else:
            return [],[]
            