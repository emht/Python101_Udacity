"""
class Movie():
	- title
	- storyline
	- poster_image_url
	- trailer_youtube_url

"""
import webbrowser

class Movie():
	# __x__: Tells that the x is special keyword in python
	# self defines the object itself
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.poster_image_url = poster_image
		self.storyline = movie_storyline
		self.trailer_youtube_url = trailer_youtube


	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
