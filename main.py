#!/usr/bin/env python
# -*-  coding: utf-8 -*-

import json
import logging
import os
import pytest
import subprocess
import sys
import threading
import time

from appium.webdriver import appium_service
from appium.webdriver.appium_service import AppiumService
from argparse import ArgumentParser
from utils.device_manager import device_id_list

CWD = os.path.dirname(os.path.abspath(__file__))
APPIUM_SERVICE_LIST = []
DEVICE_ID_LIST = None
TESTS = []
LOG_DIR = 'logs'
LOG_FILE_FORMAT = 'debug-{}.log'
RESULT_FILE_FORMAT = 'result-{}.xml'
REPORT_FIEL_FORMAT = 'report-{}.html'

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(threadName)s %(levelname)-6s%(message)s',
                    datefmt='%m-%d %H:%M',
                    filename=os.path.join(CWD, LOG_DIR, LOG_FILE_FORMAT.format(__file__)),
                    filemode='w')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)-6s%(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

def init_logger(name):
  handler = logging.FileHandler(os.path.join(CWD, LOG_DIR, LOG_FILE_FORMAT.format(name)))
  formatter = logging.Formatter('%(asctime)s %(threadName)s %(levelname)-6s%(message)s')
  handler.setFormatter(formatter)
  logging.getLogger().addHandler(handler)

class ThreadFilter(logging.Filter):
  def __init__(self, name):
    self.name = name
  
  def filter(self, record):
    return record.threadName == self.name

def parse_argvs():
  parser = ArgumentParser()
  parser.add_argument("--device-id", help="Device ID", dest="device_id")
  parser.add_argument("--package", help="Path to Android apk or iOS ipa", dest="package")
  parser.add_argument("--app", help="App name for Android and iOS", dest="app")
  parser.add_argument("--platform", help="Web, Android, or iOS", dest="platform", choices=['desktop', 'android', 'ios'])
  parser.add_argument("--browser", help="Specify brosername when platform=web", dest="browser", choices=['chrome', 'safari'])
  parser.add_argument("--testrail", help="Integrate with TestRail", dest="testrail", action='store_true')
  parser.add_argument("--tr-config", help="TestRail Config", dest="tr_config")
  parser.add_argument('--test-run-project-id', help='TestRail Project ID', dest='tr_project_id')
  parser.add_argument("--tr-testrun-suite-id", help="TestRail Suite ID", dest="tr_suite_id")
  parser.add_argument("--tr-testrun-name", help="TestRail Test Run Name", dest="tr_run_name")
  return parser.parse_known_args()

class TestRunner:
  def __init__(self, port, argvs, name):
    init_logger(name)
    self.name = name
    self.port = port
    self.argvs = argvs
    self.target = ['pytest']
    self.target.extend(argvs)
    self.__runner_thread = threading.Thread(target=self.__job, name=name)
    logging.debug('thread for {} created'.format(name))
    logging.debug(' '.join(self.target))

  def __job(self):
    p = subprocess.Popen(
      self.target,
      stdin=subprocess.DEVNULL,
      stdout=subprocess.PIPE
    )
    output = bytes()
    while p.poll() is None:
      output = p.stdout.read().decode()
      # open('logs/result-{}.report'.format(self.name), 'a').write(output)
    p.kill()

  def start(self):
    logging.info('start thread {}'.format(self.name))
    self.__runner_thread.start()

  def join(self):
    self.__runner_thread.join()


if __name__ == '__main__':
  args, tests = parse_argvs()
  logging.info('tests: {}'.format(tests))
  TESTS.extend(tests)

  if args.device_id:
    DEVICE_ID_LIST = (args.device_id.split(','))
  else:
    DEVICE_ID_LIST = device_id_list(platform=args.platform)
  logging.info('DEVICE_ID_LIST: {}'.format(DEVICE_ID_LIST))

  try:
    test_runner_list = []
    port_counter = 0
    for device_id in DEVICE_ID_LIST:
      driver_host = appium_service.DEFAULT_HOST
      driver_port = appium_service.DEFAULT_PORT + port_counter
      
      boostrap_port = driver_port + 300
      service = AppiumService()
      appium_args = ['--address', driver_host, 
                     '--port', str(driver_port), 
                     '--bootstrap-port', str(boostrap_port),
                     '--log', 'logs/appium-server-{}.log'.format(driver_port),
                     '--allow-cors']
      logging.debug(' '.join(appium_args))
      service.start(args=appium_args)
      APPIUM_SERVICE_LIST.append(service)
      
      argvs = [' '.join(TESTS), 
              '-s', 
              '--device-id={}'.format(device_id), 
              '--driver-host={}'.format(driver_host),
              '--driver-port={}'.format(driver_port)
              ]
      if args.platform:
        argvs.append('--platform={}'.format(args.platform))
      if args.app:
        argvs.append('--app={}'.format(args.app))
      if args.package:
        argvs.append('--package={}'.format(args.package))
      if args.browser:
        argvs.append('--browser={}'.format(args.browser))

      # Configure log level, log format in pytest.ini
      argvs.append('--log-file={}'.format(os.path.join(LOG_DIR, LOG_FILE_FORMAT.format(device_id))))
      argvs.append('--junitxml={}'.format(os.path.join(LOG_DIR, RESULT_FILE_FORMAT.format(device_id))))
      argvs.append('--html={}'.format(os.path.join(LOG_DIR, REPORT_FIEL_FORMAT.format(device_id))))
      argvs.append('--self-contained-html')

      logging.info('argvs: {}'.format(argvs))
      test_runner = TestRunner(driver_port, argvs, device_id)
      test_runner.start()
      test_runner_list.append(test_runner)
      port_counter += 1
    
    for test_runner in test_runner_list:
      test_runner.join()
  except Exception as ex:
    logging.error(ex)
  finally:
    for service in APPIUM_SERVICE_LIST:
      service.stop()
  
