import tornado.ioloop
import tornado.web
import tornado.options
from middlware import InspectorMiddlware

class HomePage(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello world")

application = tornado.web.Application([
    (r"/", HomePage),

],debug=True)

if __name__ == "__main__":
    application.listen(8888)
    tornado.options.parse_command_line()

    try:
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.instance().stop()
