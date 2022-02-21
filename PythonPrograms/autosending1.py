import win32gui
import win32con
import win32clipboard as w
import time
 
#发送的消息
msg = "测试代码"
#窗口名字
name = "jy"
for i in range(1,20):
    #将测试消息复制到剪切板中
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, msg)
    w.CloseClipboard()
    #获取窗口句柄
    handle = win32gui.FindWindow(None, name)
    if handle == 0:
        print('未找到窗口！')
    #while 1==1:
    if 1 == 1:
        #填充消息
        win32gui.SendMessage(handle, 770, 0, 0)
        #回车发送消息
        win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
        time.sleep(1)#延缓进程