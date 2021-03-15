import gui1
import wx

class MyGui(gui1.MyFrame1):
    def __init__(self,parent):
        gui1.MyFrame1.__init__(self,parent)

app = wx.App()
frame = MyGui (parent=None)
frame.Show()
app.MainLoop()