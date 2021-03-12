'''
This is really a very simple a64dbg python adp demo.
'''
# import basic adp definition like error/event code
from adpdef import *
# import adp api entries
from adp import *
import os

# adcpp output handler for api send2py
def adcpp_dump(data):
    print(data)

# a64dbg debugengine event for python plugin
def adp_on_event(args):
    event = args[adp_inkey_type]
    # user clicked the plugin's main menu
    if event == adp_event_main_menu:
        # demo for adcpp api
        plat = curPlatform()
        if plat == adp_local_unicornvm or \
            plat == adp_remote_unicornvm_ios or \
            plat == adp_remote_unicornvm_android:
            # dump 1024 sp bytes
            runadc(
            '''
            buf2py("adcpp_dump", (void *)sp, 1024);
            ''')
            return success()
    # ask for plugin's menu name
    if event == adp_event_menuname:
        return success('ADCppDemoPlugin')
    # ask for plugins's version and descripton 
    if event == adp_event_adpinfo:
        return success(('0.1.0', 'This is a simple ADCpp python plugin.'))
    return failed(adp_err_unimpl)
