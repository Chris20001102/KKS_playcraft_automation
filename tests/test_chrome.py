# -*- coding: UTF-8 -*-
import logging
import os
import pytest
import sys
import time
import urllib
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from appium import webdriver
from utils.dc import device_capabilities
from pages.web.sample_web import Sample_Web

# def init_logger(filename):
#   logging.basicConfig(level=logging.DEBUG,
#                       format='%(asctime)s %(threadName)s %(levelname)-6s%(message)s',
#                       datefmt='%m-%d %H:%M',
#                       filename='logs/'+filename + '.' + 'log',
#                       filemode='w')
#   console = logging.StreamHandler()
#   console.setLevel(logging.INFO)
#   formatter = logging.Formatter('%(levelname)-6s%(message)s')
#   console.setFormatter(formatter)
#   logging.getLogger('').addHandler(console)


# init_logger(pytest.device_id)

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
  'ampAppID': r'"amplitudeappid"',
  'ampProps': r'"AAA: aaa\nBBB: bbb"'
}

params_string = '&'.join([urllib.parse.quote('{}={}'.format(k, v), '=') for k, v in params.items()])
url = '?'.join((host, params_string))
logging.debug('url: {}'.format(url))
# capabilities = device_capabilities(pytest.device_id)
# if capabilities:
#   driver = webdriver.Remote('http://localhost:{}/wd/hub'.format(pytest.driver_port), capabilities)
# else:
#   driver = webdriver.Chrome('drivers/chromedriver')

# driver = webdriver.Chrome('drivers/chromedriver')

if not pytest.driver:
  raise Exception('WebDriver is not initialized.')
driver = pytest.driver

logging.debug('------------------------------------')
logging.debug('webdriver session id: {}'.format(driver.session_id))
logging.debug('pytest device_id: {}'.format(pytest.device_id))
logging.debug('pytest device_id: {}'.format(pytest.driver_host))
logging.debug('pytest driver_port: {}'.format(pytest.driver_port))
logging.debug('driver.capabilities: {}'.format(driver.capabilities))
logging.debug('------------------------------------')

driver.get(url)
sample_web = Sample_Web(driver)


def setup_module():
  """ module setup """
  logging.debug('module setup')
  # capabilities = device_capabilities('ios', device.device_id)
  # if 'desktop' == capabilities['platformName'].lower():
  #   driver = webdriver.Chrome('drivers/chromedriver')
  # elif 'android' == capabilities['platformName'].lower():
  #   capabilities['browserName'] = 'Chrome'
  #   capabilities['chromedriverExecutable'] = os.path.join(CWD, 'drivers', 'chromedriver_83.0.4103.39')
  #   driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)
  # elif 'ios' == capabilities['platformName'].lower():
  #   capabilities['browserName'] = 'Safari'
  #   driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)
    
  # driver.get(url)
  # sample_web = Sample_Web(driver)

class TestWeb:
  # @classmethod
  # def setup_class(cls):
  #   logging.info('setup class')
  
  # @classmethod
  # def teardown_class(cls):
  #   logging.info('teardown class')
  
  # @pytest.mark.test_platform('web')
  def test_sample_web(self):

    time.sleep(3)
    if sample_web.error_back_button_exists():
      print('error back button exists')
      sample_web.click_error_back_button()
    # sample_web.set_content_id(1)
    # sample_web.click_apply_button()
    # sample_web.set_content_id(2)
    # sample_web.click_apply_button()
    # sample_web.click_play_button()

  # @pytest.mark.test_platform('web')
  def test_sample_web2(self):
    # driver.get(url)
    # sample_web = Sample_Web(driver)

    time.sleep(3)
    sample_web.set_content_id(1)
    time.sleep(1)
    sample_web.click_apply_button()
    time.sleep(1)
    sample_web.set_content_id(2)
    time.sleep(1)
    sample_web.click_apply_button()
    time.sleep(1)
    sample_web.set_content_id(2)
    time.sleep(1)
    sample_web.click_apply_button()
    time.sleep(5)
    # sample_web.click_play_button()