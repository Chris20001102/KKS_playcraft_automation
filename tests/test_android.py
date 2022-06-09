# -*- coding: UTF-8 -*-
import logging
import os
import pytest
import sys
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# /Users/chuanhuihuang/Documents/Player/Automation/pass-sample-auto/tests/test_android.py  
# /Users/chuanhuihuang/Documents/Player/Automation/pass-sample-auto/tests
# /Users/chuanhuihuang/Documents/Player/Automation/pass-sample-auto
# sys.path Let Python know where the file is, so that you can find the file import later

from appium import webdriver
from datetime import datetime, timedelta
from pytest_testrail.plugin import pytestrail
from pages.android.module_page import Module_Page
from pages.android.premium_plus.project_page import Project_Page
from pages.android.premium_plus.saku_page import Saku_Page
from pages.android.setting_page import Setting_Page
from pages.android.premium_plus.choose_page import Choose_Page
from pages.android.premium_plus.download_page import Download_Page
from pages.android.premium_plus.videos_page import Videos_Page

HIDE_CONTROL_PANEL_SECONDS = 3
END_ROLL_COUNT_TIME = 10 

# Test Account
TEST_USER_ID = '41'
TEST_ACCESS_TOKEN = 'android+automation@kkstream.com'
TEST_DEVICE_ID = 'android_automation_test'

#Content Title
CONTENT_TITLE_4 = "Tears of Steel - Blender Foundation channel. Visit http://www.tearsofsteel.org for more information or downloads. All data for the film is available under Creative Commons Attribution."
CONTENT_TITLE_12 = "ターミネーター：ニュー・フェイト"
CONTENT_TITLE_13 = "ミニオンズ"
CONTENT_TITLE_14 = "忍野さら／Romance"

# Confirm that the client is connected to the driver
if not pytest.driver:
  raise Exception('WebDriver is not initialized.')
driver = pytest.driver

module_page = Module_Page(driver)
project_page = Project_Page(driver)
saku_page = Saku_Page(driver)
setting_page = Setting_Page(driver)
choose_page = Choose_Page(driver)
download_page = Download_Page(driver)
videos_page = Videos_Page(driver)

def setup_module():
  """ module setup """
  # logging.debug('module setup')

def teardown_module():
  """ module teardown """
  # logging.debug('module teardown')

def setup_function():
  # logging.debug('function setup')
  driver.launch_app()
  module_page.click_app_setting_button()
  setting_page.set_user_id(TEST_USER_ID)
  setting_page.set_device_id(TEST_DEVICE_ID)
  setting_page.scroll_up()
  if setting_page.auto_play_switch_on():
    setting_page.click_auto_play_switch()
  setting_page.click_enable_recommendation_panel_switch()
  setting_page.click_save_button()

def teardown_function():
  logging.debug('function teardown')
  logging.info('Verify complete')
  driver.close_app()

def play_vod_content(content_id):
  module_page.click_premium_plus_button()
  project_page.click_saku_button()
  saku_page.click_video_type_button()
  choose_page.set_content_id(content_id)
  choose_page.click_play_video_button()
  wait_loading()
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)

def play_live_content(content_id):
  saku_page.click_video_type_button()
  choose_page.set_content_id(content_id)
  choose_page.click_video_type_spinner()
  choose_page.click_video_type_lives()
  choose_page.click_play_video_button()
  wait_loading()
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)

def position_to_seconds(position):
  [m, n] = position.split(':')
  return int(m) * 60 + int(n)

def wait_loading(seconds=30):
  timeout = datetime.now() + timedelta(seconds=seconds)           # 現在時間+時差(30s) = Timeout 
  logging.info('wait loading timeout: {}'.format(timeout))        # wait loading timeout: 2021-02-17 HH:MM:SS.217544
  while(videos_page.is_loading()):                                # 先判斷目前是否在Loading
    if datetime.now() >= timeout:
      break
    logging.info('video is loading...')                           # datetime.now() >= timeout 還沒成立前顯示
    time.sleep(0.2)

@pytest.mark.test_platform('android')
@pytestrail.case('C1038936')
def test_series_content_ui():
  play_vod_content(13)
  videos_page.show_control_panel()                                
  videos_page.click_pause_button()                               
  assert videos_page.control_panel_is_visible()
  assert videos_page.back_button_is_visible()
  assert videos_page.title() == CONTENT_TITLE_13
  assert videos_page.episode_list_is_visible()
  assert videos_page.setting_button_is_visible()
  assert videos_page.rewind_button_is_visible()
  assert videos_page.forward_button_is_visible()
  assert videos_page.previous_button_is_visible()
  assert videos_page.next_button_is_visible()
  assert videos_page.play_button_is_visible()
  assert videos_page.position()
  assert videos_page.duration()
  assert videos_page.seekbar_is_visible()
  assert videos_page.recommendation_bar_is_visible()

@pytest.mark.test_platform('android')
@pytestrail.case('C1038937')
def test_single_content_ui():
  play_vod_content(4)
  videos_page.show_control_panel()
  videos_page.click_pause_button()
  assert videos_page.control_panel_is_visible()
  assert videos_page.back_button_is_visible()
  assert videos_page.title() == CONTENT_TITLE_4
  assert videos_page.episode_list_is_visible()
  assert videos_page.setting_button_is_visible()
  assert videos_page.rewind_button_is_visible()
  assert videos_page.forward_button_is_visible()
  assert videos_page.previous_button_is_visible() is False
  assert videos_page.next_button_is_visible() is False
  assert videos_page.play_button_is_visible()
  assert videos_page.position()
  assert videos_page.duration()
  assert videos_page.seekbar_is_visible()
  time.sleep(10)
  assert videos_page.recommendation_bar_is_visible()

@pytest.mark.test_platform('android')
@pytestrail.case('C1038938')
def test_control_panel_behavior():
  module_page.click_premium_plus_button()
  project_page.click_saku_button()
  saku_page.click_video_type_button()
  choose_page.set_content_id(12)
  choose_page.click_play_video_button()
  assert videos_page.control_panel_is_visible()
  wait_loading()
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)
  assert videos_page.control_panel_is_visible() is False
  videos_page.click_player_view()
  assert videos_page.control_panel_is_visible()
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)
  assert videos_page.control_panel_is_visible() is False

@pytest.mark.test_platform('android')
@pytestrail.case('C1038939')
def test_play_pause():
  play_vod_content(12)
  videos_page.show_control_panel()
  videos_page.click_pause_button()
  videos_page.vod_playback_is_pause()
  videos_page.click_play_button()
  videos_page.vod_playback_is_playing()

@pytest.mark.test_platform('android')
@pytestrail.case('C1038940')
def test_forward_rewind_play():
  play_vod_content(12)
  videos_page.click_forward_button()
  videos_page.click_rewind_button()
  videos_page.vod_playback_is_playing()

@pytest.mark.test_platform('android')
@pytestrail.case('C1038941')
def test_forward_rewind_pause():
  play_vod_content(13)
  videos_page.show_control_panel()
  videos_page.click_pause_button()
  last_position = videos_page.vod_convert_position_to_seconds()
  videos_page.click_forward_button() 
  now_position = videos_page.vod_convert_position_to_seconds()
  assert now_position - last_position == 10

  time.sleep(HIDE_CONTROL_PANEL_SECONDS)
  videos_page.show_control_panel()
  last_position = videos_page.vod_convert_position_to_seconds()
  videos_page.click_rewind_button()
  now_position = videos_page.vod_convert_position_to_seconds()
  assert last_position - now_position == 10  
  
@pytest.mark.test_platform('android')
@pytestrail.case('C1038942')
def test_next_previous_play():
  play_vod_content(12)
  videos_page.show_control_panel()
  assert videos_page.title() == CONTENT_TITLE_12
  videos_page.show_control_panel()
  assert videos_page.previous_button_is_visible() is False
  videos_page.show_control_panel()
  assert videos_page.next_button_is_visible()
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)

  videos_page.show_control_panel()
  videos_page.click_next_button()
  wait_loading()
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)

  videos_page.show_control_panel()
  assert videos_page.title() == CONTENT_TITLE_13
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)
  videos_page.show_control_panel()
  assert videos_page.previous_button_is_visible()
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)
  videos_page.show_control_panel()
  assert videos_page.next_button_is_visible()
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)

  videos_page.show_control_panel()
  videos_page.click_next_button()
  wait_loading()
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)

  videos_page.show_control_panel()
  assert videos_page.title() == CONTENT_TITLE_14
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)
  videos_page.show_control_panel()
  assert videos_page.previous_button_is_visible()
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)
  videos_page.show_control_panel()
  assert videos_page.next_button_is_visible() is False

@pytest.mark.test_platform('android')
@pytestrail.case('C1038942')
def test_next_previous_pause():
  play_vod_content(12)
  videos_page.show_control_panel()
  assert videos_page.title() == CONTENT_TITLE_12
  videos_page.show_control_panel()
  assert videos_page.previous_button_is_visible() is False
  videos_page.show_control_panel()
  assert videos_page.next_button_is_visible()
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)
  videos_page.show_control_panel()
  videos_page.click_pause_button()
  videos_page.click_next_button()
  wait_loading()
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)

  videos_page.show_control_panel()
  assert videos_page.title() == CONTENT_TITLE_13
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)
  videos_page.show_control_panel()
  assert videos_page.previous_button_is_visible()
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)
  videos_page.show_control_panel()
  assert videos_page.next_button_is_visible()
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)
  videos_page.show_control_panel()
  videos_page.click_pause_button()
  videos_page.click_next_button()
  wait_loading()
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)

  videos_page.show_control_panel()
  assert videos_page.title() == CONTENT_TITLE_14
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)
  videos_page.show_control_panel()
  assert videos_page.previous_button_is_visible()
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)
  videos_page.show_control_panel()
  assert videos_page.next_button_is_visible() is False
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)

@pytest.mark.test_platform('android')
@pytestrail.case('C1038946')
def test_seek_progress_bar_with_vod():
  play_vod_content(12)
  videos_page.show_control_panel()
  videos_page.seek_video(0,0.2)
  videos_page.vod_playback_is_playing()
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)

  # Change player state: Playing -> Pausing
  videos_page.show_control_panel()
  videos_page.click_pause_button()
  videos_page.seek_video(0.5,0)
  videos_page.vod_playback_is_playing()

@pytest.mark.test_platform('android')
@pytestrail.case('C1038944')
def test_rotate_screen():
  play_vod_content(12)
  driver.orientation = "LANDSCAPE"
  assert videos_page.vod_playback_is_playing()
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)
  driver.orientation = "PORTRAIT"
  assert videos_page.vod_playback_is_playing()
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)

  videos_page.show_control_panel()
  videos_page.click_pause_button()
  driver.orientation = "LANDSCAPE"
  assert videos_page.vod_playback_is_pause() 
  driver.orientation = "PORTRAIT"
  assert videos_page.vod_playback_is_pause() 

@pytest.mark.test_platform('android')
@pytestrail.case('C1038945')
def test_rotate_screen_detail():
  driver.orientation = "LANDSCAPE"
  module_page.click_premium_plus_button()
  project_page.click_saku_button()
  saku_page.click_video_type_button()
  choose_page.set_content_id(12)
  choose_page.choose_page_scroll_up()
  choose_page.click_play_video_button()
  wait_loading()
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)


  assert videos_page.vod_playback_is_playing()
  driver.orientation = "PORTRAIT"
  assert videos_page.vod_playback_is_playing()
  driver.orientation = "LANDSCAPE"
  assert videos_page.vod_playback_is_playing()

  time.sleep(HIDE_CONTROL_PANEL_SECONDS)
  videos_page.show_control_panel()
  videos_page.click_pause_button()
  assert videos_page.vod_playback_is_pause() 
  driver.orientation = "PORTRAIT"
  assert videos_page.vod_playback_is_pause() 
  driver.orientation = "LANDSCAPE"
  assert videos_page.vod_playback_is_pause()  

@pytest.mark.test_platform('android')
@pytestrail.case('C1038949')
def test_replay_button_with_vod():
  saku_page.click_app_setting_button()
  setting_page.scroll_up()
  if setting_page.enable_recommendation_panel_switch_on():
    setting_page.click_enable_recommendation_panel_switch()
  setting_page.click_save_button()

  play_vod_content(12)
  videos_page.show_control_panel()
  videos_page.seek_video(0,1)
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)
  assert videos_page.replay_button_is_visible()
  videos_page.click_replay_button()
  wait_loading()
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)

  videos_page.show_control_panel()
  position = videos_page.position()
  logging.info('position:{}'.format(position))
  assert position_to_seconds(position) < 10

@pytest.mark.test_platform('android')
@pytestrail.case('C1038952')
def test_recommendation_panel_with_vod():
  saku_page.click_app_setting_button()
  setting_page.scroll_up()
  if not setting_page.enable_recommendation_panel_switch_on():
     setting_page.click_enable_recommendation_panel_switch()
  setting_page.click_save_button()

  play_vod_content(13)
  videos_page.show_control_panel()
  assert videos_page.recommendation_bar_is_visible()
  videos_page.click_recommendation_bar()
  videos_page.verify_recommendation_panel_is_expanded()
  videos_page.swipe_down_recommendation_panel()
  assert videos_page.control_panel_is_visible()

@pytest.mark.test_platform('android')
@pytestrail.case('C1038951')
def test_autoplay_with_episode_content():
  saku_page.click_app_setting_button()
  setting_page.scroll_up()
  setting_page.click_auto_play_switch()
  setting_page.click_save_button()

  play_vod_content(12)
  videos_page.show_control_panel()
  videos_page.seek_video(0,1)
  time.sleep(END_ROLL_COUNT_TIME)
  wait_loading()
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)

  videos_page.show_control_panel()
  assert videos_page.title() == CONTENT_TITLE_13
  assert videos_page.pause_button_is_visible()
  videos_page.vod_playback_is_playing()

@pytest.mark.test_platform('android')
@pytestrail.case('C1038950')
def test_autoplay_with_single_content():
  saku_page.click_app_setting_button()
  setting_page.scroll_up()
  setting_page.click_auto_play_switch()
  setting_page.click_save_button()

  play_vod_content(4)
  videos_page.show_control_panel()
  videos_page.seek_video(0,1)
  assert not videos_page.end_roll_dialog_is_visible()
  assert videos_page.recommendation_bar_is_visible()
  videos_page.swipe_down_recommendation_panel()
  assert videos_page.replay_button_is_visible()

@pytest.mark.test_platform('android')
@pytestrail.case('')
def test_autoplay_in_settings():
  play_vod_content(12)
  videos_page.show_control_panel()
  videos_page.click_setting_button()
  videos_page.click_auto_play_switch()
  videos_page.click_dismiss_setting_panel()
  videos_page.seek_video(0,1)
  videos_page.click_end_roll_dialog_thumbnail()
  wait_loading()
  assert videos_page.title() == CONTENT_TITLE_13

@pytest.mark.test_platform('android')
@pytestrail.case('C1038954')
def test_end_roll_dialog_ui():
  saku_page.click_app_setting_button()
  setting_page.scroll_up()
  setting_page.click_auto_play_switch()
  setting_page.click_save_button()

  play_vod_content(12)
  videos_page.show_control_panel()
  videos_page.seek_video(0,1)
  assert videos_page.end_roll_dialog_is_visible()
  assert videos_page.end_roll_thumbnail_is_visible()
  assert videos_page.end_roll_play_button_is_visible()
  assert videos_page.end_roll_timer_title_is_visible()
  assert videos_page.end_roll_title() == CONTENT_TITLE_13
  assert videos_page.end_roll_close_button_is_visible()

@pytest.mark.test_platform('android')
@pytestrail.case('C1038955')
def test_click_end_roll_dialog():
  saku_page.click_app_setting_button()
  setting_page.scroll_up()
  setting_page.click_auto_play_switch()
  setting_page.click_save_button()

  play_vod_content(12)
  videos_page.show_control_panel()
  videos_page.seek_video(0,1)
  time.sleep(1)
  videos_page.click_end_roll_play_button()
  wait_loading()
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)

  videos_page.show_control_panel()
  assert videos_page.title() == CONTENT_TITLE_13
  assert videos_page.control_panel_is_visible()
  videos_page.vod_playback_is_playing()
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)

  videos_page.show_control_panel()
  videos_page.seek_video(0,1)
  videos_page.click_end_roll_dialog_thumbnail()
  wait_loading()
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)

  videos_page.show_control_panel()
  assert videos_page.title() == CONTENT_TITLE_14
  assert videos_page.control_panel_is_visible()
  videos_page.vod_playback_is_playing()

@pytest.mark.test_platform('android')
@pytestrail.case('C1038956')
def test_close_end_roll_dialog():
  saku_page.click_app_setting_button()
  setting_page.scroll_up()
  setting_page.click_auto_play_switch()
  setting_page.click_save_button()

  play_vod_content(12)
  videos_page.show_control_panel()
  videos_page.seek_video(0,1)
  assert videos_page.end_roll_dialog_is_visible()
  time.sleep(1)
  videos_page.click_close_roll_dialog()
  assert not videos_page.end_roll_dialog_is_visible()
  videos_page.swipe_down_recommendation_panel()
  assert videos_page.replay_button_is_visible()

@pytest.mark.test_platform('android')
@pytestrail.case('')
def test_end_begin_time():
  saku_page.click_app_setting_button()
  setting_page.scroll_up()
  setting_page.click_auto_play_switch()
  setting_page.click_save_button()

  play_vod_content(12)
  videos_page.show_control_panel()
  videos_page.seek_video(0,1)
  assert videos_page.end_roll_dialog_is_visible()
  videos_page.click_end_roll_play_button()
  wait_loading()
  assert videos_page.title() == CONTENT_TITLE_13

@pytest.mark.test_platform('android')
@pytestrail.case('')
def test_action_button_function():
  play_vod_content(12)
  videos_page.show_control_panel()
  videos_page.click_pause_button()
  videos_page.click_play_button()
  videos_page.click_forward_button()
  videos_page.click_rewind_button()
  videos_page.click_next_button()
  wait_loading()
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)
  videos_page.show_control_panel()
  videos_page.click_previous_button()
  wait_loading()
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)
  videos_page.show_control_panel()
  videos_page.seek_video(0,1)
  videos_page.swipe_down_recommendation_panel()
  videos_page.click_replay_button()
  wait_loading()
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)
  videos_page.vod_playback_is_playing()

######## For Live case ##################################

@pytest.mark.test_platform('android')
@pytestrail.case('C1115825')
def test_live_content_ui():
  play_live_content(1)
  videos_page.show_control_panel()
  videos_page.click_pause_button()
  assert videos_page.play_button_is_visible()
  assert videos_page.back_button_is_visible() 
  assert videos_page.live_title()
  assert videos_page.live_time()
  assert videos_page.live_subtitle() 
  assert videos_page.setting_button_is_visible()
  assert videos_page.episode_list_is_visible()
  assert videos_page.rewind_button_is_visible() is False
  assert videos_page.forward_button_is_visible() is False
  assert videos_page.previous_button_is_visible() is False
  assert videos_page.next_button_is_visible() is False
  assert videos_page.live_position()
  assert videos_page.live_duration()
  assert videos_page.seekbar_is_visible()
  assert videos_page.recommendation_bar_is_visible()

@pytest.mark.test_platform('android')
@pytestrail.case('C1115917')
def test_live_play_pause_button():
  play_live_content(1)
  videos_page.show_control_panel()
  videos_page.click_pause_button()
  videos_page.play_button_is_visible()
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)
  videos_page.click_play_button()
  videos_page.pause_button_is_visible()
  videos_page.live_playback_is_playing()

@pytest.mark.test_platform('android')
@pytestrail.case('1118742')
def test_lives_rotate_screen():
  play_live_content(1)
  driver.orientation = "LANDSCAPE"
  assert videos_page.live_playback_is_playing()
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)
  driver.orientation = "PORTRAIT"
  assert videos_page.live_playback_is_playing()
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)

  videos_page.show_control_panel()
  videos_page.click_pause_button()
  driver.orientation = "LANDSCAPE"
  assert videos_page.live_playback_is_pause() 
  driver.orientation = "PORTRAIT"
  assert videos_page.live_playback_is_pause() 

@pytest.mark.test_platform('android')
@pytestrail.case('1118743')
def test_live_rotate_screen_detail():
  driver.orientation = "LANDSCAPE"
  saku_page.click_video_type_button()
  choose_page.set_content_id(1)
  choose_page.click_video_type_spinner()
  choose_page.click_video_type_lives()
  choose_page.choose_page_scroll_up()
  choose_page.click_play_video_button()
  wait_loading()
  time.sleep(HIDE_CONTROL_PANEL_SECONDS)

  assert videos_page.live_playback_is_playing()
  driver.orientation = "PORTRAIT"
  assert videos_page.live_playback_is_playing()
  driver.orientation = "LANDSCAPE"
  assert videos_page.live_playback_is_playing()

  time.sleep(HIDE_CONTROL_PANEL_SECONDS)
  videos_page.show_control_panel()
  videos_page.click_pause_button()
  assert videos_page.live_playback_is_pause() 
  driver.orientation = "PORTRAIT"
  assert videos_page.live_playback_is_pause() 
  driver.orientation = "LANDSCAPE"
  assert videos_page.live_playback_is_pause() 