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

/*
 * standard headers
 */
// pre-include standard c headers
#include <ctype.h>   // Functions to determine the type contained in character data
#include <errno.h>	 // Macros reporting error conditions
#include <float.h>	 // Limits of float types
#include <inttypes.h>// (C99)	Format conversion of integer types
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
#import <Foundation/Foundation.h>
#import <UIKit/UIKit.h>

// pre-include c++ stl headers
#include <string>
#include <vector>
#include <set>
#include <map>
#else
// android only supports pure c/c++
#endif

/*
 * adcpp debugee side api
 */
// redirect printf/puts to a64dbg's log
#define printf send2ad
#define puts send2ad

// add log to a64dbg
void send2ad(const char *format, ...);

// send string to python3 adp, pyfn is the python3 recever function name
void send2py(const char *pyfn, const char *format, ...);

// send buffer to python3 adp, pyfn is the python3 recever function name
void send2py(const char *pyfn, long size, const void *buff);

// a valid adcpp module loaded by UnicornVM must implement one of these functions
// the start entry of adcpp module.
__ADCPP_CDECL__ void adc_main(void);

// the start entry of adcpp module which will interperte it in a new thread.
__ADCPP_CDECL__ void adc_main_thread(void);

#endif // end of __ADCPP_H__
