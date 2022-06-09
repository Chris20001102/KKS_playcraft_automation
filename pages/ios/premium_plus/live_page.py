# -*- coding: UTF-8 -*-
import pytest
import os, sys
from appium.webdriver.extensions.location import Location
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.base import Base_Page
from appium import webdriver

class Live_Page(Base_Page):
  locator = {
  }