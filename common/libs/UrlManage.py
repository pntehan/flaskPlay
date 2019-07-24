import time

class UrlManager(object):
	def __init__(self):
		pass

	@staticmethod
	def buildUrl(path):
		return path

	@staticmethod
	def buildStaticUrl(path):
		ver = time.strftime('%Y-%m-%d',time.localtime(time.time()))
		path =  "/static" + path + "?ver=" + ver
		return UrlManager.buildUrl(path)