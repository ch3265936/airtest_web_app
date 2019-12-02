# -*- encoding=utf8 -*-
__author__ = "chihai"

from airtest.core.api import *
#开始战斗（texture）
start_play="btn_startlevel"
#开始战斗-确定按钮(name)
start_confirm="ButtonStart"
#弹框关闭按钮(小锤子，手套）
close_button="CloseButton"
#每日签到确定按钮
claim_button="ClaimButton"
#战斗成功
success_name1="Congratulations"
success_name2="Spine GameObject (tap to continue)"
#新手引导奖励任务
itemReward="PanelItemReward"
#剧情对话
#3.3
char_text="BlackLineDown"
char_skip="BtnSkip"
app_id = "com.dreamhomematch.casual.free"
#DHM配置
login_mode ='local'
# from utils import *
#开启APP
auto_setup(__file__)
# def uninstall_DHM():
#     status = os.popen(
#         'adb uninstall com.dreamhomematch.casual.free')
#     list = status.readlines()
#     if list[0].find('Success') >= 0:
#         log('DHM卸载执行成功---')
#         Logging('DHM卸载执行成功---')
#     elif list[0].find('Failure') >= 0:
#         log('DHM卸载失败---')
#         Logging('DHM卸载失败---')
#     else:
#         log('DHM命令异常---')
#         Logging('DHM命令异常---')

# def install_DHM():
#     time_tup = time.localtime(time.time())
#     format_time = '%Y-%m-%d_%a_%H-%M-%S'
#     apksName = time.strftime(format_time, time_tup)
#     build_device_apks = 'D:\\testdir\\Result\\DHM_Release\\' + apksName + '.apks'
#     # 通过AAB构建APKS----代替---install(apk_path)
#     Build = os.system(
#         'java -jar D:\\testdir\\lib\\bundletool-all-0.10.2.jar build-apks --connected-device --bundle=D:\\testdir\\Result\\DHM_Release\\DHM_Release.aab --output=' + build_device_apks + ' --ks=D:\\testdir\\lib\\signature.keystore --ks-pass=pass:123456 --ks-key-alias=key --key-pass=pass:123456')
#     if Build == 0:
#         log('DHM构建成功')
#         Install = os.system(
#             'java -jar D:\\testdir\\lib\\bundletool-all-0.10.2.jar install-apks --apks=' + build_device_apks)
#         # 构建成功安装APKS
#         if Install == 0:
#             log('DHM安装成功')
#             Logging('DHM安装成功')
#             sleep(2)
#         else:
#             log('DHM安装失败')
#             Logging('DHM安装失败')
#             pass
#     else:
#         log('DHM构建失败')
#         Logging('DHM构建失败')
##########################################################
# try:
#     uninstall_DHM()
# except:
#     Logging('DHM命令异常---')
#     pass
#
# #安装DHM
# try:
#     install_DHM()
# except:
#     log('DHM安装失败')
#     Logging('DHM安装失败')
#     pass
###########################################################
stop_app(app_id)
sleep(3)
start_app(app_id)
sleep(15)
from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()
from poco.exceptions import PocoNoSuchNodeException
from poco.exceptions import PocoTargetTimeout
def currentData():#判断分支
    print("-----3----")
    touch(Template(r"tpl1572488764686.png", record_pos=(-0.13, 0.211), resolution=(2560, 1440)))
    sleep(5)
    poco.click([0.48,0.42])
    text("Confirm")
    
    sleep(2)
    poco.click([0.48,0.42])
    sleep(3)
    touch(Template(r"tpl1572493133436.png", record_pos=(0.01, 0.039), resolution=(2560, 1440)))
    sleep(10)
    print("-----4----")
    if exists(Template(r"tpl1574919826343.png", record_pos=(-0.0, -0.044), resolution=(2880, 1440))):
        poco.click([0.5,0.55])
        sleep(10)
        print("-----5----")
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
                sleep(5)
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
    if poco("BtnSkip").exists():  # 出现引导
        sleep(2)
        for n in range(10):
            # 判断是否进入主页面 提前关闭循环
            if exists(Template(r"tpl1564024885079.png", record_pos=(-0.439, 0.21), resolution=(1920, 1080))):
                break
            if poco('QuitButton'):##引导进入活动关闭
                click_Name("QuitButton")
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
    else:
        # 跳过引导
        # 日常登录进入首页（进入首页之前的所有窗口处理）
        while True:
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
                # 关闭活动奖励对话框
#             if poco(name="PanelMainLineActivity"):
#                 click_Name("ToLevelButton")
#                 sleep(5)
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
##########################################################具体业务
#登入模式可能有引导，不管是否出现引导都关闭重开（过引导）
DHM_login()
#购买金币
#购买需要用到Android原生POCO
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
androidPoco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

if poco(name="Coin").exists():
    poco("Coin").click()
    sleep(5)
    if exists(Template(r"tpl1572415016673.png", record_pos=(0.006, -0.199), resolution=(2560, 1440))):
        poco.click([0.42,0.85])
        sleep(5)
        androidPoco("一键购买").wait(5).click()
        sleep(15)
        poco.click([0.5,0.8])
        sleep(5)
        poco.click([0.5, 0.8])
stop_app(app_id)
sleep(5)


