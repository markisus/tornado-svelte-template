import tornado.ioloop
import tornado.web

class NoCacheStaticFileHandler(tornado.web.StaticFileHandler):
    def set_extra_headers(self, path):
        # Disable cache
        self.set_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect("index.html")

def make_app(autoreload):
    static_handler = NoCacheStaticFileHandler if autoreload else tornado.web.StaticFileHandler
    return tornado.web.Application([
        (r'/(.*\.(html|css|map|js))', static_handler, {'path': './public'}),
        (r"/", MainHandler),
    ], autoreload=autoreload)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='tornado web server')
    parser.add_argument('--autoreload', action='store_const', const=True, default=False)
    args = parser.parse_args()
    
    app = make_app(args.autoreload)
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
