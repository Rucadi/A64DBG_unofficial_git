'''
///////////////////////////////////YUNYOO.CN////////////////////////////////////
//                                                                             *
// A64Dbg PLUGIN PYTHON INTERFACE FILE                                         *
//                                                                             *
// Copyright(C) 2021 YunYoo Corp., ALL RIGHTS RESERVED.                        *
//                                                                             *
// Internet: yunyoo.cn                                                         *
//                                                                             *
// This code is distributed "as is", part of A64Dbg and without warranty of    *
// any kind, expressed or implied, including, but not limited to warranty of   *
// fitness for any particular purpose. In no event will A64Dbg be liable to    *
// you for any special, incidental, indirect, consequential or any other       *
// damages caused by the use, misuse, or the inability to use of this code,    *
// including anylost profits or lost savings, even if A64Dbg has been advised  *
// of the possibility of such damages.                                         *
//                                                                             *
///////////////////////////////////////*////////////////////////////////////////
'''

import _adp
import register
import importlib
from adpdef import *

# current version
adpy_version = '1.0.3'

# register instance
arm = register.arm()
arm64 = register.arm64()
x86 = register.x86()
x64 = register.x86_64()

# entry for api
def api_proc(name, args = None):
    """
    internal use.
    """
    if args is None:
        return _adp.adp_entry({'action':'api', 'name':name})
    return _adp.adp_entry({'action':'api', 'name':name, 'args':args})

def api_proc_result(api, args = None):
    """
    internal use.
    """
    result = api_proc(api, args)
    err = result[adp_outkey_error]
    if err != adp_err_ok:
        print('API %s(%s) return an error: %d.' % (api, args, err))
        return None
    return result[adp_outkey_result]

# api interface
# void (*logStatus)(const char *msg)
def logStatus(msg):
    """
    print the string msg to status bar.
    """
    api_proc('logStatus', msg)

# void (*focusCPU)();
def focusCPU():
    """
    make cpu widget as the focus window
    """
    api_proc('focusCPU')

# void (*focusLog)()
def focusLog():
    """
    make log widget as the focus window
    """
    api_proc('focusLog')

# void (*gotoCPUAdderss)(adpint addr)
def gotoCPUAdderss(addr):
    """
    make cpu disassembly widget got to address
    """
    api_proc('gotoCPUAdderss', addr)

def cpu(addr):
    """
    wrapper for gotoCPUAddress
    """
    return gotoCPUAdderss(addr)

# void (*travelModule)(adp_error_t (*handler)(const adp_module_t *module))
def travelModule(handler):
    """
    iterate all the debugee module, a sample handler:
    def handler(module):
        print(module)
        return adp_err_continue
    the module callback argument is a dict object.
    """
    api_proc('travelModule', handler)

# void (*travelFunc)(const adp_module_t *module,
#                    adp_error_t (*handler)(const adp_func_t *func))
def travelFunc(module, handler):
    """
    iterate all the function in the module. module should be a string name.
    a sample handler:
    def handler(func):
        print(func)
        return adp_err_continue
    the function callback argument is a dict object.
    """
    api_proc('travelFunc', (module, handler))

# adp_error_t (*inputString)(const char *title, char *text, adpint size)
def inputString(title):
    """
    show a string input dialog.
    """
    return api_proc_result('inputString', title)

# adp_error_t (*inputInteger)(const char *title, adpint *value)
def inputInteger(title):
    """
    show an integer input dialog.
    """
    return api_proc_result('inputInteger', title)

# adp_error_t (*inputPath)(char *path, adpint size, adpint isdir,
#                          adpint isopen)
def inputPath(isdir = False, isopen = True):
    """
    show a dir/file open/save dialog.
    """
    return api_proc_result('inputPath', (isdir, isopen))

# adp_error_t (*disassemble)(const void *opcode, char *asmcode, adpint asmsize)
def disassemble(opcode):
    """
    disassemble the opcode to string. opcode should be a bytes object.
    """
    return api_proc_result('disassemble', opcode)

def disas(opcode):
    """
    wrapper for disassemble
    """
    return disassemble(opcode)

def disasint(opcode):
    """
    disassemble the opcode to string, opcode should be an integer object.
    """
    return api_proc_result('disassembleFromInteger', opcode)

# adp_error_t (*assemble)(const char *asmcode, void *opcode)
def assemble(asmcode):
    """
    assemble the string asmcode to machine opcode, the result is a bytes object.
    """
    return api_proc_result('assemble', asmcode)

def asm(asmcode):
    """
    wrapper for assemble.
    """
    return assemble(asmcode)

def asmint(asmcode):
    """
    assemle the string asmcode to machine opcode, the result is an integer object.
    """
    return api_proc_result('assembleToInteger', asmcode)

# adp_error_t (*readMemory)(adpint addr, adp_bytes_t *buff, adpint *readed)
def readMemory(addr, size):
    """
    read memory at addr with size within the page, the result is a bytes object.
    """
    return api_proc_result('readMemory', (addr, size))

def mem1(addr):
    """
    read memory at addr with 1 byte.
    """
    return api_proc_result('readMemory1Byte', addr)

def mem2(addr):
    """
    read memory at addr with 2 bytes.
    """
    return api_proc_result('readMemory2Byte', addr)

def mem4(addr):
    """
    read memory at addr with 4 bytes.
    """
    return api_proc_result('readMemory4Byte', addr)

def mem8(addr):
    """
    read memory at addr with 8 bytes.
    """
    return api_proc_result('readMemory8Byte', addr)

# adp_error_t (*writeMemory)(adpint addr, const adp_bytes_t *buff,
#                            adpint *writed)
def writeMemory(addr, buff):
    """
    write the buff to addr, the buff should be a bytes object.
    """
    return api_proc_result('writeMemory', (addr, buff))

def writemem1(addr, val):
    """
    write 1 byte val to addr.
    """
    return api_proc_result('writeMemory1Byte', (addr, val))

def writemem2(addr, val):
    """
    write 2 bytes val to addr.
    """
    return api_proc_result('writeMemory2Byte', (addr, val))

def writemem4(addr, val):
    """
    write 4 bytes val to addr.
    """
    return api_proc_result('writeMemory4Byte', (addr, val))

def writemem8(addr, val):
    """
    write 8 bytes val to addr.
    """
    return api_proc_result('writeMemory8Byte', (addr, val))

# adpint (*isDebugging)()
def isDebugging():
    """
    return true if is debugging now.
    """
    return api_proc_result('isDebugging')

# adp_error_t (*gotoDumpAddress)(adpint addr, adpint index)
def gotoDumpAddress(addr, index = 0):
    """
    make dump widget goto the address, index range is [0, 3)
    """
    return api_proc('gotoDumpAddress', (addr, index))

def dump(addr, index = 0):
    """
    wrapper for gotoDumpAddress.
    """
    return gotoDumpAddress(addr, index)

# adp_error_t (*getIntConfig)(const char *sect, const char *key, adpint *value)
def getIntConfig(sect, key):
    """
    get an integer config from a64dbg.ini.
    """
    return api_proc_result('getIntConfig', (sect, key))

# adp_error_t (*getConfig)(const char *sect, const char *key, char *cfg,
#                           adpint cfgsize)
def getConfig(sect, key):
    """
    get a string config from a64dbg.init.
    """
    return api_proc_result('getConfig', (sect, key))

# adp_error_t (*setIntConfig)(const char *sect, const char *key, adpint value)
def setIntConfig(sect, key, value):
    """
    set an integer config to a64dbg.init.
    """
    return api_proc_result('setIntConfig', (sect, key, value))

# adp_error_t (*getConfig)(const char *sect, const char *key, const char *cfg)
def setConfig(sect, key, value):
    """
    set a string config to a64dbg.init.
    """
    return api_proc_result('setConfig', (sect, key, value))

# adp_error_t (*stepDebugee)(adpint isinto)
def stepDebugee(isinto):
    """
    step debuggee like lldb's ni/si command.
    """
    return api_proc('stepDebugee', isinto)

def stepinto():
    """
    wrapper for stepDebugee, instruction into.
    """
    return stepDebugee(True)

def stepover():
    """
    wrapper for stepDebugee, instruction over.
    """
    return stepDebugee(False)

# adp_error_t (*continueDebugee)()
def continueDebugee():
    """
    run debugee like lldb's c command.
    """
    return api_proc('continueDebugee')

# adp_error_t (*pauseDebugee)()
def pauseDebugee():
    """
    stop debugee like lldb's proc int command.
    """
    return api_proc('pauseDebugee')

# adp_error_t (*setBreakpoint)(adpint addr, adpint isoneshot,
#                              const char *condexpr)
def setBreakpoint(addr, isoneshot = False, condexpr = ''):
    """
    set a breakpoint at addr, with oneshot/cond specified.
    """
    api_proc('setBreakpoint', (addr, isoneshot, condexpr))

def bp(addr):
    """
    set a breakpoint at addr.
    """
    return setBreakpoint(addr, False, '')

def cond(addr, condexpr):
    """
    set a condtion breakpoint at addr.
    """
    return setBreakpoint(addr, False, condexpr)

def oneshot(addr):
    """
    set an oneshot breakpoint at addr.
    """
    return setBreakpoint(addr, True, '')

# adp_error_t (*unsetBreakpoint)(adpint addr);
def unsetBreakpoint(addr):
    """
    remove the breakpoint at addr.
    """
    api_proc('unsetBreakpoint', addr)

# adp_error_t (*setWatchpoint)(adpint addr, adpint size)
def setWatchpoint(addr, size):
    """
    set a watchpoint at addr with size, size should be (1, 2, 4, 8)
    """
    api_proc('setWatchpoint', (addr, size))

# adp_error_t (*unsetWatchpoint)(adpint addr)
def unsetWatchpoint(addr):
    """
    remove the watchpoint at addr.
    """
    api_proc_result('unsetWatchpoint', addr)

# adpint (*registerCommander)(const char *name,
#                             bool (*handler)(const char *cmd))
def registerCommander(name, handler):
    """
    register your own commander to the command edit, a sample handler:
    def handler(cmds):
        print('(a64dbg adp) %s' % (cmds))
        return True
    the result is the commander id, pass it to unregisterCommander to remove it.
    """
    return api_proc_result('registerCommander', (name, handler))

# void (*unregisterCommander)(adpint idval)
def unregisterCommander(idval):
    """
    remove the commander with id, idval is returned by registerCommander.
    """
    api_proc('unregisterCommander', idval)

# adp_error_t (*lldbCommand)(const char *cmd)
def lldbCommand(cmd):
    """
    execute a lldb command without result.
    """
    return api_proc('lldbCommand', cmd)

def command(cmd):
    """
    wrapper for lldbCommand.
    """
    return lldbCommand(cmd)

# adp_error_t (*lldbCommandResult)(const char *cmd, char *result, adpint size)
def lldbCommandResult(cmd):
    """
    execute a lldb command, return the string output.
    note: DO NOT EXECUTE A LONG TIME COMMAND, it will make remote lldb-server signal timeout.
    """
    return api_proc_result('lldbCommandResult', cmd)

def command2(cmd):
    """
    wrapper for lldbCommandResult.
    """
    return lldbCommandResult(cmd)

def remoteShellCommand(cmd):
    """
    execute a remote shell command without result.
    note: DO NOT EXECUTE A LONG TIME COMMAND, it will make remote lldb-server signal timeout.
    """
    return lldbCommand('plat shell ' + cmd)

def shell(cmd):
    """
    wrapper for remoteShellCommand.
    """
    return remoteShellCommand(cmd)

def remoteShellCommandResult(cmd):
    """
    execute a remote shell command, return the string output.
    note: DO NOT EXECUTE A LONG TIME COMMAND, it will make remote lldb-server signal timeout.
    """
    return lldbCommandResult('plat shell ' + cmd)

def shell2(cmd):
    """
    wrapper for remoteShellCommandResult.
    """
    return remoteShellCommandResult(cmd)

# void (*attach)(adpint pid)
def attach(pid):
    """
    attach to the process with pid.
    """
    api_proc('attach', pid)

# void (*detach)()
def detach():
    """
    detach from current debugee.
    if the debuggee is running, will keep it running.
    if the debuggee was stopped by lldb, will terminate it.
    """
    api_proc('detach')

# start a debugee with its full path
def start(path):
    """
    start a debugee with fullpath specified.
    """
    command('init "%s"' % (path))

# launch an iOS debugee with its full app path
def launch(ios_app):
    """
    launch a remote debugee the app path specified.
    """
    command('launch %s' % (ios_app))

def run():
    """
    wrapper for continueDebugee.
    """
    return continueDebugee()

def runto(addr):
    """
    run to the addr.
    """
    oneshot(addr)
    return run()

def runret():
    """
    run to return.
    """
    command('rtr')

def runbbe():
    """
    run to basicblock end or call.
    """
    command('rtbbe')

# python expression or path
def runPython(py):
    """
    run a python expression or script file.
    """
    api_proc('runPython', py)

def runpy(py):
    """
    wrapper for runPython
    """
    return runPython(py)
    
def pause():
    """
    wrapper for pauseDebugee.
    """
    return pauseDebugee()

# adp_platform_t (*curPlatform)();
def curPlatform():
    """
    return the current debugee platform, like:
    adp_local_mac = 0 # Local macOS/Simulator
    adp_remote_ios = 1 # Remote iOS
    adp_remote_android = 2 # Remote Android
    adp_local_vp_ios = 3 # Local VP iOS Simulator
    adp_remote_vp_android = 4 # Remote VP Android Emulator
    adp_local_unicornvm = 5 # Local UnicornVM
    adp_remote_unicornvm_ios = 6 # Remote UnicornVM iOS
    adp_remote_unicornvm_android = 7 # Remote UnicornVM Android
    """
    return api_proc_result('curPlatform')

# adp_arch_t (*curArch)();
def curArch():
    """
    return the current debugee arch, like:
    adp_arch_arm = 2
    adp_arch_arm64 = 3
    adp_arch_x86 = 4
    adp_arch_x64 = 5
    """
    return api_proc_result('curArch')

# adp_error_t (*addrModule)(adpint addr, adp_module_t *module);
def addrModule(addr):
    """
    get the module belongs to addr
    """
    return api_proc_result('addrModule', addr)

def addrmod(addr):
    """
    wrapper for addrModule
    """
    return addrModule(addr)

#adpint (*nextPC)();
def nextpc():
    """
    get the next pc address
    """
    return api_proc_result('nextPC')

# c/c++ expressions or path
def runADCpp(code):
    """
    run a c/c++ expression or source file inside debugee with UnicornVM.
    """
    api_proc('runADCpp', code)

def runadc(code):
    """
    wrapper for runADCpp
    """
    return runADCpp(code)

# event result wrapper
def adp_result(err, value = None):
    """
    the adp event callback should use this function to construct the result.
    """
    if value is None:
        return {adp_outkey_error:err}
    return {adp_outkey_error:err, adp_outkey_result:value}

def success(value = None):
    """
    the adp event callback success result.
    """
    return adp_result(adp_err_ok, value)

def failed(err = adp_err_failed):
    """
    the adp event callback failure result.
    """
    return adp_result(err)

# internal python plugin instance
usradp = {}

# internal used event callback for adp python3 module
def adp_on_event(args):
    global usradp
    # get user plugin module name
    name = args[adp_inkey_name]
    if name is None:
        return adp_result(adp_err_notfound)
    # get user plugin module
    module = usradp.get(name)
    if module is None:
        # import user plugin module
        module = importlib.import_module(name)
        if module is None:
            return adp_result(adp_err_failed)
        usradp[name] = module
    # pre-process event
    event = args[adp_inkey_type]
    if event == adp_event_version:
        return adp_result(adp_err_ok, adp_version)
    if event == adp_event_adcpp_output:
        # invoke user plugin's adcpp output handler
        adcpp_handler = module.__dict__.get(args[adp_inkey_extra])
        if adcpp_handler is None:
            return adp_result(adp_err_unimpl)
        adcpp_handler(args[adp_inkey_value])
        return adp_result(adp_err_ok)
    # invoke user plugin's event handler
    handler = module.adp_on_event
    if handler is None:
        return adp_result(adp_err_unimpl)
    # pass event to user plugin's handler
    return handler(args)
