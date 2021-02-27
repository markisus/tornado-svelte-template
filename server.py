import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect("index.html")

def make_app():
    return tornado.web.Application([
        (r'/(.*\.(html|css|map|js))', tornado.web.StaticFileHandler, {'path': './public'}),
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
