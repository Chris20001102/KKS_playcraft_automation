# -*- coding: UTF-8 -*-
import logging
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

class Base_Page(object):
  def __init__(self, driver):
    self.driver = driver
    self.timeout = 5

  def _wait_element(self, locator, timeout):
    try:
      return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))
    except Exception as ex:
      logging.warning(ex)
      print(ex)
      logging.info("Unable to find {} locator in {} page".format(locator, self))
      return None
  
  def _find_element(self, locator):
    try:
      return self.driver.find_element(*locator)
    except Exception as ex:
      logging.warning(ex)
      logging.warning('Element {} not exists'.format(locator))
      return False
  
  def find_elements(self, locator):
    try:
      return self.driver.find_elements(*locator)
    except Exception as ex:
      print(ex)
    return None
    

  # def _find_elements(self, locator, timeout=5):
  #   try:
  #     # return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))
  #     self.driver.find_elements()
  #   except Exception as e:
  #     print("Unable to find {} locator in {} page".format(locator, self))
  #     return None

  def exists(self, locator):
    return self._find_element(locator)
    # try:
    #   return self.driver.find_element(*locator)
    # except Exception as ex:
    #   logging.warning('Element {} not exists'.format(locator))
    #   return False
    
    # element = self._find_element(locator)
    # print('{} exists: {}'.format(locator, element))
    # logging.debug('{} exists: {}'.format(locator, element))
    # if element:
    #   return True
    # return False
  
  def is_visible(self, locator):
    element = self._find_element(locator)
    if element:
      return element.is_displayed()
    return False

  def is_checked(self, locator):
    element = self._find_element(locator)
    if element:
      return element.get_attribute('checked')
    return None

  def set_text(self, locator, value, timeout=5):
    element = self._find_element(locator)
    if element:
      element.clear()
      return element.send_keys(value)
    return False

  def get_text(self, locator, timeout=1):
    element = self._wait_element(locator, timeout)
    if element:
      return element.get_attribute('text')
    return None
  
  def get_value(self, locator, timeout=1):
    element = self._wait_element(locator, timeout)
    if element:
      return element.get_attribute('value')
    return None

  def get_label(self, locator, timeout=1):
    element = self._wait_element(locator, timeout)
    if element:
      return element.get_attribute('label')
    return None

  def click(self, locator, timeout=0.5):
    return self._wait_element(locator, timeout).click()

  # def wait(self, wait):
  #   self.driver.implicitly_wait(wait)

  def rect(self, locator):
    element = self._find_element(locator)
    if element:
      return element.rect
    return None
  
  def swipe(self, from_, to, pause=None):
    logging.info('swipe from {} to {}'.format(from_, to))
    actions = TouchAction(self.driver)
    actions.press(x=from_[0], y=from_[1])
    logging.info('[swipe] pressed')
    if pause:
      offset = [round((to[0] - from_[0]) / pause), round((to[1] - from_[1]) / pause)]
      for i in range(1, pause):
        actions.move_to(x=from_[0]+offset[0]*i, y=from_[1]+offset[1]*i)
    actions.move_to(x=to[0], y=to[1])
    logging.info('[swipe] moved to')
    actions.release()
    logging.info('[swipe] released')
    actions.perform()
    logging.info('[swipe] performed')
  
  def tap(self,tap_point):
    actions = TouchAction(self.driver)
    actions.press(x=tap_point[0], y=tap_point[1])
    actions.release()
    actions.perform()