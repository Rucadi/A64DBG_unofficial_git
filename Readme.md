# A64Dbg

#### Description

An arm/arm64/x86/x64 assembly level debugger for macOS/iOS/Android like OllyDbg & X64Dbg.
 
 * GUI Runtime is based on [Qt](https://www.qt.io/); 
 * GUI Controls is based on [X64Dbg](https://github.com/x64dbg/x64dbg);
 * DebugEngine is based on [LLDB](http://lldb.llvm.org/);
 * Assembler/Disassembler is based on [LLVM](http://llvm.org/);
 * Script is based on [Python](https://www.python.org/);
 * AnalyzeEngine is developed by [YunYoo](http://yunyoo.cn/);

Debugger:

 * Windows user: download from [A64Dbg-Win](https://gitee.com/geekneo/A64Dbg-Win);
 * Intel macOS user: download from [A64Dbg-Mac](https://gitee.com/geekneo/A64Dbg-Mac);
 * ARM macOS user: download from [A64Dbg-iOS](https://gitee.com/geekneo/A64Dbg-iOS);
 ```
macOS user: use the Preference menu to configurate the remote debugging.
Windows user: use the MainMenu/Options/Preference to configurate the remote debugging.

iOS user: only support the real iDevice IP configuration.
Android user: only support the 127.0.0.1 IP configuration.
```

Plugin DevTool:

 * Windows user: download from [ADPluginDev-Win](https://gitee.com/geekneo/ADPluginDev-Win);
 * Intel macOS user: download from [ADPluginDev-Mac](https://gitee.com/geekneo/ADPluginDev-Mac);
 * ARM macOS user: download from [ADPluginDev-iOS](https://gitee.com/geekneo/ADPluginDev-iOS);
 * The adpsdk and demo, look into include/plugin for more information.

Official Plugin:
 * iPhone2Sim: one click helper for A64Dbg and Simulator, dependent on [Textobot](https://gitee.com/geekneo/Textobot);

Debugger Server:

 * iOS user: install [a64dbg-server.deb](https://gitee.com/geekneo/A64Dbg/blob/master/a64dbg-server.deb) to iDevice
```
scp A64Dbg/a64dbg-server.deb root@ip:/tmp/
ssh root@ip dpkg -i --force-overwrite /tmp/a64dbg-server.deb
```
 * Android user: push [a64dbg-server](https://gitee.com/geekneo/A64Dbg/blob/master/a64dbg-server) to Android Device
```
adb push A64Dbg/a64dbg-server /data/local/tmp/
adb shell chmod -R 755 /data/local/tmp/a64dbg-server/
cd /data/local/tmp/a64dbg-server; ./lidadbg-server
```
```
adb forward tcp:30333 tcp:30333
```

Current Status:

|Platform|Description|Released|Business Model|
|-|-|-|-|
|Local ARM macOS/Simulator|ARM macOS及其iOS Simulator模拟器的本地调试|Yes|Free|
|Remote iOS|基于lldb-server/debugserver的传统iOS远程调试|Yes|Free|
|Remote Android|基于lldb-server的传统Android远程调试|Yes|Free|
|Local VP iOS Simulator|基于arm64翻译器的跨架构调试，比如在x64 macOS调试arm64的iOS程序|No|Buy|
|Remote VP Android Emulator|基于arm64翻译器的跨架构调试，比如在x64 Windows调试arm64的Android程序|No|Buy|
|Local UnicornVM|基于[UnicornVM-V8](https://gitee.com/geekneo/VirtualCode)的本地调试，比如在x64桌面调试arm64的代码|No|Buy|
|Remote UnicornVM iOS|基于[UnicornVM-iOS](https://gitee.com/geekneo/VirtualCode)的远程调试，执行代码跑在iOS UnicornVM虚拟机里面|No|Buy|
|Remote UnicornVM Android|基于[UnicornVM-V8](https://gitee.com/geekneo/VirtualCode)的远程调试，执行代码跑在Android UnicornVM虚拟机里面|No|Buy|

Follow us for update or bug report:

|Platform|Account|
|-|-|
|Email|liubaijiang@yunyoo.cn|
|公众号|刘柏江|
|头条抖音|刘柏江|
|微博|刘柏江VM|
|码云|https://gitee.com/geekneo/|


#### FAQ
```
Q: a64dbg-server.deb支持的iOS版本？

A: 内置的debugserver支持iOS >= 10.0，如果无法运行，请替换成自己的debugserver；
```
```
Q: 为什么首次使用时Attaching要很久？

A: 首次使用A64Dbg时很多模块lldb还未传回本地生成副本，所以会花费更多时间初始化调试模块；
```
```
Q: 输入Android设备Wifi IP连接调试服务出现error: Device "?.?.?.?" not found该如何处理？

A: 1.执行adb forward tcp:30333 tcp:30333转发调试服务端口至本机；
   2.调试器设置界面Android设备IP地址填入127.0.0.1；
```
```
Q：通过gitee下载的macOS版本，运行提示包已损坏该如何处理？

A：1.使用如下命令重新签一下名，然后首次使用时按住Control键以允许运行：
   codesign --force --deep --sign - /path/to/A64Dbg.app
   或者
   2.推荐使用git clone --depth=1的方式下载，这样以后可以通过git pull的方式更新，
   方便快捷不容易出错；
```
```
Q：iOS usbmuxd端口转发程序使用哪个命令行接口？

A：推荐使用https://github.com/TestStudio/usbmuxd/blob/master/python-client/tcprelay.py；
   或者按照该接口文件封装一个脚本配置给A64Dbg；
```

#### Version History

2021/1/24:
 * 发布V1.3.0;
 * 1.修复反汇编窗口垂直滚动条位置不正确的问题；
 * 2.修复elf反汇编内容错误的问题；
 * 3.修复分析section损坏的elf文件崩溃的问题；
 * 4.添加macOS/Android/模拟器-arm/x86/x64调试支持；
 * 5.优化调试启动初始化逻辑；

2021/1/19:
 * 发布iPhone2Sim V1.0.1；
 * 1.修复decache/iOS目录不存在时Dec2AD/Clone2Sim失败的问题；

2021/1/19:
 * 发布V1.2.0;
 * 1.修复远程模块下载失败界面不更新的问题；
 * 2.修复调试结束后模块卸载内存泄漏的问题；
 * 3.修复File/Launch启动后模块列表不全的问题；
 * 4.添加iOS usb端口映射支持；
 * 5.添加iOS launch app支持；
 * 6.添加信息窗口显示最后四行日志的支持；
 * 7.添加dp lldb-expr、dis lldb-expr、asm窗口命令；
 * 8.添加adb/usbmux端口转发程序配置;
 * 9.添加1/2/4/8字节watchpoint类型；
 * 10.添加静态文件地址拷贝；
 * 11.优化无符号文件函数分析功能；
 * 12.删除静态文件补丁和反汇编功能;

2021/1/15:
 * 发布V1.1.2（macOS/iOS）;
 * 1.修复FAT MachO加载崩溃的问题;

2021/1/14:
 * 发布iPhone2Sim V1.0.0；
 * 1.免费开放iPhone2Sim一键克隆手机App至模拟器；

2021/1/12:
 * 发布V1.1.1（macOS/iOS）;
 * 1.添加iPhone2Sim插件，支持一键解密Macho至缓存文件（Dec2AD）;
 * 2.修复iOS缓存文件重复下载的问题;

2021/1/10:
 * 发布V1.1.0;
 * 1.添加ADPlugin插件体系；
 * 2.添加adpdef.hpp插件开发sdk；
 * 3.添加两个插件样例工程；
 * 4.添加调试命令行程序启动参数输入；
 * 5.修复Dump/SDump窗口Follow QWord内存地址错误的问题；

2021/1/5:
 * 发布V1.0.1;
 * 1.修复了对带调试符号的模块下断点崩溃的问题；
 * 2.修复了Windows跳转地址表达式错误的问题；
 * 3.修复了初始化调试模块时偶尔崩溃的问题；
 * 4.修复调试状态下File/Disasm file无法正常反汇编的问题；
 * 5.修复tbz/tbnz跳转判定错误的问题；
 * 6.修复非CPU模块函数列表双击回车无法跳转至对应函数的问题；
 * 7.修复attach失败后进入假调试状态的问题；
 * 8.修复反复attach/detach状态维护错误的问题；
 * 9.十六进制显示参数窗口值；
 * 10.远程调试模式CPU窗口采用文件__text内容进行反汇编；

2021/1/1:
 * 发布V1.0.0；


#### Known Issue



#### Screenshot

![start](https://gitee.com/geekneo/PantaDocumentRes/raw/master/a64dbg/start.png)

![config](https://gitee.com/geekneo/PantaDocumentRes/raw/master/a64dbg/config.png)

![attach](https://gitee.com/geekneo/PantaDocumentRes/raw/master/a64dbg/attach.png)

![cpu](https://gitee.com/geekneo/PantaDocumentRes/raw/master/a64dbg/cpu.png)

![callstack](https://gitee.com/geekneo/PantaDocumentRes/raw/master/a64dbg/callstack.png)

![threads](https://gitee.com/geekneo/PantaDocumentRes/raw/master/a64dbg/threads.png)

![modules](https://gitee.com/geekneo/PantaDocumentRes/raw/master/a64dbg/modules.png)

![log](https://gitee.com/geekneo/PantaDocumentRes/raw/master/a64dbg/log.png)

![fileeditor](https://gitee.com/geekneo/PantaDocumentRes/raw/master/a64dbg/fileeditor.png)

![filediser](https://gitee.com/geekneo/PantaDocumentRes/raw/master/a64dbg/filediser.png)

![database](https://gitee.com/geekneo/PantaDocumentRes/raw/master/a64dbg/database.png)
