/*
 * Copyright (c) 2025 Huawei Device Co., Ltd. All rights reserved.
 * Use of this source code is governed by a BSD-style license that can be
 * found in the LICENSE_HW file.
 */
#ifndef FLUTTER_SHELL_PLATFORM_OHOS_ACCESSIBILITY_MULTI_INSTANCE_XCOMP_ACCESSIBILITY_H_
#define FLUTTER_SHELL_PLATFORM_OHOS_ACCESSIBILITY_MULTI_INSTANCE_XCOMP_ACCESSIBILITY_H_
#include <arkui/native_interface_accessibility.h>

namespace flutter {
/**
 * * @brief Multi-Instance XComponent Scenario of Accessibility Callbacks
 * * @since 15
 */
class MultiInstanceXCompAccessibility {
 public:
  MultiInstanceXCompAccessibility() = default;
  ~MultiInstanceXCompAccessibility() = default;

  void BindAccessibilityCallbackWithInstance();

  ArkUI_AccessibilityProviderCallbacksWithInstance
      a11yProviderCallbackWithInstance_;
};
}  // namespace flutter
#endif  // FLUTTER_SHELL_PLATFORM_OHOS_ACCESSIBILITY_MULTI_INSTANCE_XCOMP_ACCESSIBILITY_H_
