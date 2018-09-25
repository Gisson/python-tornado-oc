import tornado.ioloop
import tornado.web



class ExampleHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello world")

def make_app():
    return tornado.web.Application([
        (r'/',ExampleHandler),
        (r'/example',ExampleHandler)
        ])


if __name__ == '__main__':
    app=make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
