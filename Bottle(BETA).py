import os
import sys
os.system('color')
print("\033[1;31m")  # Set text color to bright red
print("""
\033[1m██████╗░░█████╗░████████╗████████╗██╗░░░░░███████╗
██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║░░░░░██╔════╝                              --------------------------------  
██████╦╝██║░░██║░░░██║░░░░░░██║░░░██║░░░░░█████╗░░      (BETA)                  |  credit = eggy#8081 (discord)| 
██╔══██╗██║░░██║░░░██║░░░░░░██║░░░██║░░░░░██╔══╝░░                              |  https://github.com/eggy22   |
██████╦╝╚█████╔╝░░░██║░░░░░░██║░░░███████╗███████╗                              | ---------------------------  |    
╚═════╝░░╚════╝░░░░╚═╝░░░░░░╚═╝░░░╚══════╝╚══════╝                                                                               
(If there is any bug contact me on discord)                """)  

print("\033[0m")  # Reset text color

print("\033[1;34m")  # Set text color to bright blue
print("""━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[1] UrlFlooder\n[2] Webhook Spammer\n[3] Nuker\n[4] IP Address Lookup\n[5] IP Pinger\n[6] IP Loggers\n[7] Screenshot Grabber\n[8] WebHook Remover\n[9] Linkvertise bypasser(NEW)\n[10] Coming Soon..
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
print("\033[0m")  # Reset text color



while True:
    print("\033[1;31m")
    q = input("\n> ")
    if q == "1":
        
        from data import UrlFlooder
        UrlFlooder.start()

    elif q == "2":
     from data import WebhookSpam
    elif q=="3":
        from data import nuke
    elif q == "4":
        from data import ipicker
    elif q == "5":
        from data import pinger
    elif q == "6":
        from data import Loggers
    elif q =="7":
        from data import screen
    elif q =="8":
        from data import webhookremover
    elif q =='9':
        from data import linkvertex
    elif q=='10':
        input("chill my g")

    else:
        print("invalid character")
    

        

        
