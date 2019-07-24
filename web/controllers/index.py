from flask import Blueprint, render_template

route_index = Blueprint("index_pages", __name__)

@route_index.route("/")
def index():
	return render_template("/index.html", title="Home")