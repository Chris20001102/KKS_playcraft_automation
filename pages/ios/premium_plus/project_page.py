# -*- coding: UTF-8 -*-
import os, sys
import pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(pytest.test_root)

from pages.base import Base_Page
from appium import webdriver

class Project_Page(Base_Page):
  locator = {
    'playcraft': ('accessibility id', 'Playcraft'),
    'blendvision_kaleido': ('accessibility id', 'BlendVision-Kaleido'),
  }

  def click_playcraft_demo_button(self):
    self.click(self.locator['playcraft'], timeout=1)

  def click_blendvision_kaleido_button(self):
    self.click(self.locator['blendvision_kaleido'], timeout=1)