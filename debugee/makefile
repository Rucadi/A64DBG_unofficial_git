armmac: debugme.cpp antidebug.cpp
	clang++ -arch arm64 -Os -o armmac/debugme debugme.cpp
	clang++ -arch arm64 -Os -o armmac/antidebug antidebug.cpp

x64mac: debugme.cpp
	clang++ -arch x86_64 -Os -o x64mac/debugme debugme.cpp

ios: debugme.cpp antidebug.cpp
	clang++ -target arm64-apple-ios10.0 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS.sdk -Os -o ios/debugme debugme.cpp
	clang++ -target arm64-apple-ios10.0 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS.sdk -Os -o ios/antidebug antidebug.cpp
