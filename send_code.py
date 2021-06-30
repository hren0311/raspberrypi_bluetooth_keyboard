import os #used to all external commands
import sys # used to exit the script
import dbus
import evdev
import keymap
import time
from time import sleep

HID_DBUS = 'org.yaptb.btkbservice'
HID_SRVC = '/org/yaptb/btkbservice'


class SendKeycode:
    """
    Send the HID messages to the keyboard D-Bus server for specified button
    """
    def __init__(self):
        self.bus = dbus.SystemBus()
        self.btkobject = self.bus.get_object(HID_DBUS,
                                             HID_SRVC)
        self.btk_service = dbus.Interface(self.btkobject,
                                          HID_DBUS)

    def popinSendKey(self, send_string):
        targetCode = int(keymap.keytable[ send_string ])
        targetKeys = [161, 1, 0, 0, targetCode, 0, 0, 0, 0, 0]
        all_keys_up = [161, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        
        self.btk_service.send_keys(targetKeys)
        time.sleep(0.001)
        self.btk_service.send_keys(all_keys_up)

# original thread's class 
class CameraRemote:
    """
    Send the HID messages to the keyboard D-Bus server for the volume-up button
    """
    def __init__(self):
        self.bus = dbus.SystemBus()
        self.btkobject = self.bus.get_object(HID_DBUS,
                                             HID_SRVC)
        self.btk_service = dbus.Interface(self.btkobject,
                                          HID_DBUS)

    def take_photo(self):
        volume_up = [161, 1, 0, 0, 237, 0, 0, 0, 0, 0]
        all_keys_up = [161, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        self.btk_service.send_keys(volume_up)
        time.sleep(0.001)
        self.btk_service.send_keys(all_keys_up)

    def take_screenshot(self):
        pwr_and_vol_down= [161, 1, 0, 0, 102, 238, 0, 0, 0, 0]
        all_keys_up = [161, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        self.btk_service.send_keys(pwr_and_vol_down)
        time.sleep(0.001)
        self.btk_service.send_keys(all_keys_up)

if __name__ == '__main__':
    #cr = CameraRemote()
    #cr.take_photo()

    if(len(sys.argv) <2):
        print ("Usage: send_string <string to send")
        exit()        

    print ("Setting up Bluetooth kb emulator client")

    skc = SendKeycode()

    string_to_send = sys.argv[1]

    print ("Sending " + string_to_send)

    skc.popinSendKey(string_to_send)

    print ("Done " + string_to_send)
