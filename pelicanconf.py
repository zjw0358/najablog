#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'spark'
SITENAME = 'NajaBlog'
SITEURL = ''
PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh'
# MARKUP = ('md', 'ipynb')
# LOCALE = 'zh_CN.utf8'
# RELATIVE_URLS = False
DISPLAY_ARTICLE_INFO_ON_INDEX = True
DATE_FORMATS = {
    'en': ((u'en_US', 'utf8'), u'%a, %d %b %Y',),
    'zh': ((u'zh_CN', 'utf8'), u'%Y年%m月%d日(周%a)',),
}
# PLUGIN_PATHS = ['./plugins']
# PLUGINS = ['ipynb.markup']
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['always_modified', 'render_math', 'ipynb2pelican', 'liquid_tags.include_code',
           'pelican-toc', 'i18n_subsites', 'tipue_search', 'neighbors']
IGNORE_FILES = ['.ipynb_checkpoints']
SEARCH_URL = "/search.html"
IPYNB_USE_METACELL = True
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
THEME = 'themes/pelican-bootstrap3'
BOOTSTRAP_THEME = "cosmo"
THEME_COLOR = True
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
BOOTSTRAP_NAVBAR_INVERSE = False
TAGS_URL = "tags.html"
CATEGORIES_URL = "/categories.html"

MAIN_MENU = True
HOME_HIDE_TAGS = False
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
DIRECT_TEMPLATES = (('search', 'index', 'categories',
                     'authors', 'archives',
                     'tags', '404',))
MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),
             ('About', '/pages/about.html'),
             )
DEFAULT_DATE = 'fs'
PYGMENTS_STYLE = 'default'

IPYNB_SUMMARY_CELL = True
MARKUP = ('md', 'ipynb', 'rst')
CACHE_CONTENT = True
LOAD_CONTENT_CACHE = True
# MATHJAX_CDN="/mathjax/latest.js"
TOC = {
    'TOC_HEADERS': '^h[2-4]',
    'TOC_RUN': 'true',
    'TOC_INCLUDE_TITLE': 'false',
}

TYPOGRIFY = False

# ABOUT_ME = '曾经在某神秘单位、校内网（人人网）和阿里巴巴 等机构重要岗位任职。'
# AVATAR = 'images/spark.jpg'

# PLUGINS += ['tag_cloud', 'optimize_images']

PYGMENTS_STYLE = 'friendly'

# CUSTOM_JS = ['https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js',
# 'https://cdnjs.cloudflare.com/ajax/libs/bokeh/1.0.1/bokeh-gl.min.js.map']

# STATIC_PATHS = ['static', 'code']
STATIC_PATHS = [
    'extra/robots.txt',
    'extra/favicon.ico',
    'images',
    'pages',
    'docs',
]

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('公司朝天吼官网', 'http://sostc.org/'),
         ('数据产品淘宝店', 'https://shop101144854.taobao.com'),
         # ('个人简历', 'http://twomouth.com/'),
         ('You can ask me to modify those links ', '#'),)

# Social widget
SOCIAL = (('朝天吼微博', 'http://weibo.com/fxmyk'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 6

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
ALWAYS_MODIFIED = True
