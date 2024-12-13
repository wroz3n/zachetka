import ctypes
import win32api
import win32con
import win32gui
import os

# Function to block keyboard layout switching
def block_keyboard_switch():
    # Set the keyboard layout to Russian and English
    os.system('powershell.exe Set-WinUserLanguageList -LanguageList "ru-RU","en-US" -Force')

    # Block the key combinations for switching layouts
    def low_level_keyboard_handler(nCode, wParam, lParam):
        if wParam == win32con.WM_KEYDOWN:
            vk_code = lParam[0]
            if vk_code in (0x15, 0x20):  # VK_OEM_102 and VK_SPACE
                return 1  # Block the key
        return ctypes.windll.user32.CallNextHookEx(None, nCode, wParam, lParam)

    # Set the hook
    hook = win32api.SetWindowsHookEx(win32con.WH_KEYBOARD_LL, low_level_keyboard_handler, None, 0)

    # Message loop
    msg = ctypes.wintypes.MSG()
    while ctypes.windll.user32.GetMessageA(ctypes.byref(msg), 0, 0, 0) != 0:
        ctypes.windll.user32.TranslateMessage(ctypes.byref(msg))
        ctypes.windll.user32.DispatchMessageA(ctypes.byref(msg))

# Run the function
if __name__ == "__main__":
    block_keyboard_switch()
