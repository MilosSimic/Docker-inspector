import tornado.ioloop
from middlware import InspectorMiddlware
from heandlers import HomePage

class Application(tornado.web.Application):
    def __init__(self, handlers, settings, start=False):
        tornado.web.Application.__init__(self, handlers, **settings)
        self.start = start

        self.middlware = InspectorMiddlware()
        self.config_port = self.middlware.port()
        self._setup()

        if self.start:
            self.loop()

    def _setup(self):
        self.listen(self.config_port)

    def loop(self):
        if not self.start:
            try:
                tornado.ioloop.IOLoop.instance().start()
            except KeyboardInterrupt:
                tornado.ioloop.IOLoop.instance().stop()
        else:
            print "Already started"


if __name__ == "__main__":
    a = Application([(r"/", HomePage)],dict(debug=True))
    a.loop()
