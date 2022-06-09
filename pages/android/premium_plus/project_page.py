# -*- coding: UTF-8 -*-
import logging
import pytest
import sys
from pages.base import Base_Page
from appium import webdriver

sys.path.append(pytest.test_root)

class Project_Page(Base_Page):
    locator = {
    'saku_button': ('id', 'com.kkstream.android.ottfs.playerservice:id/btn_saku_demo'),
    'blendvision_kaleido': ('id', 'com.kkstream.android.ottfs.playerservice:id/btn_bvtv_demo')
  }
  
    def click_saku_button(self):
        self.click(self.locator['saku_button'], timeout=1)

    def click_blendvision_kaleido_button(self):
        self.click(self.locator['blendvision_kaleido'], timeout=1)