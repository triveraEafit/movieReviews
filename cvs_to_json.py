import pandas as pd
import json

df = pd.read_csv('movies_initial.csv')


df.to_json('movies_initial.json', orient='records')

with open('movies_initial.json') as file:
    movies = json.load(file)

for i in range(100):
    movie = movies[i]
    print(movie.title)
    break
