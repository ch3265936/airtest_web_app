# -*- encoding=utf8 -*-
__author__ = "tianyabin"
__title__ = "关卡-配置体力、金币"
__desc__ = '''
            1、一小时体力
            2、300W金币
            '''
from airtest.core.api import *
app_id = "com.dreamhomematch.casual.free"
auto_setup(__file__)
stop_app(app_id)
sleep(3)
start_app(app_id)
sleep(10)

using("DHM_common.air")
from DHM_common import *
#进入主页
DHM_login_local()

#无限体力、金币
gm_time()
gm_gold()
gm_star()
gm_speed_up()
initialize_log()
exists_main()