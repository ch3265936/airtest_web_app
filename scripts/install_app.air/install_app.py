# -*- encoding=utf8 -*-

__author__ = "tianyabin"
__title__ = '安装APP'
__desc__ = '''1安装apk
            2、启动app，并等待启动界面'''

from airtest.core.api import *
from utils import *
auto_setup(__file__)


def install_DHM():
    app_id = "com.dreamhomematch.casual.free"
    time_tup = time.localtime(time.time())
    format_time = '%Y-%m-%d_%a_%H-%M-%S'
    apksName = time.strftime(format_time, time_tup)
    build_device_apks = 'D:\\testdir\\Result\\DHM_4.4.10_2367_Release\\' + apksName + '.apks'
    # 通过AAB构建APKS----代替---install(apk_path)
    DHMBuild = os.system(
        'java -jar D:\\testdir\\lib\\bundletool-all-0.10.2.jar build-apks --connected-device --bundle=D:\\testdir\\Result\\DHM_4.4.10_2367_Release\\DHM_4.4.10_2367_Release_Debug.aab --output=' + build_device_apks + ' --ks=D:\\testdir\\lib\\signature.keystore --ks-pass=pass:123456 --ks-key-alias=key --key-pass=pass:123456')
    if DHMBuild == 0:
        log('DHM构建成功')
        DHMInstall = os.system(
            'java -jar D:\\testdir\\lib\\bundletool-all-0.10.2.jar install-apks --apks=' + build_device_apks)
        # 构建成功安装APKS
        if DHMInstall == 0:
            log('DHM安装成功')
            Logging('DHM安装成功')
            sleep(2)
            start_app(app_id)
            sleep(30)
            from poco.drivers.unity3d import UnityPoco
            poco = UnityPoco()
            if poco("ButtonOk"):
                poco.click([0.49, 0.57])
                sleep(3)
            log('DHM打开成功')
            Logging('DHM打开成功')
            stop_app(app_id)
            sleep(3)

        else:
            log('DHM安装失败')
            Logging('DHM安装失败')
            pass
    else:
        log('DHM构建失败')
        Logging('DHM构建失败')


def install_TBC():
    app_id = "com.toybrickcrush.casual.avidly"
    app_path ="D:\\testdir\\Result\\ToyBrickCrush.apk"
    DHMInstall = os.system(
        'adb install ' + app_path)
    # 构建成功安装APKS
    if DHMInstall == 0:
        log('TBC安装成功')
        Logging('TBC安装成功')
        sleep(2)
        start_app(app_id)
        sleep(10)
        log('TBC打开成功')
        Logging('TBC打开成功')
        stop_app(app_id)
        sleep(3)

    else:
        log('TBC安装失败')
        Logging('TBC安装失败')
        pass
try:
    install_TBC()
except:
    log('TBC安装失败')
    Logging('TBC安装失败')
    pass
try:
    install_DHM()
except:
    log('DHM安装失败')
    Logging('DHM安装失败')
    pass

