# -*- coding: UTF-8 -*-
import pytest
import os, sys
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.base import Base_Page
from appium import webdriver

class Playcraft_Page(Base_Page):
  locator = {
    'back_button': ('accessibility id', 'Premium+'),
    'video_button': ('accessibility id', 'ptvc_itemVideo'),
    'live_button': ('accessibility id', 'ptvc_itemLives'),
    'download_button': ('accessibility id', 'ptvc_itemOffline'),
  }

  def edit_button_exists(self):
    return self.exists(self.locator['edit_button'])

  def edit_button_is_visible(self):
    return self.is_visible(self.locator['edit_button'])

  def click_edit_button(self):
    self.click(self.locator['edit_button'])
  
  def click_video_button(self):
    self.click(self.locator['video_button'])
    time.sleep(1)
  
  def click_live_button(self):
    self.click(self.locator['live_button'])
  
  def click_download_button(self):
    self.click(self.locator['download_button'])
  
  def click_download_phase2_button(self):
    self.click(self.locator['download_phase2_button'])

  def video_button_exist(self):
    return self.exists(self.locator['video_button'])

  def live_button_exist(self):
    return self.exists(self.locator['live_button'])

  def download_button_exist(self):
    return self.exists(self.locator['download_button'])
    
  def download_phase2_button_exist(self):
    return self.exists(self.locator['download_phase2_button'])