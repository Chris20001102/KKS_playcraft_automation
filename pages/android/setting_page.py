# -*- coding: UTF-8 -*-
import logging
import pytest
import sys
import time
sys.path.append(pytest.test_root)

from pages.base import Base_Page
from appium import webdriver

locator = {
  'playbackServerUrl': ('id', 'com.kkstream.android.ottfs.playerservice:id/playback_server_url'),
  'user_id': ('id', 'com.kkstream.android.ottfs.playerservice:id/user_id'),
  'access_token': ('id', 'com.kkstream.android.ottfs.playerservice:id/access_token'),
  'api_version': ('id', 'com.kkstream.android.ottfs.playerservice:id/api_version'),
  'device_id': ('id', 'com.kkstream.android.ottfs.playerservice:id/device_id'),
  'auto_play_switch': ('id', 'com.kkstream.android.ottfs.playerservice:id/auto_play'),
  'enable_recommendation_panel_switch': ('id', 'com.kkstream.android.ottfs.playerservice:id/enable_recommendation_panel'),
  'save_button': ('id', 'com.kkstream.android.ottfs.playerservice:id/btn_save'),
  'scroll_view': ('id', 'com.kkstream.android.ottfs.playerservice:id/scrollView')
}

class Setting_Page(Base_Page):
  def click_save_button(self):
    self.click(locator['save_button'])
    time.sleep(0.5)

  def auto_play_switch_on(self):
    return self.is_checked(locator['auto_play_switch'])

  def enable_recommendation_panel_switch_on(self):
    return self.is_checked(locator['enable_recommendation_panel_switch'])

  def click_auto_play_switch(self):
    self.click(locator['auto_play_switch'])
  
  def click_enable_recommendation_panel_switch(self):
    self.click(locator['enable_recommendation_panel_switch'])
  
  def set_user_id(self, value):
    return self.set_text(locator['user_id'], value)

  def set_access_token(self, value):
    return self.set_text(locator['access_token'], value)
  
  def set_device_id(self, value):
    return self.set_text(locator['device_id'], value)

  def scroll_up(self):
    rect1 = self.rect(locator['api_version'])
    rect2 = self.rect(locator['playbackServerUrl'])
    win_size = self.driver.get_window_size()
    from_ = [win_size['width']-10, rect1['y']]
    to = [win_size['width']-10, rect2['y']]
    self.swipe(from_, to)    