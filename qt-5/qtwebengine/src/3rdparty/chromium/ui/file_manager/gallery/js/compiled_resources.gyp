# Copyright 2014 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
{
  'targets': [
    {
      'target_name': 'background',
      'variables': {
        'depends': [
          '../../../../third_party/jstemplate/compiled_resources.gyp:jstemplate',
          '../../../webui/resources/js/cr.js',
          '../../../webui/resources/js/cr/event_target.js',
          '../../../webui/resources/js/cr/ui/array_data_model.js',
          '../../../webui/resources/js/cr/ui/dialogs.js',
          '../../../webui/resources/js/load_time_data.js',
          '../../file_manager/common/js/util.js',
          '../../file_manager/common/js/async_util.js',
          '../../file_manager/common/js/volume_manager_common.js',
          '../../file_manager/background/js/volume_manager.js',
          '../../file_manager/common/js/error_util.js',
          '../../file_manager/foreground/js/file_type.js'
        ],
        'externs': [
          '<(CLOSURE_DIR)/externs/chrome_send_externs.js',
          '<(CLOSURE_DIR)/externs/chrome_extensions.js',
          '<(CLOSURE_DIR)/externs/file_manager_private.js',
        ],
      },
      'includes': [
        '../../../../third_party/closure_compiler/compile_js.gypi'
      ],
    },
    {
      'target_name': 'gallery_scripts',
      'variables': {
        'depends': [
          '../../../../third_party/jstemplate/compiled_resources.gyp:jstemplate',
          '../../file_manager/background/js/volume_manager.js',
          '../../file_manager/common/js/volume_manager_common.js',
          '../../file_manager/common/js/async_util.js',
        ],
        'externs': [
          '<(CLOSURE_DIR)/externs/chrome_send_externs.js',
          '<(CLOSURE_DIR)/externs/chrome_extensions.js',
          '<(CLOSURE_DIR)/externs/file_manager_private.js',
          '<(CLOSURE_DIR)/externs/metrics_private.js',
        ],
      },
      'includes': [
        '../../../../third_party/closure_compiler/compile_js.gypi'
      ],
    }
  ],
}


