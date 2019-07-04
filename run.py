#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import time
import unittest
import sys

from HTMLTestRunner import HTMLTestRunner_py3

test_dir = './testcase'
discover = unittest.defaultTestLoader.discover(start_dir='./testcase', pattern="*.py")

if __name__ == "__main__":

    report_dir = './test_report'
    os.makedirs(report_dir, exist_ok=True)
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    report_name = '{0}/{1}.html'.format(report_dir, now)
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

    with open(report_name, 'wb')as f:
        runner = HTMLTestRunner_py3.HTMLTestRunner(stream=f, verbosity=2, title='敏感词测试报告', description='执行人：sxs')
        runner.run(discover)

