# A64Dbg

#### Description

An arm/arm64/x86/x64 assembly level debugger for macOS/iOS/Android like OllyDbg & X64Dbg.

An arm/arm64 virtualization debugger(uvmdbg) based on UraniumVM for macOS/iOS/Android.
 
 * GUI Runtime is based on [Qt](https://www.qt.io/); 
 * GUI Controls is based on [X64Dbg](https://github.com/x64dbg/x64dbg);
 * DebugEngine is based on [LLDB](http://lldb.llvm.org/);
 * Assembler/Disassembler is based on [LLVM](http://llvm.org/);
 * Script is based on [Python](https://www.python.org/);
 * AnalyzeEngine is developed by [YunYoo](http://yunyoo.cn/);
 * UVMEngine is developed by [YunYoo](http://yunyoo.cn/);

[Debugger Version](https://gitee.com/geekneo/A64Dbg/blob/master/Version.md):

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
 * Android uvmdbg user: push [a64dbg-server-arm64.uvm](https://gitee.com/geekneo/A64Dbg/tree/master/a64dbg-server-arm64.uvm) to Android Device
```
adb push A64Dbg/a64dbg-server-arch.uvm /data/local/tmp/
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
```
Q：Windows平台lidadbg-server启动报错的原因？

A：在Windows平台如果你是用git clone的方式下载A64Dbg软件包的，手机端执行服务程序可能会报错：
      angler:/data/local/tmp/a64dbg-server-arm # ./lidadbg-server
      /system/bin/sh: ./lidadbg-server: No such file or directory
   报错的原因是git对脚本lidadbg-server添加了'\r'字符，导致sh无法解析该脚本。解决办法：
      git config --global core.autocrlf input，禁止其添加'\r'字符；
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
