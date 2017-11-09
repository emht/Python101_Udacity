#-------------------Import Libraries------------------------------------#
import webbrowser	# To open web browsers for Youtube songs from python
import sys			# To use various system variable and all
import time			# To use time related functions and keep track of time


#----------------------------------------------------------------------#

#-------------------Function Definitions-------------------------------#
def open_browser():
	new = 2		# open in new tab, if possible
	# Open a public url, say Youtube.com
	url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
	webbrowser.open(url, new=new)

	# To open a html file from system,, 
#	url = "file://X://abc/x.html"
#	webbrowser.open(url, new=new)



def pick_random_vevo_link():
	"""
	This function picks any random link for vevo playlists to play and call the open browser function to open up that link.
	
	Make similar function for spotify playlist or so
	"""

def wait(n_seconds):
	""" 
	This function calls the time.wait() to wait for n seconds.
	"""
	time.wait(10)


#-------------------Driving Program-----------------------------------#
if __name__ == "__main__":
	
	# Few Global variables
	break_count = 0
	total_breaks = 3

#----------------------------------------------------------------------#
