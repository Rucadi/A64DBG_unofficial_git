# A64Dbg

#### Description

An arm/arm64/x86/x64 assembly level debugger for macOS/iOS/Linux/Android like OllyDbg & X64Dbg.

An arm/arm64 virtualization debugger(uvmdbg) based on UraniumVM for macOS/iOS/Android.

Running desktop platform supports Windows/Linux/macOS.

The debugee platform supports macOS/Linux/iOS/Android.

||Local|Remote Android|Remote iOS|
|-|-|-|-|
|Windows|No|Yes|No|
|Intel Linux|Yes|Yes|No|
|ARM Linux|Yes|Yes|No|
|Intel macOS|Yes|Yes|Yes|
|ARM macOS|Yes|Yes|Yes|

 * GUI Runtime is based on [Qt](https://www.qt.io/); 
 * GUI Controls is based on [X64Dbg](https://gitee.com/geekneo/X64Dbg/);
 * DebugEngine is based on [LLDB](http://lldb.llvm.org/);
 * Assembler/Disassembler is based on [LLVM](http://llvm.org/);
 * Decompiler is based on [RetDec](https://retdec.com/);
 * Script is based on [Python](https://www.python.org/);
 * AnalyzeEngine is developed by [YunYoo](http://yunyoo.cn/);
 * UVMEngine is developed by [YunYoo](https://gitee.com/yunyoo/UraniumVCPU/);

[Debugger Version](https://gitee.com/geekneo/A64Dbg/blob/master/Version.md):

 * Windows user: download from [A64Dbg-Win](https://gitee.com/geekneo/A64Dbg-Win);
 * Linux user: download from [A64Dbg-Linux](https://gitee.com/geekneo/A64Dbg-Linux);
 * ARM Linux user: download from [A64Dbg-LinuxARM](https://gitee.com/geekneo/A64Dbg-LinuxARM);
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
 * Python3: builtin adp python framework;

Debugger Server:

 * iOS user: install [a64dbg-server.deb](https://gitee.com/geekneo/A64Dbg/blob/master/a64dbg-server.deb) to iDevice
```
scp A64Dbg/a64dbg-server.deb root@ip:/tmp/
ssh root@ip dpkg -i --force-overwrite /tmp/a64dbg-server.deb
```
 * iOS uvmdbg user: install [](https://gitee.com/geekneo/A64Dbg/blob/master/a64dbg-server.uvm.deb) to iDevice
```
scp A64Dbg/a64dbg-server.uvm.deb root@ip:/tmp/
ssh root@ip dpkg -i --force-overwrite /tmp/a64dbg-server.uvm.deb
```
 * Android user: push [a64dbg-server-arm64](https://gitee.com/geekneo/A64Dbg/tree/master/a64dbg-server-arm64) to Android Device
```
adb push A64Dbg/a64dbg-server-arch /data/local/tmp/
adb shell chmod -R 755 /data/local/tmp/a64dbg-server-arch/
cd /data/local/tmp/a64dbg-server-arch; ./lidadbg-server
```
```
adb forward tcp:30333 tcp:30333
```
 * Android uvmdbg user: push [a64dbg-server-arm64.uvm](https://gitee.com/geekneo/A64Dbg/tree/master/a64dbg-server-arm64.uvm) to Android Device and turn off SELinux
```
adb push A64Dbg/a64dbg-server-arch.uvm /data/local/tmp/
setenforce 0
```

Current Status:

|Platform|Description|Released|Business Model|
|-|-|-|-|
|Local ARM macOS/Simulator|ARM macOS及其iOS Simulator模拟器的本地调试|Yes|Free|
|Remote iOS|基于lldb-server/debugserver的传统iOS远程调试|Yes|Free|
|Remote Android|基于lldb-server的传统Android远程调试|Yes|Free|
|Local VP iOS Simulator|基于arm64翻译器的跨架构调试，比如在x64 macOS调试arm64的iOS程序|No|Buy|
|Remote VP Android Emulator|基于arm64翻译器的跨架构调试，比如在x64 Windows调试arm64的Android程序|No|Buy|
|Local UraniumVM|基于[UraniumVM-V8](https://gitee.com/yunyoo/UraniumVCPU/tree/master/mac/arm64)的本地调试，比如在x64桌面调试arm64的代码|Yes|Buy|
|Remote UraniumVM iOS|基于[UraniumVM-iOS](https://gitee.com/yunyoo/UraniumVCPU/tree/master/ios/arm64)的远程调试，执行代码跑在iOS UraniumVM虚拟机里面|Yes|Buy|
|Remote UraniumVM Android|基于[UraniumVM-V8](https://gitee.com/yunyoo/UraniumVCPU/tree/master/android)的远程调试，执行代码跑在Android UraniumVM虚拟机里面|Yes|Buy|

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

A: 1.在调试器设置界面设置adb全路径（建议使用android sdk里面的adb），然后在Android设备IP
   地址填入127.0.0.1（由于lldb的限制，目前Android只支持这个IP地址），点击Save保存配置；
   2.这样配置之后，每次启动A64Dbg就会自动设置端口转发，不再需要手动设置，你只需要保持手机
   调试服务端一直处于运行状态即可；
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
```
Q：Windows平台lidadbg-server启动报错的原因？

A：在Windows平台如果你是用git clone的方式下载A64Dbg软件包的，手机端执行服务程序可能会报错：
      angler:/data/local/tmp/a64dbg-server-arm # ./lidadbg-server
      /system/bin/sh: ./lidadbg-server: No such file or directory
   报错的原因是git对脚本lidadbg-server添加了'\r'字符，导致sh无法解析该脚本。解决办法：
      git config --global core.autocrlf input，禁止其添加'\r'字符；
```
```
Q：macOS平台启动调试会话报debugserver not found的原因？

A：在macOS平台如果你把A64Dbg软件包放在沙盒目录AppTranslocation，启动调试会话时会报错：
      /bin/sh: debugserver: inaccessible or not found
   解决办法：将A64Dbg移出沙盒目录，比如移至Applications，Documents，Downloads之类的非沙盒目录；
```
```
Q：UraniumVM虚拟化调试模式Attach/Launch之后没有反应的原因？

A：虚拟化调试模式不同于LLDB通过Ptrace的方式控制目标进程，而是自建TCP通道与A64Dbg交互调试上下文，所以
   如果出现无反应的现象，按照如下方式逐一排查：
   1.手机是否关闭了SELinux：setenforce 0；
   2.手机与桌面是否处于同一局域网：adb shell ping desktop-ipv4；
   3.手机目标Debugee是否具备网络权限：如果没有可以通过修改系统配置文件添加；
   4.首次运行A64Dbg时是否允许了使用网络通信：如果没有则在防火墙白名单里面添加A64Dbg主程序；
```

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
