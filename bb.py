import winreg as reg
import os
import ctypes

def disable_polish_keyboard():
    # Disable Polish keyboard layout
    key = reg.OpenKey(reg.HKEY_CURRENT_USER, r"Keyboard Layout\Preload", 0, reg.KEY_SET_VALUE)
    reg.SetValueEx(key, "1", 0, reg.REG_SZ, "00000415")  # Set to Polish layout
    reg.CloseKey(key)

def add_to_startup():
    # Add script to startup
    file_path = os.path.join(os.getenv("APPDATA"), "Microsoft\\Windows\\Start Menu\\Programs\\Startup", "disable_polish_keyboard.py")
    with open(file_path, "w") as f:
        f.write('''import winreg as reg
import os

def disable_polish_keyboard():
    key = reg.OpenKey(reg.HKEY_CURRENT_USER, r"Keyboard Layout\\Preload", 0, reg.KEY_SET_VALUE)
    reg.SetValueEx(key, "1", 0, reg.REG_SZ, "00000415")
    reg.CloseKey(key)

disable_polish_keyboard()
''')

if __name__ == "__main__":
    disable_polish_keyboard()
    add_to_startup()
