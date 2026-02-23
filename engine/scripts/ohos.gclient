# Copy this file to the root of your flutter checkout to bootstrap gclient
# or just run gclient sync in an empty directory with this file.
solutions = [
  {
    "custom_deps": {
        "engine/src/flutter/third_party/libcxx_ohos": "https://gitcode.com/openharmony-sig/fluttertpc_libcxx@98f5ffbfe302be8d2757a82f6cce94d0916c6ecb",
        "engine/src/flutter/third_party/libcxxabi_ohos": "https://gitcode.com/openharmony-sig/fluttertpc_libcxxabi@0f87c1cbc8bb0cc7e0e21796fec356f99e3dbab4",
        "engine/src/flutter/third_party/vulkan-deps": "https://gitcode.com/openharmony-sig/fluttertpc_vulkan-deps@8739b8400449c9c4d96862aa7e3863a0a58637cf",
        "engine/src/flutter/third_party/dart/third_party/pkg/native": "https://gitcode.com/openharmony-sig/fluttertpc_dart_native.git@44a561397003f2abc9d6de96430f0eab8e8c405a",
        "engine/src/flutter/third_party/skia": "https://gitcode.com/openharmony-sig/fluttertpc_skia.git@302d699a100e1317b54bff76ec7157df7c431913",
        "engine/src/flutter/third_party/zlib": "https://gitcode.com/openharmony-sig/fluttertpc_zlib.git@99f35b24b64a4abaeaac8b4e716506eecdcf3b4f",
        "engine/src/flutter/third_party/swiftshader": "https://gitcode.com/openharmony-sig/fluttertpc_swiftshader.git@1d62dd49e04056e5ad006821d1ee38e8358cef7a",
        "engine/src/flutter/third_party/angle": "https://gitcode.com/openharmony-sig/fluttertpc_angle.git@bff414babe33898719e2e4004348389e6f7002fd",
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
