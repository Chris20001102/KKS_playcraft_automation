# -*- coding: UTF-8 -*-
import pytest
import sys
from pages.base import Base_Page
from appium import webdriver

sys.path.append(pytest.test_root)

class Module_Page(Base_Page):
  locator = {
    'network_alert': ('xpath', '(//XCUIElementTypeAlert[@name="“KKSPaaSSample” would like to find and connect to devices on your local network."]'),
    'bluetooth_alert': ('xpath', '//XCUIElementTypeAlert[@name="“KKSPaaSSample” Would Like to Use Bluetooth"]'),
    'alert_ok_button': ('accessibility id', 'OK'),
    'premium_plus': ('accessibility id', 'lightweight_demo'),
    'premium': ('accessibility id', 'playcraft_demo'),
    'core_player': ('accessibility id', 'blendvision_demo'),
    'app_setting': ('accessibility id', 'App Setting')
  }
  def click_premium_plus_button(self):
      self.click(self.locator['premium_plus'], timeout=1)

  def click_premium_button(self):
      self.click(self.locator['premium'], timeout=1)

  def click_core_player_button(self):
        self.click(self.locator['core_player'], timeout=1)
    
  def click_app_setting_button(self):
        self.click(self.locator['app_setting'], timeout=1) 