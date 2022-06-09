# -*- coding: UTF-8 -*-
import pytest
import sys
import time
sys.path.append(pytest.test_root)

from pages.base import Base_Page
from appium import webdriver

locator = { 
  'content_id': ('id', 'com.kkstream.android.ottfs.playerservice:id/content_id_input'),
  'video_type_spinner': ('id', 'com.kkstream.android.ottfs.playerservice:id/video_type_spinner'),
  'media_source_type_text': ('id', 'com.kkstream.android.ottfs.playerservice:id/media_source_type_text'),
  'media_source_type_spinner': ('id', 'com.kkstream.android.ottfs.playerservice:id/media_source_type_spinner'),
  'video_type_videos': ('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[1]'),
  'video_type_lives': ('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]'),
  'mediaSourceTypeText': ('id', 'com.kkstream.android.ottfs.playerservice:id/media_source_type_text'),
  'media_source_type_null': ('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[1]'),
  'media_source_type_subtitle': ('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]'),
  'media_source_type_dubbed': ('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[3]'),
  'switch_auto_load_option': ('id', 'com.kkstream.android.ottfs.playerservice:id/sw_should_auto_load'),
  'play_video_button': ('id', 'com.kkstream.android.ottfs.playerservice:id/play_video_button'),
  'alert_message': ('id', 'android:id/message'),
  'alert_ok_button': ('id', 'android:id/button1')
}

class Choose_Page(Base_Page):
  def set_content_id(self, id):
    self.set_text(locator['content_id'], id)

  def click_play_video_button(self):
    self.click(locator['play_video_button'])
    time.sleep(0.5)

  def click_video_type_spinner(self):
    self.click(locator['video_type_spinner'])
    time.sleep(0.5)

  def click_video_type_videos(self):
    self.click(locator['video_type_videos'])

  def click_video_type_lives(self):
    self.click(locator['video_type_lives'])

  def click_media_source_type_spinner(self):
    self.click(locator['media_source_type_spinner'])
    time.sleep(0.5)
  
  def click_media_source_type_null(self):
    self.click(locator['media_source_type_null'])
  
  def click_media_source_type_subtitle(self):
    return self.click(locator['media_source_type_subtitle'])
  
  def click_media_source_type_dubbed(self):
    return self.click(locator['media_source_type_dubbed'])

  def alert_exists(self):
    return self.exists(locator['alert'])
  
  def get_alert_message(self):
    return self.get_value(locator['alert_message'])
  
  def click_alert_ok_button(self):
    return self.click(locator['alert_ok_button'])

  def choose_page_scroll_up(self):
    rect1 = self.rect(locator['media_source_type_text'])
    rect2 = self.rect(locator['content_id'])
    win_size = self.driver.get_window_size()
    from_ = [(win_size['width']/2), rect1['y']]
    to = [(win_size['width']-2), rect2['y']]
    self.swipe(from_, to)
  
  # def video_type_list(self):
  #   self.click_video_type_spinner()
  #   self.click_video_type_videos()
    # element = self._find_element(locator['video_type_videos'])
    # print(element)
    # elements = self.driver.find_elements(*locator['video_type_videos'])
    # elements = self.find_elements(locator['video_type_videos'])
    # print(elements)
    # print(type(elements))
    # type_list = []
    # i = 0
    # for i in range(len(elements)):
    #   element = elements[i]
    # # for element in elements:
    #   text = element.get_attribute('text')
    #   print(text)
    #   type_list.append(text)
    #   i = i + 1
    
    # return type_list