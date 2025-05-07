# Project Title

A movie analyzer, its main objective is to take a list of movies from a csv and give recomendations.

---

## Features

- Provides a top list of movies classified as fresh with function top_certified_fresh_movies
  by default the function returns the top 10 movies but with the extra parameter you can change the count
- It allows you to start a very simple rest service with flask so you can pull the movies list http://localhost:5000/movies/top
- It also includes a script to print the top ten fresh movies
---

##  Installation
poetry install

## Run top ten script
cd scripts
python top_movies.py 

## Run server 
poetry run start-server

## Run tests