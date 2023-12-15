# coding=utf-8

import wx
import Sign_Page


def main():
    app = wx.App(False)
    frame = Sign_Page.SignPage()
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
