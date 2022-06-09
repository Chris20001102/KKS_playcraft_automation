# -*- coding: UTF-8 -*-
import os, sys
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.base import Base_Page
from appium import webdriver

class Setting_Page(Base_Page):
  locator = {
    'back_button': ('accessibility id', 'Playcraft Version： 1.7.11 (Develop)'),
    'content_id': ('accessibility id', 'avc_itemContentId'),
    'content_text':('xpath', '//XCUIElementTypeApplication[@name=\"KKSPaaSSample\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField'),
    'clear_text':('accessibility id', 'Clear text'),
    'submit_button':('accessibility id', 'submitButton'),
    'auto_play_switch':('accessibility id', 'avc_itemAutoplay'),
    'thumbnail_seeking_switch':('accessibility id', 'avc_itemThumbnailSeeking'),
    'recommendation_switch':('accessibility id', 'avc_itemRecommend'),
  }

  def back_button(self):
    return self.exists(self.locator['back_button'])

  def back_button_is_visible(self):
    return self.is_visible(self.locator['back_button'])

  def click_back_button(self):
    self.click(self.locator['back_button'])

  def click_content_id(self):
    self.click(self.locator['content_id'])
    time.sleep(1)
  
  def set_content_id(self, value):
    return self.set_text(self.locator['content_text'], value)
  
  def click_submit_button(self):
    self.click(self.locator['submit_button'])

  def click_auto_play_switch(self):
    self.click(self.locator['auto_play_switch'])
  
  def click_thumbnail_seeking_switch(self):
    self.click(self.locator['thumbnail_seeking_switch'])

  def click_recommendation_switch(self):
    self.click(self.locator['recommendation_switch'])