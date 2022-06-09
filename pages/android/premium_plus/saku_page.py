# -*- coding: UTF-8 -*-
import pytest
import sys
sys.path.append(pytest.test_root)

from pages.base import Base_Page
from appium import webdriver

class Saku_Page(Base_Page):
  locator = {
    'video_type_button': ('id', 'com.kkstream.android.ottfs.playerservice:id/btn_mock_choose_video_type'),
    'download_item_button': ('id', 'com.kkstream.android.ottfs.playerservice:id/btn_download_items_button'),
  }

  def click_video_type_button(self):
    self.click(self.locator['video_type_button'], timeout=1)
  
  def click_download_item_button(self):
    self.click(self.locator['download_item_button'], timoeout=1)