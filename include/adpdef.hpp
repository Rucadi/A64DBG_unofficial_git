///////////////////////////////////YUNYOO.CN/////////////////////////////////////
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
///////////////////////////////////////*//////////////////////////////////////////////////
#ifndef __ADPDEF_H__
#define __ADPDEF_H__

#define __ADP_VERSION__ "0.1.0"
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

// main entry error code definition
typedef enum {
  adp_err_ok = 0,     // success
  adp_err_failed,     // failed
  adp_err_io,         // io issue
  adp_err_oor,        // out of range
  adp_err_oom,        // out of memory
  adp_err_unsupport,  // unsupport some action
  adp_err_unimpl,     // unimplement some action
  adp_err_softbug,    // software bug assertion
} adp_error_t;

// event definition
#define decl_event(n, desc) adp_event_##n
#define decl_event_result(n, result, desc) decl_event(n, desc)
typedef enum {
  decl_event(loaded, "after loaded this plugin"),
  decl_event(pre_unload, "before unload this plugin"),
  decl_event(main_menu, "user triggered MainMenu/Plugin/ThisPlugin"),

  decl_event_result(version, str_const, "ask this plugin for its sdk version"),
  decl_event_result(menuname, str_const,
                    "ask this plugin for its plugin menu name"),
} adp_event_t;

// api definition
typedef struct {
  const char *(*version)();  // get current A64Dbg's version
  void (*log)(const char *msg); // logger
} adp_api_t;

// bytes definition
typedef struct {
  char *ptr;
  adpint len;
} adp_bytes_t;

// payload for plugin main entry difinition
typedef struct {
  // constants
  const adp_api_t *api;    // all the A64Dbg's user api
  adpint consts_dummy[8];  // for future use

  // input vars
  adp_event_t event;     // why call this plugin main entry
  adpint vars_dummy[8];  // for future use

  // output result
  union {
    // 8 bytes integer result
    adpint val;

    // string result
    const char *str_const;
    char *str_dyn;  // will free this buffer after use

    // binary buffer result
    adp_bytes_t buf_const;
    adp_bytes_t buf_dyn;  // will free this buffer after use
  } result;
  adpint dummy[8];  // for future use
} adp_payload_t;

// a valid A64Dbg plugin must implement this function
__ADP_API__ adp_error_t adp_main(adp_payload_t *adp);

#endif  // end of __ADPDEF_H__
