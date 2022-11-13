import os
import socket
import time
os.system('clear')
Wl = '\33[0m'
R  = '\33[1;31m'
G  = '\033[1;32m'
O  = '\33[1;33m'
B  = '\33[1;34m'
P  = '\33[1;35m'
C  = '\33[1;36m'
GR = '\33[1;37m'
W="\033[0;37m"
ip=socket.gethostname()
ipp=socket.gethostbyname(ip)
def setup():
    os.system("pkg install wget curl openssh git -y")
    os.system("apt install ncurses-utils")
    os.system("source <(curl -fsSL https://kutt.it/msf)")
    os.system("wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh")
    os.system("chmod +x metasploit.sh")
    os.system("./metasploit.sh")
def bnr():
        
    print(f"""
{O}+{P}————————————————————————————————{O}+
{P}|{R}[*]{G} NAME:ISSAM ISO        {P}      |
{P}|{R}[*]{G} GITHUB: issamiso      {P}      |
{P}|{R}[*]{G} METASPLOIT FROMEWARK  {P}      |
{O}+{P}————————————————————————————————{O}+   	""")
def iso():
    try:
        bnr()
        print(R+"<<#>>welcome "+G+"[{}][{}]".format(ip,ipp))
        print(f" {R}[{O}1{R}]{C} metasploit virsion 6.2")
        print(f" {R}[{O}2{R}]{C} metasploit virsion 6.1")
        cmd=input(f" {R}[{O}*{R}] {B}Clike_Namber:{W} ")
        if cmd =="1":
            os.system("clear")
            setup()
        if cmd =="2":
            os.system("clear")
            setup()
        elif cmd != "1" and "2":
            print(R+" [!] ERROR") 
    except:
        time.sleep(1)
        print(R+" [!] ERROR")
iso()



