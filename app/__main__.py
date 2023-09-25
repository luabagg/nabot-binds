import random, string
from pynput import keyboard
from configobj import ConfigObj

print("Hello! Executing Keybinds...")

cfg = ConfigObj('keybinds.cfg')

def random_alphanumeric(length):
    return ''.join(
        random.choice(
            string.ascii_lowercase + string.digits
        ) for _ in range(int(length)))

def random_number(length):
    return ''.join(
        random.choice(
            string.digits
        ) for _ in range(int(length)))

def on_activate(chars):
    kb = keyboard.Controller()
    kb.type(chars)

def execute_hotkeys(k, alphanumeric, number):
    alphanumeric(l.canonical(k))
    number(l.canonical(k))

def for_canonical(alphanumeric, number):
    return lambda k: execute_hotkeys(k, alphanumeric, number)

print("Alphanumeric HotKey:", cfg["alphanumeric_bind"], "Chars:", cfg["alphanumeric_qty"])
alphanumeric = keyboard.HotKey(
    keyboard.HotKey.parse(cfg["alphanumeric_bind"]),
    lambda: on_activate(
        random_alphanumeric(cfg["alphanumeric_qty"])
    )
)

print("Numeric HotKey:", cfg["numeric_bind"], "Chars:", cfg["numeric_qty"])
number = keyboard.HotKey(
    keyboard.HotKey.parse(cfg["numeric_bind"]),
    lambda: on_activate(
        random_number(cfg["numeric_qty"])
    )
)

with keyboard.Listener(
    on_press=for_canonical(alphanumeric.press, number.press),
    on_release=for_canonical(alphanumeric.release, number.release)
) as l: l.join()