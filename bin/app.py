import web
from gothonweb import map

urls = (
    '/game', 'GameEngine',
    '/', 'Index',
)

app = web.application(urls, globals())

# little hack so that debug mode works with sessions
if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store, initializer={'room': None})
    web.config._session = session
else:
    session = web.config._session

render = web.template.render('templates/', base="layout")


class Index(object):
    def GET(self):
        # this is used to "setup" the session with starting values
        session.guesses = 0
        session.room = map.START
        web.seeother("/game")


class GameEngine(object):

        def GET(self):
            if session.room:
                return render.show_room(room=session.room)
            else:
                #why is this here?  Do you need it?
                return render.you_died()

        def POST(self):
            form = web.input(action=None)

            if session.room.name == "Laser Weapon Armory" and session.guesses < 10:
                session.guesses += 1
                print form.action
                print map.code
                if form.action == map.code:
                    session.room = map.the_bridge
                else:
                    session.room = map.laser_weapon_armory
            elif session.guesses == 10:
                session.room = map.generic_death
            # there is a bug here, can you fix it?
            elif session.room and form.action:
                session.room = session.room.go(form.action)

            web.seeother("/game")

if __name__ == "__main__":
    app.run()
