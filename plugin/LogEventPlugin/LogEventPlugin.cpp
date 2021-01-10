//
//  LogEventPlugin.cpp
//  LogEventPlugin
//
//  Created by Baijiang Liu on 2021/1/7.
//

#include "LogEventPlugin.hpp"
#include "LogEventPluginPriv.hpp"

#include <string>

#define case_event(n, desc) case adp_event_##n: { \
  return log_event(adp, adp_event_##n, #n, desc); \
}

#define case_event_input(n, input, desc) case_event(n, desc)
#define case_event_result(n, result, desc) case_event(n, desc)
#define case_event_io(n, input, result, desc) case_event(n, desc)

static adp_error_t log_event(adp_payload_t *adp, adp_event_t event,
                      const char *name, const char *desc) {
  std::string msg(name);
  char eval[16];
  sprintf(eval, ".%d : ", event);
  msg += eval;
  msg += desc;
  msg += "\n";
  adp->api->log(msg.data());
  
  if (event == adp_event_menuname) {
    adp->result.str_const = "LogEvent";
    return adp_err_ok;
  } else if (event == adp_event_version) {
    adp->result.str_const = __ADP_VERSION__;
    return adp_err_ok;
  } else if (event == adp_event_adpinfo) {
    adp->result.ptr.p0 = (void *)"0.1.0";
    adp->result.ptr.p1 = (void *)"This is a very simple NonGUI AD plugin.";
    return adp_err_ok;
  }
  return adp_err_unimpl;
}

adp_error_t adp_main(adp_payload_t *adp) {
  switch (adp->event) {
    // event with no Input/Output
    case_event(loaded, "after loaded this plugin")
    case_event(pre_unload, "before unload this plugin")
    case_event(main_menu, "user triggered MainMenu/Plugin/ThisPlugin")
    case_event(debug_initialized, "tell plugin a new debug session initialized")
    case_event(debug_running, "tell plugin the debuggee is running")
    case_event(debug_paused, "tell plugin the debugee has bee paused")
    case_event(debug_terminated, "tell plugin the debug session has terminated")

    // event with Input
    // vars.ptr is adp_module_t*
    case_event_input(module_analyzed, ptr,
                     "tell plugin finished analyzing a module")

    // event for Result
    case_event_result(version, str_const, "ask this plugin for its sdk version")
    case_event_result(menuname, str_const, "ask this plugin for its plugin menu name")
    case_event_result(adpinfo, ptr,
                      "ask this plugin for its self version and description")
    default:
      break;
  }
  return adp_err_unimpl;
}
