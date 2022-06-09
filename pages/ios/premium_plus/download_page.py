# -*- coding: UTF-8 -*-
import pytest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.base import Base_Page
from appium import webdriver

class Download_Page(Base_Page):
  locator = {
  }	