# -*- encoding=utf8 -*-
__author__ = "chihai"

from airtest.core.api import *

app_id = "com.dreamhomematch.casual.free"
from constant import *
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
#########################################################
try:
    uninstall_DHM()
except:
    Logging('DHM命令异常---')
    pass

#安装DHM
try:
    install_DHM()
except:
    log('DHM安装失败')
    Logging('DHM安装失败')
    pass
