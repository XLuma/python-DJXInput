import vgamepad

buttons = {
    "DPAD_UP" : vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP,
    "DPAD_DOWN" : vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN,
    "DPAD_LEFT" : vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT,
    "DPAD_RIGHT" : vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT,
    "A" : vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_A,
    "B" : vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_B,
    "X" : vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_X,
    "Y" : vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_Y,
    "LS" : vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER,
    "RS" : vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER,
    "LTHUMB_CLICK" : vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB,
    "RTHUMB_CLICK" : vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB,
    #"LT" : vgamepad.VX360Gamepad.left_trigger(255),
    #"RT" : vgamepad.VX360Gamepad.right_trigger(255),
    # LT = vgamepad.VX360Gamepad.left_trigger(255)
    # RT = vgamepad.VX360Gamepad.right_trigger(255) 0 to disable
    # Left stick = vgamepad.VX360Gamepad.left_joystick_float()
    # Right stick = vgamepad.VX360Gamepad.right_joystick_float()
    "START" : vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_START,
    "SELECT" : vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_GUIDE
}