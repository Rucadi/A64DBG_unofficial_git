#include <iostream>
#include <unistd.h>

int main(int argc, const char *argv[]) {
  // modify register to continue
  for (int i = argc; i < 10000000; i++) {
    printf("You should change the register to quit this infinite loop %d.\n", i);
    sleep(2);
  }

  // modify opcode as nop to continue
  std::cout << "You should nop the SIGSEGV operation to continue.\n";
  *(void **)main = nullptr;

  // what a nice day...
  puts("Have fun with A64Dbg ~");
  return 0;
}
