# -*- coding: UTF-8 -*-

import json
import os
import sys
CWD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(CWD)

DEVICES_SETTING_PATH = os.path.join(CWD, 'devices.json')

def device_id_list(platform=None):
  id_list = []
  with open(DEVICES_SETTING_PATH, 'r') as f:
    devices = json.loads(f.read())
    for device in devices:
      if platform:
        if platform == device['platformName'].lower():
          id_list.append(device['udid'])
      else:
        id_list.append(device['udid'])
  return id_list

def device_capabilities(device_id, platform=None):
  with open(DEVICES_SETTING_PATH, 'r') as f:
    devices = json.loads(f.read())
    d = []
    for device in devices:
      if device_id == device['udid']:
        if platform:
          if platform.lower() == device['platformName'].lower():
            d.append(device)
    return d[0]
  return None

