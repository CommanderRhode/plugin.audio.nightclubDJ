# -*- coding: utf-8 -*-

class Properties:

  def __init__(self, args):
    try:
      self.handle = int(args[1])
      self.baseurl = str(args[0])
    except Exception, e:
      self.handle = 0
      self.baseurl = ''

  def addonHandle(self):
    return self.handle

  def baseURL(self):
    return self.baseurl
