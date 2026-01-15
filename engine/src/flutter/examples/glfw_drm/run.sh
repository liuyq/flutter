#!/bin/bash
# Copyright 2013 The Flutter Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
set -e # Exit if any program returns an error.

dir_parent=$(cd $(dirname $0); pwd)

if uname -m | grep "arm64"; then
    variant="host_debug_unopt_arm64"
else
    variant="host_debug_unopt"
fi
#################################################################
# Make the host C++ project.
#################################################################
if [ ! -d debug ]; then
    mkdir debug
fi
cd debug
cmake -DCMAKE_BUILD_TYPE=Debug ..
make

#################################################################
# Make the guest Flutter project.
#################################################################
# Since cannot create a project within the Flutter SDK. Let's create
# the app project under one temporary directory
# and use absolute path as much as posisble
dir_tmp=$(mktemp -d)
name_app="myapp"
dir_app="${dir_tmp}/${name_app}"
cd ${dir_tmp}
if [ ! -d "${name_app}" ]; then
    flutter create "${name_app}"
fi
cd "${name_app}"
flutter pub add flutter_spinkit
cp ${dir_parent}/main.dart lib/main.dart
flutter build bundle \
        --local-engine-src-path ${dir_parent}/../../../ \
        --local-engine="${variant}" \
        --local-engine-host="${variant}"
cd -

#################################################################
# Run the Flutter Engine Embedder
#################################################################
${dir_parent}/debug/flutter_glfw ${dir_tmp}/${name_app} ${dir_parent}/../../third_party/icu/common/icudtl.dat
