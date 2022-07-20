import os
import sys
import vgamepad
import mido
import json
from constants import buttons
import midi

def json_to_button(msg: mido.Message, map):
    return buttons[map['map'][str(msg.note)]]

def process_midi(msg: mido.Message, gamepad: vgamepad.VX360Gamepad, map: json = 0):
    try:
        if (msg.type != 'clock'): #doesnt do control_change type stuff, gotta handle that eventually, also error handling for keys that arent defined.. maybe also look into changing rgb colors for pads
            if (msg.velocity != 0):
                gamepad.press_button(json_to_button(msg, map))
            elif (msg.velocity == 0):
                gamepad.release_button(json_to_button(msg, map))
            gamepad.update()
            print(msg, json_to_button(msg, map))
    except:
        pass

def input_main():
    gamepad = vgamepad.VX360Gamepad()
    mido.set_backend('mido.backends.rtmidi')
    print(mido.get_input_names())
    
    inport = mido.open_input(mido.get_input_names()[int(input('Select your midi device\n')) - 1]) # -1 cause idk i expect people to count from 1 rather than 0
    gamepad.press_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_A) # wake the controller up
    gamepad.update()
    file = open('maps/novation_launchkey_mini_mk3.json', 'rb') # need a way to get device name to map more easily
    map = json.loads(file.read())
    while(1):
        msg = inport.receive()
        if (msg.type != 'clock'): #midi devices contantly send clock events. ignore those
            process_midi(msg, gamepad, map)
            #print(msg)
        
def test_map():
    midi_map = midi.Midi_Map()
    inport = mido.open_input(mido.get_input_names()[int(input('Select your midi device\n')) - 1])
    midi_map.fill_object(inport)
    inport.close()
    midi_map.output_to_json()

if __name__ == "__main__":
    test_map()

#need to study the code above cuz it comes from an example. goal is to get it to interface with the ddj sb3
#this looks like a good solution with mido... https://stackoverflow.com/questions/60182510/mido-how-to-get-midi-data-in-realtime-from-different-ports

#So the way shit works is that we receive Message stuff (https://mido.readthedocs.io/en/latest/message_types.html) and in it,different attributes. The ones we only
# care about are note_on events, and we only need to pay attention to: the note (tells which thing has been pressed, at least for our novation launchkey, might be different on the ddj-sb3)
# and the velocity to tell if a key is released or not. This complicates a little bit for dj controllers because we have jogwheels lmao, but we will figure this out.
#thers also control values, which go from 0 to 127, so with some maths for thresholds, we have.. item selectors and whatnots
# the velocity is great for detecting pads, which should be the buttons of a controller. if we can simulate a button being held, we are gucci
#the vgamepad library actually may allow this directly due to how it updates stuff... might have to try it out, and play with timings when doing midi->xinput