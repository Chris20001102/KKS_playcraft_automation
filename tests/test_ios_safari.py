# -*- coding: UTF-8 -*-
import logging
import os
import pytest
import sys
import time
import urllib
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from appium import webdriver
from pytest_testrail.plugin import pytestrail
from utils.dc import device_capabilities
from pages.web.sample_web import Sample_Web

host = 'https://playcraft-release.kksweb.vercel.app/player/'
params = {
  'licenseKey': r'"b22d1638-c775-436a-bca8-190560419369"',
  'lang': r'"en"',
  'autoPlay': r'"false"',
  'customHeader': r'"X-Device-Type: web"',
  'deviceId': r'"1"',
  'contentId': r'"2"',
  'host': r'"https://playcraft-release.kksweb.vercel.app/player/"',
  'accessToken': r'"paas12@gmail.com"',
  'contentType': r'"videos"',
  'thumbnailSeeking': r'"true"',
  'quality': r'"360p"',
  'appId': '"castreceiverappid"',
  'contentOther': r'"licenseId: 1"',
  'langCustomCode': r'"TEXT_CODE: text code\nERROR_MESSAGE_WITH_CODE: error message {CODE}"',
  'relatedPanel': r'true',
  'limitOnePlaybackAtSameTime': r'true',
  'supportEnvironmentList': r'"{\n  \"chrome\": \"chromebrowser\",\n  \"safari\": \"safaribrowser\"\n}"',
  'config': r'"{\n  \"conf\": \"play conf1\",\n  \"conf2\": \"play conf2\"\n}"',
  'ampAppID': r'"amplitudeappid"',
  'ampProps': r'"AAA: aaa\nBBB: bbb"'
}

# capabilities = device_capabilities('ios', pytest.device_id)
# if not capabilities:
#   logging.info('cannot find capabilitites for device_id: {}'.format(pytest.device_id))
#   raise Exception('cannot find capabilitites for device_id: {}'.format(pytest.device_id))
# logging.debug(capabilities)

# capabilities['browserName'] = 'Safari'

if not pytest.driver:
  raise Exception('WebDriver is not initialized.')
driver = pytest.driver


# driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)
# params_string = '&'.join([urllib.parse.quote('{}={}'.format(k, v), '=') for k, v in params.items()])
# url = '?'.join((host, params_string))

sample_web = None
def init_pages():
  driver.get(url)
  sample_web = Sample_Web(driver)

def setup_module():
  """ module setup """
  logging.debug('module setup')

def teardown_module():
  """ module teardown """
  logging.debug('module teardown')
  driver.close_app()

def setup_function():
  logging.debug('function setup')

def teardown_function():
  logging.debug('function teardown')

@pytest.mark.test_platform('web')
@pytestrail.case('1234')
def test_ios_safari_sample1():
  init_pages()
  time.sleep(5)
  assert sample_web.error_back_button_exists()
  logging.info('error back button exists')
  sample_web.click_error_back_button()
  time.sleep(10)