'''
This is really a very simple a64dbg python adp demo.
'''
# import basic adp definition like error/event code
from adpdef import *
# import adp api entries
from adp import *
import os

# adcpp output handler for api send2py
def adcpp_output(data):
    print(data)

# auto attach the Calculator process
def attach_calculator(name):
    # execute an lldb command to list the calcular process
    procs = command2('plat shell ps -ef|grep %s' % (name))
    lines = procs.split('\n')
    for l in lines:
        if l.find(name) < 0:
            continue
        print('Checking line: %s' % (l))
        items = l.lstrip().split(' ')
        if (items[0] == 'root' or items[0] == 'shell'):
            continue
        for i in range(1, len(items)):
            if len(items[i]):
                pid = int(items[i])
                if pid:
                    attach(pid)
                    return True
                break
    print(procs)
    return False

# a64dbg debugengine event for python plugin
def adp_on_event(args):
    event = args[adp_inkey_type]
    # user clicked the plugin's main menu
    if event == adp_event_main_menu:
        plat = curPlatform()
        print('Current platform is %d.' % (plat))
        if plat == adp_local_mac or plat == adp_local_unicornvm:
            if not attach_calculator('Calculator'):
                # ask user to select a file to debug
                debugee = inputPath()
                if debugee and os.path.exists(debugee):
                    start(debugee)
        elif plat == adp_remote_ios or plat == adp_remote_unicornvm_ios:
            attach_calculator('Calculator')
        elif plat == adp_remote_android or plat == adp_remote_unicornvm_android:
            attach_calculator('calculator')
        return success()
    # ask for plugin's menu name
    if event == adp_event_menuname:
        return success('PyDemoPlugin')
    # ask for plugins's version and descripton 
    if event == adp_event_adpinfo:
        return success(('0.1.0', 'This is a simple AD python plugin.'))
    # run c/c++ code inside debugee
    if event == adp_event_debug_initialized:
        # demo for adcpp api
        plat = curPlatform()
        if plat == adp_local_unicornvm or \
            plat == adp_remote_unicornvm_ios or \
            plat == adp_remote_unicornvm_android:
            runadc(
            '''
            printf("Hello world from PyDemoPlugin's runadc.\\n");
            str2py("adcpp_output", "Hello, ADCpp. My pid in %d.\\n", getpid());
            ''')
            return success()
    # print(args)
    return failed(adp_err_unimpl)
