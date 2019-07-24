from flask import request, session
from glob import glob
import os
from common.libs.UrlManage import UrlManager
from common.models.user.User import User, db

def check_login():
	req = request.values
	login_name = req["login_name"]
	login_pwd = req["login_pwd"]
	# print("Name:{}\nPasswd:{}".format(login_name, login_pwd))
	if len(login_name) < 1 or len(login_pwd) < 1:
		return False
	user_info = User.query.filter_by(name=login_name).first()
	# print(user_info)
	if not user_info:
		return False
	else:
		if user_info.pwd == login_pwd:
			session["name"] = user_info.name
			session["type"] = user_info.type
			return True
		else:
			return False

def check_register():
	req = request.values
	login_name = req["login_name"]
	login_pwd = req["login_pwd"]
	login_pwd_2 = req["pwd"]
	if len(login_name) < 1 or len(login_pwd) < 1:
		return False
	if login_pwd != login_pwd_2:
		return False
	new = User(login_name, login_pwd, 2)
	db.session.add(new)
	db.session.commit()
	session["name"] = login_name
	session["type"] = 2
	return True

def init_index():
	data = []
	num = 1
	songNames = os.listdir("./web/static/songs/")
	for songName in songNames:
		info = {}
		info["name"] = songName
		info["id"] = num
		info["image"] = "/static/images/{}.jpg".format(songName)
		data.append(info)
		num += 1
	return data

def get_list(songName):
	songs = os.listdir("./web/static/songs/{}/".format(songName))
	return songs

def createPlayList(folder, name):
	pass

def get_movies():
	movies = os.listdir("./web/static/movies/")
	data = []
	for movie in movies:
		info = {}
		info["name"] = movie.split(".")[0]
		info["image"] = "/static/images/{}.jpg".format(movie.split(".")[0])
		data.append(info)
	return data