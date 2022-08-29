#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi


def notfound_404(environ, start_response):
    start_response('404 Not Found', [('Content-type', 'text/plain')])
    return [b'Not Found']

class PathDispatcher:
    def __init__(self):
        self.pathmap = {}

    def __call__(self,environ, start_response):
        path = environ['PATH_INFO']
        params = cgi.FieldStorage(environ['wsgi.input'],environ=environ)

        method = environ['REQUEST_METHOD'].lower()

        environ['params'] = { key:params.getvalue(key) for key in path}
        handler = self.pathmap.get((method,path),notfound_404)
        return handler(environ=environ,start_response=start_response)

    def register(self,method,path,function):
        self.pathmap[method.lower(),path] = function
        return function

import time

_hello_resp = ''''''

def hello_world(environ,start_response):
    start_response('200 OK',[('Content-type','application/xml')])
    resp = _lo