'''File handles all the work related to Movie Class'''
import webbrowser
class Movie():
    '''Movie Class'''
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        '''Method to initialise Movie Class
               Parameters:
               movie_title (str): represent Movie Title
               movie_storyline (str): represent Movie Storyline
               poster_image (str): represent Movie Poster Image
               trailer_youtube (str): represent Movie Trailer YouTube URL
        '''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    def show_trailer(self):
        '''Show Movie Trailer'''
        webbrowser.open(self.trailer_youtube_url)
