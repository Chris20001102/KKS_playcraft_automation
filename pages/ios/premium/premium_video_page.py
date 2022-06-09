# -*- coding: UTF-8 -*-
import pytest
import sys
from pages.base import Base_Page
from appium import webdriver

sys.path.append(pytest.test_root)

class Premium_Video_Page(Base_Page):
  locator = {
    'play_pause_button': ('accessibility id', 'pvc_skipBackwardButtonId')
  }

  def click_play_pause_button(self):
        self.click(self.locator['play_pause_button'], timeout=1)

  def click_play_pause_button_many_time(self):
        i=0
        while i < 100 :
          self.click_play_pause_button()
          i = i + 1