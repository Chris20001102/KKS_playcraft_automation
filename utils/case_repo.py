#!/usr/bin/env python
# -*-  coding: utf-8 -*-

import json
from testrail import *

client = APIClient('https://kkstream.testrail.net/')
client.user = r'alexlin@kkstream.com'
client.password = r'aSObLdpuubGUs7v1jfAB-SJ1BBYVlHc3Q9j7lR1BM'

if __name__ == '__main__':
  project_id = '24'
  suite_id = '524'
  cases = client.send_get('get_cases/{}&suite_id={}'.format(project_id, suite_id))
  # cases = json.loads(cases)
  print(json.dumps(cases))