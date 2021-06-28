int got_hook_printf(const char *format, ...) {
  va_list ap;
  char tmp[4096];
  va_start(ap, format);
  int result = vsnprintf(tmp, sizeof(tmp), format, ap);
  va_end(ap);
  printf("hooked printf : {\n%s}\n", tmp);
  return result;
}

static void *orig_sleep = nullptr;
void inline_hook_sleep(unsigned sec) {
  printf("hooked sleep : debugee want to sleep %d seconds.\n", sec);
  ((void (*)(unsigned))orig_sleep)(sec);
}

void adc_main_thread() {
  hook_got("debugme", "printf", (void *)got_hook_printf);
  hook_inline((void *)sleep, (void *)inline_hook_sleep, &orig_sleep);
  puts("fired hook for sleep and printf for debugee program.\n");
}
