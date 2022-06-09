# -*- coding: UTF-8 -*-
import pytest
import sys
sys.path.append(pytest.test_root)

from pages.base import Base_Page
from appium import webdriver

locator = {
    'content_id': ('id', 'com.kkstream.android.ottfs.playerservice:id/content_id_input'),
    'download_list_button': ('id', 'com.kkstream.android.ottfs.playerservice:id/btn_download_List'),
    'download_button': ('id', 'com.kkstream.android.ottfs.playerservice:id/btn_download'),
    'cancel_button': ('id', 'android:id/button2',)
  }

class Download_Page(Base_Page):
  def set_content_id(self, id):
    self.set_text(locator['content_id'], id)

  def click_download_list_button(self):
    self.click(self.locator['download_list_button'])

  def click_download_button(self):
    self.click(self.locator['download_button'])

  def click_cancel_button(self):
    self.click(self.locator['cancel_button'])