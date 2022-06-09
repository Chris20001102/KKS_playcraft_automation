# -*- coding: UTF-8 -*-
import logging
import os
import pytest
import sys
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from appium import webdriver
from datetime import datetime, timedelta
from pytest_testrail.plugin import pytestrail
from pages.ios.module_page import Module_Page
from pages.ios.premium_plus.project_page import Project_Page
from pages.ios.premium_plus.playcraft_page import Playcraft_Page
from pages.ios.setting_page import Setting_Page
from pages.ios.premium_plus.video_page import Video_Page
from pages.ios.premium_plus.live_page import Live_Page
from pages.ios.premium_plus.download_page import Download_Page
from pages.ios.premium.feature_demo_page import Feature_Demo_Page
from pages.ios.premium.single_Item_playback_page import Single_Item_Playback_Page
from pages.ios.premium.premium_video_page import Premium_Video_Page

HIDE_CONTROL_PANEL_SECONDS = 3
END_ROLL_COUNT_TIME = 10 

#Content Title
CONTENT_TITLE_4 = "Tears of Steel - Blender Foundation channel. Visit http://www.tearsofsteel.org for more information or downloads. All data for the film is available under Creative Commons Attribution."
CONTENT_TITLE_12 = "ターミネーター：ニュー・フェイト"
CONTENT_TITLE_13 = "ミニオンズ"
CONTENT_TITLE_14 = "忍野さら／Romance"

# Confirm that the client is connected to the driver
if not pytest.driver:
  raise Exception('WebDriver is not initialized.')
driver = pytest.driver

# driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)
module_page = Module_Page(driver)
project_page = Project_Page(driver)
playcraft_page = Playcraft_Page(driver)
setting_page = Setting_Page(driver)
video_page = Video_Page(driver)
live_page = Live_Page(driver)
download_page = Download_Page(driver)
feature_demo_page = Feature_Demo_Page(driver)
single_item_playback_page = Single_Item_Playback_Page(driver)
premium_video_page = Premium_Video_Page(driver)

def setup_module():
  logging.debug('module setup')

def teardown_module():
  logging.debug('module teardown')
  driver.close_app()

def setup_function():
  logging.info("function setup")
  driver.launch_app()

def teardown_function():
  logging.debug('function teardown')
  logging.info('Verify done!')
  driver.close_app()

def play_vod_content(content_id):
  module_page.click_app_setting_button()
  setting_page.click_content_id()
  setting_page.set_content_id(content_id)
  setting_page.click_submit_button()
  setting_page.click_thumbnail_seeking_switch()
  setting_page.click_recommendation_switch()
  setting_page.click_back_button()
  module_page.click_premium_plus_button()
  project_page.click_playcraft_demo_button()
  playcraft_page.click_video_button()
  if video_page.alert_view_is_visible():
    video_page.click_play_this_quality_button()
  wait_loading()
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)

def wait_loading(seconds=15):
  timeout = datetime.now() + timedelta(seconds=seconds)           
  logging.info('wait loading timeout: {}'.format(timeout))        
  while(video_page.is_loading()):                                
    if datetime.now() >= timeout:
      break
    logging.info('video is loading...')                           
    time.sleep(0.2)

@pytest.mark.test_platform('ios')
@pytestrail.case('C1038936')
def test_series_content_ui():
  play_vod_content(13)
  video_page.show_control_panel()
  video_page.click_pause_button()
  # assert video_page.control_panel_is_visible()
  assert video_page.back_button_is_visible()
  assert video_page.title_is_visible()
  assert video_page.episode_list_is_visible()
  assert video_page.setting_button_is_visible()
  assert video_page.rewind_button_is_visible()
  assert video_page.forward_button_is_visible()
  assert video_page.previous_button_is_visible()
  assert video_page.next_button_is_visible()
  assert video_page.play_button_is_visible()
  assert video_page.duration_time_is_visible()
  assert video_page.total_time_is_visible()
  assert video_page.seekbar_is_visible()
  assert video_page.recommendation_panel_is_visible()

@pytest.mark.test_platform('ios')
@pytestrail.case('C1038937')
def test_single_content_ui():
  play_vod_content(4)
  video_page.show_control_panel()
  video_page.click_pause_button()
  # assert video_page.control_panel_is_visible()
  assert video_page.back_button_is_visible()
  assert video_page.title_is_visible()
  assert video_page.episode_list_is_visible()
  assert video_page.setting_button_is_visible()
  assert video_page.rewind_button_is_visible()
  assert video_page.forward_button_is_visible()
  assert video_page.previous_button_is_visible() is False
  assert video_page.next_button_is_visible() is False
  assert video_page.play_button_is_visible()
  assert video_page.duration_time_is_visible()
  assert video_page.total_time_is_visible()
  assert video_page.seekbar_is_visible()
  assert video_page.recommendation_panel_is_visible()

@pytest.mark.test_platform('ios')
@pytestrail.case('C1038938')
def test_control_panel_behavior():
  play_vod_content(12)
  assert video_page.control_panel_is_visible() is False
  video_page.click_player_view()
  assert video_page.control_panel_is_visible()
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)
  assert video_page.control_panel_is_visible() is False
  video_page.click_player_view()
  video_page.click_pause_button()
  assert video_page.control_panel_is_visible()
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)
  assert video_page.control_panel_is_visible()

@pytest.mark.test_platform('ios')
@pytestrail.case('C1038939')
def test_play_pause():
  play_vod_content(12)
  if video_page.alert_view_is_visible():
    video_page.click_play_this_quality_button()
  wait_loading()
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)
  video_page.show_control_panel()
  assert video_page.pause_button_is_visible
  video_page.click_pause_button()
  assert video_page.vod_playback_is_pause()
  assert video_page.play_button_is_visible()
  video_page.click_play_button()
  assert video_page.vod_playback_is_playing()

@pytest.mark.test_platform('ios')
@pytestrail.case('C1038942')
def test_next_previous_play():
  play_vod_content(13)
  video_page.show_control_panel()
  assert video_page.title() == CONTENT_TITLE_13
  video_page.show_control_panel()
  assert video_page.previous_button_is_visible() 
  video_page.show_control_panel()
  assert video_page.next_button_is_visible()
  assert video_page.vod_playback_is_playing()

  video_page.show_control_panel()
  video_page.click_next_episode_button()
  if video_page.alert_view_is_visible():
    video_page.click_play_this_quality_button()
  wait_loading()

  video_page.show_control_panel()
  assert video_page.title() == CONTENT_TITLE_14
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)
  video_page.show_control_panel()
  assert video_page.previous_button_is_visible()
  video_page.show_control_panel()
  assert video_page.next_button_is_visible() is False
  assert video_page.vod_playback_is_playing()

  video_page.show_control_panel()
  video_page.click_previous_episode_button()
  if video_page.alert_view_is_visible():
    video_page.click_play_this_quality_button()
  wait_loading()

  video_page.show_control_panel()
  assert video_page.title() == CONTENT_TITLE_13
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)
  video_page.show_control_panel()
  assert video_page.previous_button_is_visible()
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)
  video_page.show_control_panel()
  assert video_page.next_button_is_visible() 
  video_page.show_control_panel()
  assert video_page.vod_playback_is_playing()
  
  video_page.show_control_panel()
  video_page.click_previous_episode_button()
  if video_page.alert_view_is_visible():
    video_page.click_play_this_quality_button()
  wait_loading()

  video_page.show_control_panel()
  assert video_page.title() == CONTENT_TITLE_12
  video_page.show_control_panel()
  assert video_page.previous_button_is_visible() is False
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)
  video_page.show_control_panel()
  assert video_page.next_button_is_visible() 
  assert video_page.vod_playback_is_playing()

@pytest.mark.test_platform('ios')
@pytestrail.case('C1038942')
def test_next_previous_pause():
  play_vod_content(13)
  video_page.show_control_panel()
  assert video_page.title() == CONTENT_TITLE_13
  video_page.show_control_panel()
  assert video_page.previous_button_is_visible() 
  video_page.show_control_panel()
  assert video_page.next_button_is_visible()
  assert video_page.vod_playback_is_playing()
  video_page.show_control_panel()
  video_page.click_pause_button()

  video_page.click_next_episode_button()
  if video_page.alert_view_is_visible():
    video_page.click_play_this_quality_button()
  wait_loading()

  video_page.show_control_panel()
  assert video_page.title() == CONTENT_TITLE_14
  video_page.show_control_panel()
  assert video_page.previous_button_is_visible()
  video_page.show_control_panel()
  assert video_page.next_button_is_visible() is False
  assert video_page.vod_playback_is_playing()
  video_page.show_control_panel()
  video_page.click_pause_button()

  video_page.show_control_panel()
  video_page.click_previous_episode_button()
  if video_page.alert_view_is_visible():
    video_page.click_play_this_quality_button()
  wait_loading()

  video_page.show_control_panel()
  assert video_page.title() == CONTENT_TITLE_13
  video_page.show_control_panel()
  assert video_page.previous_button_is_visible()
  video_page.show_control_panel()
  assert video_page.next_button_is_visible() 
  assert video_page.vod_playback_is_playing()
  video_page.show_control_panel()
  video_page.click_pause_button()

  video_page.show_control_panel()
  video_page.click_previous_episode_button()
  if video_page.alert_view_is_visible():
    video_page.click_play_this_quality_button()
  wait_loading()

  video_page.show_control_panel()
  assert video_page.title() == CONTENT_TITLE_12
  video_page.show_control_panel()
  assert video_page.previous_button_is_visible() is False
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)
  video_page.show_control_panel()
  assert video_page.next_button_is_visible() 
  video_page.show_control_panel()
  assert video_page.vod_playback_is_playing()

# @pytest.mark.test_platform('ios')
# @pytestrail.case('C1038942')
# def test_click_play_pause_bug():
#   module_page.click_premium_button()
#   feature_demo_page.click_single_item_playback_button()
#   single_item_playback_page.click_play_button()
#   # wait_loading()
#   time.sleep(2)
#   premium_video_page.click_play_pause_button()
#   premium_video_page.click_play_pause_button_many_time()
  
