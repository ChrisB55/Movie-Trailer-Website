import fresh_tomatoes
import media
# Above we import the two other key files for this project.
# Below we define the variables for each movie instance, including the movie titles, the links for the posters and trialers
toy_story = media.Movie("Toy Story", "Toys come to life and make Pixar lots of money.",
"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
"https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)
avatar = media.Movie("Avatar", "It's a lot like Dune.",
"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
"https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)

selma = media.Movie("Selma", "Civil Rights leaders fight for the passage voting rights legislation.",
"https://upload.wikimedia.org/wikipedia/en/8/8f/Selma_poster.jpg",
"https://www.youtube.com/watch?v=x6t7vVTxaic")

la_la_land = media.Movie("La La Land", "LA-based romance and musical.",
"https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",
"https://www.youtube.com/watch?v=0pdqf4P9MB8")

birdman= media.Movie("Birdman", "Former movie actor stages broadway play while struggling with his mental health.",
"https://upload.wikimedia.org/wikipedia/en/8/8f/Selma_poster.jpg",
"https://www.youtube.com/watch?v=uJfLoE6hanc")

force_awakens = media.Movie("Star Wars: The Force Awakens", "A generation of Star Wars characters are introduced.",
"https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg",
"https://www.youtube.com/watch?v=sGbxmsDFVnE")

movies= [toy_story, avatar, selma, la_la_land, birdman, force_awakens]
fresh_tomatoes.open_movies_page(movies)
#Function takes in movies from above array of movies.  
