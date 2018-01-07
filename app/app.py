import tornado.ioloop
import tornado.web
import tornado.options
import docker
import json

cli = docker.from_env()

class HomePage(tornado.web.RequestHandler):
    def get(self):

        images = cli.images()

        self.write(json.dumps(images))

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
