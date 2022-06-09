# -*- coding: UTF-8 -*-
import pytest
import sys
from pages.base import Base_Page
from appium import webdriver

sys.path.append(pytest.test_root)

class Feature_Demo_Page(Base_Page):
  locator = {
    'single_item_playback': ('accessibility id', 'Single Item Playback')
  }
  
  def click_single_item_playback_button(self):
        self.click(self.locator['single_item_playback'], timeout=1)