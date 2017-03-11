class RequestHandler:
    def __call__(self, environ, start_response):
        start_response('200 OK', [('Content-Type', 'text/html')])
        response_body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'python')
        return [response_body.encode("utf-8")]
