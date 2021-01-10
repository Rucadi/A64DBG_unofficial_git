///////////////////////////////////YUNYOO.CN////////////////////////////////////
//                                                                             *
// A64Dbg PLUGIN HEADER FILE                                                   *
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
#ifndef __ADPDEF_H__
#define __ADPDEF_H__

#define __ADP_VERSION__ "1.0.0"
#define __ADP_CDECL__ extern "C"

// windows definition
#if defined(_WIN32) || defined(_WIN64)

#define __ADP_EXPORT__ __declspec(dllexport)

typedef long long adpint;

// macOS definition
#else

#define __ADP_EXPORT__ __attribute__((visibility("default")))

typedef long adpint;

#endif  // end of _WIN

// c api definition
#define __ADP_API__ __ADP_CDECL__ __ADP_EXPORT__

// api entry error code definition
enum adp_error_t {
  adp_err_ok = 0,      // success
  adp_err_failed,      // failed
  adp_err_canceled,    // canceled
  adp_err_param,       // bad parameter
  adp_err_notfound,    // cannot find something
  adp_err_io,          // io issue
  adp_err_thread,      // thread issue, some api must run at ui thread
  adp_err_oor,         // out of range
  adp_err_oom,         // out of memory
  adp_err_auth,        // license issue
  adp_err_permission,  // permission issue
  adp_err_unsupport,   // unsupport some action
  adp_err_unimpl,      // unimplement some action
  adp_err_softbug,     // software bug assertion
  adp_err_continue,    // for traverser
  adp_err_break,       // for traverser
};

// event definition
#define decl_event(n, desc) adp_event_##n
#define decl_event_input(n, input, desc) decl_event(n, desc)
#define decl_event_result(n, result, desc) decl_event(n, desc)
#define decl_event_io(n, input, result, desc) decl_event(n, desc)
enum adp_event_t {
  // event with no Input/Output
  decl_event(loaded, "after loaded this plugin"),
  decl_event(pre_unload, "before unload this plugin"),
  decl_event(main_menu, "user triggered MainMenu/Plugin/ThisPlugin"),
  decl_event(debug_initialized, "tell plugin a new debug session initialized"),
  decl_event(debug_running, "tell plugin the debuggee is running"),
  decl_event(debug_paused, "tell plugin the debugee has bee paused"),
  decl_event(debug_terminated, "tell plugin the debug session has terminated"),

  // event with Input
  // input.ptr is adp_module_t*
  decl_event_input(module_analyzed, ptr,
                   "tell plugin finished analyzing a module"),

  // event for Result
  decl_event_result(version, str_const, "ask this plugin for its sdk version"),
  decl_event_result(menuname, str_const,
                    "ask this plugin for its plugin menu name"),
  // ptr.p0 should be adp's self version string
  // ptr.p1 should be adp's description
  decl_event_result(adpinfo, ptr,
                    "ask this plugin for its self version and description"),

  // event with Input for Result
  // currently nothing

  //...
  // Tell me, what the extra event do you want ?
};

// bytes definition
struct adp_bytes_t {
  char *ptr;
  adpint len;
};

// pair definition
struct adp_pair_t {
  void *p0;
  void *p1;
};

// module definition
struct adp_module_t {
  const char *path;
  // whether loaded its adb file
  adpint hasadb;
  adpint start;
  // note, it's not the real end address, usually it's the next module's start
  adpint end;
};

// function definition
struct adp_func_t {
  const char *name;
  // rva to its parent module
  adpint rvastart;
  adpint rvaend;
};

// api definition
struct adp_api_t {
  /*
   * add by adp v1.0.0
   */
  // get current A64Dbg's version
  const char *(*version)();
  // logger
  void (*log)(const char *msg);
  // logger for status bar
  void (*logStatus)(const char *msg);
  // make main window focus on cpu window
  void (*focusCPU)();
  // make main window focus on log window
  void (*focusLog)();
  // make cpu window goto the specified address
  void (*gotoCPUAdderss)(adpint addr);
  // iterate modules
  void (*travelModule)(adp_error_t (*handler)(const adp_module_t *module));
  // iterate functions
  void (*travelFunc)(const adp_module_t *module,
                     adp_error_t (*handler)(const adp_func_t *func));
  // check whether is debugging
  adpint (*isDebugging)();
  // make dump window goto the specified address, 0,1,2
  adp_error_t (*gotoDumpAddress)(adpint addr, adpint index);
  // get configuration
  adp_error_t (*getIntConfig)(const char *sect, const char *key, adpint *value);
  adp_error_t (*getConfig)(const char *sect, const char *key, char *cfg,
                           adpint cfgsize);
  // set configuration
  adp_error_t (*setIntConfig)(const char *sect, const char *key, adpint value);
  adp_error_t (*setConfig)(const char *sect, const char *key, const char *cfg);
  // ask user to input a string
  adp_error_t (*inputString)(const char *title, char *text, adpint size);
  // ask user to input an integer
  adp_error_t (*inputInteger)(const char *title, adpint *value);
  // ask user to select a path
  adp_error_t (*inputPath)(char *path, adpint size, adpint isdir,
                           adpint isopen);
  // disassemble an arm64 opcode
  adp_error_t (*disassemble)(unsigned opcode, char *asmcode, adpint asmsize);
  // assemble an arm64 asm instruction
  adp_error_t (*assemble)(const char *asmcode, unsigned *opcode);
  // pickup current register value like x0-x29,lr,sp,pc
  adp_error_t (*getRegister)(const char *regname, adpint *regvalue);
  // set register value
  adp_error_t (*setRegister)(const char *regname, adpint regvalue);
  // read memory at addr in the page
  adp_error_t (*readMemory)(adpint addr, adp_bytes_t *buff, adpint *readed);
  // write memory at addr in the page
  adp_error_t (*writeMemory)(adpint addr, const adp_bytes_t *buff,
                             adpint *writed);
  // step one instruction
  adp_error_t (*stepDebugee)(adpint isinto);
  // continue debugee
  adp_error_t (*continueDebugee)();
  // pause debugee
  adp_error_t (*pauseDebugee)();
  // set breakpoint at the specified address
  adp_error_t (*setBreakpoint)(adpint addr, adpint isoneshot,
                               const char *condexpr);
  // unset breakpoint at the specified address
  adp_error_t (*unsetBreakpoint)(adpint addr);
  // set watchpoint at the specified address
  adp_error_t (*setWatchpoint)(adpint addr, adpint size);
  // unset watchpoint at the specified address
  adp_error_t (*unsetWatchpoint)(adpint addr);
  // execute an lldb command
  adp_error_t (*lldbCommand)(const char *cmd);
  adp_error_t (*lldbCommandResult)(const char *cmd, char *result, adpint size);
  // register plugin's command handler, return its id for unregister
  adpint (*registerCommander)(const char *name,
                              bool (*handler)(const char *cmd));
  // unregister command handler, idval is returned by registerCommander
  void (*unregisterCommander)(adpint idval);
  // attach to the pid for selected default platform
  void (*attach)(adpint pid);
  // detach from current debugee
  void (*detach)();
  //...
  // Tell me, what the extra api do you want ?
};

// main entry input vars definition
struct adp_input_t {
  // 8 bytes integer input
  adpint val;

  // string input
  const char *str;

  // binary buffer input
  adp_bytes_t buf;

  // depend on event
  const void *ptr;
};

// main entry output result
union adp_result_t {
  // 8 bytes integer result
  adpint val;

  // string result
  const char *str_const;
  char *str_dyn;  // will free this buffer after use

  // binary buffer result
  adp_bytes_t buf_const;
  adp_bytes_t buf_dyn;  // will free this buffer after use

  // depend on event
  adp_pair_t ptr;
};

// payload for plugin main entry difinition
struct adp_payload_t {
  // constants
  const adp_api_t *api;    // all the A64Dbg's user api
  adpint consts_dummy[8];  // for future use

  // input vars
  adp_event_t event;      // why call this plugin main entry
  adp_input_t input;      // input vars for plugin
  adpint input_dummy[8];  // for future use

  // output result
  adp_result_t result;
  adpint dummy[8];  // for future use
};

// a valid A64Dbg plugin must implement this function
__ADP_API__ adp_error_t adp_main(adp_payload_t *adp);

#endif  // end of __ADPDEF_H__
