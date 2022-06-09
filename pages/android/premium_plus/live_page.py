# -*- coding: UTF-8 -*-
import logging
import pytest
import sys
import time
sys.path.append(pytest.test_root)

from pages.base import Base_Page

locator = {
  # Control
  'control_panel': ('id', 'com.kkstream.android.ottfs.playerservice:id/controlPanel'),
  'player_view': ('id', 'com.kkstream.android.ottfs.playerservice:id/kksPlayerView'),
  # topControlPanel
  'back_button': ('id', 'com.kkstream.android.ottfs.playerservice:id/backButton'),
  'title': ('id', 'com.kkstream.android.ottfs.playerservice:id/title'),
  'subtitle': ('id', 'com.kkstream.android.ottfs.playerservice:id/subtitle'),
  'live_time': ('id', 'com.kkstream.android.ottfs.playerservice:id/time'),
  'cast_button': ('id', 'com.kkstream.android.ottfs.playerservice:id/castButton'),
  'setting_button': ('id', 'com.kkstream.android.ottfs.playerservice:id/settingButton'),
  'episode_button': ('id', 'com.kkstream.android.ottfs.playerservice:id/iv_menu_sample'),
  # midControlPanel
  'loading': ('id', 'com.kkstream.android.ottfs.playerservice:id/loadingBar'),
  'play_button': ('id', 'com.kkstream.android.ottfs.playerservice:id/playButton'),
  'pause_button': ('id', 'com.kkstream.android.ottfs.playerservice:id/pauseButton'),
  # botControlPanel
  'position': ('id', 'com.kkstream.android.ottfs.playerservice:id/videoPosition'),
  'porgress_bar': ('id', 'com.kkstream.android.ottfs.playerservice:id/progressBar'),
  'duration': ('id', 'com.kkstream.android.ottfs.playerservice:id/videoDuration'),  
  'recommendation_bar': ('id', 'com.kkstream.android.ottfs.playerservice:id/rv_recommendation'),
}

class Live_Page(Base_Page):
  def is_loading(self):
    if self.exists(locator['loading']):
      return True
    else:
      return False

  def click_player_view(self):
    player_view = self.exists(locator['player_view'])
    if player_view:
      logging.info('player view exists')
      player_view.click()
    else:
      logging.info('Cannot click player_view since it does not exist.')

  def show_control_panel(self):
    if not self.exists(locator['control_panel']):
      self.click_player_view()
  
  def hide_control_panel(self):
    if self.exists(locator['control_panel']):
      self.click_player_view()
  
  def title(self):
    return self.get_text(locator['title'])

  def click_setting_button(self):
    self.click(locator['setting_button'])
    time.sleep(0.5)

  def click_dismiss_setting_panel(self):
    self.click(locator['dismiss_setting_panel'])
  
  def click_play_button(self):
    self.click(locator['play_button'])
  
  def click_pause_button(self):
    self.click(locator['pause_button'])

  def click_recommendation_bar(self):
    self.click(locator['recommendation_bar'])

  def position(self):
    return self.get_text(locator['position'])

  def duration(self):
    return self.get_text(locator['duration'])

  def live_subtitle(self):
    return self.is_visible(locator['subtitle'])

  def live_time(self):
    return self.is_visible(locator['time'])

  def control_panel_is_visible(self):
    return self.is_visible(locator['control_panel'])
  
  def back_button_is_visible(self):
    return self.is_visible(locator['back_button'])

  def episode_list_is_visible(self):
    return self.is_visible(locator['episode_button'])

  def setting_button_is_visible(self):
    return self.is_visible(locator['setting_button'])
  
  def pause_button_is_visible(self):
    return self.is_visible(locator['pause_button'])
  
  def play_button_is_visible(self):
    return self.is_visible(locator['play_button'])
  
  def seekbar_is_visible(self):
    return self.is_visible(locator['porgress_bar'])

  def recommendation_bar_is_visible(self):
    return self.is_visible(locator['recommendation_bar'])
  
  def playback_is_playing(self):
    self.show_control_panel()
    time1 = self.vod_convert_position_to_seconds()
    time.sleep(3)
    self.show_control_panel()
    time2 = self.vod_convert_position_to_seconds()
    return time2 > time1 
    
  def playback_is_pause(self):
    self.show_control_panel()
    time1 = self.vod_convert_position_to_seconds()
    time.sleep(3)
    self.show_control_panel()
    time2 = self.vod_convert_position_to_seconds()
    return time2 == time1 

  def convert_position_to_seconds(self):
    self.show_control_panel()
    position = self.position()
    logging.info('position: {}'.format(position))
    [m, n] = position.split(':')
    position_time = int(m) * 60 + int(n)
    return position_time  

  def swipe_down_recommendation_panel(self):
    rect1 = self.rect(locator['recommendation_bar'])
    logging.info('{}'.format(rect1))
    tap_point = [(rect1['width']/2), rect1['y']-100]
    self.tap(tap_point) 
  
  def verify_recommendation_panel_is_expanded(self):
    assert self.recommendation_bar_is_visible()
    assert not self.pause_button_is_visible()