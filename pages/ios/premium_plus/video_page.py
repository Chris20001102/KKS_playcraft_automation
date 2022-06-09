# -*- coding: UTF-8 -*-
import logging
import pytest
import os, sys
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.base import Base_Page
from appium import webdriver

class Video_Page(Base_Page):
  # locator = ('accessibility id', 'editButtonItem')
  locator = {
    'player_view': ('accessibility id', 'pvc_backgroundViewId'),
    # 'control_panel': ('accessibility id', 'pvc_playbackControlPanelId'),
    'control_panel': ('xpath', '//XCUIElementTypeOther[@name="pvc_backgroundViewId"]/XCUIElementTypeOther/XCUIElementTypeOther[1]'),
    # Top_Controller
    'back_button': ('accessibility id', 'pvc_backButtonId'),
    'title': ('accessibility id', 'pvc_titleLabelId'),
    'airplay_button': ('accessibility id', 'AirPlay'),
    'chromecast_button': ('accessibility id', 'pvc_googlecastButtonId'),
    'episode_button': ('accessibility id', 'pvc_episodeButtonId'),
    'setting_button': ('accessibility id', 'pvc_settingButtonId'),
    # Mid_Controller
    # 'play_button': ('accessibility id', 'pvc_playPauseButtonId'),
    # 'pause_button': ('accessibility id', 'pvc_playPauseButtonId'),
    # 'rewind_button': ('accessibility id', 'pvc_skipBackwardButtonId'),
    # 'forward_button': ('accessibility id', 'pvc_skipForwardButtonId'),
    # 'next_button': ('accessibility id', 'pvc_nextEpisodeButtonId'),
    # 'previous_button': ('accessibility id', 'pvc_previousEpisodeButtonId'),
    'play_button': ('accessibility id', 'pvc_skipBackwardButtonId'),
    'pause_button': ('accessibility id', 'pvc_skipBackwardButtonId'),
    'rewind_button': ('accessibility id', 'pvc_skipForwardButtonId'),
    'forward_button': ('accessibility id', 'pvc_nextEpisodeButtonId'),
    'next_button': ('accessibility id', 'pvc_previousEpisodeButtonId'),
    'previous_button': ('accessibility id', 'pvc_playPauseButtonId'),
    'replay_button': ('accessibility id', 'pvc_playPauseButtonId'),
    'loading': ('accessibility id', 'pvc_busyActivityViewId'),
    'alert_view': ('accessibility id','pvc_alertViewId'),
    'play_this_quality_button': ('accessibility id', 'Play this Quality'),
    # Buttton_Controller
    'duration_time': ('accessibility id', 'pvc_currentTimeLableId'),
    'slider': ('accessibility id', 'pvc_progressBarId'),
    'total_time': ('accessibility id', 'pvc_totalTimeLabelId'),
    'recommendation_panel': ('accessibility id', 'pvc_recommandViewId'),
  }

  def vod_convert_position_to_seconds(self):
    self.show_control_panel()
    position = self.duration_time()
    logging.info('position1: {}'.format(position))
    [m,n] = position.split(':')
    position_time = int(m) * 60 + int(n)
    logging.info('position2: {}'.format(position_time))
    return position_time 

  def vod_playback_is_playing(self):
    self.show_control_panel()
    time1 = self.vod_convert_position_to_seconds()
    logging.info('position1: {}'.format(time1))
    time.sleep(3)
    self.show_control_panel()
    time2 = self.vod_convert_position_to_seconds()
    logging.info('position2: {}'.format(time2))
    return time2 > time1

  def vod_playback_is_pause(self):
    self.show_control_panel()
    time1 = self.vod_convert_position_to_seconds()
    logging.info('position1: {}'.format(time1))
    time.sleep(3)
    self.show_control_panel()
    time2 = self.vod_convert_position_to_seconds()
    logging.info('position2: {}'.format(time2))
    return time2 == time1
  
  # Get component value
  def title(self):
    return self.get_value(self.locator['title'])
  
  def duration_time(self):
    return self.get_label(self.locator['duration_time'])

  def total_time(self):
    return self.get_value(self.locator['total_time'])

  # Click function
  def click_player_view(self):
    player_view = self.exists(self.locator['player_view'])
    if player_view:
      logging.info('player view exists')
      player_view.click()
    else:
      logging.info('Cannot click player_view since it does not exist.')

  def click_back_button(self):
    self.click(self.locator['back_button'])

  def click_pause_button(self):
    self.click(self.locator['pause_button'])

  def click_play_button(self):
    self.click(self.locator['play_button'])
  
  def click_rewind_button(self):
    self.click(self.locator['rewind_button'])
  
  def click_forward_button(self):
    self.click(self.locator['forward_button'])
  
  def click_next_episode_button(self):
    self.click(self.locator['next_button'])
  
  def click_previous_episode_button(self):
    self.click(self.locator['previous_button'])

  def click_play_this_quality_button(self):
    self.click(self.locator['play_this_quality_button'])

  # Verify that the UI exists 
  def is_loading(self):
    if self.exists(self.locator['loading']):
      return True
    else:
      return False

  def show_control_panel(self):
    if not self.exists(self.locator['pause_button']):
      self.click_player_view()
  
  def control_panel_is_visible(self):
    return self.is_visible(self.locator['control_panel'])

  def back_button_is_visible(self):
    return self.is_visible(self.locator['back_button'])
  
  def title_is_visible(self):
    return self.is_visible(self.locator['title'])

  def airplay_button_is_visible(self):
    return self.is_visible(self.locator['airplay_button'])

  def episode_list_is_visible(self):
    return self.is_visible(self.locator['episode_button'])

  def setting_button_is_visible(self):
    return self.is_visible(self.locator['setting_button'])
  
  def rewind_button_is_visible(self):
    return self.is_visible(self.locator['rewind_button'])
  
  def forward_button_is_visible(self):
    return self.is_visible(self.locator['forward_button'])

  def previous_button_is_visible(self):
    self.show_control_panel()
    return self.is_visible(self.locator['previous_button'])

  def next_button_is_visible(self):
    self.show_control_panel()
    return self.is_visible(self.locator['next_button'])
  
  def pause_button_is_visible(self):
    return self.is_visible(self.locator['pause_button'])
  
  def play_button_is_visible(self):
    return self.is_visible(self.locator['play_button'])
  
  def seekbar_is_visible(self):
    return self.is_visible(self.locator['slider'])
  
  def duration_time_is_visible(self):
    return self.is_visible(self.locator['duration_time'])

  def total_time_is_visible(self):
    return self.is_visible(self.locator['total_time'])

  def recommendation_panel_is_visible(self):
    return self.is_visible(self.locator['recommendation_panel'])
  
  def replay_button_is_visible(self):
    return self.is_visible(self.locator['replay_button'])

  def end_roll_dialog_is_visible(self):
    return self.is_visible(self.locator['end_roll_panel'])
  
  def end_roll_thumbnail_is_visible(self):
    return self.is_visible(self.locator['end_roll_thumbnail'])
  
  def end_roll_play_button_is_visible(self):
    return self.is_visible(self.locator['end_roll_play_button'])

  def end_roll_timer_title_is_visible(self):
    return self.is_visible(self.locator['end_roll_timer_title'])

  def end_roll_close_button_is_visible(self):
    return self.is_visible(self.locator['end_roll_close_button'])
  
  def alert_view_is_visible(self):
    return self.is_visible(self.locator['alert_view'])