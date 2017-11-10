import media
import fresh_tomatoes	# in same file folder so...

toy_story = media.Movie("Toy Story",
						"A story about living toy",
						"http://www.imagespourtoi.com/lesimages/toy-story/image-toy-story-3.jpg",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
					 "Marine on alien planet",
					 "https://i.ytimg.com/vi/fUWrhetZh9M/maxresdefault.jpg",
					 "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#print(toy_story.storyline)
#print(avatar.storyline)
#avatar.show_trailer()

movies = [toy_story, avatar]	# Movie() object list to call for webpage rendering
fresh_tomatoes.open_movies_page(movies)
