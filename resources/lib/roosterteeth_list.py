#
# Imports
#
from BeautifulSoup import BeautifulSoup
from roosterteeth_const import __addon__, __settings__, __language__, __images_path__, __date__, __version__
import requests
import os
import re
import sys
import urllib, urllib2
import urlparse
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin

reload(sys)  
sys.setdefaultencoding('utf8')

#
# Main class
#
class Main:
	#
	# Init
	#
	def __init__( self ) :
		# Get plugin settings
		self.DEBUG = __settings__.getSetting('debug')
		
		if (self.DEBUG) == 'true':
			xbmc.log( "[ADDON] %s v%s (%s) debug mode, %s = %s, %s = %s" % ( __addon__, __version__, __date__, "ARGV", repr(sys.argv), "File", str(__file__) ), xbmc.LOGNOTICE )

		# Parse parameters
		#self.plugin_category = urlparse.parse_qs(urlparse.urlparse(sys.argv[2]).query)['plugin_category'][0]
		self.video_list_page_url = urlparse.parse_qs(urlparse.urlparse(sys.argv[2]).query)['show_url'][0]
		self.next_page_possible = urlparse.parse_qs(urlparse.urlparse(sys.argv[2]).query)['next_page_possible'][0]
	
		if (self.DEBUG) == 'true':
			xbmc.log( "[ADDON] %s v%s (%s) debug mode, %s = %s" % ( __addon__, __version__, __date__, "self.video_list_page_url", str(self.video_list_page_url) ), xbmc.LOGNOTICE )
		
		#
		# Get the videos...
		#
		self.getVideos()
	
	#
	# Get videos...
	#
	def getVideos( self ) :
		#
		# Init
		#
		#pos_in_html_source = 0
		previous_video_page_url = ''
		# 
		# Get HTML page
		#
		response = requests.get(self.video_list_page_url)
 		html_source = response.text
		html_source = html_source.encode('utf-8', 'ignore')
	
		# Parse response
		soup = BeautifulSoup( html_source )
		
		pos_of_recently_added_videos = str(html_source).find('Recently Added Videos')
		xbmc.log('pos of recently added videos' + str(pos_of_recently_added_videos))
		pos_of_all_time_favorites = str(html_source).find('All-Time Favorites')
		xbmc.log('pos of All-Time Favorites' + str(pos_of_all_time_favorites))
		pos_of_episodes = str(html_source).find('tab-episodes')
		xbmc.log('pos of episodes' + str(pos_of_episodes))

		#<li>
		#	<a href="http://ah.roosterteeth.com/episode/red-vs-blue-season-13-episode-2">
		# 			<div class="block-container">
		# 				<div class="image-container">
		# 					<img src="//s3.amazonaws.com/cdn.roosterteeth.com/uploads/images/bfa39842-943e-49ea-9207-e71efe9544d2/md/ep10610.jpg">
		# 				</div>
		# 				<div class="watch-status-container">
		# 				</div>
		# 				<div class="play-button-container">
		# 					<p class="play-circle"><i class="icon ion-play"></i></p>
		# 					<p class="timestamp">8:11</p>
		# 				</div>
		# 			</div>
		#		<p class="name">Episode 2</p>
		#	</a>
		#	<p class="post-stamp">3 months ago</p>
		#</li>
		
		episodes = soup.findAll('li')
		
		if (self.DEBUG) == 'true':
			xbmc.log( "[ADDON] %s v%s (%s) debug mode, %s = %s" % ( __addon__, __version__, __date__, "len(episodes)", str(len(episodes)) ), xbmc.LOGNOTICE )
		
		#pos_in_url = 0
		
		for episode in episodes:
			# Skip if the recently-added url
 			if str(episode).find('recently-added') >= 0:
 				continue
# 				xbmc.log('h3 found')
# 				if str(episode).find('Recently Added Videos') >= 0:
# 					xbmc.log('Recently Added Videos found')
# 				continue
# 			
			# Skip an episode if it does not contain class="name"
			pos_classname = str(episode).find('class="name"')
			if pos_classname == -1:
				continue

			video_page_url = episode.a['href']
			
			if (self.DEBUG) == 'true':
				xbmc.log( "[ADDON] %s v%s (%s) debug mode, %s = %s" % ( __addon__, __version__, __date__, "video_page_url", str(video_page_url) ), xbmc.LOGNOTICE )
			
			# Skip a video_page_url is empty
			if video_page_url == '':
				continue
			
			# Skip episode if it's the same as the previous one
			if video_page_url == previous_video_page_url:
				continue
			else:
				previous_video_page_url = video_page_url
			
#  			xbmc.log('video_page_url' + str(video_page_url))
#  			#video_page_url = str(video_page_url).replace('www.','') 
# 			#xbmc.log('video_page_url altered' + str(video_page_url))
# 
#  			#pos_of_url = str(html_source).find(str(video_page_url), pos_in_html_source)
#  			xbmc.log('pos of html source' + str(pos_in_html_source))
#  			pos_of_url = str(html_source).find(str(video_page_url), pos_in_html_source)
#  			xbmc.log('pos of url' + str(pos_of_url))
#  			
#  			if pos_of_url == -1:
#  				continue
# #  				xbmc.log('zzz' + html_source[pos_in_html_source:])
# #  				sys.exit()
# #  				pos_in_html_source = pos_in_html_source + 1
# #  				continue
#  			
#  			if pos_of_url >= pos_of_episodes:
#  				pos_in_html_source = pos_of_url
#  				pos_in_html_source = pos_in_html_source + 1
#  				xbmc.log('pos html:' + str(pos_in_html_source))
#  				pass
#  			else:
#  				pos_in_html_source = pos_of_url
#  				pos_in_html_source = pos_in_html_source + 1
#  				continue

# 				xbmc.log( "aaaa" + str(html_source) )
#  				sys.exit()
#  				continue
# 				xbmc.log('stopping!')
#  				sys.exit()
			
# 			if pos_of_url >= pos_of_episodes:
# 				pos_of_url = pos_in_url + 1
# 				xbmc.log('new' + str(pos_in_url))
# 				pos_in_html_source = pos_in_url
# 				xbmc.log('new pos in html source:' + str(pos_in_html_source))
# 				pass
# 			#elif pos_of_url >= pos_of_recently_added_videos and pos_of_url <= pos_of_all_time_favorites:
# 			elif pos_of_url >= pos_of_recently_added_videos:			
# 		  		pos_of_url = pos_in_url + 1
# 	 			#pos_in_html_source = pos_in_url
# 	 		 	xbmc.log('neww pos in html source:' + str(pos_in_html_source))
#  			 	pass
#  			else:
#  				continue
 					
#  			if pos_of_url == -1:
# 	 			video_page_url = str(video_page_url).replace('www.','') 
# 				xbmc.log('video_page_url altered' + str(video_page_url))	
# 	  			pos_of_url = str(html_source).find(str(video_page_url), pos_in_html_source)
# 	  			if pos_of_url == -1:
# 		  			xbmc.log('stopping!')
#   					sys.exit()
#   				else:
#   					xbmc.log('stopping for now')
#   					sys.exit()	
# #   				xbmc.log('skipping1')
# #   				xbmc.log('pos_in_html_source:' + str(pos_in_html_source))
# #   				continue
#   			else:
#   				if pos_of_url < pos_of_recently_added_videos:
#   					xbmc.log('skipping2')
#   					continue
#   				else:
#  			  		pos_in_html_source = pos_of_url + 1
 			
 			#sys.exit()
 				
# 			pos_of_url = str(html_source).find(video_page_url, pos_in_html_source)
# 			xbmc.log('pos of url' + str(pos_of_url))
# 			if pos_of_url == -1:
# 				#if no url was found, retry search without 'www.' in the video_page_url
# 				video_page_url = str(video_page_url).replace('www.','')
# 				xbmc.log('retry video_page_url' + str(video_page_url))
# 				pos_of_url = str(html_source).find(video_page_url, pos_in_html_source)
# 				xbmc.log('retry pos of url' + str(pos_of_url))
# 				#xbmc.log('zzzzzzzzzz' + html_source[pos_in_html_source:])
# 				if pos_of_url >= 0:
# 					pos_in_html_source = pos_of_url + 1 
# 			else:
# 				#set the pos_in_html_source further than the just found pos_in_url
# 				pos_in_html_source = pos_of_url + 1 
# 				
# 			xbmc.log('pos of html_source' + str(html_source))
# 			
# 			# Skip an episode if it does not come after tab-episodes
# 			if pos_of_url < pos_of_episodes:
# 				continue
			
			try:
				thumbnail_url = "https:" + episode.img['src']
			except:
				thumbnail_url = ''
			
			title = str(episode)[pos_classname + len('class="name"') + 1:]
			pos_smallerthan = title.find("<")
			title = title [0:pos_smallerthan]

			#Clean up title
			title = title.encode('utf-8')
			title = title.replace('-',' ')
			title = title.replace('/',' ')
			title = title.replace(' i ',' I ')
			title = title.replace(' ii ',' II ')
			title = title.replace(' iii ',' III ')
			title = title.replace(' iv ',' IV ')
			title = title.replace(' v ',' V ')
			title = title.replace(' vi ',' VI ')
			title = title.replace(' vii ',' VII ')
			title = title.replace(' viii ',' VIII ')
			title = title.replace(' ix ',' IX ')
			title = title.replace(' x ',' X ')
			title = title.replace(' xi ',' XI ')
			title = title.replace(' xii ',' XII ')
			title = title.replace(' xiii ',' XIII ')
			title = title.replace(' xiv ',' XIV ')
			title = title.replace(' xv ',' XV ')
			title = title.replace(' xvi ',' XVI ')
			title = title.replace(' xvii ',' XVII ')
			title = title.replace(' xviii ',' XVIII ')
			title = title.replace(' xix ',' XIX ')
			title = title.replace(' xx ',' XXX ')
			title = title.replace(' xxi ',' XXI ')
			title = title.replace(' xxii ',' XXII ')
			title = title.replace(' xxiii ',' XXIII ')
			title = title.replace(' xxiv ',' XXIV ')
			title = title.replace(' xxv ',' XXV ')
			title = title.replace(' xxvi ',' XXVI ')
			title = title.replace(' xxvii ',' XXVII ')
			title = title.replace(' xxviii ',' XXVIII ')
			title = title.replace(' xxix ',' XXIX ')
			title = title.replace(' xxx ',' XXX ')
			title = title.replace('  ',' ')
			title = title.replace('  ',' ')
			#welcome to characterset-hell
			title = title.replace('&amp;#039;',"'")
			title = title.replace('&amp;#39;',"'")
			title = title.replace('&amp;quot;','"')
			title = title.replace("&#039;","'")
  			title = title.replace("&#39;","'")
  			title = title.replace('&amp;amp;','&')
  			title = title.replace('&amp;','&')
  			title = title.replace('&quot;','"')
  		 	title = title.replace('&ldquo;','"')
  		  	title = title.replace('&rdquo;','"')
  		  	title = title.replace('&rsquo;',"'")
  		  	
			# Add to list...
			parameters = {"action" : "play", "video_page_url" : video_page_url}
			url = sys.argv[0] + '?' + urllib.urlencode(parameters)
			listitem = xbmcgui.ListItem( title, iconImage="DefaultVideo.png", thumbnailImage=thumbnail_url )
			listitem.setInfo( "video", { "Title" : title, "Studio" : "roosterteeth" } )
			folder = False
			xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ] ), url = url, listitem=listitem, isFolder=folder)
  		
#		xbmc.log('zzzzzzzzz' + str(html_source))
		
		# Disable sorting...
		xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_NONE )
 		
		# End of directory...
		xbmcplugin.endOfDirectory( handle=int( sys.argv[ 1 ] ), succeeded=True )