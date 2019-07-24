from application import app
from web.controllers.user.User import route_user
from web.controllers.music.music import route_music
from web.controllers.movie.movie import route_movie
from web.controllers.index import route_index

app.register_blueprint(route_user, url_prefix="/user")
app.register_blueprint(route_music, url_prefix="/music")
app.register_blueprint(route_movie, url_prefix="/movie")
app.register_blueprint(route_index, url_prefix="/")