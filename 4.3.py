ms = 60

print('*****治愈者*****')
print('剧情简介：\n有这样一位患抑郁症，许烟雨，是一名服装设计师。身边人的一言一行都会对她造成一定程度的影响，甚至导致她的死亡。她的情绪也在潜移默化地影响着身边的人。\n'
      '你打算如何与她相处呢？希望在你的帮助下，能引导她摆脱病魔的折磨，看到充满希望的美好生活！')
print('1.开始治愈  2.放弃她')
a = int(input('请慎重选择：'))
if a == 1:
    print('今天是许烟雨的生日，她怀着些许期待起床，但家中的父母似乎完全忘记了这回事，还责怪她起得晚，没做早饭')
    b = int(input('在早晨，你选择：\n1.最近总熬夜工作，忘了她生日，睡觉ing \n2.你记得她的生日，并打电话亲口说了生日快乐，还约下班后一起庆祝\n'))
    if b == 1:
        print('许烟雨很难过，自己工作如此忙还要承受父母亲的责骂，打开手机，发现微信静悄悄的，没有任何祝福消息。\n'
              '来到公司，许烟雨发现上级抄袭她未发表的作品，并在会议上公开，她气愤难过，想私下询问清楚，却被同同事拦下\n'
              '同事说：\n1.“别去，你没有证据证明她抄袭，她官大一级，大家会更信任她，你要找证据证明作品是你的”\n'
              '2.（想到许烟雨总被领导夸赞，自己没有出头之日）”呦，心情又不好了，能别整天装高冷抑郁吗？谁想看你这副脸色！“')
        c = int(input('请选择：'))
        if c == 1:
            print('在这位同事的帮助下，许烟雨找到了证据，你的上级被开除，你很欣慰。')
            ms += 5
            print("现在许烟雨的心情值是", ms)
        elif c == 2:
            print('许烟雨心情沉重，不被人理解的痛苦席卷全身，她离开了公司。')
            ms -= 10
            print("现在许烟雨的心情值是", ms)
            if ms < 60:
                print('许烟雨心情值过低，自杀了！')
    elif b == 2:
        print('许烟雨虽然很难过父母的不理解，但听到朋友热情的祝福与关心，心情又稍好了些。')
        ms += 5
        print("现在许烟雨的心情值是", ms)
elif a == 2:
    print('你放弃了她，身边人一次又一次的语言伤害让她痛苦万分。某一天清晨，她从顶楼跳了下去。')

bei = []
c = int(input('接下来来到了另一天，今天下午你和许烟雨约好了见面，出门前你看见门口放着的伞.\n这时候你想： 1.拿上雨伞 2.相信天气预报今天不会下雨'))

print('你和她坐地铁，在地铁上有调皮的小孩踹脏了她的裙摆，她很不高兴')
ms -= 10

print('地铁到站，你和许烟雨正在一边讲话一边往地铁的出口处走，刚到门口就下起大暴雨\n 许烟雨联想刚刚被小孩踢了一脚，想出门又碰上了大雨，心情更沮丧了，说了一句：“生活真是太艰难了！')

if c == 1:
    bei = ['背包']
    print('你看了看她失落的表情：“没关系啦！我刚好带了雨伞，你不要伤心，我来为你遮风挡雨。”接着你从背包里拿出了伞')
    bei.pop(0)
    print(bei)
    print('许烟雨被朋友的话触动，心情好了很多')
    ms += 5
    print("现在许烟雨的心情值是", ms)

else:
    try:
        bei.pop(0)
    except:
        print('你今天没有带伞')