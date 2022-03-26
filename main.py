import requests
import asyncio
from tasksio import TaskPool
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System



 
async def joinah(inviteCode):
 with open("data/account.txt") as f:
        read = f.read()
        tokens = read.split("\n") 
        for token in tokens: 
            headers = {
	        'authority': 'api.revolt.chat',
            'origin': 'https://app.revolt.chat',
            'referer': 'https://app.revolt.chat/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.3',
            'x-session-token': token
        	}
            res = requests.post(f'https://api.revolt.chat/invites/{inviteCode}',headers=headers,json={})
            if res.status_code == 200:
                print(f"[JOINER] Joined Server on token ---> {token}")
            else:
            
                print(f"[JOINER] Failed Joined Server on token ---> {token}")    
async def spammer(channelid,msg):
 with open("data/account.txt") as f:
        read = f.read()
        tokens = read.split("\n") 
        while True:   
          for token in tokens: 
            headers = {
	        'authority': 'api.revolt.chat',
            'origin': 'https://app.revolt.chat',
            'referer': 'https://app.revolt.chat/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.3',
            'x-session-token': token
        	}
            res = requests.post(f'https://api.revolt.chat/channels/{channelid}/messages',headers=headers,json={'content': msg})
            if res.status_code == 200:
                print(f"[SPAMMER] Sent Message on token ---> {token}")
            else:
                print(f"[SPAMMER] Failed Sent Message on token ---> {token}")    






async def revoltFucker():
 banner1 = """         
    
██████╗ ███████╗██╗   ██╗ ██████╗ ██╗  ████████╗    
██╔══██╗██╔════╝██║   ██║██╔═══██╗██║  ╚══██╔══╝    
██████╔╝█████╗  ██║   ██║██║   ██║██║     ██║       
██╔══██╗██╔══╝  ╚██╗ ██╔╝██║   ██║██║     ██║       
██║  ██║███████╗ ╚████╔╝ ╚██████╔╝███████╗██║       
╚═╝  ╚═╝╚══════╝  ╚═══╝   ╚═════╝ ╚══════╝╚═╝       
                                                    
███████╗██╗   ██╗ ██████╗██╗  ██╗███████╗██████╗    
██╔════╝██║   ██║██╔════╝██║ ██╔╝██╔════╝██╔══██╗   
█████╗  ██║   ██║██║     █████╔╝ █████╗  ██████╔╝   
██╔══╝  ██║   ██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗   
██║     ╚██████╔╝╚██████╗██║  ██╗███████╗██║  ██║   
╚═╝      ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   
                                                    
 1) Joiner
 2) Spammer
 
 """
 Anime.Fade(Center.Center(banner1), Colors.purple_to_red, Colorate.Vertical, enter=True)   
 choice = input("Select Choice [>]")
 if '1' in choice:  
     inviteCode = input('Invite CODE [!] > ')
     await joinah(inviteCode)
     
 elif '2' in choice:
     msg = input("Message to spam? [>]")
     channelid = input("Channel ID [>]")
     await spammer(msg, channelid)
            
     
     
     
if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.run_until_complete(revoltFucker())          
