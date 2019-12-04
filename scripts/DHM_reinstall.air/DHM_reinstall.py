# -*- encoding=utf8 -*-
__author__ = "colin"

from airtest.core.api import *
__title__ = '任务剧情'
__desc__ = '''1、安装旧包后执行任务剧情
           2、进入任务剧情'''
import random
app_id = "com.dreamhomematch.casual.free"
from utils import *
#开启APP
auto_setup(__file__)


def uninstall_DHM():
    status = os.popen(
        'adb uninstall com.dreamhomematch.casual.free')
    list = status.readlines()
    if list[0].find('Success') >= 0:
        log('DHM卸载执行成功---')
        Logging('DHM卸载执行成功---')
    elif list[0].find('Failure') >= 0:
        log('DHM卸载失败---')
        Logging('DHM卸载失败---')
    else:
        log('DHM命令异常---')
        Logging('DHM命令异常---')

def install_OLD_DHM():
    time_tup = time.localtime(time.time())
    format_time = '%Y-%m-%d_%a_%H-%M-%S'
    apksName = time.strftime(format_time, time_tup)
    build_device_apks = 'D:\\testdir\\Result\\DHM_Release\\' + apksName + '.apks'
    # 通过AAB构建APKS----代替---install(apk_path)
    Build = os.system(
        'java -jar D:\\testdir\\lib\\bundletool-all-0.10.2.jar build-apks --connected-device --bundle=D:\\testdir\\Result\\DHM_Release\\DHM_Release_old.aab --output=' + build_device_apks + ' --ks=D:\\testdir\\lib\\signature.keystore --ks-pass=pass:123456 --ks-key-alias=key --key-pass=pass:123456')
    if Build == 0:
        log('DHMOLD构建成功')
        Install = os.system(
            'java -jar D:\\testdir\\lib\\bundletool-all-0.10.2.jar install-apks --apks=' + build_device_apks)
        # 构建成功安装APKS
        if Install == 0:
            log('DHMOLD安装成功')
            Logging('DHMOLD安装成功')
            sleep(2)
        else:
            log('DHMOLD安装失败')
            Logging('DHMOLD安装失败')
            pass
    else:
        log('DHMOLD构建失败')
        Logging('DHMOLD构建失败')
#########################################################
try:
    uninstall_DHM()
except:
    Logging('DHM命令异常---')
    pass

#安装DHM
try:
    install_OLD_DHM()
except:
    log('DHMOLD安装失败')
    Logging('DHMOLD安装失败')
    pass

########################安装旧包执行任务
start_app(app_id)
sleep(30)
login_mode ='facebook'
dev = device()
sy = dev.display_info['width']
sx = dev.display_info['height']
from constant import *
from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()
from poco.exceptions import PocoNoSuchNodeException
from poco.exceptions import PocoTargetTimeout

def currentData():  # 判断分支
    print("-----3----")
    touch(Template(r"tpl1575344814663.png", record_pos=(0.145, 0.207), resolution=(1920, 1080)))

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
def taskDay():
    # click_Name("Renwu")
    poco("Main(Clone)").child("LeftBar").child("Renwu").click()
    sleep(1)
    if exists(Template(r"tpl1563872365821.png", record_pos=(-0.154, 0.226), resolution=(1920, 1080))):
        click_Name("ConsumeStarCount")
        sleep(1)
    else:
        try:
            poco("Main(Clone)").child("PanelDayOverBonus2").wait_for_appearance(10)
            sleep(3)
            get_DayOverBonus()
        except:
            pass
        sleep(1)
        click_Name("ConsumeStarCount")

    # 任务界面点击剧情
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
            clear_touch(0.5, 0.5, 1)
        else:
            break

    # 三选一
def repair_select():
    for per in range(5):
        if poco("Main(Clone)").child("PanelRepairSelect").exists():
            # 随机选择第一个地板
            a = ['1', '2', '3']
            b = "BtnSelectTemplate_" + random.choice(a)
            click_Name(b)
            sleep(3)
            # 确认选择
            click_Name("BtnConfirm")
        skip_button = poco("Main(Clone)").child("PanelNewComic").child("BtnSkip")
        try:
            if skip_button.wait_for_appearance(15).exists():
                break
        except:
            if poco("Main(Clone)").child("PanelRepairSelect").exists():
                repair_select()

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
                log('当前界面无任何弹框')
                break

def taskDay():
    poco("Main(Clone)").child("LeftBar").child("Renwu").click()
    sleep(1)
    if exists(Template(r"tpl1563872365821.png", record_pos=(-0.154, 0.226), resolution=(1920, 1080))):
        click_Name("ConsumeStarCount")
        sleep(10)
    else:
        try:
            poco("Main(Clone)").child("PanelDayOverBonus2").wait_for_appearance(10)
            get_DayOverBonus()
        except:
            pass
        click_Name("ConsumeStarCount")

def talk():
    while True:
        if poco("Main(Clone)").child("PanelNewComic").child("BtnSkip").exists():
            poco("Main(Clone)").child("PanelNewComic").child("BtnSkip").click()
            sleep(3)
        else:
            break
# 循环对话
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
def clear_touch(qx1,qy1,time):
    try:
        touch((sx*qx1,sy*qy1),times=time)
    except PocoTargetTimeout:
        print('timeout')
        sleep(5)
    sleep(2)
def get_DayOverBonus():
     if poco("Main(Clone)").child("PanelDayOverBonus2").exists():
        clear_touch(0.5, 0.5, 1)
        sleep(3)
        poco("ConsumeStarCount").wait_for_appearance(15)

def get_errorlog():
    poco.start_gesture([0.5, 0.5]).hold(0.1).to([0.5, 0.65]).to([0.65, 0.65]).to([0.65, 0.5]).to([0.5, 0.5]).to(
        [0.5, 0.65]).to([0.65, 0.65]).to([0.65, 0.5]).to([0.5, 0.5]).up()
    snapshot()
    clear_touch(0.02, 0.03, 1)
    clear_touch(0.98, 0.03, 1)
    snapshot()

def initialize_log():
    poco.start_gesture([0.5, 0.5]).to([0.5, 0.65]).hold(1).to([0.65, 0.65]).to([0.65, 0.5]).to([0.5, 0.5]).to(
        [0.5, 0.65]).to([0.65, 0.65]).to([0.65, 0.5]).to([0.5, 0.5]).up()
    clear_touch(0.83, 0.03, 1)
    clear_touch(0.89, 0.03, 1)
    clear_touch(0.02, 0.03, 1)
    clear_touch(0.98, 0.03, 1)
##############################################################具体业务
#登入模式
DHM_login()
sleep(5)
for i in range(3):
    try:
        taskDay()  # 接任务
        sleep(5)
        while True:
            if poco("Main(Clone)").child("PanelRepairSelect").exists():  # 进入三选一
                repair_select()
            if poco(name="BtnSkip").exists():  # 进入聊天
                talk()
            if exists(Template(r"tpl1575275010665.png", record_pos=(-0.058, -0.001), resolution=(1920, 1080))):#完成一个阶段任务领取奖励
                touch(Template(r"tpl1575275010665.png", record_pos=(-0.058, -0.001), resolution=(1920, 1080)))
                sleep(3)
                if poco(name="BtnClose").exists():
                    poco(name="BtnClose").click()
                    sleep(1)
            if exists(Template(r"tpl1564024885079.png", record_pos=(-0.439, 0.21), resolution=(1920, 1080))):
                log('当前界面回到主页 ')
                break
        snapshot()
        sleep(3)

    except:
        get_errorlog()
        clear_touch(0.5, 0.5, 1)
        exists_main()
        raise Exception("task error")

stop_app(app_id)
sleep(3)

####################覆盖安装# #########################
from utils import *
def install_DHM():
    time_tup = time.localtime(time.time())
    format_time = '%Y-%m-%d_%a_%H-%M-%S'
    apksName = time.strftime(format_time, time_tup)
    build_device_apks = 'D:\\testdir\\Result\\DHM_Release\\' + apksName + '.apks'
    # 通过AAB构建APKS----代替---install(apk_path)
    Build = os.system(
        'java -jar D:\\testdir\\lib\\bundletool-all-0.10.2.jar build-apks --connected-device --bundle=D:\\testdir\\Result\\DHM_Release\\DHM_Release.aab --output=' + build_device_apks + ' --ks=D:\\testdir\\lib\\signature.keystore --ks-pass=pass:123456 --ks-key-alias=key --key-pass=pass:123456')
    if Build == 0:
        log('DHM构建成功')
        Install = os.system(
            'java -jar D:\\testdir\\lib\\bundletool-all-0.10.2.jar install-apks --apks=' + build_device_apks)
        # 构建成功安装APKS
        if Install == 0:
            log('DHM安装成功')
            Logging('DHM安装成功')
            sleep(2)
        else:
            log('DHM安装失败')
            Logging('DHM安装失败')
            pass
    else:
        log('DHM构建失败')
        Logging('DHM构建失败')
#直接覆盖
# 安装DHM
try:
    log('开始覆盖安装')
    Logging('开始覆盖安装')
    install_DHM()
except:
    log('DHM安装失败')
    Logging('DHM安装失败')
    pass
