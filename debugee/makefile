mac: debugme.cpp
	clang++ -arch arm64 -Os -o armmac/debugme debugme.cpp

ios: debugme.cpp
	clang++ -target arm64-apple-ios10.0 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS.sdk -Os -o ios/debugme debugme.cpp

android: debugme.cpp
	cd android; ndk-build
