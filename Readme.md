# A64Dbg

#### Description

An arm64 assembly level debugger for macOS/iOS/Android like OllyDbg & X64Dbg.
 
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
Q：通过gitee下载的macOS版本，运行提示包以损坏该如何处理？

A：使用如下命令重新签一下名，然后首次使用时按住Control键以允许运行：
   codesign --force --deep --sign - /path/to/A64Dbg.app
```


#### Version History

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
