LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)

LOCAL_MODULE := debugme
LOCAL_SRC_FILES := ../../debugme.cpp 

LOCAL_CFLAGS += -fvisibility=hidden
LOCAL_CPPFLAGS += -std=gnu++17
LOCAL_LDLIBS += -llog

include $(BUILD_EXECUTABLE)

include $(CLEAR_VARS)

LOCAL_MODULE := antidebug
LOCAL_SRC_FILES := ../../antidebug.cpp 

LOCAL_CFLAGS += -fvisibility=hidden
LOCAL_CPPFLAGS += -std=gnu++17
LOCAL_LDLIBS += -llog

include $(BUILD_EXECUTABLE)
