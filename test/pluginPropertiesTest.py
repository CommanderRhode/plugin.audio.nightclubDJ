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
      args = ['plugin://plugin.video.nightclubdj/', '2', '3']
      properties = Properties(args)
      self.assertEqual(properties.addonHandle(), 2)
      self.assertEqual(properties.baseURL(), 'plugin://plugin.video.nightclubdj/')

    def test_invalid_handle_is_caught(self):
      args = ['plugin://plugin.video.nightclubdj/','two', '3']
      properties = Properties(args)
      self.assertEqual(properties.addonHandle(), 0)
