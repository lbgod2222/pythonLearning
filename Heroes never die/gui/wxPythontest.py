import wx
# simple app use the OO design
app = wx.App()
frame = wx.Frame(parent = None)
frame.Show()
app.MainLoop()

# complex app use class method
class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent = None,
            title='Ben\'s scritp',
            size=(400,300),
            pos=(50,50))
        panel = wx.Panel(frame,-1)
        self.buttonDraw = wx.Button(panel,
            -1,
            'Pixal',
            size=(175,125),
            pos=(100,100))
        self.Bind(wx.EVT_BUTTON,self.OnButtonDraw,self.buttonDraw)
        frame.Show()
        return True
    def OnButtonDraw(self,event):
        for i in range(5):
            turtle.forward(150)
            turtle.right(144)
    
if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()