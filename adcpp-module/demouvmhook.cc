static void *orig_sleep = nullptr;
void inline_hook_uvm_sleep(unsigned sec) {
  printf("uvm hooked sleep : debugee want to sleep %d seconds.\n", sec);
  ((void (*)(unsigned))orig_sleep)(sec);
}

void adc_main_thread() {
  hook_inline_uvm((void *)sleep, (void *)inline_hook_uvm_sleep, &orig_sleep);
  puts("fired uvmhook for sleep for debugee program.\n");
}
