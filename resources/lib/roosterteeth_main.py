#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#
# Imports
#
from future import standard_library
standard_library.install_aliases()
from builtins import object
import sys
import urllib.request, urllib.parse, urllib.error
import xbmcgui
import xbmcplugin
import os

from roosterteeth_const import LANGUAGE, SETTINGS, IMAGES_PATH, ROOSTERTEETH_SERIES_URL, \
    ROOSTERTEETH_RECENTLY_ADDED_VIDEOS_SERIES_URL, ACHIEVEMENTHUNTER_RECENTLY_ADDED_VIDEOS_SERIES_URL, \
    FUNHAUS_RECENTLY_ADDED_VIDEOS_SERIES_URL, INSIDE_GAMING_RECENTLY_ADDED_VIDEOS_SERIES_URL, \
    SCREWATTACK__RECENTLY_ADDED_VIDEOS_SERIES_URL, SUGARPINE7__RECENTLY_ADDED_VIDEOS_SERIES_URL, \
    COWCHOP_RECENTLY_ADDED_VIDEOS_SERIES_URL, GAMEATTACK_RECENTLY_ADDED_VIDEOS_SERIES_URL, \
    JTMUSIC_RECENTLY_ADDED_VIDEOS_SERIES_URL, KINDAFUNNY_RECENTLY_ADDED_VIDEOS_SERIES_URL, LIVE_URL

#
# Main class
#
class Main(object):
    def __init__(self):
        # Get the command line arguments
        # Get the plugin url in plugin:// notation
        self.plugin_url = sys.argv[0]
        # Get the plugin handle as an integer number
        self.plugin_handle = int(sys.argv[1])

        #
        # My Channels (if enabled)
        #
        if SETTINGS.getSetting('mychannels') == "true":
            parameters = {"action": "my-channels",
                        "show_serie_name": "True", "next_page_possible": "False", "check_source_url": "True"}
            url = self.plugin_url + '?' + urllib.parse.urlencode(parameters)
            list_item = xbmcgui.ListItem(LANGUAGE(30322))
            is_folder = True
            list_item.setArt({'fanart': os.path.join(IMAGES_PATH, 'fanart-rooster-teeth.png')})
            list_item.setProperty('IsPlayable', 'false')
            xbmcplugin.addDirectoryItem(handle=self.plugin_handle, url=url, listitem=list_item, isFolder=is_folder)

        #
        # Live
        #
        if SETTINGS.getSetting('live_streams') == "true":
            parameters = {"action": "list-streams", "plugin_category": LANGUAGE(30321), "url": LIVE_URL,
                        "show_serie_name": "True", "next_page_possible": "False", "check_source_url": "True"}
            url = self.plugin_url + '?' + urllib.parse.urlencode(parameters)
            list_item = xbmcgui.ListItem(LANGUAGE(30321))
            is_folder = True
            list_item.setArt({'fanart': os.path.join(IMAGES_PATH, 'fanart-rooster-teeth.png')})
            list_item.setProperty('IsPlayable', 'false')
            xbmcplugin.addDirectoryItem(handle=self.plugin_handle, url=url, listitem=list_item, isFolder=is_folder)

        #
        # Series
        #
        parameters = {"action": "list-series", "plugin_category": LANGUAGE(30302), "url": ROOSTERTEETH_SERIES_URL,
                      "show_serie_name": "True", "next_page_possible": "False"}
        url = self.plugin_url + '?' + urllib.parse.urlencode(parameters)
        list_item = xbmcgui.ListItem(LANGUAGE(30302))
        is_folder = True
        list_item.setArt({'fanart': os.path.join(IMAGES_PATH, 'fanart-rooster-teeth.png')})
        list_item.setProperty('IsPlayable', 'false')
        xbmcplugin.addDirectoryItem(handle=self.plugin_handle, url=url, listitem=list_item, isFolder=is_folder)

        #
        # Roosterteeth Recently Added Episodes
        #
        parameters = {"action": "list-episodes", "plugin_category": LANGUAGE(30301),
                      "url": ROOSTERTEETH_RECENTLY_ADDED_VIDEOS_SERIES_URL,
                      "show_serie_name": "True", "next_page_possible": "False"}
        url = self.plugin_url + '?' + urllib.parse.urlencode(parameters)
        list_item = xbmcgui.ListItem(LANGUAGE(30301))
        is_folder = True
        list_item.setArt({'fanart': os.path.join(IMAGES_PATH, 'fanart-rooster-teeth.png')})
        list_item.setProperty('IsPlayable', 'false')
        xbmcplugin.addDirectoryItem(handle=self.plugin_handle, url=url, listitem=list_item, isFolder=is_folder)

        #
        # Achievement Hunter Recently Added Episodes
        #
        parameters = {"action": "list-episodes", "plugin_category": LANGUAGE(30303),
                      "url": ACHIEVEMENTHUNTER_RECENTLY_ADDED_VIDEOS_SERIES_URL,
                      "show_serie_name": "True", "next_page_possible": "False"}
        url = self.plugin_url + '?' + urllib.parse.urlencode(parameters)
        list_item = xbmcgui.ListItem(LANGUAGE(30303))
        is_folder = True
        list_item.setArt({'fanart': os.path.join(IMAGES_PATH, 'fanart-achievement-hunter.png')})
        list_item.setProperty('IsPlayable', 'false')
        xbmcplugin.addDirectoryItem(handle=self.plugin_handle, url=url, listitem=list_item, isFolder=is_folder)

        #
        # Funhaus Recently Added Episodes
        #
        parameters = {"action": "list-episodes", "plugin_category": LANGUAGE(30305),
                      "url": FUNHAUS_RECENTLY_ADDED_VIDEOS_SERIES_URL,
                      "show_serie_name": "True", "next_page_possible": "False"}
        url = self.plugin_url + '?' + urllib.parse.urlencode(parameters)
        list_item = xbmcgui.ListItem(LANGUAGE(30305))
        is_folder = True
        list_item.setArt({'fanart': os.path.join(IMAGES_PATH, 'fanart-funhaus.png')})
        list_item.setProperty('IsPlayable', 'false')
        xbmcplugin.addDirectoryItem(handle=self.plugin_handle, url=url, listitem=list_item, isFolder=is_folder)

        #
        # Inside Gaming Recently Added Episodes
        #
        parameters = {"action": "list-episodes", "plugin_category": LANGUAGE(30315),
                      "url": INSIDE_GAMING_RECENTLY_ADDED_VIDEOS_SERIES_URL,
                      "show_serie_name": "True", "next_page_possible": "False"}
        url = self.plugin_url + '?' + urllib.parse.urlencode(parameters)
        list_item = xbmcgui.ListItem(LANGUAGE(30315))
        is_folder = True
        list_item.setArt({'fanart': os.path.join(IMAGES_PATH, 'fanart-inside-gaming.png')})
        list_item.setProperty('IsPlayable', 'false')
        xbmcplugin.addDirectoryItem(handle=self.plugin_handle, url=url, listitem=list_item, isFolder=is_folder)

        #
        # Screw Attack Recently Added Episodes
        #
        parameters = {"action": "list-episodes", "plugin_category": LANGUAGE(30307),
                      "url": SCREWATTACK__RECENTLY_ADDED_VIDEOS_SERIES_URL,
                      "show_serie_name": "True", "next_page_possible": "False"}
        url = self.plugin_url + '?' + urllib.parse.urlencode(parameters)
        list_item = xbmcgui.ListItem(LANGUAGE(30307))
        is_folder = True
        list_item.setArt({'fanart': os.path.join(IMAGES_PATH, 'fanart-screwattack.png')})
        list_item.setProperty('IsPlayable', 'false')
        xbmcplugin.addDirectoryItem(handle=self.plugin_handle, url=url, listitem=list_item, isFolder=is_folder)

        #
        # Sugar Pine 7 Recently Added Episodes
        #
        parameters = {"action": "list-episodes", "plugin_category": LANGUAGE(30311),
                      "url": SUGARPINE7__RECENTLY_ADDED_VIDEOS_SERIES_URL,
                      "show_serie_name": "True", "next_page_possible": "False"}
        url = self.plugin_url + '?' + urllib.parse.urlencode(parameters)
        list_item = xbmcgui.ListItem(LANGUAGE(30311))
        is_folder = True
        list_item.setArt({'fanart': os.path.join(IMAGES_PATH, 'fanart-sugar-pine-7.png')})
        list_item.setProperty('IsPlayable', 'false')
        xbmcplugin.addDirectoryItem(handle=self.plugin_handle, url=url, listitem=list_item, isFolder=is_folder)

        #
        # Cow Chop Recently Added Episodes
        #
        parameters = {"action": "list-episodes", "plugin_category": LANGUAGE(30309),
                      "url": COWCHOP_RECENTLY_ADDED_VIDEOS_SERIES_URL,
                      "show_serie_name": "True", "next_page_possible": "False"}
        url = self.plugin_url + '?' + urllib.parse.urlencode(parameters)
        list_item = xbmcgui.ListItem(LANGUAGE(30309))
        is_folder = True
        list_item.setArt({'fanart': os.path.join(IMAGES_PATH, 'fanart-cow-chop.png')})
        list_item.setProperty('IsPlayable', 'false')
        xbmcplugin.addDirectoryItem(handle=self.plugin_handle, url=url, listitem=list_item, isFolder=is_folder)

        #
        # Game Attack Recently Added Episodes
        #
        parameters = {"action": "list-episodes", "plugin_category": LANGUAGE(30313),
                      "url": GAMEATTACK_RECENTLY_ADDED_VIDEOS_SERIES_URL,
                      "show_serie_name": "True", "next_page_possible": "False"}
        url = self.plugin_url + '?' + urllib.parse.urlencode(parameters)
        list_item = xbmcgui.ListItem(LANGUAGE(30313))
        is_folder = True
        list_item.setArt({'fanart': os.path.join(IMAGES_PATH, 'fanart-game-attack.png')})
        list_item.setProperty('IsPlayable', 'false')
        xbmcplugin.addDirectoryItem(handle=self.plugin_handle, url=url, listitem=list_item, isFolder=is_folder)

        #
        # JT Music Recently Added Episodes
        #
        parameters = {"action": "list-episodes", "plugin_category": LANGUAGE(30317),
                      "url": JTMUSIC_RECENTLY_ADDED_VIDEOS_SERIES_URL,
                      "show_serie_name": "True", "next_page_possible": "False"}
        url = self.plugin_url + '?' + urllib.parse.urlencode(parameters)
        list_item = xbmcgui.ListItem(LANGUAGE(30317))
        is_folder = True
        list_item.setArt({'fanart': os.path.join(IMAGES_PATH, 'fanart-jt-music.png')})
        list_item.setProperty('IsPlayable', 'false')
        xbmcplugin.addDirectoryItem(handle=self.plugin_handle, url=url, listitem=list_item, isFolder=is_folder)

        #
        # Kinda Funny Recently Added Episodes
        #
        parameters = {"action": "list-episodes", "plugin_category": LANGUAGE(30319),
                      "url": KINDAFUNNY_RECENTLY_ADDED_VIDEOS_SERIES_URL,
                      "show_serie_name": "True", "next_page_possible": "False"}
        url = self.plugin_url + '?' + urllib.parse.urlencode(parameters)
        list_item = xbmcgui.ListItem(LANGUAGE(30319))
        is_folder = True
        list_item.setArt({'fanart': os.path.join(IMAGES_PATH, 'fanart-kinda-funny.png')})
        list_item.setProperty('IsPlayable', 'false')
        xbmcplugin.addDirectoryItem(handle=self.plugin_handle, url=url, listitem=list_item, isFolder=is_folder)

        # Disable sorting
        xbmcplugin.addSortMethod(handle=self.plugin_handle, sortMethod=xbmcplugin.SORT_METHOD_NONE)
        # Finish creating a virtual folder.
        xbmcplugin.endOfDirectory(self.plugin_handle)
