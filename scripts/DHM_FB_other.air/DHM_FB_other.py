# -*- encoding=utf8 -*-
__author__ = "chihai"

from airtest.core.api import *
app_id = "com.dreamhomematch.casual.free"
import random
from constant import *
auto_setup(__file__)
stop_app(app_id)
sleep(3)
start_app(app_id)
sleep(15)
dev = device()
sy = dev.display_info['width']
sx = dev.display_info['height']
login_mode ='facebook'
from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()
from poco.exceptions import PocoNoSuchNodeException
from poco.exceptions import PocoTargetTimeout


def currentData():  # 判断分支
    print("-----3----")
    touch(Template(r"tpl1572488764686.png", record_pos=(-0.13, 0.211), resolution=(2560, 1440)))
    sleep(5)
    poco.click([0.48, 0.42])
    text("Confirm")

    sleep(2)
    poco.click([0.48, 0.42])
    sleep(3)
    touch(Template(r"tpl1572493133436.png", record_pos=(0.01, 0.039), resolution=(2560, 1440)))
    sleep(10)
    print("-----4----")
    if exists(Template(r"tpl1574919826343.png", record_pos=(-0.0, -0.044), resolution=(2880, 1440))):
        poco.click([0.5, 0.55])
        sleep(10)
        print("-----5----")
    if exists(Template(r"tpl20191202095928.png", record_pos=(0.15, 0.196), resolution=(2560, 1440))):#下载新阶段内容
        poco.click([0.5, 0.55])
        sleep(28)
        if exists(Template(r"tpl20191202100008.png", record_pos=(0.15, 0.196), resolution=(2560, 1440))):
            touch(Template(r"tpl20191202100008.png", record_pos=(0.15, 0.196), resolution=(2560, 1440)))
            sleep(3)
    if exists(Template(r"tpl1572408025013.png", record_pos=(0.15, 0.196), resolution=(2560, 1440))):
        touch(Template(r"tpl1572408025013.png", record_pos=(0.15, 0.196), resolution=(2560, 1440)))
        sleep(5)


# 登录facebook首页方法
def DHM_login():
    if poco("PanelUserAcceptTips").child("RootNode").child("TransContent").child("ButtonOk"):
        poco.click([0.5,0.57])
        sleep(10)
         #选择本地或者服务器数据
    if poco('CurrentDataButton').exists():
        currentData()
    else:#无选择数据分支
        sleep(25)
        if login_mode=='facebook':
            if poco('FacebookLogin').exists():
                touch(Template(r"tpl1574912559868.png", record_pos=(-0.144, 0.176), resolution=(2880, 1440)))
                sleep(20)
                print("-----1----")
                if poco('CurrentDataButton').exists():
                    currentData()
                else:
                    sleep(30)
                    poco.click([0.48, 0.55])
                    print("-----6----")
            else:
                touch(Template(r"tpl1572408025013.png", record_pos=(0.15, 0.196), resolution=(2560, 1440)))
        else:
            touch(Template(r"tpl1572408025013.png", record_pos=(0.15, 0.196), resolution=(2560, 1440)))
            print("-----7----")
        sleep(5)
    sleep(10)
# 日常登录进入首页（进入首页之前的所有窗口处理包括引导）
    while True:
        if poco("BtnSkip").exists():  # 出现引导
            poco("BtnSkip").click()
        if poco(name="CloBtn"):
            click_Name("CloBtn")
        # 关闭每日签到奖励对话框
        if poco(name=claim_button):
            click_Name(claim_button)
        if poco('QuitButton'):
            click_Name("QuitButton")
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
            # 如果有新手引导礼物，关闭对话框
        if poco(name=itemReward):
            click_Name("OKButtonText")
            sleep(5)
        # 关闭每日签到奖励对话框
        if poco(name="PanelDailyReward"):
            click_Name("ClaimButton")
            sleep(5)
            # 判断是否进入主页面
        if exists(Template(r"tpl1564024885079.png", record_pos=(-0.439, 0.21), resolution=(1920, 1080))):
            log('当前界面无任何弹框')
            break

# 点击类型为name按钮并等待UI跟新
def remove_swipe(sx,sy,qx1,qy1,way):
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

def playGame():
    for x in range(2):  # 循环次
        print("--------------------------------------------")
        if exists(Template(r"tpl1564024885079.png", record_pos=(-0.439, 0.21), resolution=(1920, 1080))):  # 退出游戏了进入首页
            log('已经回到首页游戏结束')
            break
        # 随机方向滑动4次
        sleep(10)
        log('随机滑动4次')
        remove_swipe(sx, sy, random.uniform(0.3, 0.8), random.uniform(0.3, 0.8),
                        random.choice(['up', 'down', 'left', 'right']))
            # 滑累了来锤子
        remove_swipe(sx, sy, random.uniform(0.3, 0.8), random.uniform(0.3, 0.8),
                         random.choice(['up', 'down', 'left', 'right']))
        remove_swipe(sx, sy, random.uniform(0.3, 0.8), random.uniform(0.3, 0.8),
                         random.choice(['up', 'down', 'left', 'right']))
        remove_swipe(sx, sy, random.uniform(0.3, 0.8), random.uniform(0.3, 0.8),
                         random.choice(['up', 'down', 'left', 'right']))
        log('滑个球球老夫不滑了，霸王锤搞起来50次，0.2-0.7的坐标锤')
        for n in range(5):  # 配合錘子次數
            if exists(Template(r"tpl1570781963752.png", rgb=True, record_pos=(0.436, -0.007), resolution=(1920, 1080))):
                    touch(Template(r"tpl1570781963752.png",rgb=True, record_pos=(0.436, -0.007), resolution=(1920, 1080)))
                    sleep(1)
                    poco.click([random.uniform(0.2, 0.7), random.uniform(0.1, 0.9)])
            sleep(3)
            if exists(Template(r"tpl1574927430723.png", record_pos=(-0.009, -0.007), resolution=(2880, 1440))):

                touch(Template(r"tpl1574927430723.png", record_pos=(-0.009, -0.007), resolution=(2880, 1440)))
                sleep(10)
                break
        # 进入首页
        # 跳出循环没锤子不玩了
        log('锤了50次还没搞定--老夫撤退了')
        if poco("ButtonSetting").exists():
            poco("ButtonSetting").click()
            sleep(1)
            poco("ButtonQuit").click()
            sleep(5)
            break

def click_Name(arg):
    ui = poco(name=arg)
    try:
        ui.invalidate()
        ui.wait_for_appearance(timeout=30)
        ui.click()
        text('succee click--' + str(arg))
    except PocoTargetTimeout as to:
        print('PocoTargetTimeout',to)
        sleep(1)
    except PocoNoSuchNodeException as ns:
        print('PocoNoSuchNodeException',ns)
        sleep(1)

    # 判断当前界面是否位于主界面
def exists_main():
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
        # 如果有新手引导礼物，关闭对话框
        elif poco(name=itemReward):
            click_Name("OKButtonText")
            sleep(5)
        # 关闭活动奖励对话框
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

 
 ###广告观看
def gotoTv():
    tv=40
    if poco("Main(Clone)").child("LeftBar").child("Renwu").exists():
        poco("Main(Clone)").child("LeftBar").child("Renwu").click()
        sleep(3)
    if poco("ImgAdTip").exists():
        poco("ImgAdTip").click()
        while True:
            tv -= 1
            sleep(1)
            if tv == 1:
                keyevent("BACK")
                break
        sleep(5)
        poco.click([0.5, 0.5])
        sleep(3)
        if assert_exists(Template(r"tpl1575016329101.png", record_pos=(-0.006, 0.069), resolution=(1920, 1080)),
                         "广告结束获取奖励"):
            poco.click([0.5, 0.5])
    else:
        log('无广告可以观看')
def gotoTv2():
    tv=40
    if poco("BtnFreeCoin").exists():
        poco("BtnFreeCoin").click()
        while True:
            tv -= 1
            sleep(1)
            if tv == 1:
                keyevent("BACK")
                break
        sleep(5)
        poco.click([0.5, 0.5])
        sleep(3)
        if assert_exists(Template(r"tpl1575016329101.png", record_pos=(-0.006, 0.069), resolution=(1920, 1080)),
                         "广告结束获取奖励"):
            poco.click([0.5, 0.5])
    else:
        log('无广告可以观看')
DHM_login()
sleep(5)
import random
while True:# 随机切换家具3选一
    sleep(5)
    poco.long_click([random.uniform(0.3, 0.8), random.uniform(0.3, 0.8)] ,duration=3)
    if exists(Template(r"tpl1574997974732.png", record_pos=(0.453, -0.172), resolution=(1920, 1080))):
        a=([0.8,0.35],[0.9,0.35],[0.8,0.55])
        b=random.choice(a)
        poco.click(b)
        sleep(1)
        poco.click([0.86,0.73])
        sleep(3)
        break
#other check
touch(Template(r"tpl1575258021330.png", record_pos=(-0.362, 0.085), resolution=(2280, 1080)))
sleep(3)
poco.swipe((0.85,0.5),(0.15,0.5))
sleep(1)
poco.swipe((0.15,0.5),(0.85,0.5))
log('左滑一次，右滑一次')
sleep(1)
poco.long_click([0.5,0.5])
sleep(5)
if poco("ButtonShare").exists():
    poco("ButtonShare").click()
    sleep(20)
    if exists(Template(r"tpl1575265012267.png", record_pos=(-0.001, -0.158), resolution=(2280, 1080))):
        poco.swipe((0.46,0.67),(0.46,0.47))
        sleep(1)
        #touch(Template(r"tpl1575264992127.png", record_pos=(0.0, 0.157), resolution=(2280, 1080)))
        poco.click([0.5,0.82])
        sleep(8)
    else:
        poco.click([0.88,0.07])
        sleep(8)
sleep(5)
poco("ButtonClose").click()
sleep(3)
#进入设置
poco(texture="setting_fg").click()
sleep(1)
poco("ButtonContactUs").click()
sleep(1)
poco.click([0.47,0.40])
sleep(1)
text("very good！")
sleep(1)
poco("ButtonSend").click()
log('反馈联系完成')
#打分
poco("ButtonRate").click()
sleep(3)
snapshot()
sleep(1)
keyevent("BACK")
sleep(3)
poco("ButtonPrivacy").click()
sleep(1)
poco("ButtonUrl1").click()
sleep(3)
snapshot()
sleep(1)
keyevent("BACK")
sleep(3)
poco("ButtonUrl2").click()
sleep(3)
snapshot()
sleep(1)
keyevent("BACK")
sleep(1)
poco("PanelUserTips").offspring("ButtonClose").click()
sleep(3)
poco("ButtonClose").click()
sleep(3)
assert_exists(Template(r"tpl1564024885079.png", record_pos=(-0.439, 0.21), resolution=(1920, 1080)),"购买成功回到主页面")
##
 ###广告观看
a=random.choice([1,2])
if a==1:
    gotoTv()
else:
    gotoTv2()
sleep(3)
stop_app(app_id)


