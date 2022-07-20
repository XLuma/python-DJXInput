import mido
from constants import buttons
import json

class Midi_Map:
    #class to map midi notes to button. maybe need to create a note class and CC class ?   
    def __init__(self):
        self.profileName = ""
        self.map = {}

    def fill_object(self, inport : mido.ports.IOPort): #initializes a new profile
        self.profileName = input("Input a name for the profile\n")
        for button in buttons:
            print("Press a key to map button " + button)
            msg = inport.receive()
            while msg.type is 'clock':
                msg = inport.receive()
            if (msg.type != 'clock' and msg.velocity is not 0):
                self.map[button] = msg.note
            #TODO: Block velocity 0 events, and make it so it doesnt go to the next button
            #TODO: Add support for CC controls, with a deadzone value. might need to improve dict format

    def output_to_json(self): #Output midi map to a json file that can be modified and loaded back up
        json = json.dumps(self)
        file = open(self.profileName + ".json", "w")
        file.write(json)
        file.close()