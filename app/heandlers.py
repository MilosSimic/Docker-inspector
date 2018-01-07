import tornado.web

class HomePage(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello my world")

