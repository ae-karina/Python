import wx


class TransparentStaticText(wx.StaticText):
    """
    重写StaticText控件
    """

    def __init__(self, parent, id=wx.ID_ANY, label='', pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.TRANSPARENT_WINDOW, name='TransparentStaticText'):
        wx.StaticText.__init__(self, parent, id, label, pos, size, style, name)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_ERASE_BACKGROUND, lambda event: None)
        self.Bind(wx.EVT_SIZE, self.OnSize)

    def OnPaint(self, event):
        bdc = wx.PaintDC(self)
        dc = wx.GCDC(bdc)
        font_face = self.GetFont()
        font_color = self.GetForegroundColour()
        dc.SetFont(font_face)
        dc.SetTextForeground(font_color)
        dc.DrawText(self.GetLabel(), 0, 0)

    def OnSize(self, event):
        self.Refresh()
        event.Skip()


class SignPage(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Login", size=(400, 300))
        panel = wx.Panel(self)
        panel.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack)

        title = TransparentStaticText(panel, -1, 'Login Page', style=wx.TRANSPARENT_WINDOW)
        title.SetFont(wx.Font(24, wx.DECORATIVE, wx.NORMAL, wx.NORMAL))
        title.SetForegroundColour('#fd4a0d')

        labelUser = TransparentStaticText(panel, -1, 'User', style=wx.TRANSPARENT_WINDOW)
        labelUser.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL))

        userText = wx.TextCtrl(panel, -1, size=(175, -1))

        labelPwd = TransparentStaticText(panel, -1, 'Password')
        labelPwd.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL))

        pwdText = wx.TextCtrl(panel, -1, size=(175, -1), style=wx.TE_PASSWORD)

        ###SignButton###
        SignButton = wx.Button(panel, -1, "Sign", size=(75, 25))
        SignButton.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL))
        SignButton.SetBackgroundColour("#c9f3f2")
        SignButton.Bind(wx.EVT_BUTTON, self.OnButtonSign, SignButton)

        ###RegButton###
        RegButton = wx.Button(panel, -1, "Register", size=(75, 25))
        RegButton.Bind(wx.EVT_BUTTON, self.OnButtonReg, RegButton)
        RegButton.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL))
        RegButton.SetBackgroundColour("#c9f3f2")

        ###Sizer###
        myStyle = wx.EXPAND | wx.ALL
        titSizer = wx.BoxSizer()
        titSizer.Add(title, flag=myStyle, border=10)

        lab1Sizer = wx.BoxSizer(wx.VERTICAL)
        lab1Sizer.Add(labelUser, flag=myStyle, border=15)
        lab1Sizer.Add(labelPwd, flag=myStyle, border=15)

        lab2Sizer = wx.BoxSizer(wx.VERTICAL)
        lab2Sizer.Add(userText, flag=myStyle, border=10)
        lab2Sizer.Add(pwdText, flag=myStyle, border=10)

        sumSizer = wx.BoxSizer()
        sumSizer.Add(lab1Sizer, myStyle, border=10)
        sumSizer.Add(lab2Sizer, myStyle, border=10)

        btnSizer = wx.BoxSizer()
        btnSizer.Add(SignButton, flag=myStyle, border=10)
        btnSizer.Add(RegButton, flag=myStyle, border=10)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(titSizer, flag=wx.CENTER)
        mainSizer.Add(sumSizer, flag=myStyle, border=10)
        mainSizer.Add(btnSizer, flag=wx.CENTER)

        panel.SetSizer(mainSizer)

    def OnButtonSign(self, event):
        pass

    def OnButtonReg(self, event):
        pass

    def OnEraseBack(self, event):
        dc = event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("j.jpg")
        dc.DrawBitmap(bmp, 0, 0)


app = wx.App(False)
frame = SignPage()
frame.Show()
app.MainLoop()
