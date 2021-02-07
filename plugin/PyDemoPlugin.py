from adpdef import *
from adp import *
import os

def attach_calculator(name):
    procs = command2('plat shell ps -ef|grep %s' % (name))
    lines = procs.split('\n')
    items = lines[0].lstrip().split(' ')
    pid = int(itesm[1])
    if pid:
        attach(pid)
        return True
    print(procs)
    return False

def adp_on_event(args):
    event = args[adp_inkey_type]
    if event == adp_event_main_menu:
        plat = curPlatform()
        print('Current platform is %d.' % (plat))
        if plat == adp_local_mac or plat == adp_local_unicornvm:
            if not attach_calculator('Calculator'):
                debugee = inputPath()
                if debugee and os.path.exists(debugee):
                    start(debugee)
        elif plat == adp_remote_ios or plat == adp_remote_unicornvm_ios:
            attach_calculator('Calculator')
        elif plat == adp_remote_android or plat == adp_remote_unicornvm_android:
            attach_calculator('calculator')
        return success()
    if event == adp_event_menuname:
        return success('PyDemoPlugin')
    if event == adp_event_adpinfo:
        return success(('0.1.0', 'This is a simple AD python plugin.'))
    # print(args)
    return failed(adp_err_unimpl)
