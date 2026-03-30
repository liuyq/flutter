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
        #"engine/src/flutter/third_party/dart": "https://gitcode.com/gcw_jOhhwlE7/fluttertpc_dart_sdk@ca8d45cd1a14561ed447427d67b8ca492978523f",
        "engine/src/flutter/third_party/dart": "https://gitcode.com/gcw_jOhhwlE7/fluttertpc_dart_sdk@ohos-flutter_3.38.7_deps",
        # https://dart.googlesource.com/native.git
        # "engine/src/flutter/third_party/dart/third_party/pkg/native": "https://gitcode.com/openharmony-sig/fluttertpc_dart_native.git@44a561397003f2abc9d6de96430f0eab8e8c405a",
        "engine/src/flutter/third_party/dart/third_party/pkg/native": "https://gitcode.com/gcw_jOhhwlE7/fluttertpc_dart_native.git@097597a3920e1b5154728bae61714482a72db1a9", # ohos-flutter_3.38.7_deps

        # https://chromium.googlesource.com/chromium/src/third_party/zlib.git
        "engine/src/flutter/third_party/zlib": "https://gitcode.com/openharmony-sig/fluttertpc_zlib.git@99f35b24b64a4abaeaac8b4e716506eecdcf3b4f",

        # https://chromium.googlesource.com/vulkan-deps
        #"engine/src/flutter/third_party/vulkan-deps": "https://gitcode.com/openharmony-sig/fluttertpc_vulkan-deps@8739b8400449c9c4d96862aa7e3863a0a58637cf",
        "engine/src/flutter/third_party/vulkan-deps": "https://gitcode.com/gcw_jOhhwlE7/fluttertpc_vulkan-deps.git@6a3e36afc0ef8712e29e0fed569b8d7ba38fd15e", # ohos-flutter_3.38.7_deps

        # https://skia.googlesource.com/skia.git
        #"engine/src/flutter/third_party/skia": "https://gitcode.com/openharmony-sig/fluttertpc_skia.git@302d699a100e1317b54bff76ec7157df7c431913",
        "engine/src/flutter/third_party/skia": "https://gitcode.com/gcw_jOhhwlE7/fluttertpc_skia.git@4336110fbc7d0291f95973d8dfb72e090de2ac59", # ohos-flutter_3.38.7_deps
        # https://swiftshader.googlesource.com/SwiftShader.git
        "engine/src/flutter/third_party/swiftshader": "https://gitcode.com/openharmony-sig/fluttertpc_swiftshader.git@1d62dd49e04056e5ad006821d1ee38e8358cef7a",
        # https://flutter.googlesource.com/third_party/angle
        # "engine/src/flutter/third_party/angle": "https://gitcode.com/openharmony-sig/fluttertpc_angle.git@bff414babe33898719e2e4004348389e6f7002fd",
        "engine/src/flutter/third_party/angle": "https://gitcode.com/gcw_jOhhwlE7/fluttertpc_angle.git@c301c98a1e79f027b6038a3c1ed53eb3a32ec3f7", # ohos-flutter_3.38.7_deps
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
