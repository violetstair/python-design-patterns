# 모델 뷰 컨트롤러 패턴 사용 사례

import tornado
import tornado.web
import tornado.ioloop
import tornado.httpserver
import sqlite3


class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        query = "select * from task"
        todos = _execute(query)
        self.render('index.html', todos=todos)


class NewHandler(tornado.web.RequestHandler):

    def post(self):
        name = self.get_argument('name', None)
        query = "create table if not exists task (id INTEGER PRIMARY KEY, name TEXT, status NUMERIC)"
        _execute(query)
        query = "insert into task (name, status) values ('%s', %d)" % (name, 1)
        _execute(query)
        self.redirect('/')


class UpdateHandler(tornado.web.RequestHandler):

    def get(self, id, status):
        query = "update task set status=%d where id=%s" % (int(status), id)
        _execute(query)
        self.redirect('/')


class DeleteHandler(tornado.web.RequestHandler):

    def get(self, id):
        query = "delete from task where id=%s" % id
        _execute(query)
        self.redirect('/')


class RunApp(tornado.web.RequestHandler):

    def __init__(self):
        Handlers = [
            (r'/', IndexHandler),
            (r'/todo/new', NewHandler),
            (r'/todo/update/(\d+)/status/(\d+)', UpdateHandler),
            (r'/todo/delete/(\d+)', DeleteHandler),
        ]
        settings = dict(
            debug=True,
            template_path='templates',
            static_path="static",
        )
        tornado.web.Application.__init__(self, Handlers, **settings)


if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(RunApp())
    http_server.listen(5000)
    tornado.ioloop.IOLoop.instance().start()
