from flask import Blueprint, render_template
from common.libs.function import init_index, get_list

route_music = Blueprint("music_pages", __name__)

@route_music.route("/")
def index():
	return render_template("music/index.html", title="music", contents=init_index())

@route_music.route("/list-<name>")
def content(name):
	return render_template("music/list.html", title=name, content=get_list(name))

@route_music.route("/<folder>_<name>")
def music(folder, name):
	return render_template("music/music.html", title=name, path="/songs/"+folder+"/"+name)

