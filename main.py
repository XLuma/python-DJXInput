import os
import sys
#import vgamepad
import mido
from mido import backends
import rtmidi

def process_midi(mido.Message msg):
    if (msg.type != 'clock'): # Need to maybe make a resource json to map notes to buttons
            if (msg.note == 56 and msg.velocity != 0): #up
                gamepad.press_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
            if (msg.note == 56 and msg.velocity == 0):
                gamepad.release_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
            if (msg.note == 57 and msg.velocity != 0):
                gamepad.press_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
            if (msg.note == 57 and msg.velocity == 0):
                gamepad.release_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
            if (msg.note == 40 and msg.velocity != 0):
                gamepad.press_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_A)
            if (msg.note == 40 and msg.velocity == 0):
                gamepad.release_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_A)
            if (msg.note == 41 and msg.velocity != 0):
                gamepad.press_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_B)
            if (msg.note == 41 and msg.velocity == 0):
                gamepad.release_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_B)
            gamepad.update()
            print(msg)

def input_main():
    #gamepad = vgamepad.VX360Gamepad()
    mido.set_backend('mido.backends.rtmidi')
    print(mido.get_input_names())
    inport = mido.open_input(mido.get_input_names()[0])
    #gamepad.press_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_A)
    #gamepad.update()
    while(1):
        msg = inport.receive()
        if (msg.type != 'clock'): #use process midi
            print(msg)
        

if __name__ == "__main__":
    input_main()

#need to study the code above cuz it comes from an example. goal is to get it to interface with the ddj sb3
#this looks like a good solution with mido... https://stackoverflow.com/questions/60182510/mido-how-to-get-midi-data-in-realtime-from-different-ports

#So the way shit works is that we receive Message stuff (https://mido.readthedocs.io/en/latest/message_types.html) and in it,different attributes. The ones we only
# care about are note_on events, and we only need to pay attention to: the note (tells which thing has been pressed, at least for our novation launchkey, might be different on the ddj-sb3)
# and the velocity to tell if a key is released or not. This complicates a little bit for dj controllers because we have jogwheels lmao, but we will figure this out.
#thers also control values, which go from 0 to 127, so with some maths for thresholds, we have.. item selectors and whatnots
# the velocity is great for detecting pads, which should be the buttons of a controller. if we can simulate a button being held, we are gucci
#the vgamepad library actually may allow this directly due to how it updates stuff... might have to try it out, and play with timings when doing midi->xinput