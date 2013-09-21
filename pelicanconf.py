#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Marco Minutoli'
SITENAME = u'Bit that Bite'
SITEURL = 'http://mminutoli.github.io'

GOOGLE_ANALYTICS = 'UA-42899189-1'

TIMEZONE = "Europe/Rome"
# THEME = u'/home/mminutoli/tools/pelican-themes/mnmlist'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.rss.xml'
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  ()

# Social widget
SOCIAL = (('github', 'https://github.com/mminutoli'),
          ('Google+', 'https://plus.google.com/114057888676170815651'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
