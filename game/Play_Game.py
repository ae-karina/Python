import wx



class play(wx.Frame):

        def __init__(self):
            wx.Frame.__init__(self, None, -1, "PlayGame", size=(600, 500))

        def total(self):
            print('*****治愈者*****')
            print('剧情简介：\n有这样一位患抑郁症，许烟雨，是一名服装设计师。身边人的一言一行都会对她造成一定程度的影响，甚至导致她的死亡。她的情绪也在潜移默化地影响着身边的人。\n'
                  '你打算如何与她相处呢？希望在你的帮助下，能引导她摆脱病魔的折磨，看到充满希望的美好生活！\n注意：当许烟雨的心情值低于40就会自杀。\n许烟雨的心情值是：60')
            print('1.开始治愈  2.放弃她')
            a = int(input('请慎重选择：'))
            mo = 60
            if a == 1:
                m = hang_out(at_company(at_home(mo)))
                return m
            elif a == 2:
                print('你放弃了她，身边人一次又一次的语言伤害让她痛苦万分。某一天清晨，她从顶楼跳了下去......')
                m = 0
                return m

        def at_home(self):
            panel = wx.Panel(self)
            panel.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack("ho.png"))
            print('今天是许烟雨的生日，但她并没有多高兴。起床后想倒杯水喝，却不小心，“Pia!”打碎了杯子。母亲闻声赶来说：')
            print('1.“怎么了？！呀！没伤到吧？‘碎碎’平安，‘碎碎’平安啊。  2.咋了？哎呀，笨手笨脚的，快收拾。”')
            b = int(input('请选择：'))
            if b == 1:
                print('许烟雨心想：哎，下次小心点吧，不能总让妈妈担心...')
                return self
            elif b == 2:
                print('许烟雨心想：自己怎么什么都做不好，活着一点价值都看不到')
                self -= 10
                print("现在许烟雨的心情值是", self)
                return self


        def OnEraseBack(self, event, image):
            dc = event.GetDC()
            if not dc:
                dc = wx.ClientDC(self)
                rect = self.GetUpdateRegion().GetBox()
                dc.SetClippingRect(rect)
            dc.Clear()
            bmp = wx.Bitmap(image)
            dc.DrawBitmap(bmp, 0, 0)





        def at_company(self):
            panel = wx.Panel(self)
            panel.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack("ho.png"))
            print('许烟雨打开手机，发现微信静悄悄的，没有任何祝福消息。\n'
                  '来到公司，许烟雨发现上级抄袭她未发表的作品，并在会议上公开，她气愤难过，想私下询问清楚，却被同同事拦下\n'
                  '同事说：\n1.“别去，你没有证据证明她抄袭，她官大一级，大家会更信任她，你要找证据证明作品是你的”\n'
                  '2.（想到许烟雨总被领导夸赞，自己没有出头之日）”呦，心情又不好了，能别整天装高冷抑郁吗？谁想看你这副脸色！“')
            c = int(input('请选择：'))
            if c == 1:
                print('在这位同事的帮助下，许烟雨找到了证据，她的上级被开除，她很欣慰。')
                m += 5
                print("现在许烟雨的心情值是", m)
                return m

            elif c == 2:
                print('许烟雨心情沉重，不被人理解的痛苦席卷全身，她离开了公司。')
                m -= 10
                print("现在许烟雨的心情值是", m)
                return m

    def hang_out(m):
        bei = []
        c = int(input('接下来来到了另一天，今天下午你和许烟雨约好了见面，出门前你看见门口放着的伞.\n这时候你想： 1.拿上雨伞 2.相信天气预报今天不会下雨'))
        print('你和她坐地铁，在地铁上有调皮的小孩踹脏了她的裙摆，她很不高兴')

        print('地铁到站，你和许烟雨正在一边讲话一边往地铁的出口处走，刚到门口就下起大暴雨\n 许烟雨联想刚刚被小孩踢了一脚，想出门又碰上了大雨，心情更沮丧了，说了一句：“生活真是太艰难了！')
        if c == 1:
            bei = ['背包']
            print('你看了看她失落的表情：“没关系啦！我刚好带了雨伞，你不要伤心，我来为你遮风挡雨。”接着你从背包里拿出了伞')
            bei.pop(0)
            print('许烟雨被朋友的话触动，心情好了很多')
            m += 5
            print("现在许烟雨的心情值是", m)
            print('game over')
            return m

        elif c == 2:
            print('你今天没有带伞')
            m -= 10
            if m < 40:
                print('许烟雨心情值过低，自杀了！')
            print("game over!")
            return m


