import win32com.client as win32

hwp = win32.gencache.EnsureDispatch('HWPFrame.HwpObject')
hwp.XHwpWindows.Item(0).Visible = True
hwp.Quit()