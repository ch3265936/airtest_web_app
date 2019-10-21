# -*- encoding=utf8 -*-
__author__ = "chihai"

from airtest.core.api import *
app_id = "com.dreamhomematch.casual.free"
from constant import *
#开启APP
auto_setup(__file__)
stop_app(app_id)
sleep(10)
start_app(app_id)
sleep(30)

#购买需要用到Android原生POCO
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
androidPoco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()
from poco.exceptions import PocoNoSuchNodeException
from poco.exceptions import PocoTargetTimeout
#登入本地方法
def DHM_login_local():
    if poco("PanelUserAcceptTips").child("RootNode").child("TransContent").child("ButtonOk"):
        poco("PanelUserAcceptTips").child("RootNode").child("TransContent").child("ButtonOk").click()
    sleep(30)
    click_Name('Login')
    sleep(5)
    if poco("BtnSkip"):  # 出现引导
        sleep(2)
        for n in range(10):
            # 判断是否进入主页面 提前关闭循环
            if exists(Template(r"tpl1564024885079.png", record_pos=(-0.439, 0.21), resolution=(1920, 1080))):
                break
            ui = poco(name="BtnSkip")
            try:
                ui.invalidate()
                ui.wait_for_appearance(timeout=20)
                ui.click()
                text('succee click--')
            except PocoTargetTimeout as to:
                print('PocoTargetTimeout', to)
                sleep(1)
            except PocoNoSuchNodeException as ns:
                print('PocoNoSuchNodeException', ns)
                sleep(1)
            if exists(Template(r"tpl1570707145770.png", record_pos=(0.006, 0.041), resolution=(2160, 1080))):
                touch(Template(r"tpl1570707145770.png", record_pos=(-0.003, 0.037), resolution=(2160, 1080)))
                # 选好名字
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
        # 跳过引导
        # 日常登录进入首页（进入首页之前的所有窗口处理）
        while 1:
            if poco(name="CloBtn"):
                click_Name("CloBtn")
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
                # 如果有新手引导礼物，关闭对话框
            if poco(name=itemReward):
                click_Name("OKButtonText")
                sleep(5)
                # 关闭活动奖励对话框
            if poco(name="PanelMainLineActivity"):
                click_Name("ToLevelButton")
                sleep(5)
                # 关闭每日签到奖励对话框
            if poco(name="PanelDailyReward"):
                click_Name("ClaimButton")
                sleep(5)
                # 判断是否进入主页面
            if exists(Template(r"tpl1564024885079.png", record_pos=(-0.439, 0.21), resolution=(1920, 1080))):
                text('当前界面无任何弹框')
                break
    pass
# 登录facebook首页方法
def DHM_login_facebook():
    if poco("PanelUserAcceptTips").child("RootNode").child("TransContent").child("ButtonOk"):
        poco("PanelUserAcceptTips").child("RootNode").child("TransContent").child("ButtonOk").click()
    sleep(20)
    click_Name('FacebookLogin')
    sleep(10)
    poco.click([0.5, 0.55])
    sleep(5)
    if poco("BtnSkip"):  # 出现引导
        sleep(2)
        for n in range(10):
            # 判断是否进入主页面 提前关闭循环
            if exists(Template(r"tpl1564024885079.png", record_pos=(-0.439, 0.21), resolution=(1920, 1080))):
                break
            ui = poco(name="BtnSkip")
            try:
                ui.invalidate()
                ui.wait_for_appearance(timeout=20)
                ui.click()
                text('succee click--')
            except PocoTargetTimeout as to:
                print('PocoTargetTimeout', to)
                sleep(1)
            except PocoNoSuchNodeException as ns:
                print('PocoNoSuchNodeException', ns)
                sleep(1)
            if exists(Template(r"tpl1570707145770.png", record_pos=(0.006, 0.041), resolution=(2160, 1080))):
                touch(Template(r"tpl1570707145770.png", record_pos=(-0.003, 0.037), resolution=(2160, 1080)))
                # 选好名字
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
        # 跳过引导
        # 日常登录进入首页（进入首页之前的所有窗口处理）
        while 1:
            if poco(name="CloBtn"):
                click_Name("CloBtn")
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
                # 如果有新手引导礼物，关闭对话框
            if poco(name=itemReward):
                click_Name("OKButtonText")
                sleep(5)
                # 关闭活动奖励对话框
            if poco(name="PanelMainLineActivity"):
                click_Name("ToLevelButton")
                sleep(5)
                # 关闭每日签到奖励对话框
            if poco(name="PanelDailyReward"):
                click_Name("ClaimButton")
                sleep(5)


                # 判断是否进入主页面
            if exists(Template(r"tpl1564024885079.png", record_pos=(-0.439, 0.21), resolution=(1920, 1080))):
                text('当前界面无任何弹框')
                break
    pass
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
##############################################################具体业务
#登入模式
if login_mode=='facebook':
    DHM_login_facebook()
else:
    DHM_login_local()
sleep(5)
#购买金币
if poco(name="Coin").exists():
    poco("Coin").click()
    click_Name("Coin")
    sleep(5)
    if poco("new_Pack_2").child("BuyButton").exists():
        poco("new_Pack_2").child("BuyButton").click()
        sleep(5)
        androidPoco("一键购买").wait(5).click()
        sleep(10)
        if poco("CloseButton").exists():
            poco("CloseButton").click()
        sleep(3)
        touch(Template(r"tpl1570768645697.png", record_pos=(-0.007, 0.211), resolution=(1920, 1080)))
        sleep(5)
        touch(Template(r"tpl1570768645697.png", record_pos=(-0.007, 0.211), resolution=(1920, 1080)))
        sleep(5)
stop_app(app_id)


        
         


        



