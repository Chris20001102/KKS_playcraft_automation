# -*- coding: UTF-8 -*-
import pytest
import sys
from pages.base import Base_Page
from appium import webdriver

sys.path.append(pytest.test_root)

class Single_Item_Playback_Page(Base_Page):
  locator = {
    'play_button': ('accessibility id', 'TODO')
  }

  def click_play_button(self):
        self.click(self.locator['play_button'], timeout=1)