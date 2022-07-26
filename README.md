# python-DJXInput
Program to MIDI ->XInput, written in python

# Why I made this
For fun. I couldn't find a program that allowed to map MIDI to a game controller, only MIDI to keyboard and mouse. Plus, the only (good) software to do that is Bome's midi translator, which is paid software (granted, has way more features than this program will ever get). But, I needed a way to map a game controller, not a keyboard and mouse. So DJXinput was made.


# Usage
Currently, this program only supports the DDJ-SB3. The reason being it is the reason I am building this program. But, eventually, creating configurations for\n
other controllers will be possible

To create a new map, see the json resources in the maps folder. Essentially, every json is labelled with the device name, and then you can build a dict similar to the ones there to associate keys, knobs, pads... to button


# setup
`pip install mido vgamepad rtmidi json`

`python main.py`

# DDJ-SB3 NOTES

Each deck is controlled individually via channel 0 (left ) and 1 (right). mixer section, only a few knobs are operated on channel 6, the rest is controlled via the respective side the knob is on. same for the channel faders, crossfader is channel 6.
Knobs calculations are weird. essentially, each knob sends two control values., both ranging from 0-127, and the second one increasing the 'fastest'. with some maths, we could just only take the first one and have thresholds and we okay

Jog wheels are weird... the documentation says 'Different count value from when previous operated' with two values if turned clockwise (65) or counter-clockwise(63), and sends a note_on with note:54 when the top is touched. What we can do maybe, is just.. use touch over side, because we know when its being pressed.
And we just set maximum value to the joystick because we dont have ANY way of having some kind of midi control actual value. all we have is if its clockwise or counterclockwise which is more than enough. paired with tempo faders, and some maths, it should be okay maybe

Hot cue mode is to be used on all 16 pads. other modes act as a CC event, and fucks with us. Otherwise we just have to label the channel and notes and its easy af

Play button is to be mapped to start buttom
Cue to select


