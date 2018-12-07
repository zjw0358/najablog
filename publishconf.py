#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'http://518.is'
# RELATIVE_URLS = False

#FEED_ALL_ATOM = 'feeds/all.atom.xml'
#CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = "najablog"
GOOGLE_ANALYTICS = "UA-4002013-9"

TWITTER_USERNAME = 'zjw0358'
COPYRIGHT_YEAR = 2019
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}
CC_LICENSE = "BY-SA"
#ADD_THIS_ID = 'ra-592e4f7b8a3ce59f'

MATHJAX_CDN = None
RELATIVE_URLS = False
USE_LESS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
#CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
CACHE_CONTENT = False
LOAD_CONTENT_CACHE = False
DELETE_OUTPUT_DIRECTORY = True
ALWAYS_MODIFIED = True
PLUGINS += ['sitemap', 'related_posts', ]
# CUSTOM_JS="https://cdn.rawgit.com/peijunz/90da9dc4c7d753f9c5b128d45a23fecb/raw/add_blog_buttons.js"
# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
BUSUANZI = True
