import requests, colorama, ctypes, time, os
from colorama import Fore, Back, Style

colorama.init(autoreset=True)
ctypes.windll.kernel32.SetConsoleTitleW("bye bye linkvertise ~ array")

def bypass():
    link = input(f"{Fore.LIGHTBLUE_EX}[?]{Fore.WHITE} Linkvertise link: ")

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    }

    try:
        response = requests.get(f"https://bypass.bot.nu/bypass2?url={link}", headers=headers)
        original_link = response.json()["destination"]
        print(f"{Fore.LIGHTGREEN_EX}[!]{Fore.WHITE} Original Link: {original_link}")
        input(f"\n{Fore.LIGHTBLACK_EX}Press anything to continue")
        os.system('cls')
        bypass()
    except:
        print(f"{Fore.LIGHTRED_EX}[!]{Fore.WHITE} An unexpected error occurred")
        time.sleep(1)
        os.system('cls')
        bypass()
bypass()