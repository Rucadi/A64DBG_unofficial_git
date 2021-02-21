##################################YUNYOO.CN####################################
#                                                                             *
# AUTO GENERTATED A64Dbg PLUGIN PYTHON INTERFACE FILE                         *
#                                                                             *
# Copyright(C) 2021 YunYoo Corp., ALL RIGHTS RESERVED.                        *
#                                                                             *
# Internet: yunyoo.cn                                                         *
#                                                                             *
# This code is distributed "as is", part of A64Dbg and without warranty of    *
# any kind, expressed or implied, including, but not limited to warranty of   *
# fitness for any particular purpose. In no event will A64Dbg be liable to    *
# you for any special, incidental, indirect, consequential or any other       *
# damages caused by the use, misuse, or the inability to use of this code,    *
# including anylost profits or lost savings, even if A64Dbg has been advised  *
# of the possibility of such damages.                                         *
#                                                                             *
######################################*#######################################/

# keys for adp_on_event args
adp_inkey_name = 'name' # plugin module name
adp_inkey_type = 'event' # event type
adp_inkey_value = 'value' # event payload
adp_outkey_error = 'error' # return error code
adp_outkey_result = 'result' # return value

adp_local_mac = 0 # Local macOS/Simulator
adp_remote_ios = 1 # Remote iOS
adp_remote_android = 2 # Remote Android
adp_local_vp_ios = 3 # Local VP iOS Simulator
adp_remote_vp_android = 4 # Remote VP Android Emulator
adp_local_unicornvm = 5 # Local UnicornVM
adp_remote_unicornvm_ios = 6 # Remote UnicornVM iOS
adp_remote_unicornvm_android = 7 # Remote UnicornVM Android
adp_invalid_platform = 8

adp_arch_unsupport = 0
adp_arch_armv5te = 1
adp_arch_arm = 2
adp_arch_arm64 = 3
adp_arch_x86 = 4
adp_arch_x64 = 5

adp_version = '1.0.2'

adp_err_ok = 0 # success
adp_err_failed = 1 # failed
adp_err_canceled = 2 # canceled
adp_err_param = 3 # bad parameter
adp_err_notfound = 4 # cannot find something
adp_err_io = 5 # io issue
adp_err_thread = 6 # thread issue, some api must run at ui thread
adp_err_oor = 7 # out of range
adp_err_oom = 8 # out of memory
adp_err_auth = 9 # license issue
adp_err_permission = 10 # permission issue
adp_err_unsupport = 11 # unsupport some action
adp_err_unimpl = 12 # unimplement some action
adp_err_softbug = 13 # software bug assertion
adp_err_continue = 14 # for traverser
adp_err_break = 15 # for traverser

adp_event_loaded = 0 # after loaded this plugin
adp_event_pre_unload = 1 # before unload this plugin
adp_event_main_menu = 2 # user triggered MainMenu/Plugin/ThisPlugin
adp_event_debug_initialized = 3 # tell plugin a new debug session initialized
adp_event_debug_running = 4 # tell plugin the debuggee is running
adp_event_debug_paused = 5 # tell plugin the debugee has bee paused
adp_event_debug_terminated = 6 # tell plugin the debug session has terminated
adp_event_module_analyzed = 7 # tell plugin finished analyzing a module
adp_event_version = 8 # ask this plugin for its sdk version
adp_event_menuname = 9 # ask this plugin for its plugin menu name
adp_event_adpinfo = 10 # ask this plugin for its self version and description

