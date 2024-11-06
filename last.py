from time import sleep,time

nowgame="0"
# def printf(text):
#     for i in range(len(text)):
#         print(text[i],end='')
#         sleep(0.05)
#     print()

def breakgo():
    global nowgame
    bggame = nowgame
    if bggame == "1":
        plot1()
    elif bggame == "2":
        plot2()
    elif bggame == "3":
        plot3()
    elif bggame=="31":
        plotQ3A1()
    elif bggame=="32":
        plotQ3A2()
    elif bggame=="41":
        plotQ4A1()
    elif bggame=="51":
        plotQ5A1()
    elif bggame=="52":
        plotQ5A2()
    elif bggame=="61":
        plotQ6A1()
    elif bggame=="62":
        plotQ6A2()
    elif bggame=="52":
        plotQ5A2()
    elif bggame=="22":
        plotQ2A2()
    




    else:
        print("文字冒险")
def memst():
    with open("mesa.dll",'w',encoding='utf-8') as f:
        f.write('')
def write_mem():
    global nowgame
    with open("mesa.dll",'w',encoding='utf-8') as f:
        f.write(str(nowgame))
def read_mem():
    global nowgame
    me=''
    melist=[]
    with open("mesa.dll",'w+',encoding='utf-8') as f:
        me=f.readline()
        if me=='':
            return
        melist=me.split(' ')
        nowgame=melist[0]
def plot1():
    global nowgame
    write_mem()
    input("在提笔落笔间，[我]诞生了。(enter继续)")
    input("[我]所在的这个世界，虽是二维，但却也十分精彩。繁华都市，静谧乡村，也有自然风光，雪山、丛林，万物皆由字组成，可万物都很美妙。[我]生活在这世间，虽安宁但缺兴奋感，直到......(enter继续)")
    input("我]有天在文字广场时，见到了一个我未曾见过的字，[你]。那纤细的单人旁，简洁而动人的“尔”部使[我]情。[我]走上去，很快与[你]亲热起来。(enter继续)")
    input("[我]与[你]漫步于文字广场上，[我]如沐春风。一的小文字们讲着故事：“从前，仓颉为万字之神，他创造了们，一万的文字来到人间，供苍生使用； 而一万的文字则留了天上，供神明使用，而天上的这部分文字则过着比我们更快的生活。如果你们来世想留在天上，就要好好表现.....(enter继续)")
    input("[我]与[你]，听着这，相视一笑。(enter继续)")
    input("可不久后，[你]却说有事情要做，就离开了，[我]着[你]的背影消失在字海中。(enter继续)")
    input("幸好，[我]与[你]还相约了第二天还在文字广场面。这天夜里，[我]辗转难眠。(enter继续)")
    input("第二天，[我]按照约定的时间走向广场，可找来找去没找到[你]，偶然看见街角处贴着一告示，上面画着个十分似的字。(enter继续)")
    input("[我]心中一惊，走近一看，发现却真是[你]，继续下去。(enter继续)")
    input("'有一文字今于文字广场失踪，据目击者称，绑架该字的字为一种结构简单，表意单一的字，现该字已向本国北方逸。警方现已介入调查。'(enter继续)")
    input("[我]内心一惊，随之而来的也有悲伤。(enter继续)")
    input("[我]走到街边的告示牌边，撕下手中笔记本画了[你的书页，写了个寻字告示贴在路边，因为[我]外形特别，不会引来了许多字。一个[16]问为何[我]长这个样子以及墙上的是什么。(enter继续)")
    input("[我]立刻解释自己是从文字城来的，[我]的朋友似被你们这里的某个字给带到了这里来，但我并不知道，也[你]也不愿意。[16]立即明白，建议[我]去报警。(enter续)")
    input("[我]于是沿着路标，向着警局走去。[我]环望四周看见这里大小街道都有十分发达的科技，单轨列车在空中行驶街上车水马龙。想到[你]即使来了这地方也会过得很好吧(enter继续)")
    while(1):
        ans=input("1.四处询问周围的文字(输入数字)")
        if(ans=='save'):
            write_mem()
        if(ans=="1"):
            nowgame=2
            plot2()
        else:
            print("")
def plot2():
    global nowgame
    write_mem()
    input("[我]截住一个[的]，却没有问出什么。后来又截住了个[甚]，知道了这群匪徒向郊区去了，我赶快记下来。")
    input("[我]赶快叫了辆车，来到本市的郊外。发现路上有一道道的车轮印，[我]继续跟着走。")
    input("[我]走过这片郊区，走入了一个树林。[我]继续随车轮印走着。过了树林，又走过草原，已过去一个星期。")
    input("在[我]将要放弃时，[我]走到了一个城市，可与[我]住的地方不大一样，这里的居民就如别的字描述的一样简单，有些单个出行，有些结伴出行，[我]拿出本子画下了他们的样子： 1 2 3 4......")
    input("于是[我]到了警局，向其报案后，剩下的也只有等待了。")

    while(1):
        ans=input("1.向这座城市郊区走\n2.在市中心转悠")
        if(ans=='save'):
            write_mem()
        if(ans=="1"):
            nowgame=3
            plot3()
        elif(ans=="2"):
            nowgame=22
            plotQ2A2()
        else:
            print("输入失败，请重新输入")
def plot3():
    global nowgame

    write_mem()
    input("[我]渐渐往这城市的郊区走去，此时太阳已渐渐归西。起初路上还有几个字，后来便渐渐没有几个了，最后便无字了，出了城就只剩下原野。忽然，[我]在泥地上似乎又发现了与路上一样的车轮印。[我]又激动起来。")

    while(1):
        ans=input("1.快速地追寻车轮印2.回警局报警寻求援助")
        if(ans=='save'):
            write_mem()
        if(ans=="1"):
            nowgame=31
            plotQ3A1()
        elif(ans=="2"):
            nowgame=32
            plotQ3A2()
        else:
            print("输入失败，请重新输入")
def plotQ3A1():
    global nowgame
    write_mem()
    input("[我]追寻着车轮印迹，一直走了很远，最终到了一座看样子废弃很久的城堡外，这城堡令人感到阴森与恐惧，[我]现在唯一的防身工具只有一把水果刀。")

    while(1):
        ans=input("1.直接拿着刀进入城堡2.回警局报警寻求援助")
        if(ans=='save'):
            write_mem()
        if(ans=="1"):
            nowgame=41
            plotQ4A1()
        elif(ans=="2"):
            nowgame=32
            plotQ3A2()
def plotQ4A1():
    global nowgame
    write_mem()
    input("[我]进入这阴森的古堡，它并没有门，可以直接进入，里面十分黑暗，只有古旧的煤油灯闪烁着微光，这时，[我]我发现了个楼梯。")

    while(1):
        ans=input("1.在一楼继续探索2.上楼")
        if(ans=='save'):
            write_mem()
        if(ans=="1"):
            nowgame=51
            plotQ5A1()
        elif(ans=="2"):
            nowgame=52
            plotQ5A2()
        

def plotQ5A1():
    global nowgame
    write_mem()
    input("[我]在一楼继续探索着，发现一张发黄的画着两个凶神恶煞的字的画像，大概是这个样子：4，13。这令我毛骨悚然，又看见地上有张便条，上面写到：“该字已到。”忽然，楼梯上传来脚步声。")

    while(1):
        ans=input("1.躲在一楼？2.逃出城堡")
        if(ans=='save'):
            write_mem()
        if(ans=="1"):
            nowgame=61
            plotQ6A1()
        elif(ans=="2"):
            nowgame=62
            plotQ6A2()

def plotQ6A1():
    global nowgame
    write_mem()
    input("[我]躲在了一楼，那个[4]下来，左右看了一圈，并未发现什么，可这时，[我]碰到了个瓶子，发出了一些声音，[4]我发现了[我]。[4]向[我]攻击。")
    input("10秒后连按10下enter即可战斗成功")
    for i in range(0,10):
        print(10-i)
        sleep(1)
    start=time()
    input(10)
    input(9)
    input(8)
    input(7)
    input(6)
    input(5)
    input(4)
    input(3)
    input(2)
    input(1)
    end=time()
    if(end-start>10):
        print("[我]输了")
        nowgame=52
        plotQ5A2()
    else:
        print("[我]赢了")
        nowgame=51
        plotQ5A2()
def plotQ5A2():
    global nowgame
    write_mem()
    input("[我]上楼，看见一扇上锁的铁门，门中不断传来讲话声")
    Q7()

def plotQ6A2():
    global nowgame
    write_mem()
    input("即使[我]的脚步声很大，但也未被发现，[我]见那[4]下了楼，看了一圈后又上去了")
    plotQ5A2()

def plotQ3A2():
    global nowgame
    write_mem()
    input("警方与[我]顺着[我]所描述的车轮印一路前行，最终到达了一座阴森的古堡。[我]由于有警方的陪同，便无比激动与勇敢。可警方只让[我]待在车里，他们派特警部队进入。\n城堡中响起脚步声与枪声。")
    nowgame=1
    END()
def plotQ2A2():
    global nowgame
    write_mem()
    input("[我]在市中心左看右看，过了约两三小时，警方便说调查有了进展。\n[我]赶紧前往警局，与警方交流，后警方称在本市郊区找到了线索。")
    nowgame=32
    plotQ3A2()
def Q7():
    global nowgame
    write_mem()
    while(1):
        ans=input("1.直接开门2.报警叫支援并继续偷听3.偷听但不报警")
        if(ans=='save'):
            write_mem()
        if(ans=="1"):
            nowgame=2
            print("[我]用力撞开了门，挥舞着刀进去，奈何里面字实在太多，寡不敌众，被捉住了.......（Game over）")
            plot2()
        elif(ans=="2"):
            print("[我]报警后，继续偷听，后听到了关于[你]的消息，半小时后警察来到，解决了[4]与[13]。")
            nowgame=1
            END()
        elif(ans=="3"):
            Q8()
        else:
            print("输入失败，请重新输入")

def Q8():
    global nowgame
    write_mem()
    input("[我]在门后偷听，但没有报警，后又发现可以进入该房间的一扇后门。")
    input("[我]在小门偷袭了[4]与[13]，在他们还未察觉时，就将两字绑起，也救出了被他们关押的[你]，[我]带着他们回了数字城。居民们得知[我]独身一人就捉住两大通缉犯，对[我]心生敬佩之心。[我]后来才得知[你]是文字城的重要字，绑架她可用于勒索大量赎金，才理解了[4]与[13]绑架她的用意。")
    nowgame=1
    END()
def END():
    global nowgame
    nowgame=1
    write_mem()
    print("[我]心心念念的[你]被救出，笑着向[我]与警方道谢。此时[我]也向你道明了心意。可[你]只是对[我]笑笑，与[我]一起回了文字城。\n后来才知，[我]与[你]永远无法结为一对，因为[我]与[你]无法组词，因此无法并行。[我]为这个而伤心了很多天，但回想起那段回忆故事，心中又多了份慰藉。")
    ans=input("END!(save推出  again重新开始)")
    while(1):
        if(ans=='save'):
            memst()
            quit()
        elif(ans=="again"):
            plot2()
        else:
            print("输入失败，请重新输入")



def init():
    ans=input("初始化完成")
    if(ans=="init"):
        memst()
        main()
    breakgo()
    plot1()
def main():
    read_mem()
    init()
try:
    main()
except:
    pass
