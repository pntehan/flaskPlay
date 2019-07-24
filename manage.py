from application import manager, app
from flask_script import Server
import www

manager.add_command(
	"runserver",
	Server(host=app.config["SERVER_IP"],
		port=app.config["SERVER_PORT"],
		use_debugger=app.config["DEBUG"],
		use_reloader=app.config["RELOAD"],
		threaded=app.config["THREAD"]))

def main():
	manager.run()

if __name__ == '__main__':
	try:
		import sys
		sys.exit(main())
	except Exception as e:
		import traceback
		traceback.print_exc()
		