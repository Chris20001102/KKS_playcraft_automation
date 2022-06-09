# -*- coding: UTF-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from base import Base_Page
# from appium import webdriver
from selenium import webdriver

class Sample_Web(Base_Page):
  locator = {
    'apply_button': ('xpath', '//*[@id="app"]/form/div[1]/div/button'),
    'cast_receiver_app_id': ('id', 'Cast Receiver Application Id'),
    'license_id': ('id', 'License Key'),
    'host': ('id', 'Host'),
    'access_token': ('Access Token'),
    'device_id': ('id', 'Device Id'),
    'content_id': ('id', 'Content Id'),
    'play_button': ('css selector', 'kks-player__square-button kks-player__play-button kks-player__play-button--paused'),
    'current_time': ('xpath', '//*[@id="app"]/div[1]/div/div[2]/div[3]/div[1]/text()[1]'),
    'total_time': ('xpath', '//*[@id="app"]/div[1]/div/div[2]/div[3]/div[1]/text()[2]'),
    'slider': ('xpath', '//*[@id="app"]/div[1]/div/div[2]/div[3]/div[1]/div'),
    'forward': ('css selector', 'button[class*="kks-player__square-button kks-player__forward-button"]'),
    'rewind': ('css selector', 'button[class*="kks-player__square-button kks-player__rewind-button"]'),
    'setting_button': ('css selector', 'button[class*="kks-player__square-button kks-player__setting-button"]'),
    'pause_button': ('css selector', 'button[class*="kks-player__square-button kks-player__play-button kks-player__play-button--playing"]'),
    'error_back_button': ('css selector', 'button[class*="kks-player__text-button kks-player__error__back-button"]'),
    'reload_player_button': ('xpath', '//*[@id="app"]/button')
  }

  def click_apply_button(self):
    return self.click(self.locator['apply_button'])
  
  def set_content_id(self, content_id):
    return self.set_text(self.locator['content_id'], content_id)

  def click_play_button(self):
    return self.click(self.locator['play_button'])
  
  def error_back_button_exists(self):
    return self.exists(self.locator['error_back_button'])
  
  def click_error_back_button(self):
    return self.click(self.locator['error_back_button'])