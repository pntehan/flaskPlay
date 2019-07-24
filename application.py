from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
import os

class Application(Flask):

	def __init__(self, import_name, template_folder=None, static_folder=None):
		super().__init__(import_name, template_folder=template_folder, static_folder=static_folder)
		self.config.from_pyfile("config.py")
		db.init_app(self)

db = SQLAlchemy()
app = Application(__name__, template_folder=os.getcwd()+"/web/templates/", static_folder=os.getcwd()+"/web/static")
app.config['SECRET_KEY'] = '123456'
manager = Manager(app)

from common.libs.UrlManage import UrlManager
app.add_template_global(UrlManager.buildUrl, "buildUrl")
app.add_template_global(UrlManager.buildStaticUrl, "buildStaticUrl")
app.add_template_global(session, "session")