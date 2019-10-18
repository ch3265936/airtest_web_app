# -*- encoding=utf8 -*-
__author__ = "tianyabin"

__desc__ = '''
            1、接口说明-QM平台UI自动化用例
            '''

from airtest.core.api import *
from airtest.core.android.adb import *
# auto_setup(__file__)

from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()
from poco.exceptions import PocoNoSuchNodeException
from poco.exceptions import PocoTargetTimeout
#
# using("DHM_common.air")
# from DHM_common import *
app_id = "com.dreamhomematch.casual.free"
# adb = ADB()
# devicesList = adb.devices()
# adb_device = devicesList[0][0]
# cmd = "adb -s " + str(adb_device) + " shell wm size"
# proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
# read = str(proc.stdout.read()).split()[2].split("\\")[0].split("x")
# sx = float(read[1]) #Hight
# sy = float(read[0]) #wight
#手机显示屏幕sx=Hight，wight

dev = device()
sy = dev.display_info['width']
sx = dev.display_info['height']

# 点击类型为Texture按钮并等待UI跟新
def click_TextureUi(arg):
    ui = poco(texture=arg)
    try:
        ui.invalidate()
        ui.wait_for_appearance(timeout=10)
        ui.click()
        text('succee click--' + str(arg))
    except PocoTargetTimeout as to:
        print('PocoTargetTimeout',to)
        sleep(1)
    except PocoNoSuchNodeException as ns:
        print('PocoNoSuchNodeException',ns)
        sleep(1)
        
# 点击类型为Text按钮并等待UI跟新
def click_TextUi(arg):
    ui = poco(text=arg)
    try:
        ui.invalidate()
        ui.wait_for_appearance(timeout=10)
        ui.click()
        text('succee click--' + str(arg))
    except PocoTargetTimeout as to:
        print('PocoTargetTimeout',to)
        sleep(1)
    except PocoNoSuchNodeException as ns:
        print('PocoNoSuchNodeException',ns)
        sleep(1)

# 点击类型为name按钮并等待UI跟新
def click_Name(arg):
    ui = poco(name=arg)
    try:
        ui.invalidate()
        ui.wait_for_appearance(timeout=10)
        ui.click()
        text('succee click--' + str(arg))
    except PocoTargetTimeout as to:
        print('PocoTargetTimeout',to)
        sleep(1)
    except PocoNoSuchNodeException as ns:
        print('PocoNoSuchNodeException',ns)
        sleep(1)

#################常用通关#######################
#常用控件名
#开始战斗（texture）
start_play="btn_startlevel"
#开始战斗-确定按钮(name)
start_confirm="ButtonStart"

#弹框关闭按钮(小锤子，手套）
close_button="CloseButton"
#每日签到确定按钮
claim_button="ClaimButton"
#关卡界面控件
level=poco("LevelInspector").child("AnchorLeftCenter").child(name="LevelText")
#战斗成功
success_name1="Congratulations"
success_name2="Spine GameObject (tap to continue)"
#新手引导奖励任务
itemReward="PanelItemReward"

#剧情对话
#3.3
char_text="BlackLineDown"
char_skip="BtnSkip"

#循环对话
def click_talk(arg):
    sleep(0.5)
    if poco(name=char_skip).exists():
        for n in range(arg):
            click_Name(char_text)
            sleep(0.5)
    else:
        text('当前不处于对话界面')
        raise Exception("Current page is not talk")
        sleep(1)

#跳过剧情对话
def click_talk_stip(arg):
    sleep(1)
    if poco(name=char_skip).exists():
        for n in range(arg):
            click_Name(char_skip)
            sleep(10)
    else:
        text('当前不处于对话界面')
        raise Exception("Current page is not talk")
        sleep(1)

#开始挑战
def click_start():
    click_TextureUi(start_play)
    sleep(2)
    click_Name(start_confirm)
    sleep(10)

#判断当前界面是否位于主界面
def exists_main():
    #判断是否上一关卡未通关结束
    if level.exists():
        gm_pass()
    # 循环检测4次
    for per in range(4):
        if poco(name="BtnSkip").exists():
            click_Name("BtnSkip")
            sleep(20)
         # 关闭每日签到奖励对话框
        if poco(name=claim_button):
            click_Name(claim_button)
         # 关闭弹出来的对话框
        elif poco(name=close_button):
            click_Name(close_button)
        # 如果只存在ok对话，关闭对话框
        elif poco("ButtonOk"):
             click_Name("ButtonOk")
        # 如果上一关未结束，关闭对话框
        elif poco(name=success_name1):
            click_Name(success_name1)
            sleep(5)
        #如果有新手引导礼物，关闭对话框
        elif poco(name=itemReward):
            click_Name("OKButtonText")
            sleep(5)
        #关闭活动奖励对话框
        elif poco(name="PanelMainLineActivity"):
            click_Name("ToLevelButton")
            sleep(5)
        # 关闭每日签到奖励对话框
        elif poco(name="PanelDailyReward"):
            click_Name("ClaimButton")
            sleep(5)
        else:
            text('当前界面无任何弹框')
            break
    #再次检测是否在主界面
    exists_play()
        
def exists_play():
    #判断是否有开始控件，如果有说明在主界面。
    #if poco(texture=start_play):
    if exists(Template(r"tpl1564024885079.png", record_pos=(-0.439, 0.21), resolution=(1920, 1080))):

        text('当前处于主界面')
    else:
        raise Exception("current page is not main")
        sleep(1)

#判断当前进入关卡界面
def exists_level():
    #进入游戏界面判定
    sleep(1)
    for per in range(10):
        if level.exists():
            text("当前处于关卡挑战界面")
            break
        else:
            raise Exception("current page is not remove")
            sleep(5)
            text("当前未处于关卡挑战界面")
    sleep(5)
    
#新手指引动画
def guide(arg):
    sleep(2)
    for n in range(arg):
        if poco(name="ButtonOk"):
            click_Name("ButtonOk")
        elif poco(texture="comic_base"):
            click_TextureUi("comic_base")
        elif poco(texture="BtnSkip"):
            click_TextureUi("BtnSkip")
        else:
            sleep(2)
    sleep(3)
def renwu():
    #click_Name("Renwu")
    poco("Main(Clone)").child("LeftBar").child("Renwu").click()
    sleep(1)
    if exists(Template(r"tpl1563872365821.png", record_pos=(-0.154, 0.226), resolution=(1920, 1080))):
        click_Name("ConsumeStarCount")
    else:
        try:
            poco("Main(Clone)").child("PanelDayOverBonus2").wait_for_appearance(10)
            get_DayOverBonus()
        except:
            pass
        click_Name("ConsumeStarCount")
def taskDay():
    #click_Name("Renwu")
    poco("Main(Clone)").child("LeftBar").child("Renwu").click()
    sleep(1)
    if exists(Template(r"tpl1563872365821.png", record_pos=(-0.154, 0.226), resolution=(1920, 1080))):
        click_Name("ConsumeStarCount")
        sleep(1)         
    else:
        try:
            poco("Main(Clone)").child("PanelDayOverBonus2").wait_for_appearance(10)
            get_DayOverBonus()
        except:
            pass
        click_Name("ConsumeStarCount")
#进入关卡
def common_start():
    try:
        exists_main()
        click_start()
        exists_level()
    except:
        clear_touch(0.9,0.9,1)
        sleep(3)
        clear_touch(0.5,0.9,1)
        sleep(15)

#任务界面点击剧情
def common_talk():
    for per in range(10):
        if poco("Main(Clone)").child("PanelConstruct").child("TransConstructBlock").exists():
            for per in range(50):
                if poco("Main(Clone)").child("PanelNewComic").child("BtnSkip").exists():
                    try:
                        click_talk(1)
                    except:
                        pass
                else:
                    break
            sleep(3)
            clear_touch(0.5,0.5,1)
        else:
            break
    
#三选一
def repair_select():
    for per in range(5):
        if poco("Main(Clone)").child("PanelRepairSelect").exists():
            #随机选择第一个地板
            a = ['1', '2', '3']
            b = "BtnSelectTemplate_" + random.choice(a)
            click_Name(b)
            #确认选择
            click_Name("BtnConfirm")
        skip_button=poco("Main(Clone)").child("PanelNewComic").child("BtnSkip")
        try:
            if skip_button.wait_for_appearance(15):
                break
        except:
            if poco("Main(Clone)").child("PanelRepairSelect").exists():
                repair_select()

def get_DayOverBonus():
    if poco("Main(Clone)").child("PanelDayOverBonus2").exists():
        clear_touch(0.5,0.5,1)
        poco("ConsumeStarCount").wait_for_appearance(15)

def get_errorlog():
    poco.start_gesture([0.5, 0.5]).hold(0.1).to([0.5, 0.65]).to([0.65, 0.65]).to([0.65, 0.5]).to([0.5, 0.5]).to([0.5, 0.65]).to([0.65, 0.65]).to([0.65, 0.5]).to([0.5, 0.5]).up()
    snapshot()
    clear_touch(0.02,0.03,1)
    clear_touch(0.98,0.03,1)
    snapshot()

def initialize_log():
    poco.start_gesture([0.5, 0.5]).to([0.5, 0.65]).hold(1).to([0.65, 0.65]).to([0.65, 0.5]).to([0.5, 0.5]).to([0.5, 0.65]).to([0.65, 0.65]).to([0.65, 0.5]).to([0.5, 0.5]).up()
    clear_touch(0.83,0.03,1)
    clear_touch(0.89,0.03,1)
    clear_touch(0.02,0.03,1)
    clear_touch(0.98,0.03,1)


#################关卡期间#######################

# def remove_swipe(arg,x,y):
#     if poco("BoardGroupRoot").child("BoardRoot(Clone)").child("NodeLayer").child(arg).exists():
#         try:
#             poco("BoardGroupRoot").child("BoardRoot(Clone)").child("NodeLayer").child(arg).swipe([x, y])
#         except PocoTargetTimeout:
#             print('poco target swipe timeout')
#             sleep(5)
#     else:
#         print('poco no such node -- ' + arg)
#         sleep(5)
#指定棋子移动消除，需要传递被棋子的pos坐标及方向
#qx1,qy1 初始坐标,查看pos
#qx2,qy2 移动坐标,自动计算
#way：up/down/left/right
def \
        remove_swipe(sx,sy,qx1,qy1,way):
    #如果存在新手引导框
    if way == "up":
        qx2 = qx1
        qy2 = qy1 - 0.1
    elif way == "down":
        qx2 = qx1
        qy2 = qy1 + 0.1
    elif way == "left":
        qy2 = qy1
        qx2 = qx1 - 0.07
    elif way == "right":
        qy2 = qy1
        qx2 = qx1 + 0.07
    else:
        text('Error passing parameter:way')
    sleep(2)
    try:
        swipe((sx*qx1,sy*qy1),(sx*qx2,sy*qy2))
    except PocoTargetTimeout:
        print('timeout')
        sleep(3)
#指定棋子点击消除，需要传递被棋子的pos坐标及点击次数
def clear_touch(qx1,qy1,time):
    try:
        touch((sx*qx1,sy*qy1),times=time)
    except PocoTargetTimeout:
        print('timeout')
        sleep(5)
    sleep(2)

#指定棋子移动消除（多个棋盘关卡），需要传递棋盘参数n
def remove_lot_swipe(n,arg,x,y):
    if poco(texture="comic_base"):
        if poco("BoardGroupRoot").child("BoardRoot(Clone)")[n].child("NodeLayer").child(arg).exists():
            try:
                poco("BoardGroupRoot").child("BoardRoot(Clone)")[n].child("NodeLayer").child(arg).swipe([x, y])
            except PocoTargetTimeout:
                print('timeout')
                sleep(5)
        else:
            text('poco no such node -- ' + str(arg))
            sleep(5)
    else:
        text("当前无需执行新手引导操作")

# 步数不足，购买步数。步骤充足，结算跳转，返回主界面
def gm_step():
    i = 30
    while i > 0:
        #判断是否需要购买金币
        if poco(name="ContinueButton").exists():
            click_Name("ContinueButton")
        else:
            sleep(2)
        if poco(name="ButtonStart").exists():
            try:
               gm_pass()
               break
            except PocoTargetTimeout:
               raise
        #如果已经返回主界面，则结束循环
        if poco(texture=start_play):
            break
        if i == 0:
            break
        sleep(5)
        i = i - 1
    sleep(2)
#######################GM工具############################
def safe_wait(v, interval, timeout):
    try:
        pos = wait(v, interval=interval, timeout=timeout)
    except Exception:
        return False
    else:
        return pos

#打开GM工具
def gm_open():
    click_TextUi("Cheat")

#关闭GM工具
def gm_close():
    if poco(name="ButtonClose"):
        touch(Template(r"tpl1552716995134.png", record_pos=(0.463, -0.209), resolution=(2220, 1080)))

        # click_Name("ButtonClose")
    else:
        print('not such target-- ButtonClose')

#清除玩家数据记录
def gm_player_clear():
    gm_open()
    click_TextUi("玩家信息")
    

    if poco(text="星星").exists():
        swipe(Template(r"tpl1550910328600.png", record_pos=(-0.239, 0.11), resolution=(1600.0, 900.0)), vector=[-0.0095, -0.6721])
        sleep(2)
        click_TextUi("清除记录(本地)")
        # if poco("_content").exists():
        #     click_TextUi("清除记录(全部)")
        # touch(Template(r"tpl1552477446417.png", record_pos=(0.115, 0.247), resolution=(1920, 1080)))
    else:
        print('not find such pic')

    
#GM修改无限体力
def gm_time():
    gm_open()
    click_TextUi("玩家信息")
    child = poco("AnchorRight").child("ScrollView").child("_content").child("CheatTaskTemplate(Clone)")[6].child("CheatObjects")
    for child1 in child.children():
        pre = False
        pre1 = True
        for child2 in child1.children():
            print(pre1)
            child2_name = child2.get_name()
            child2_text = child2.get_text()
            if child2_name == "_title" and pre1:
                child2.click()
                text("3600")
                if exists(Template(r"tpl1547109703240.png", record_pos=(0.42, 0.203), resolution=(1920, 1080))):
                    touch(Template(r"tpl1547109703240.png", record_pos=(0.42, 0.203), resolution=(1920, 1080)))
                pre1 = False
                sleep(10)
            if child2_text == "Apply&Close":
                #child2.click()
                if exists(Template(r"tpl1561433823564.png", record_pos=(-0.061, 0.07), resolution=(2560, 1440))):
                    touch(Template(r"tpl1561433856106.png", record_pos=(0.08, 0.072), resolution=(2560, 1440)))


                pre = True
                break
            
        if pre:
            break
    text("无限体力")

#GM修改无限金币
def gm_gold():
    gm_open()
    click_TextUi("玩家信息")

    child = poco("AnchorRight").child("ScrollView").child("_content").child("CheatTaskTemplate(Clone)")[8].child("CheatObjects")
    for child1 in child.children():
        pre = False
        pre1 = True
        for child2 in child1.children():
            child2_name = child2.get_name()
            child2_text = child2.get_text()
            if child2_name == "_title" and pre1:
                child2.click()
                text("90000")
                if exists(Template(r"tpl1547109703240.png", record_pos=(0.42, 0.203), resolution=(1920, 1080))):
                    touch(Template(r"tpl1547109703240.png", record_pos=(0.42, 0.203), resolution=(1920, 1080)))
                pre1 = False
            if child2_text == "Apply&Close":
                #child2.click()
                if exists(Template(r"tpl1561433350151.png", record_pos=(-0.016, 0.199), resolution=(2560, 1440))):
                    touch(Template(r"tpl1561433367164.png", record_pos=(0.17, 0.2), resolution=(2560, 1440)))


                pre = True
                break
            
        if pre:
            break
    text("无限金币")

def gm_star():
    gm_open()
    click_TextUi("玩家信息")
    swipe(Template(r"tpl1563439052110.png", record_pos=(-0.259, 0.123), resolution=(2160, 1080)), vector=[-0.0365, -0.4778])
    child = poco("AnchorRight").child("ScrollView").child("_content").child("CheatTaskTemplate(Clone)")[9].child("CheatObjects")
    for child1 in child.children():
        pre = False
        pre1 = True
        for child2 in child1.children():
            child2_name = child2.get_name()
            child2_text = child2.get_text()
            if child2_name == "_title" and pre1:
                child2.click()
                text("888")
                if exists(Template(r"tpl1563439170411.png", record_pos=(0.434, 0.188), resolution=(2160, 1080))):
                    touch(Template(r"tpl1563439170411.png", record_pos=(0.434, 0.188), resolution=(2160, 1080)))
                    
                pre1 = False
            if child2_text == "Apply&Close":
                if exists(Template(r"tpl1563438531449.png", record_pos=(-0.032, 0.15), resolution=(2160, 1080))):
                    touch(Template(r"tpl1563438556117.png", record_pos=(0.163, 0.152), resolution=(2160, 1080)))
                pre = True
                break
        if pre:
            break
    text("增加星星")

def gm_speed_up():
    gm_open()
    click_TextUi("时间")
    if exists(Template(r"tpl1564046868505.png", record_pos=(-0.077, -0.119), resolution=(1920, 1080))):
        swipe(Template(r"tpl1564046868505.png", record_pos=(-0.077, -0.119), resolution=(1920, 1080)), vector=[0.2496, -0.003])
    touch(Template(r"tpl1564046925597.png", record_pos=(0.318, -0.121), resolution=(1920, 1080)))


#GM自动消除
def gm_auto():
    click_TextureUi("UISprite")
    sleep(10)

def gm_close_tutorial():
    gm_open()
    sleep(1)
    swipe(Template(r"tpl1552713419083.png", record_pos=(-0.414, 0.123), resolution=(2220, 1080)),vector=[0.0011, -0.5579])
    sleep(1)
    click_TextUi("开关")
    sleep(1)
    touch(Template(r"tpl1552897057579.png", record_pos=(0.116, -0.215), resolution=(2220, 1080)))
    sleep(1)
    # touch(Template(r"tpl1552897057579.png", record_pos=(0.116, -0.215), resolution=(2220, 1080)))
    gm_close()
    text("开启教程")
    sleep(10)
#GM自动通关
def gm_pass():
    gm_open()
    sleep(1)
    swipe(Template(r"tpl1552713419083.png", record_pos=(-0.414, 0.123), resolution=(2220, 1080)), vector=[0.0011, -0.5579])
    sleep(1)
    click_TextUi("Debug")
    sleep(1)
    click_TextUi("Show")
    sleep(1)
    gm_close()
    touch(Template(r"tpl1552730957339.png", record_pos=(-0.408, -0.069), resolution=(1920, 1080)))
    # poco("ButtonTaskTemplate(Clone)").child("ButtonTemplate(Clone)")[0].click()

    
    if poco(name="ButtonClose").exists():
        click_Name("ButtonClose")
    if poco(name="ButtonClose").exists():
        click_Name("ButtonClose")
    text("#########使用GM通关，当前关卡存在异常，需要检查###########")
    sleep(10)


#登录本地进入首页方法   (facebook 登录一次后  其他脚本调用此方法也可以用于facebook登录)
def DHM_login_local():
    if poco("PanelUserAcceptTips").child("RootNode").child("TransContent").child("ButtonOk"):
        poco("PanelUserAcceptTips").child("RootNode").child("TransContent").child("ButtonOk").click()
    sleep(20)
    click_Name('FacebookLogin')
    sleep(5)
    if poco("BtnSkip"):#出现引导
        sleep(2)
        for n in range(10):            
          #判断是否进入主页面 提前关闭循环 
            if exists(Template(r"tpl1564024885079.png", record_pos=(-0.439, 0.21), resolution=(1920, 1080))):
                break
            ui = poco(name="BtnSkip") 
            try:            
                ui.invalidate()
                ui.wait_for_appearance(timeout=20)
                ui.click()
                text('succee click--')
            except PocoTargetTimeout as to:
                print('PocoTargetTimeout',to)
                sleep(1)
            except PocoNoSuchNodeException as ns:
                print('PocoNoSuchNodeException',ns)
                sleep(1)        
            if exists(Template(r"tpl1570707145770.png", record_pos=(0.006, 0.041), resolution=(2160, 1080))):
                touch(Template(r"tpl1570707145770.png", record_pos=(-0.003, 0.037), resolution=(2160, 1080)))
                #选好名字
                sleep(10)
                if poco("BtnSkip").exists():
                    poco("BtnSkip").click()   
                sleep(10)
                stop_app(app_id)          
                sleep(3)
                break
            sleep(10)
        sleep(3)
    else:       
    #跳过引导
    #日常登录进入首页（进入首页之前的所有窗口处理）
        while 1:
            if poco(name="CloBtn"):    
                click_Name("CloBtn")
#             if poco("PanelStore").offspring("new_Pack_2").child("BuyButton").exists():
#                 poco("PanelStore").offspring("new_Pack_2").child("BuyButton").click()
#             if exists(Template(r"tpl1570617613443.png", record_pos=(0.323, -0.235), resolution=(1920, 1080))):
#                 click(Template(r"tpl1570617613443.png", record_pos=(0.323, -0.235), resolution=(1920, 1080)))
             # 关闭每日签到奖励对话框
            if poco(name=claim_button):
                click_Name(claim_button)
         # 关闭弹出来的对话框
            if poco(name=close_button):
                click_Name(close_button)
        # 如果只存在ok对话，关闭对话框
            if poco("ButtonOk"):
                click_Name("ButtonOk")
        # 如果上一关未结束，关闭对话框
            if poco(name=success_name1):
                click_Name(success_name1)
                sleep(5)
        #如果有新手引导礼物，关闭对话框
            if poco(name=itemReward):
                click_Name("OKButtonText")
                sleep(5)
        #关闭活动奖励对话框
            if poco(name="PanelMainLineActivity"):
                click_Name("ToLevelButton")
                sleep(5)
        # 关闭每日签到奖励对话框
            if poco(name="PanelDailyReward"):
                click_Name("ClaimButton")
                sleep(5)
    
            
        #判断是否进入主页面    
            if exists(Template(r"tpl1564024885079.png", record_pos=(-0.439, 0.21), resolution=(1920, 1080))):
                text('当前界面无任何弹框')
                break        
    pass


#登录facebook首页方法
def DHM_login_facebook():
    if poco("PanelUserAcceptTips").child("RootNode").child("TransContent").child("ButtonOk"):
        poco("PanelUserAcceptTips").child("RootNode").child("TransContent").child("ButtonOk").click()
    sleep(20)
    click_Name('FacebookLogin')
    sleep(10)   
    poco.click([0.5,0.55])
    sleep(5)
    if poco("BtnSkip"):#出现引导
        sleep(2)
        for n in range(10):            
          #判断是否进入主页面 提前关闭循环 
            if exists(Template(r"tpl1564024885079.png", record_pos=(-0.439, 0.21), resolution=(1920, 1080))):
                break
            ui = poco(name="BtnSkip") 
            try:            
                ui.invalidate()
                ui.wait_for_appearance(timeout=20)
                ui.click()
                text('succee click--')
            except PocoTargetTimeout as to:
                print('PocoTargetTimeout',to)
                sleep(1)
            except PocoNoSuchNodeException as ns:
                print('PocoNoSuchNodeException',ns)
                sleep(1)        
            if exists(Template(r"tpl1570707145770.png", record_pos=(0.006, 0.041), resolution=(2160, 1080))):
                touch(Template(r"tpl1570707145770.png", record_pos=(-0.003, 0.037), resolution=(2160, 1080)))
                #选好名字
                sleep(10)
                if poco("BtnSkip").exists():
                    poco("BtnSkip").click()   
                sleep(10)
                stop_app(app_id)          
                sleep(3)
                break
            sleep(10)
        sleep(3)
    else:       
    #跳过引导
    #日常登录进入首页（进入首页之前的所有窗口处理）
        while 1:
            if poco(name="CloBtn"):    
                click_Name("CloBtn")
#             if poco("PanelStore").offspring("new_Pack_2").child("BuyButton").exists():
#                 poco("PanelStore").offspring("new_Pack_2").child("BuyButton").click()
#             if exists(Template(r"tpl1570617613443.png", record_pos=(0.323, -0.235), resolution=(1920, 1080))):
#                 click(Template(r"tpl1570617613443.png", record_pos=(0.323, -0.235), resolution=(1920, 1080)))
             # 关闭每日签到奖励对话框
            if poco(name=claim_button):
                click_Name(claim_button)
         # 关闭弹出来的对话框
            if poco(name=close_button):
                click_Name(close_button)
        # 如果只存在ok对话，关闭对话框
            if poco("ButtonOk"):
                click_Name("ButtonOk")
        # 如果上一关未结束，关闭对话框
            if poco(name=success_name1):
                click_Name(success_name1)
                sleep(5)
        #如果有新手引导礼物，关闭对话框
            if poco(name=itemReward):
                click_Name("OKButtonText")
                sleep(5)
        #关闭活动奖励对话框
            if poco(name="PanelMainLineActivity"):
                click_Name("ToLevelButton")
                sleep(5)
        # 关闭每日签到奖励对话框
            if poco(name="PanelDailyReward"):
                click_Name("ClaimButton")
                sleep(5)
    
            
        #判断是否进入主页面    
            if exists(Template(r"tpl1564024885079.png", record_pos=(-0.439, 0.21), resolution=(1920, 1080))):
                text('当前界面无任何弹框')
                break        
    pass
def playGame():
    for x in range(3):#循环次
        print("--------------------------------------------")
        if exists(Template(r"tpl1564024885079.png", record_pos=(-0.439, 0.21), resolution=(1920, 1080))):#退出游戏了进入首页
            break
           #随机方向滑动4次 
        remove_swipe(sx,sy,random.uniform(0.3,0.8),random.uniform(0.3,0.8),random.choice(['up', 'down', 'left','right']))
           #滑累了来锤子
        remove_swipe(sx,sy,random.uniform(0.3,0.8),random.uniform(0.3,0.8),random.choice(['up', 'down', 'left','right']))  
        remove_swipe(sx,sy,random.uniform(0.3,0.8),random.uniform(0.3,0.8),random.choice(['up', 'down', 'left','right']))  
        remove_swipe(sx,sy,random.uniform(0.3,0.8),random.uniform(0.3,0.8),random.choice(['up', 'down', 'left','right']))  
        for n in range(50):#配合錘子次數  
            if exists(Template(r"tpl1570781963752.png", record_pos=(0.436, -0.007), resolution=(1920, 1080))):
                touch(Template(r"tpl1570781963752.png", record_pos=(0.436, -0.007), resolution=(1920, 1080)))
                sleep(1)
                poco.click([random.uniform(0.2,0.7),random.uniform(0.1,0.9)])  
            if exists(Template(r"tpl1570784810783.png", record_pos=(0.009, 0.227), resolution=(1920, 1080))):
                touch(Template(r"tpl1570784810783.png", record_pos=(0.009, 0.227), resolution=(1920, 1080)))
                sleep(10)
                break
                #进入首页
             #跳出循环没锤子不玩了
        if poco("ButtonSetting").exists():
            poco("ButtonSetting").exists()
            sleep(1)
            poco("ButtonQuit").click()
            sleep(5)
            break
        
           
   
