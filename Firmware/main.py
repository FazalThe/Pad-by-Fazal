import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import Keys
from kmk.modules.encoder import EncoderHandler

# Initialize the keyboard
keyboard = KMKKeyboard()

# --- 1. SETUP PINS (Direct Wiring) ---

keyboard.matrix = Keys(
    pins=(
        board.GP26, board.GP27, board.GP28, # SW1, SW2, SW3
        board.GP29, board.GP6,  board.GP7,  # SW4, SW5, SW6
        board.GP0,  board.GP1,  board.GP2,  # SW7, SW8, SW9
    ),
    value_when_pressed=False,
    pull=True,
)

# --- 2. SETUP ENCODER ---
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

encoder_handler.pins = ((board.GP3, board.GP4, None, False),)

# --- 3. KEYMAP FOR DAVINCI RESOLVE ---

MOD = KC.LCTRL 

keyboard.keymap = [
    [
        # SW1 (Top Left)
        KC.SPACE,    # Play/Pause

        # SW2 (Middle Left)
        MOD(KC.B),   # Razor/Split (Ctrl+B)

        # SW3 (Bottom Left)
        KC.BSPC,     # Ripple Delete (Backspace)

        # SW4 (Top Middle)
        MOD(KC.EQUAL), # Zoom In

        # SW5 (Center)
        KC.LSFT(KC.Z), # Fit to Window (Shift+Z)

        # SW6 (Bottom Middle)
        MOD(KC.MINUS), # Zoom Out

        # SW7 (Top Right)
        MOD(KC.Z),     # Undo

        # SW8 (Middle Right)
        MOD(KC.LSFT(KC.Z)), # Redo (Ctrl+Shift+Z)

        # SW9 (Bottom Right)
        KC.A,          # Selection Mode (A)
    ]
]

# --- 4. ENCODER MAP ---
encoder_handler.map = [
    ((KC.LEFT, KC.RIGHT, None),),
]

if __name__ == '__main__':
    keyboard.go()