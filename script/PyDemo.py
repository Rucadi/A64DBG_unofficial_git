from adpdef import *
from adp import *

def logger(log):
    print('PyDemo: %s' % (log))

def list_module(module):
    logger(module)
    return adp_err_continue

def list_func(func):
    logger(func)
    return adp_err_continue

logger('hello, world~')

logger('arm r0 %d' % (arm.r0))
logger('arm d0 %d' % (arm.d0))
logger('arm64 x0 %d' % (arm64.x0))
logger('arm64 q0 %s' % str(arm64.q0))
logger('x86 eax %d' % (x86.eax))
logger('x86 mm0 %d' % (x86.mm0))
logger('x64 rax %d' % (x64.rax))
logger('x64 xmm0 %s' % str(x64.xmm0))
logger('x64 ymm0 %s' % str(x64.ymm0))
logger('sp %d, pc %d' % (arm64.sp, arm64.pc))

logStatus('PyDemo log to status.\n')

focusCPU()
cpu(0)
dump(0)

focusLog()

travelModule(list_module)
travelFunc('debugme', list_func)

opcode = asmint('nop')
logger('nop opcode is %d.' % (opcode))
opcasm = disasint(opcode)
logger('%d disas to %s.' % (opcode, opcasm))

logger('mem1 %s' % str(mem1(0)))
logger('mem2 %s' % str(mem2(0)))
logger('mem4 %s' % str(mem4(0)))
logger('mem8 %s' % str(mem8(0)))
logger('wrmem1 %s' % str(writemem1(0, 0)))
logger('wrmem2 %s' % str(writemem2(0, 0)))
logger('wrmem4 %s' % str(writemem4(0, 0)))
logger('wrmem8 %s' % str(writemem8(0, 0)))

logger('is debuggine %s.' % (isDebugging()))

logger('get int config %d.' % (getIntConfig('A64Dbg', 'RemoteAndroidPort')))
logger('get string config %s.' % (getConfig('A64Dbg', 'RemoteAndroidIP')))

stepinto()
stepover()
pause()
bp(0)
unsetBreakpoint(0)
setWatchpoint(0, 0)
unsetBreakpoint(0)
command('help plat proc')
logger('plat shell id %s.\n' % (command2('plat shell id')))
attach(0)
detach()
runto(0)

logger('Current platform %d.' % (curPlatform()))
logger('Current arch %d.' % (curArch()))
logger('Current python plugins %s.' % (str(usradp)))

runpy('print("I am a string from python expression string.")')
