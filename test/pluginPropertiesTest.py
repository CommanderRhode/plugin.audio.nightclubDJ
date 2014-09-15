# -*- coding: utf-8 -*-

import sys
import os
testdirectory = os.path.dirname(__file__)
srcdirectory = '../src'
sys.path.insert(0, os.path.abspath(os.path.join(testdirectory, srcdirectory)))

from pluginProperties import Properties
import unittest
import mock

class TestProperties(unittest.TestCase):
    def test_turning_args_into_properties(self):
      args = ['1', '2', '3']
      properties = Properties(args)
      self.assertEqual(properties.addonHandle(), 2)
