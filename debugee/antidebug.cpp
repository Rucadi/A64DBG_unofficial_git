#include <iostream>
#include <unistd.h>
#include <dlfcn.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/sysctl.h>

#if __APPLE__
typedef int (*ptrace_ptr_t)(int _request, pid_t _pid, caddr_t _addr, int _data);

void anti_debug() {
  ptrace_ptr_t ptrace_ptr = (ptrace_ptr_t)dlsym(RTLD_SELF, "ptrace");
  ptrace_ptr(31, 0, 0, 0); // PTRACE_DENY_ATTACH = 31
}

// Returns true if the current process is being debugged (either
// running under the debugger or has a debugger attached post facto).
static bool am_I_being_debugged(void) {
  int                 junk;
  int                 mib[4];
  struct kinfo_proc   info;
  size_t              size;

  // Initialize the flags so that, if sysctl fails for some bizarre
  // reason, we get a predictable result.
  info.kp_proc.p_flag = 0;

  // Initialize mib, which tells sysctl the info we want, in this case
  // we're looking for information about a specific process ID.
  mib[0] = CTL_KERN;
  mib[1] = KERN_PROC;
  mib[2] = KERN_PROC_PID;
  mib[3] = getpid();

  // Call sysctl.
  size = sizeof(info);
  sysctl(mib, sizeof(mib) / sizeof(*mib), &info, &size, NULL, 0);
  // We're being debugged if the P_TRACED flag is set.
  return ( (info.kp_proc.p_flag & P_TRACED) != 0 );
}
#else
#endif

int main(int argc, const char *argv[]) {
  anti_debug();

  // modify register to continue
  for (int i = argc; i < 10000000; i++) {
    printf("You should change the register to quit this infinite loop %d.\nI'm being debugged(%s).\n", 
      i, am_I_being_debugged() ? "true" : "false");
    sleep(2);
  }

  // what a nice day...
  puts("Have fun with A64Dbg UnicornVM virtualization debug mode~");
  return 0;
}
