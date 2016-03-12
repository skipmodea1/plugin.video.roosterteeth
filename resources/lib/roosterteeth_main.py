#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#
# Imports
#
import sys
import urllib
import xbmcgui
import xbmcplugin

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
        #
        # Recently Added Episodes
        #
        parameters = {"action": "list-episodes", "plugin_category": LANGUAGE(30000), "url": RECENTLYADDEDURL,
                      "next_page_possible": "True"}
        url = sys.argv[0] + '?' + urllib.urlencode(parameters)
        list_item = xbmcgui.ListItem(LANGUAGE(30000))
        is_folder = True
        xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=list_item, isFolder=is_folder)
        #
        # Roosterteeth
        #
        parameters = {"action": "list-shows", "plugin_category": LANGUAGE(30001), "url": ROOSTERTEETHSHOWSURL,
                      "next_page_possible": "False"}
        url = sys.argv[0] + '?' + urllib.urlencode(parameters)
        list_item = xbmcgui.ListItem(LANGUAGE(30001))
        is_folder = True
        xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=list_item, isFolder=is_folder)
        #
        # Achievement Hunter
        #
        parameters = {"action": "list-shows", "plugin_category": LANGUAGE(30002), "url": ACHIEVEMENTHUNTERURL,
                      "next_page_possible": "False"}
        url = sys.argv[0] + '?' + urllib.urlencode(parameters)
        list_item = xbmcgui.ListItem(LANGUAGE(30002))
        is_folder = True
        xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=list_item, isFolder=is_folder)
        #
        # The Know Tv
        #
        parameters = {"action": "list-shows", "plugin_category": LANGUAGE(30003), "url": THEKNOWSHOWSURL,
                      "next_page_possible": "False"}
        url = sys.argv[0] + '?' + urllib.urlencode(parameters)
        list_item = xbmcgui.ListItem(LANGUAGE(30003))
        is_folder = True
        xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=list_item, isFolder=is_folder)

        #
        # Fun Haus
        #
        parameters = {"action": "list-shows", "plugin_category": LANGUAGE(30004), "url": FUNHAUSSHOWSURL,
                      "next_page_possible": "False"}
        url = sys.argv[0] + '?' + urllib.urlencode(parameters)
        list_item = xbmcgui.ListItem(LANGUAGE(30004))
        is_folder = True
        xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=list_item, isFolder=is_folder)

        # Disable sorting...
        xbmcplugin.addSortMethod(handle=int(sys.argv[1]), sortMethod=xbmcplugin.SORT_METHOD_NONE)

        # End of list...
        xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=True)
