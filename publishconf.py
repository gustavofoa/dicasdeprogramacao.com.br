#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://dicasdeprogramacao.com.br'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

TIMEZONE = 'America/Sao_Paulo'
# Your language.
DEFAULT_LANG = u'pt_BR'
OG_LOCALE = u'pt_BR'
LOCALE = ('pt','bra', 'pt_BR')
LANGUAGE = u'pt_BR'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# Plugins
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['sitemap', 'minify', 'share_post', 'tag_cloud']

MINIFY = {
 'remove_comments': True,
 'remove_all_empty_space': True,
 'remove_optional_attribute_quotes': False
}
