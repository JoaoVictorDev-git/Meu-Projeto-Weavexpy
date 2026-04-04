from flask_socketio import SocketIO
from .server import *
import json

def _safe(v):
    return json.dumps(v)

def importJS(JS):
    global js
    js = JS



class JavaScript:

    class document:

        @staticmethod
        def write(text):
            return js(f'document.write({_safe(text)});')

        @staticmethod
        def query(selector):
            return f'document.querySelector({_safe(selector)})'

    class window:

        @staticmethod
        def alert(message):
            return js(f'window.alert({_safe(message)});')

        @staticmethod
        def open(url, target="_self"):
            return js(f'window.open({_safe(url)}, {_safe(target)});')

        @staticmethod
        def reload():
            return js('window.location.reload();')

    class console:

        @staticmethod
        def log(data):
            return js(f'console.log({_safe(data)});')

        @staticmethod
        def error(data):
            return js(f'console.error({_safe(data)});')

        @staticmethod
        def warn(data):
            return js(f'console.warn({_safe(data)});')

    @staticmethod
    def setText(selector, text):
        return js(
            f'document.querySelector({_safe(selector)}).textContent = {_safe(text)};'
        )

    @staticmethod
    def setHTML(selector, html):
        return js(
            f'document.querySelector({_safe(selector)}).innerHTML = {_safe(html)};'
        )

    @staticmethod
    def setStyle(selector, prop, value):
        return js(
            f'document.querySelector({_safe(selector)}).style[{_safe(prop)}] = {_safe(value)};'
        )

    @staticmethod
    def addClass(selector, class_name):
        return js(
            f'document.querySelector({_safe(selector)}).classList.add({_safe(class_name)});'
        )

    @staticmethod
    def removeClass(selector, class_name):
        return js(
            f'document.querySelector({_safe(selector)}).classList.remove({_safe(class_name)});'
        )
    
    @staticmethod
    def createElement(tag, parent_selector=None):
        code = f"""
        var el = document.createElement({json.dumps(tag)});
        """
        if parent_selector:
            code += f"""
            document.querySelector({json.dumps(parent_selector)}).appendChild(el);
            """
        return js(code)
    
    @staticmethod
    def addEvent(selector, event, message):
        return js(f"""
            document.querySelector({json.dumps(selector)})
            .addEventListener({json.dumps(event)}, function(){{
                console.log({json.dumps(message)});
            }});
        """)


    class JSSelector:
        def __init__(self, selector):
            self.selector = selector

        def text(self, value):
            js(f'document.querySelector("{self.selector}").textContent = {json.dumps(value)};')
            return self

        def html(self, value):
            js(f'document.querySelector("{self.selector}").innerHTML = {json.dumps(value)};')
            return self

        def style(self, prop, value):
            js(f'document.querySelector("{self.selector}").style[{json.dumps(prop)}] = {json.dumps(value)};')
            return self

        def addClass(self, name):
            js(f'document.querySelector("{self.selector}").classList.add({json.dumps(name)});')
            return self