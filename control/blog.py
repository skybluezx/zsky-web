#
# 日志控制器
#

import tornado.web


class BlogHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("../view/blog.html", title="blob")