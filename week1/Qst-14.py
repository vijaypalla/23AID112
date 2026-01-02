# Create an empty list
favorite_movies = []

for i in range(5):
    movie = input(f"Enter favorite movie #{i+1}: ")
    favorite_movies.append(movie)
    
print(f"Your favorite movies are: {favorite_movies}")
