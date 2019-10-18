# -*- encoding=utf8 -*-

__author__ = "tianyabin"
__title__ = '卸载安装APP'
__desc__ = '''1、卸载apk
            2、启动app，并等待启动界面'''

from airtest.core.api import *

from utils import *
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

def uninstall_TBC():
    status = os.popen(
        'adb uninstall com.toybrickcrush.casual.avidly')
    list = status.readlines()
    if list[0].find('Success') >= 0:
        log('TBC卸载执行成功---')
        Logging('TBC卸载执行成功---')
    elif list[0].find('Failure') >= 0:
        log('TBC卸载失败---')
        Logging('TBC卸载失败---')
    else:
        log('TBC命令异常---')
        Logging('TBC命令异常---')

try:
    uninstall_DHM()
except:
    Logging('DHM命令异常---')
    pass

try:
    uninstall_TBC()
except:
    Logging('TBC命令异常---')
    pass