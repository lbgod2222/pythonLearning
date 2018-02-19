import wx
import time
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'Title',size=(350,600))
        panel = wx.Panel(self)
        # UPPER
        labelAll = wx.StaticText(panel,-1,'Panel',pos=(20,0))
        self.textAll = wx.TextCtrl(panel,
            -1,
            size=(330,180),
            pos=(0,50),
            style=wx.TE_MULTILINE | wx.TE_READONLY,)
        # BOTTOM
        labelMine = wx.StaticText(panel,-1,'Panel',pos=(20,240))
        self.textIn = wx.TextCtrl(panel,
            -1,
            size=(330,180),
            pos=(0,260),
            style=wx.TE_MULTILINE)

        self.btnSend = wx.Button(panel,-1,'Sent',size=(75,25),pos=(150,500))
        self.btnClear = wx.Button(panel,-1,'Clear',size=(75,25),pos=(260,500))
        self.Bind(wx.EVT_BUTTON,self.OnButtonSend,self.btnSend)
        self.Bind(wx.EVT_BUTTON,self.OnButtonClear,self.btnClear)

        # Grid in wx module
        btnSizer = wx.BoxSizer()
        btnSizer.Add(self.btnSend,proportion=0)
        btnSizer.Add(self.btnClear,proportion=0)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(labelAll,proportion=0,flag=wx.ALIGN_CENTER)
        mainSizer.Add(self.textAll,proportion=1,flag=wx.EXPAND)
        mainSizer.Add(labelMine,proportion=0,flag=wx.ALIGN_CENTER)
        mainSizer.Add(self.textIn,proportion=0,flag=wx.EXPAND)
        mainSizer.Add(btnSizer,proportion=0,flag=wx.ALIGN_CENTER)

        panel.SetSizer(mainSizer)

        # define the button funcs
        def OnButtonSend(self,event):
            userInput = self.textIn.GetValue() #get input value
            self.textIn.Clear()
            mow - time.ctime()
            inmsg = 'You (%s): \n%s \n' % (now,userInput)
            self.textAll.AppendText(userInput)
            # self.textAll.SetValue(userInput)

        def OnButtonClear(self,event):
            pass

app = wx.App()
frame = MyFrame()
frame.Show()
app.MainLoop