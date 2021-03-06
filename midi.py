import mido
from constants import buttons
import json
import jsonpickle

class Midi_Map: #class to map midi notes to button. maybe need to create a note class and CC class ?   

    def __init__(self): # object init
        self.profileName = ""
        self.map = {}
 
    def fill_object(self, inport : mido.ports.IOPort): # initializes a new profile
        self.profileName = input("Input a name for the profile\n")
        for button in buttons:
            print("Press a key to map button " + button)
            msg = inport.receive()
            while msg.type == 'clock' or msg.velocity == 0:
                msg = inport.receive()
            if (msg.type != 'clock' and msg.velocity != 0):
                #self.map[button] = msg.note
                self.map[str(msg.note)] = dict()
                #join in a string event type, underscore note number or control event number
            #TODO: Add support for CC controls, with a deadzone value. might need to improve dict format
            #note : cc sends a control event with a unique value for each knobs. use that for detection of control change events

    def output_to_json(self): # Output midi map to a json file that can be modified and loaded back up
        jsons = json.dumps(self.map, indent=1)
        file = open("maps/" + self.profileName + ".json", "w")
        #file.write(jsons)
        file.write(jsonpickle.encode(self, indent=1))
        file.close()

    def load_profile(profileName: str): # Loads a profile with the given filename, and returns the object
        file = open(profileName)
        data = jsonpickle.decode(file.read())
        print(data.profileName)
        print(data.map)
        #return data
