#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#
# Imports
#
from future import standard_library
standard_library.install_aliases()
from builtins import object
import os
import requests
import sys
import urllib.request, urllib.parse, urllib.error
import xbmcgui
import xbmcplugin
import json

from roosterteeth_const import IMAGES_PATH, HEADERS, LANGUAGE, convertToUnicodeString, log, \
    SPONSOR_ONLY_VIDEO_TITLE_PREFIX, ROOSTERTEETH_BASE_URL

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

        # log("ARGV", repr(sys.argv))
        #
        # Parse parameters...
        self.url = urllib.parse.parse_qs(urllib.parse.urlparse(sys.argv[2]).query)['url'][0]
        self.next_page_possible = urllib.parse.parse_qs(urllib.parse.urlparse(sys.argv[2]).query)['next_page_possible'][0]

        # log("self.url", self.url)

        # log("self.show_serie_name", self.show_serie_name)

        #
        # Get the streams...
        #
        self.getStreams()

    #
    # Get videos...
    #
    def getStreams(self):
        #
        # Init
        #
        # Create a list for our items.
        listing = []

        #
        # Get HTML page
        #
        response = requests.get(self.url, headers=HEADERS)

        html_source = response.text
        html_source = convertToUnicodeString(html_source)

        # log("html_source", html_source)

        try:
            json_data = json.loads(html_source)

            # for item in json_data['data']:
            #     log("attribute1", item['canonical_links']['self'])
            #     log("attribute2", item['attributes']['title'])
            #     exit(1)

        except (ValueError, KeyError, TypeError):
            xbmcgui.Dialog().ok(LANGUAGE(30000), LANGUAGE(30109))
            exit(1)

        for item in json_data['data']:

            episode_title = item['attributes']['title']

            caption = item['attributes']['description']

            channel_slug = item['attributes']['channel_slug']

            url = item['attributes']['source_url']

            thumb = item['included']['images'][0]['attributes']['medium']

            is_sponsor_only = item['attributes']['is_sponsors_only']

            if is_sponsor_only:
                title = SPONSOR_ONLY_VIDEO_TITLE_PREFIX + ' ' + episode_title

            title = convertToUnicodeString(title)

            thumbnail_url = thumb

            plot = caption

            studio = channel_slug
            studio = convertToUnicodeString(studio)
            studio = studio.replace("-", " ")
            studio = studio.capitalize()

            # Add to list...
            if url != '':
                list_item = xbmcgui.ListItem(label=title, thumbnailImage=thumbnail_url)
                list_item.setInfo("video",
                                {"title": title, "studio": studio, "mediatype": "video",
                                "plot": plot})
                list_item.setArt({'thumb': thumbnail_url, 'icon': thumbnail_url,
                                'fanart': os.path.join(IMAGES_PATH, 'fanart-rooster-teeth.png')})
                list_item.setProperty('IsPlayable', 'true')

                # let's remove any non-ascii characters from the title, to prevent errors with urllib.parse.parse_qs
                # of the parameters
                title = title.encode('ascii', 'ignore')

                parameters = {"action": "play", "functional_url": url, "technical_url": url,
                            "title": title, "is_sponsor_only": is_sponsor_only, "next_page_possible": "False", "is_livestream": "True"}

                plugin_url_with_parms = self.plugin_url + '?' + urllib.parse.urlencode(parameters)
                is_folder = False
                # Add refresh option to context menu
                list_item.addContextMenuItems([('Refresh', 'Container.Refresh')])
                # Add our item to the listing as a 3-element tuple.
                listing.append((plugin_url_with_parms, list_item, is_folder))

        # Add our listing to Kodi.
        # Large lists and/or slower systems benefit from adding all items at once via addDirectoryItems
        # instead of adding one by ove via addDirectoryItem.
        xbmcplugin.addDirectoryItems(self.plugin_handle, listing, len(listing))
        # Disable sorting
        xbmcplugin.addSortMethod(handle=self.plugin_handle, sortMethod=xbmcplugin.SORT_METHOD_NONE)
        # Finish creating a virtual folder.
        xbmcplugin.endOfDirectory(self.plugin_handle)