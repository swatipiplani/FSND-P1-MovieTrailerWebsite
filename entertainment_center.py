'''Display List of Movies on Website and Show their trailers'''
import fresh_tomatoes
import media
# Movie Objects that you want to show on your website
# Add your own favourite movies object
doctor_strange = media.Movie(
    "Doctor Strange",  # Name of the Movie
    "A neurosurgeon after an accident"
    "finds mystical power",  # Story Line of the Movie
    "https://upload.wikimedia.org/wikipedia/en/thumb/c/c7/Doctor_Strange_poster.jpg/220px-Doctor_Strange_poster.jpg",  # NOQA
    # Poster Image of the Movie
    "https://www.youtube.com/watch?v=h7gvFravm4A")  # YouTube URL of the Movie
big_short = media.Movie(
    "Big Short",
    "Four denizens in the world of high-finance predict"
    "the credit and housing bubble collapse of"
    " the mid-2000s, and decide to take on the big banks for"
    "their greed and lack of foresight.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BNDc4MThhN2EtZjMzNC00ZDJmLThiZTgtNThlY2UxZWMzNjdkXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL__QL50.jpg",  # NOQA
    "https://www.youtube.com/watch?v=vgqG3ITMv1Q")
lord_rings = media.Movie(
    "The Lord of the Rings: The Fellowship of the Ring",
    "A meek Hobbit from the Shire and eight"
    "companions set out on a journey to destroy the "
    "powerful One Ring and save Middle Earth from "
    "the Dark Lord Sauron.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BNTEyMjAwMDU1OV5BMl5BanBnXkFtZTcwNDQyNTkxMw@@._V1_UY268_CR0,0,182,268_AL__QL50.jpg",  # NOQA
    "https://www.youtube.com/watch?v=V75dMMIW2B4")
benjamin_button = media.Movie(
    "The Curious Case of Benjamin Button",
    "Tells the story of Benjamin Button, a man who starts"
    "aging backwards with "
    "bizarre consequences.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BNjQ0NTY2ODY2M15BMl5BanBnXkFtZTgwMjE4MzkxMDE@._V1_UX182_CR0,0,182,268_AL__QL50.jpg",  # NOQA
    "https://www.youtube.com/watch?v=O6wP_LKA0DE")
up = media.Movie(
    "Up",
    "Seventy-eight year old Carl Fredricksen travels to Paradise Falls"
    "in his home equipped"
    "with balloons, inadvertently taking a young stowaway.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk3NDE2NzI4NF5BMl5BanBnXkFtZTgwNzE1MzEyMTE@._V1_UX182_CR0,0,182,268_AL__QL50.jpg",  # NOQA
    "https://www.youtube.com/watch?v=ORFWdXl_zJ4")
inside_out = media.Movie(
    "Inside Out",
    "After young Riley is uprooted from her Midwest life and moved to"
    "San Francisco, "
    "her emotions - Joy, Fear, Anger, Disgust and Sadness - "
    "conflict on how best to navigate "
    "a new city, house, and school.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BOTgxMDQwMDk0OF5BMl5BanBnXkFtZTgwNjU5OTg2NDE@._V1_UX182_CR0,0,182,268_AL__QL50.jpg",  # NOQA
    "https://www.youtube.com/watch?v=yRUAzGQ3nSY")


movie_list = [
    doctor_strange,
    big_short,
    lord_rings,
    benjamin_button,
    up,
    inside_out]

fresh_tomatoes.open_movies_page(movie_list)
