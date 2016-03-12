#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#
# Imports
#
<<<<<<< HEAD
import os
=======
>>>>>>> origin/master
import sys
import urllib
import xbmcgui
import xbmcplugin
import os

from roosterteeth_const import ADDON, SETTINGS, LANGUAGE, IMAGES_PATH, DATE, VERSION

from roosterteeth_const import LANGUAGE

RECENTLYADDEDURL = 'http://roosterteeth.com/episode/recently-added?page=001'
ROOSTERTEETHSHOWSURL = 'http://www.roosterteeth.com/show/'
ACHIEVEMENTHUNTERURL = 'http://achievementhunter.com/show/'
THEKNOWSHOWSURL = 'http://theknow.tv/show'
FUNHAUSSHOWSURL = 'http://fun.haus/show'


#
# Main class
#
class Main:
    def __init__(self):
<<<<<<< HEAD
        # Get the command line arguments
        # Get the plugin url in plugin:// notation
        self.plugin_url = sys.argv[0]
        # Get the plugin handle as an integer number
        self.plugin_handle = int(sys.argv[1])

=======
>>>>>>> origin/master
        #
        # Recently Added Episodes
        #
        parameters = {"action": "list-episodes", "plugin_category": LANGUAGE(30000), "url": RECENTLYADDEDURL,
                      "next_page_possible": "True"}
<<<<<<< HEAD
        url = self.plugin_url + '?' + urllib.urlencode(parameters)
        list_item = xbmcgui.ListItem(LANGUAGE(30000))
        is_folder = True
        list_item.setArt({'fanart': os.path.join(IMAGES_PATH, 'fanart-blur.jpg')})
        list_item.setProperty('IsPlayable', 'false')
        xbmcplugin.addDirectoryItem(handle=self.plugin_handle, url=url, listitem=list_item, isFolder=is_folder)
=======
        url = sys.argv[0] + '?' + urllib.urlencode(parameters)
        list_item = xbmcgui.ListItem(LANGUAGE(30000))
        is_folder = True
        xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=list_item, isFolder=is_folder)
>>>>>>> origin/master
        #
        # Roosterteeth
        #
        parameters = {"action": "list-shows", "plugin_category": LANGUAGE(30001), "url": ROOSTERTEETHSHOWSURL,
                      "next_page_possible": "False"}
<<<<<<< HEAD
        url = self.plugin_url + '?' + urllib.urlencode(parameters)
        list_item = xbmcgui.ListItem(LANGUAGE(30001))
        is_folder = True
        list_item.setArt({'fanart': os.path.join(IMAGES_PATH, 'fanart-blur.jpg')})
        list_item.setProperty('IsPlayable', 'false')
        xbmcplugin.addDirectoryItem(handle=self.plugin_handle, url=url, listitem=list_item, isFolder=is_folder)
=======
        url = sys.argv[0] + '?' + urllib.urlencode(parameters)
        list_item = xbmcgui.ListItem(LANGUAGE(30001))
        is_folder = True
        xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=list_item, isFolder=is_folder)
>>>>>>> origin/master
        #
        # Achievement Hunter
        #
        parameters = {"action": "list-shows", "plugin_category": LANGUAGE(30002), "url": ACHIEVEMENTHUNTERURL,
                      "next_page_possible": "False"}
<<<<<<< HEAD
        url = self.plugin_url + '?' + urllib.urlencode(parameters)
        list_item = xbmcgui.ListItem(LANGUAGE(30002))
        is_folder = True
        list_item.setArt({'fanart': os.path.join(IMAGES_PATH, 'fanart-blur.jpg')})
        list_item.setProperty('IsPlayable', 'false')
        xbmcplugin.addDirectoryItem(handle=self.plugin_handle, url=url, listitem=list_item, isFolder=is_folder)
=======
        url = sys.argv[0] + '?' + urllib.urlencode(parameters)
        list_item = xbmcgui.ListItem(LANGUAGE(30002))
        is_folder = True
        xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=list_item, isFolder=is_folder)
>>>>>>> origin/master
        #
        # The Know Tv
        #
        parameters = {"action": "list-shows", "plugin_category": LANGUAGE(30003), "url": THEKNOWSHOWSURL,
                      "next_page_possible": "False"}
<<<<<<< HEAD
        url = self.plugin_url + '?' + urllib.urlencode(parameters)
        list_item = xbmcgui.ListItem(LANGUAGE(30003))
        is_folder = True
        list_item.setArt({'fanart': os.path.join(IMAGES_PATH, 'fanart-blur.jpg')})
        list_item.setProperty('IsPlayable', 'false')
        xbmcplugin.addDirectoryItem(handle=self.plugin_handle, url=url, listitem=list_item, isFolder=is_folder)
=======
        url = sys.argv[0] + '?' + urllib.urlencode(parameters)
        list_item = xbmcgui.ListItem(LANGUAGE(30003))
        is_folder = True
        xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=list_item, isFolder=is_folder)
>>>>>>> origin/master

        #
        # Fun Haus
        #
        parameters = {"action": "list-shows", "plugin_category": LANGUAGE(30004), "url": FUNHAUSSHOWSURL,
                      "next_page_possible": "False"}
<<<<<<< HEAD
        url = self.plugin_url + '?' + urllib.urlencode(parameters)
        list_item = xbmcgui.ListItem(LANGUAGE(30004))
        is_folder = True
        list_item.setArt({'fanart': os.path.join(IMAGES_PATH, 'fanart-blur.jpg')})
        list_item.setProperty('IsPlayable', 'false')
        xbmcplugin.addDirectoryItem(handle=self.plugin_handle, url=url, listitem=list_item, isFolder=is_folder)

        # Disable sorting
        xbmcplugin.addSortMethod(handle=self.plugin_handle, sortMethod=xbmcplugin.SORT_METHOD_NONE)
        # Finish creating a virtual folder.
        xbmcplugin.endOfDirectory(self.plugin_handle)
=======
        url = sys.argv[0] + '?' + urllib.urlencode(parameters)
        list_item = xbmcgui.ListItem(LANGUAGE(30004))
        is_folder = True
        xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=list_item, isFolder=is_folder)

        # Disable sorting...
        xbmcplugin.addSortMethod(handle=int(sys.argv[1]), sortMethod=xbmcplugin.SORT_METHOD_NONE)

        # End of list...
        xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=True)
>>>>>>> origin/master
