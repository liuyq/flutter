# Copy this file to the root of your flutter checkout to bootstrap gclient
# or just run gclient sync in an empty directory with this file.
solutions = [
  {
    "custom_deps": {
      # specified in ./src/build/config/BUILDCONFIG.gn
      # https://github.com/llvm-mirror/libcxx.git
      # https://llvm.googlesource.com/llvm-project/libcxx
      "engine/src/flutter/third_party/libcxx_ohos": "https://gitcode.com/openharmony-sig/fluttertpc_libcxx@98f5ffbfe302be8d2757a82f6cce94d0916c6ecb",
      # https://github.com/llvm-mirror/libcxxabi.git
      # https://llvm.googlesource.com/llvm-project/libcxxabi
      "engine/src/flutter/third_party/libcxxabi_ohos": "https://gitcode.com/openharmony-sig/fluttertpc_libcxxabi@0f87c1cbc8bb0cc7e0e21796fec356f99e3dbab4",

      # https://dart.googlesource.com/sdk.git
      # "engine/src/flutter/third_party/dart": "https://gitcode.com/openharmony-sig/fluttertpc_dart_sdk.git@fbe3ce7a1bc11b1b3d19d02d98cd3f4054cdb073",
      #"engine/src/flutter/third_party/dart": "https://gitcode.com/gcw_jOhhwlE7/fluttertpc_dart_sdk@43e7ae757461f5f2be96c764651d771a62dde638",
      "engine/src/flutter/third_party/dart": "https://gitcode.com/gcw_jOhhwlE7/fluttertpc_dart_sdk@304d9e874e29c3bec53501e102f056c69b6873d8", # ohos-flutter_3.41.6_deps
      # https://dart.googlesource.com/native.git
      # "engine/src/flutter/third_party/dart/third_party/pkg/native": "https://gitcode.com/openharmony-sig/fluttertpc_dart_native.git@44a561397003f2abc9d6de96430f0eab8e8c405a",
      "engine/src/flutter/third_party/dart/third_party/pkg/native": "https://gitcode.com/gcw_jOhhwlE7/fluttertpc_dart_native.git@db18bb050bc11761ca434bae8f8acedeac8554c0", # ohos-flutter_3.41.6_deps

      # https://chromium.googlesource.com/chromium/src/third_party/zlib.git
      "engine/src/flutter/third_party/zlib": "https://gitcode.com/openharmony-sig/fluttertpc_zlib.git@99f35b24b64a4abaeaac8b4e716506eecdcf3b4f",

      # https://chromium.googlesource.com/vulkan-deps
      #"engine/src/flutter/third_party/vulkan-deps": "https://gitcode.com/openharmony-sig/fluttertpc_vulkan-deps@8739b8400449c9c4d96862aa7e3863a0a58637cf",
      "engine/src/flutter/third_party/vulkan-deps": "https://gitcode.com/gcw_jOhhwlE7/fluttertpc_vulkan-deps.git@6a3e36afc0ef8712e29e0fed569b8d7ba38fd15e", # ohos-flutter_3.38.7_deps

      # https://skia.googlesource.com/skia.git
      #"engine/src/flutter/third_party/skia": "https://gitcode.com/openharmony-sig/fluttertpc_skia.git@302d699a100e1317b54bff76ec7157df7c431913",
      "engine/src/flutter/third_party/skia": "https://gitcode.com/gcw_jOhhwlE7/fluttertpc_skia.git@a4b7a8c52748682d323e5857f1098997a784aef3", # ohos-flutter_3.41.6_deps
      # https://swiftshader.googlesource.com/SwiftShader.git
      "engine/src/flutter/third_party/swiftshader": "https://github.com/liuyq/SwiftShader.git@19b4cd1f79eac7b9ffc08eb464c5bcb768de90bc", # ohos-flutter_3.41.6_deps
      # https://flutter.googlesource.com/third_party/angle
      # "engine/src/flutter/third_party/angle": "https://gitcode.com/openharmony-sig/fluttertpc_angle.git@bff414babe33898719e2e4004348389e6f7002fd",
      "engine/src/flutter/third_party/angle": "https://gitcode.com/gcw_jOhhwlE7/fluttertpc_angle.git@bf9abb9e92a7eeef2cd55d2b0bfd18b61858eb1a", # ohos-flutter_3.41.6_deps
    },
    "deps_file": "DEPS",
    "managed": False,
    "name": ".",
    "safesync_url": "",

    # If you are using SSH to connect to GitHub, change the URL to:
    # git@github.com:flutter/flutter.git
    "url": "https://github.com/flutter/flutter.git",

    # Uncomment the custom_vars section below if you plan to build the web engine.
    # "custom_vars": {
    #   "download_emsdk": True,
    # },
  },
]
