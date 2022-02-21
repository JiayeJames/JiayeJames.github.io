import win32gui
import win32con
import win32clipboard as w
import time
 
msg = "python D:\Others\PythonPrograms\autosending.py"
name = ["jy", "猪猪", "黎真呈",'杨佳怡','我的安卓手机']
for i in name:
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, msg)
    w.CloseClipboard()
    handle = win32gui.FindWindow(None, i)
    #while 1==1:
    if 1 == 1:
        win32gui.SendMessage(handle, 770, 0, 0)
        win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
        win32gui.SendMessage(handle, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
        time.sleep(1)