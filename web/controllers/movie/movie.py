from flask import Blueprint, render_template
from common.libs.function import get_movies

route_movie = Blueprint("movie_pages", __name__)

@route_movie.route("/")
def index():
	return render_template("movie/index.html", title="movie", contents=get_movies())

@route_movie.route("/<name>")
def movie(name):
	return render_template("movie/movie.html", title=name, path="/movies/"+"/"+name+".mp4")