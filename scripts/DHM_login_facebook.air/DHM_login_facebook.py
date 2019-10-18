# -*- encoding=utf8 -*-
__author__ = "tianyabin"
__title__ = "login_game"
__desc__ = '''
            1、初始化测试环境
            2、启动游戏
            '''
from airtest.core.api import *


app_id = "com.dreamhomematch.casual.free"
#登录游戏
auto_setup(__file__)
stop_app(app_id)
sleep(3)
start_app(app_id)
sleep(10)
#打开APP后需要引入poco（common 已经集成）
using("DHM_common.air")
from DHM_common import *
DHM_login_facebook()
    

