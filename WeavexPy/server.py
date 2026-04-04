from flask import Flask, request, send_file
import flask_cors
import flask
import random
from datetime import datetime
from threading import Thread
import json
from flask_socketio import SocketIO
from .dom import *
 
class Request:
    def __init__(self):
        self.form = request.form
        self.method = request.method
        self.files = request.files
        
    def __str__(self):
        return request
    
    def GetElementValueByName (input_name):
        if request.method == 'POST' :
            value = request.form.get(str(input_name))
            return str(value)
        
    def GetElementsForm() :
        return request.form
    
    def MultipleData(input_name):
        return request.form.getlist(str(input_name))
    
    def GetHeaders(ua='User-Agent'): 
        return request.headers.get(str(ua))
    
    def GetCookies(ck):
        return request.cookies.get(str(ck))


class Server:
    def __init__(self, object_app, pages):
        self.app = Flask(object_app)
        self.pages:dict = pages
        self.socketio = SocketIO(self.app, async_mode="threading")
        def js(cod):
            self.socketio.emit("__eval-js__", cod)
        importJS(js)

        @self.app.post("/WeavexPy/events/__JSLOG__")
        def receber_logs_js():
            log = request.get_json(force=True)
            cor = '\033[38;5;208m' if log['tipo'] == 'log' else '\033[31m' if log['tipo'] == 'error' else '\033[34m' if log['tipo'] == 'warn' else '\033[32m' if log['tipo'] == 'info' else '\033[33m'
            time = datetime.now()
            print(f'{cor}{log['mensagem']}\033[0m \n')
            return "ok"

        
        if not isinstance(pages, dict) : print('[ERRO]')
        
    def __img__(self, src, mimetype):
        return send_file(src, mimetype=mimetype)
            
    def veri(self):
        for k, v in self.pages.items():
            endpointNumber = f'{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}'
            route = '/' if k == 'home' else f'/{k}'

            if isinstance(v, str):
                def make_view(html):
                    def view():
                        return html
                    return view

                view_func = make_view(v)
                self.app.add_url_rule(
                    route,
                    endpoint=f"page_{k}{endpointNumber}",
                    view_func=view_func
                )

            elif callable(v):
                v.__name__ = f"page_{k}{endpointNumber}"
                self.app.add_url_rule(
                    route,
                    endpoint=f"page_{k}{endpointNumber}",
                    view_func=v,
                    methods=["GET", "POST"] 
                )

        return self.app
            
cors = flask_cors.CORS
