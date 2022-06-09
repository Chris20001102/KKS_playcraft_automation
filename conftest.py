import logging
import os
import pytest
import sys
CWD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(CWD)
pytest.test_root = CWD
from utils.device_manager import device_capabilities

def pytest_addoption(parser):
  parser.addoption("--device-id", action="store")
  parser.addoption("--driver-host", action="store")
  parser.addoption("--driver-port", action="store")
  parser.addoption("--app", action="store", default=None)
  parser.addoption("--platform", action="store", default=None)
  parser.addoption("--browser", action="store", default=None)
  parser.addoption("--package", action="store", default=None)

def pytest_configure(config):
  pytest.device_id = config.getoption('--device-id')
  pytest.driver_host = config.getoption('--driver-host')
  pytest.driver_port = config.getoption('--driver-port')
  pytest.app = config.getoption('--app')
  pytest.platform = config.getoption('--platform')
  pytest.browser = config.getoption('--browser')
  pytest.package = config.getoption('--package')
  capabilities = device_capabilities(pytest.device_id, pytest.platform)
  
  if 'android' == capabilities['platformName'].lower():
    if 'web' == pytest.app:
      capabilities['browserName'] = pytest.browser
      capabilities['chromedriverExecutable'] = os.path.join(CWD, 'drivers', 'chromedriver')
    else:
      if pytest.app:
        package, activity = pytest.app.split('/')
        capabilities['appPackage'] = package
        capabilities['appActivity'] = activity
      if pytest.package:
        capabilities['app'] = pytest.package
  elif 'ios' == capabilities['platformName'].lower():
    if 'web' == pytest.app:
      capabilities['browserName'] = pytest.browser
    else:
      capabilities['bundleId'] = pytest.app
      if pytest.package:
        capabilities['app'] = pytest.package
  logging.debug('capabilities: {}'.format(capabilities))
  pytest.driver = get_driver(capabilities)
  pytest.driver.implicitly_wait(0.7)

  if 'android' == capabilities['platformName'].lower():
    pytest.driver.update_settings({'waitForIdleTimeout': 200})
    
  config.addinivalue_line("markers", "test_platform(platform): this mark execute tests for the given platform")

def pytest_runtest_setup(item):
  platforms = [mark.args[0] for mark in item.iter_markers(name="test_platform")]
  if platforms:
    if not set(item.config.getoption("--platform").split(',')).intersection(set(platforms)):
      pytest.skip("Test skipped because platform is not {!r}".format(platforms))

def get_driver(capabilities):
  if capabilities:
    if capabilities['platformName'].lower() in ['android', 'ios']:
      from appium import webdriver
      return webdriver.Remote('http://{}:{}/wd/hub'.format(pytest.driver_host, pytest.driver_port), capabilities)
    elif capabilities['platformName'].lower() in ['desktop']:
      from selenium import webdriver
      # https://selenium-python.readthedocs.io/api.html
      if 'chrome' == capabilities['browserName'].lower():
        return webdriver.Chrome('drivers/chromedriver')
      elif 'safari' == capabilities['browserName'].lower():
        return webdriver.Safari()
      else:
        return None
  else:
    return None