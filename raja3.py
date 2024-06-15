# Decompiled by sukhix3pawan baja tool crack cython-311.so

from urllib import response
import mechanize
import os
import datetime
import getpass
import time
import sys
import requests
from time import sleep
browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36')]
browser.set_handle_refresh(False)
url = 'https://m.facebook.com/login'

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('xdg-open https://www.facebook.com/Mr.Raja6970')

def sp(stri):
    for letter in stri:
        print(letter, end='')
        sys.stdout.flush()
        sleep(0.03)
logo = '\x1b[1;36m𝙒𝙀𝙇𝘾𝙊𝙈𝙀 𝙏𝙊 𝙏𝙃𝙀 𝙍𝙊𝙈𝘼 𝙍𝙐𝙇𝙀𝙓 𝙏𝙊𝙊𝙇\n\n\x1b[1;32m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\x1b[1;37m๑۩♡۩๑\x1b[1;32m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\n\x1b[1;30m __  __  _      __    __  _     _     ___  _\n\x1b[1;30m/  _\\/  _ \\/ \\_/|/  _ \\  /  _\\/ \\ /\\/ \\   /  _/\\  \\//\n\x1b[1;30m|  \\/|| / \\|| |\\/||| / \\|  |  \\/|| | ||| |   |  \\   \\  / \n\x1b[1;30m|    /| \\/|| |  ||| |-||  |    /| \\/|| |/\\|  /_  /  \\ \n\x1b[1;30m\\/\\\\_/\\/  \\|\\/ \\|  \\/\\\\_/\\_/\\_\\/__/\\\n                                         \n\x1b[1;32m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\x1b[1;37m๑۩♡۩๑\x1b[1;32m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\n\x1b[1;36m━▷ \x1b[1;36m𝙊𝙒𝙉𝙀𝙍    \x1b[1;36m◈✙◈\x1b[1;33mMR RAJA\n\x1b[1;36m━▷ \x1b[1;36m𝙏𝙀𝘼𝙈     \x1b[1;36m◈✙◈\x1b[1;33mTEAM OF ROMA RULEX\n\x1b[1;36m━▷ \x1b[1;36m𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆  \x1b[1;36m◈✙◈ \x1b[1;33mfb.com/Mr.Raja6970\n\x1b[1;36m━▷ \x1b[1;36m𝙎𝙏𝘼𝙏𝙐𝙎  \x1b[1;36m◈✙◈ \x1b[1;33mCONVO LOADER TOOL\n\x1b[1;36m━▷ \x1b[1;36m𝙑𝙀𝙍𝙎𝙄𝙊𝙉  \x1b[1;36m◈✙◈ \x1b[1;33m9.0\n\x1b[1;36m━▷ \x1b[1;36m𝙁𝙀𝙀𝙇 𝙏𝙃𝙀 𝙋𝙊𝙒𝙀𝙍 𝙈𝙍 𝙍𝘼𝙅𝘼 𝙊𝙒𝙉𝙀𝙍 𝙊𝙁 𝙍𝙊𝙈𝘼 𝙍𝙐𝙇𝙀𝙓 \n\x1b[1;32m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\x1b[1;37m๑۩♡۩๑\x1b[1;32m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●'

def approval():
    os.system('git pull')
    time.sleep(1)
    uuid = str(os.geteuid()) + 'DS' + str(os.geteuid())
    id = 'ROMA-' + ''.join(uuid)
    os.system('clear')
    print(logo)
    sp('\x1b[1;37m [\x1b[36m•\x1b[1;37m] You Need Approval To Use This Tool   \x1b[1;37m')
    print('\x1b[1;37m [\x1b[36m•\x1b[1;37m] Your Key :\x1b[36m ' + id)
    time.sleep(0.1)
    print('\x1b[1;37m----------------------------------------------')
    try:
        httpCaht = requests.get('https://romarulex.blogspot.com/p/n3w-ch4t-64-bit.html').text
        if id in httpCaht:
            sp('\x1b[1;97m >> Your Key Has Been Approved !!!')
            msg = str(os.geteuid())
            time.sleep(1)
        else:
            sp('\x1b[1;97m >> Sorry Your Key Has Not Been Approved ')
            time.sleep(0.1)
            input('IF U WANT TO BUY THEN PRESS ENTER ')
            tks = 'Hello%20Sir%20!%20Please%20Approve%20My%20Token%20The%20Token%20Is%20:%20' + id
            (os.system('am start https://wa.me/+923040176170?text=' + tks), approval())
            time.sleep(1)
            exit()
    except Exception as e:
        print(e)
        sp(' >> Unable To Fetch Data From Server ')
        time.sleep(2)
        exit()
attemps = 0
if attemps < 12345677901:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if username == 'Roma-70':
        if password == '6970':
            print('You have successfully logged in.')
    print('Incorrect Please Trying ')
    attemps += 1
os.system('clear')

def login():
    browser.open(url)
    browser.select_form(nr=0)
    browser.form['email'] = USERNAME
    browser.form['pass'] = PASSWORD
    r = browser.submit()
    f = open('login.html', 'wb')
    f.write(r.read())
    f.close()
    browser.select_form(nr=0)
    print('\x1b[1m\x1b[36m', end='')
    print('\x1b[1;32m[+]================================[+]')
    sp('\x1b[1;32m[?] Enter the 2 factor code by google authenticator\n')
    print('\x1b[1;32m[+]================================[+]')
    apr = str(input('\x1b[1;32m[?] Enter Code : '))
    try:
        browser.form['approvals_code'] = apr
    except mechanize._form_controls.ControlNotFoundError:
        print('Wrong password or some shit, check generated file')
        f = open('epage_' + str(USERNAME) + '.html', 'wb')
        f.write(r.read())
        f.close()
        exit(1)
    r = browser.submit()
    browser.select_form(nr=0)
    try:
        browser.form['name_action_selected'] = ['save_device']
    except mechanize._form_controls.ControlNotFoundError:
        print('Some shit gone down, check generated file')
        f = open('epage_' + str(USERNAME) + '.html', 'wb')
        f.write(r.read())
        f.close()
        exit(1)
    r = browser.submit()
    f = open('full_login_' + str(USERNAME) + '.html', 'wb')
    f.write(r.read())
    f.close()

def findtextchat(curl):
    r = browser.open(curl)
    x = browser.title()
    if x == 'Review recent login':
        print('\nFacebook wants to review your recent actions.\nPlease fix that and then re run the program.')
        exit(1)
    if x == 'Login approval needed':
        print('\nYour account is stuck on verification\nPlease do it and then re run the program.')
        exit(1)
    if x == 'Epsilon':
        print('\nYour account got locked, recover it kindly and re run the script.')
        exit(1)

def sendtextconvo(comment):
    try:
        browser.select_form(nr=1)
    except mechanize._mechanize.FormNotFoundError:
        print('Some error occured while finding text area, please check your account')
        exit(1)
    try:
        browser.form['body'] = comment
    except mechanize._form_controls.ControlNotFoundError:
        print('Some error occured while filling text, please check your account')
        exit(1)
    r = browser.submit()
    e = datetime.datetime.now()
    print('\x1b[1;32m', end='')
    print(e.strftime('MESSEGE SEND SUCCESSFUL :: Date - %d/%m/%Y  Time - %I:%M:%S %p'))
    print('>>  WELCOME TO ROMA RULEX :: ', hater, line, '\n')
approval()
os.system('clear')
print('\x1b[1;32m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\x1b[1;37m๑۩♡۩๑\x1b[1;32m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●')
print('\x1b[1;33;40m', end='')
print(logo)
print('  ☾⋆                                           ⋆☽ ')
sp('\x1b[1;32m[+] \x1b[1;32m𝗟𝗢𝗚𝗜𝗡 𝗙𝗕 𝗜𝗗 𝗧𝗬𝗣𝗘 𝗡𝗨𝗠𝗕𝗘𝗥 & 𝗘𝗠𝗔𝗜𝗟 𝗔𝗡𝗗 𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗 \n')
print('  ☾⋆                                           ⋆☽ ')
print('\x1b[1;32m[+]================================[+]')
USERNAME = str(input('\x1b[1;32m[+] 𝗧𝗬𝗣𝗘 𝗡𝗨𝗠𝗕𝗘𝗥 & 𝗘𝗠𝗔𝗜𝗟  : '))
print('\x1b[1;33;40m', end='')
print('\x1b[1;32m[+]================================[+]')
sp('\x1b[1;32m[+] \x1b[1;32m𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟 \n')
print('\x1b[1;32m[+]================================[+]')
PASSWORD = str(input('\x1b[1;32m[?] 𝗧𝗬𝗣𝗘 𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗 : '))
login()
print('\x1b[1;34;40m', end='')
print('\x1b[1;32m[+]================================[+]')
sp('\x1b[1;32m[?] \x1b[1;32mEnter Chat/inbox Link\n')
print('\x1b[1;32m[+]================================[+]')
cid = str(input('\x1b[1;32m[?] \x1b[1;32mEnter Link : '))
curl = 'https://m.facebook.com/messages/t/' + str(cid)
print('\x1b[1;34;40m', end='')
print('\x1b[1;32m[+]================================[+]')
sp('\x1b[1;32m[?] \x1b[1;32mEnter File Name\n')
print('\x1b[1;32m[+]================================[+]')
np = str(input('\x1b[1;32m[?] \x1b[1;32mEnter File Name : '))
f = open(np, 'r')
lines = f.readlines()
f.close()
print('\x1b[1;33;40m', end='')
print('\x1b[1;32m[+]================================[+]')
hater = input(' [+] Haters Name : ')
print('\x1b[1;33;40m', end='')
print('\x1b[1;32m[+]================================[+]')
sp('\x1b[1;32m[?] \x1b[1;32mEnter The Time Delay In Seconds\n')
print('\x1b[1;32m[+]================================[+]')
t = int(input('\x1b[1;32m[?] \x1b[1;32mEnter Time : '))
os.system('clear')
print(logo)
count = 0
while True:
    try:
        for line in lines:
            if len(line) > 3 and count != 0:
                sleep(t)
                findtextchat(curl)
                sendtextconvo(hater + line)
                count += 1
                if count % 10 == 0:
                    sleep(1)
                    clear()
                    print('\x1b[1;32m')
    except Exception as e:
        print(e)
        sleep(3)
