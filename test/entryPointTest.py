# -*- coding: utf-8 -*-

import sys
import os
testdirectory = os.path.dirname(__file__)
srcdirectory = '../src'
sys.path.insert(0, os.path.abspath(os.path.join(testdirectory, srcdirectory)))

from entryPoint import *
import unittest
import mock

class TestEntryPoint(unittest.TestCase):
    def test_valid_process_handle(self):
      self.assertEqual(processHandle, 1)
