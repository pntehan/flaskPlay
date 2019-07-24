from flask import Blueprint, request, render_template, redirect, session
from common.libs.function import check_login, check_register

route_user = Blueprint("user_pages", __name__)

@route_user.route("/login", methods=["GET", "POST"])
def login():
	if request.method == "GET":
		return render_template("user/login.html", title="login")
	elif request.method == "POST":
		if check_login():
			return redirect("/")
		else:
			return "<h1>用户名或者密码错误...</h1>"

@route_user.route("/register", methods=["GET", "POST"])
def register():
	if request.method == "GET":
		return render_template("user/register.html", title="register")
	elif request.method == "POST":
		if check_register():
			return redirect("/play/")
		else:
			return "<h1>两次密码输入错误...</h1>"

@route_user.route("/edit", methods=["GET", "POST"])
def edit():
	if request.method == "GET":
		return render_template("user/edit.html")
	elif request.method == "POST":
		return "Editting..."

@route_user.route("/reset_pwd", methods=["GET", "POST"])
def reset_pwd():
	if request.method == "GET":
		return render_template("user/reset_pwd.html")
	elif request.method == "POST":
		return "Editting..."

@route_user.route("/loginout")
def loginout():
	session.clear()
	return redirect("/play/")

