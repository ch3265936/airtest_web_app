# -*- encoding=utf8 -*-
__author__ = "chihai"

from airtest.core.api import *

auto_setup(__file__)

app_id ='com.toybrickcrush.casual.avidly'
stop_app(app_id)
sleep(10)
start_app(app_id)
sleep(30)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
poco.click([0.49,0.58])
sleep(5)
touch(Template(r"tpl1571380055680.png", record_pos=(-0.05, -0.924), resolution=(1440, 2880)))
sleep(5)

if exists(Template(r"tpl1571380134096.png", record_pos=(0.265, 0.298), resolution=(1440, 2880))):
    touch(Template(r"tpl1571380134096.png", record_pos=(0.265, 0.298), resolution=(1440, 2880)))
    
elif exists(Template(r"tpl1571380226587.png", record_pos=(0.263, 0.714), resolution=(1440, 2880))):
    touch(Template(r"tpl1571380226587.png", record_pos=(0.263, 0.714), resolution=(1440, 2880)))
else:
    touch(Template(r"tpl1571380299942.png", record_pos=(0.201, -0.529), resolution=(1440, 2880)))
sleep(10)

if poco('一键购买').exists():
    poco('一键购买').click()
    sleep(10)
if exists(Template(r"tpl1571380941037.png", record_pos=(0.433, -0.947), resolution=(1440, 2880))):
    touch(Template(r"tpl1571380941037.png", record_pos=(0.433, -0.947), resolution=(1440, 2880)))

sleep(5)
stop_app(app_id)

