from webob import Request, Response

class PyFrameApp:
    def __init__(self):
        self.routes = dict()

    def __call__(self, environ, start_response):
        request = Request(environ)
        response = self.handle_request(request)
        return response(environ, start_response)

    def handle_request(self, request):
        response = Response()
        handler = self.routes.get(request.path)
        if handler:
            handler(request, response)
        else:
            self.default_response(response)
        return response

    def default_response(self, response):
        response.status_code = 404
        response.text = "Not Found."

    def route(self, path):
        def wrapper(handler):
            self.routes[path] = handler
            return handler
        return wrapper


