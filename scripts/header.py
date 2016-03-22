#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    head for script files
'''

import sys
import locale
from os import environ

reload(sys)
sys.setdefaultencoding("utf-8")
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

environ['DJANGO_SETTINGS_MODULE'] = 'gestorpsi.settings'
sys.path.append('..')

# libray
#sys.path.append("/home/redepsi/lib/python2.7")

# import hardcode
path="/home/tiago/Desktop/dev/gestorpsi/scripts"

# root project
sys.path.append("%s/gestorpsi" % path )
sys.path.append("%s/gestorpsi/gestorpsi" % path)
