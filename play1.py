import wx, wx.animate


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


class PlayPage(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "PlayGame", size=(600, 500))

    def home(self):
        panel = wx.Panel(self)
        image = wx.Image('ho.png', wx.BITMAP_TYPE_PNG)
        self.animateGIF(image)
        title = TransparentStaticText(panel, -1, '今天是许烟雨的生日，但她并没有多高兴。起床后想倒杯水喝，却不小心，“Pia!”打碎了杯子。母亲闻声赶来说：',
                                      style=wx.TRANSPARENT_WINDOW)
        title.SetFont(wx.Font(24, wx.DECORATIVE, wx.NORMAL, wx.NORMAL))
        title.SetForegroundColour('#fd4a0d')

    def animateGIF(self, image):
        if self.gif:
            self.gif.Stop()
            self.gif.Destory()

        gif = wx.animate.GIFAnimationCtrl(self, -1, image)
        gif.GetPlayer()
        gif.Play()

    # def OnEraseBack(self, event):
    #     dc = event.GetDC()
    #     if not dc:
    #         dc = wx.ClientDC(self)
    #         rect = self.GetUpdateRegion().GetBox()
    #         dc.SetClippingRect(rect)
    #     dc.Clear()
    #     bmp = wx.Bitmap("j.jpg")
    #     dc.DrawBitmap(bmp, 0, 0)


if __name__ == "__main__":
    app = wx.App(False)
    frame = PlayPage()
    frame.Show()
    app.MainLoop()
