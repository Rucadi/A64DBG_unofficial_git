///////////////////////////////////YUNYOO.CN////////////////////////////////////
//                                                                             *
// A64Dbg ADCPP HEADER FILE                                                    *
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
#ifndef __ADCPP_H__
#define __ADCPP_H__

#define __ADCPP_VERSION__ "1.0.0"
#define __ADCPP_CDECL__ extern "C"

// function with this prefix is the real user api
#define __ADCPP_API__ static inline

/*
 * standard headers
 */
// pre-include standard c headers
#include <stddef.h>
#include <ctype.h>   // Functions to determine the type contained in character data
#include <errno.h>	 // Macros reporting error conditions
#include <float.h>	 // Limits of float types
#include <inttypes.h>// Format conversion of integer types
#include <limits.h>	 // Sizes of basic types
#include <locale.h>	 // Localization utilities
#include <math.h>	 // Common mathematics functions
#include <signal.h>	 // Signal handling
#include <stdarg.h>	 // Variable arguments
#include <stdbool.h> // Macros for boolean type
#include <stddef.h>	 // Common macro definitions
#include <stdint.h>  // Fixed-width integer types
#include <stdio.h>	 // Input/output
#include <stdlib.h>	 // General utilities: memory management, program utilities, string conversions, random numbers, algorithms
#include <string.h>	 // String handling
#include <time.h>	 // Time/date utilities

// pre-include unix c headers
#include <pthread.h>
#include <dlfcn.h>
#include <unistd.h>
#include <sys/mman.h>

// pre-include for different platforms
#if __APPLE__
// macos/ios supports objc/stl
// pre-include basic objc framework
#if __OBJC__
#import <Foundation/Foundation.h>
#import <UIKit/UIKit.h>
#endif

// pre-include c++ stl headers
#include <string>
#include <vector>
#include <set>
#include <map>
#else
// android only supports pure c/c++
#include <jni.h>
#include <android/log.h>

#endif

#if __arm__
// arm common register like r0 r1 ... lr sp pc
typedef union cmmreg_t {
  unsigned int w;
  int sw;
  const void *p;
  const char *s;
} cmmreg_t;

// arm neon register like s0 d0 ...
typedef union neonreg_t {
  unsigned int i[2];
  unsigned long long l;
  int si[2];
  long long sl;
  float f[2];
  double d;
} neonreg_t;

// arm execution context
typedef struct regctx_t {
  cmmreg_t r[16];  // 0-12, 13-sp, 14-lr, 15-reserved
  neonreg_t v[32];
  cmmreg_t pc;
} regctx_t;
#else
// arm64 common register like x0 x1 ... lr sp pc
typedef union cmmreg_t {
  unsigned int w;
  unsigned long long x;
  int sw;
  long long sx;
  const void *p;
  const char *s;
  unsigned int ws[2];
  int sws[2];
} cmmreg_t;

// arm64 neon register like s0 d0 q0 ...
typedef union neonreg_t {
  unsigned int i[4];
  unsigned long long l[2];
  int si[4];
  long long sl[2];
} neonreg_t;

// arm64 execution context
typedef struct regctx_t {
  cmmreg_t r[32];  // 0-28,29-fp,30-lr,31-sp
  neonreg_t v[32];
  cmmreg_t pc;
} regctx_t;
#endif

/*
 * adcpp debugee side api, exported by pointer to improve performance.
 * you should keep in mind : call function by pointer is faster than by address.
 *
 * so, if you want to run your adcpp code faster, change some cpu-heavily 
 * function call to pointer. for example:
 
 void slow_address_call() {
   // UnicornVM will interprete it into elf-plt/macho-stub code.
   cpu_heavily_function();
 }

 void (*cpu_heavily_function_ptr)(void);
 void init_fns() {
   cpu_heavily_function_ptr = cpu_heavily_function;
 }
 void fast_pointer_call() {
   init_fns();
   // UnicornVM will call it directly in native mode
   cpu_heavily_function_ptr();
 }
 */
struct adcpp_api_t {
  // add log to a64dbg
  void (*send2ad)(const char *format, ...);

  // send string to python3 adp, pyfn is the python3 recever function name
  void (*sendstr2py)(const char *pyfn, const char *format, ...);

  // send buffer to python3 adp, pyfn is the python3 recever function name
  void (*sendbuf2py)(const char *pyfn, const void *buff, long size);
  
  // get the debugee thread register context, return null if there's no debugee thread
  const regctx_t *(*current_regs)();

#if __APPLE__ // macOS/iOS
#else // android
  // get the android jvm instance
  JavaVM *(*current_jvm)();

  // get the current JNIEnv attached by current thread
  JNIEnv *(*current_jenv)();
#endif
};

// get the adcpp api instance from uvmdbg runtime
const adcpp_api_t *uvmdbg_adcapi();

#if !ADCPP_IMPL
/*
 * api wrappers
 */
__ADCPP_API__ const adcpp_api_t *adcapi() {
  // cache it to improve performance
  static const adcpp_api_t *api = nullptr;
  if (!api) api = uvmdbg_adcapi();
  return api;
}
// dump buffer to python
__ADCPP_API__ void buf2py(const char *pyfn, const void *buff, long size) {
  adcapi()->sendbuf2py(pyfn, buff, size);
}
// dump string to python
#define str2py(pyfn, format, ...) adcapi()->sendstr2py(pyfn, format, __VA_ARGS__)
#if __APPLE__ // macOS/iOS
#else // android
__ADCPP_API__ JavaVM *current_jvm() {
  return adcapi()->current_jvm();
}
__ADCPP_API__ JNIEnv *current_jenv() {
  return adcapi()->current_jenv();
}
#endif
#endif // end of !ADCPP_IMPL

// some register wrapper
#if __arm__
#define r0  adcapi()->current_regs()->r[0].w
#define r1  adcapi()->current_regs()->r[1].w
#define r2  adcapi()->current_regs()->r[2].w
#define r3  adcapi()->current_regs()->r[3].w
#define r4  adcapi()->current_regs()->r[4].w
#define r5  adcapi()->current_regs()->r[5].w
#define r6  adcapi()->current_regs()->r[6].w
#define r7  adcapi()->current_regs()->r[7].w
#define r8  adcapi()->current_regs()->r[8].w
#define r9  adcapi()->current_regs()->r[9].w
#define r10 adcapi()->current_regs()->r[10].w
#define r11 adcapi()->current_regs()->r[11].w
#define r12 adcapi()->current_regs()->r[12].w
#define r13 adcapi()->current_regs()->r[13].w
#define r14 adcapi()->current_regs()->r[14].w
#define r15 adcapi()->current_regs()->pc.w
#define fp  adcapi()->current_regs()->r[12].w
#define sp  adcapi()->current_regs()->r[13].w
#define lr  adcapi()->current_regs()->r[14].w
#define pc  adcapi()->current_regs()->pc.w
#else
#define x0  adcapi()->current_regs()->r[0].x
#define x1  adcapi()->current_regs()->r[1].x
#define x2  adcapi()->current_regs()->r[2].x
#define x3  adcapi()->current_regs()->r[3].x
#define x4  adcapi()->current_regs()->r[4].x
#define x5  adcapi()->current_regs()->r[5].x
#define x6  adcapi()->current_regs()->r[6].x
#define x7  adcapi()->current_regs()->r[7].x
#define x29 adcapi()->current_regs()->r[29].x
#define x30 adcapi()->current_regs()->r[30].x
#define x31 adcapi()->current_regs()->r[31].x
#define fp  adcapi()->current_regs()->r[29].x
#define sp  adcapi()->current_regs()->r[30].x
#define lr  adcapi()->current_regs()->r[31].x
#define pc  adcapi()->current_regs()->pc.x
#endif

// redirect printf/puts to a64dbg's log
#define printf adcapi()->send2ad
#define puts adcapi()->send2ad

// asm function macro helper
#define __ASM__ __asm__ __volatile__
#define __NAKED__ __attribute__((naked))

// a valid adcpp module loaded by UnicornVM must implement one of these functions
// the start entry of adcpp module.
__ADCPP_CDECL__ void adc_main(void);

// the start entry of adcpp module which will interperte it in a new thread.
__ADCPP_CDECL__ void adc_main_thread(void);

#endif // end of __ADCPP_H__
