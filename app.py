import tornado.ioloop
import tornado.web



class ExampleHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello world")

class SharkHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<html><img src=\"https://cdn0.vox-cdn.com/thumbor/D7eWJa6P3c7wqfBnhLMMGo4qauY=/0x0:750x422/1600x900/cdn0.vox-cdn.com/uploads/chorus_image/image/46801036/sharknado2.0.0.jpg\" /> </html>")

def make_app():
    return tornado.web.Application([
        (r'/',ExampleHandler),
        (r'/example',ExampleHandler)
        (r'/shark',SharkHandler)
        ])


if __name__ == '__main__':
    app=make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
