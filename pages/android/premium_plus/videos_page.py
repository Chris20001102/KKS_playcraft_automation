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
  'cast_button': ('id', 'com.kkstream.android.ottfs.playerservice:id/castButton'),
  'setting_button': ('id', 'com.kkstream.android.ottfs.playerservice:id/settingButton'),
  'episode_button': ('id', 'com.kkstream.android.ottfs.playerservice:id/iv_menu_sample'),
  # midControlPanel
  'loading': ('id', 'com.kkstream.android.ottfs.playerservice:id/loadingBar'),
  'rewind_button': ('id', 'com.kkstream.android.ottfs.playerservice:id/rewindButton'),
  'forward_button': ('id', 'com.kkstream.android.ottfs.playerservice:id/fastFowardButton'),
  'previous_button': ('id', 'com.kkstream.android.ottfs.playerservice:id/previousButton'),
  'next_button': ('id', 'com.kkstream.android.ottfs.playerservice:id/nextButton'),
  'play_button': ('id', 'com.kkstream.android.ottfs.playerservice:id/playButton'),
  'pause_button': ('id', 'com.kkstream.android.ottfs.playerservice:id/pauseButton'),
  'replay_button': ('id', 'com.kkstream.android.ottfs.playerservice:id/replayButton'),
  # botControlPanel
  'position': ('id', 'com.kkstream.android.ottfs.playerservice:id/mezzaninePosition'),
  'porgress_bar': ('id', 'com.kkstream.android.ottfs.playerservice:id/progressBar'),
  'duration': ('id', 'com.kkstream.android.ottfs.playerservice:id/mezzanineDuration'),
  'thumbnail': ('id', 'com.kkstream.android.ottfs.playerservice:id/thumbnailView'),
  'recommendation_bar': ('id', 'com.kkstream.android.ottfs.playerservice:id/rv_recommendation'),
  # Setting Panel
  'dismiss_setting_panel': ('id', 'com.kkstream.android.ottfs.playerservice:id/iv_back'),
  'setting_quality_options': ('id', 'com.kkstream.android.ottfs.playerservice:id/tv_quality_value'),
  'auto_play_option': ('id', 'com.kkstream.android.ottfs.playerservice:id/sc_auto_play'),
  # End Roll Dialog
  'end_roll_panel': ('id', 'com.kkstream.android.ottfs.playerservice:id/endRollPanel'),
  'end_roll_title': ('id', 'com.kkstream.android.ottfs.playerservice:id/tv_end_roll_content_title'),
  'end_roll_thumbnail': ('id', 'com.kkstream.android.ottfs.playerservice:id/endRollThumbnail'),
  'end_roll_play_button': ('id', 'com.kkstream.android.ottfs.playerservice:id/iv_endRollPlayButton'),
  'end_roll_timer_title': ('id', 'com.kkstream.android.ottfs.playerservice:id/tv_timer_title'),
  'end_roll_close_button': ('id', 'com.kkstream.android.ottfs.playerservice:id/endRollCloseButton')
}

class Videos_Page(Base_Page):
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
  
  def click_setting_quality_options(self):
    self.click(locator['setting_quality_options'])
    time.sleep(0.5)

  def click_quality_720p(self):
    self.find_element_by_accessibility_id('720p').click()  

  def click_setting_options(self, quality):
    elements = self.find_elements(locator['setting_options'])
    for element in elements:
      text = element.get_attribute('text')
      logging.info(text)
      if text == quality:
        element.click()
        logging.info('quality {} found and clicked'.format(quality))
        time.sleep(0.5)
        return
  
  def click_play_button(self):
    self.click(locator['play_button'])
  
  def click_pause_button(self):
    self.click(locator['pause_button'])
  
  def click_previous_button(self):
    self.click(locator['previous_button'])

  def click_next_button(self):
    self.click(locator['next_button'])

  def click_rewind_button(self):
    self.show_control_panel()
    self.click(locator['rewind_button'])

  def click_forward_button(self):
    self.show_control_panel()
    self.click(locator['forward_button'])

  def click_replay_button(self):
    self.click(locator['replay_button'])

  def click_recommendation_bar(self):
    self.click(locator['recommendation_bar'])
  
  def click_end_roll_play_button(self):
    self.click(locator['end_roll_play_button'])

  def click_end_roll_dialog_thumbnail(self):
    self.click(locator['end_roll_thumbnail'])
  
  def click_close_roll_dialog(self):
    self.click(locator['end_roll_close_button'])
  
  def click_dismiss_setting_panel(self):
    self.click(locator['dismiss_setting_panel'])
  
  def click_auto_play_switch(self):
    self.click(locator['auto_play_option'])

  def position(self):
    return self.get_text(locator['position'])

  def duration(self):
    return self.get_text(locator['duration'])

  def live_position(self):
    return self.get_text(locator['live_position'])

  def live_duration(self):
    return self.get_text(locator['live_duration'])

  def end_roll_title(self):
    return self.get_text(locator['end_roll_title'])

  # def click_play_button(self):
  #   return self.get_text(locator['title'])

  def seek_video(self,start_p,end_p):
    rect = self.rect(locator['porgress_bar']) #{'height': 78, 'width': 755, 'x': 143, 'y': 1926}
    if not rect:
       logging.info('No rect info')
       return 

    rect_x = rect['x'] # 143
    rect_y = rect['y'] # 1926 
    rect_width = rect['width']# 755

    x_start_offset = int(rect_width * start_p) # 0 
    x_end_offset = int(rect_width * end_p) # 1 

    from_ = [rect_x + x_start_offset, rect_y] # [143, 1926]
    to = [rect_x + x_end_offset, rect_y] # [898, 1926]
    self.swipe(from_,to)
      
  def live_title(self):
    return self.is_visible(locator['title'])
  
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
  
  def rewind_button_is_visible(self):
    return self.is_visible(locator['rewind_button'])
  
  def forward_button_is_visible(self):
    return self.is_visible(locator['forward_button'])

  def previous_button_is_visible(self):
    return self.is_visible(locator['previous_button'])
    # logging.info('previous_button visible: {}'.format(visible))
    # if visible:
    #   logging.info('click previous button since it is visible')
    #   self.click(locator['previous_button'])
    # return visible

  def next_button_is_visible(self):
    return self.is_visible(locator['next_button'])
    # logging.info('next_button visible: {}'.format(visible))
    # return visible
  
  def pause_button_is_visible(self):
    return self.is_visible(locator['pause_button'])
  
  def play_button_is_visible(self):
    return self.is_visible(locator['play_button'])
  
  def seekbar_is_visible(self):
    return self.is_visible(locator['porgress_bar'])

  def recommendation_bar_is_visible(self):
    return self.is_visible(locator['recommendation_bar'])
  
  def replay_button_is_visible(self):
    return self.is_visible(locator['replay_button'])

  def end_roll_dialog_is_visible(self):
    return self.is_visible(locator['end_roll_panel'])
  
  def end_roll_thumbnail_is_visible(self):
    return self.is_visible(locator['end_roll_thumbnail'])
  
  def end_roll_play_button_is_visible(self):
    return self.is_visible(locator['end_roll_play_button'])

  def end_roll_timer_title_is_visible(self):
    return self.is_visible(locator['end_roll_timer_title'])

  def end_roll_close_button_is_visible(self):
    return self.is_visible(locator['end_roll_close_button'])
  
  def vod_playback_is_playing(self):
    self.show_control_panel()
    time1 = self.vod_convert_position_to_seconds()
    time.sleep(3)
    self.show_control_panel()
    time2 = self.vod_convert_position_to_seconds()
    return time2 > time1 
    
  def vod_playback_is_pause(self):
    self.show_control_panel()
    time1 = self.vod_convert_position_to_seconds()
    time.sleep(3)
    self.show_control_panel()
    time2 = self.vod_convert_position_to_seconds()
    return time2 == time1 

  def vod_convert_position_to_seconds(self):
    self.show_control_panel()
    position = self.position()
    logging.info('position: {}'.format(position))
    [m, n] = position.split(':')
    position_time = int(m) * 60 + int(n)
    return position_time 

  def live_playback_is_playing(self):
    self.show_control_panel()
    time1 = self.live_convert_position_to_seconds()
    time.sleep(3)
    self.show_control_panel()
    time2 = self.live_convert_position_to_seconds()
    return time2 > time1 

  def live_playback_is_pause(self):
    self.show_control_panel()
    time1 = self.live_convert_position_to_seconds()
    time.sleep(3)
    self.show_control_panel()
    time2 = self.live_convert_position_to_seconds()
    return time2 == time1 
    
  def live_convert_position_to_seconds(self):
    self.show_control_panel()
    position = self.live_position()
    logging.info('live_position: {}'.format(position))
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