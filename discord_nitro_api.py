import requests
import json
import time
import os
import random
import threading
import string
from colorama import Fore

green = Fore.GREEN
red = Fore.RED
white = Fore.WHITE
yellow = Fore.YELLOW
blue = Fore.BLUE
purple = Fore.MAGENTA
lblue = Fore.LIGHTBLUE_EX
lmag = Fore.LIGHTMAGENTA_EX

os.system("title Nitro Gen/home")
os.system("mode 75, 15")

def banner():
    print(f"""
    {lmag}███╗   ██╗██╗████████╗██████╗  ████{white}██╗   ██████╗ ███████╗███╗   ██╗
    {lmag}████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══█{white}█╗ ██╔════╝ ██╔════╝████╗  ██║
    {lmag}██╔██╗ ██║██║   ██║   ██████╔╝██║   █{white}█║ ██║  ███╗█████╗  ██╔██╗ ██║
    {lmag}██║╚██╗██║██║   ██║   ██╔══██╗██║   {white}██║ ██║   ██║██╔══╝  ██║╚██╗██║
    {lmag}██║ ╚████║██║   ██║   ██║  ██║╚████{white}██╔╝ ╚██████╔╝███████╗██║ ╚████║
    {lmag}╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚════{white}═╝   ╚═════╝ ╚══════╝╚═╝  ╚═══╝ {white}
    auto run[acive]""")

def auto():
    os.system(f"title Nitro Gen/active")
    print("    ╔[Amount of codes]")
    amount = int(input(f'    ╚[$]~[>{lmag} '))
    global proxy_list
    proxy_list = [
            '95.217.34.209: 3128',
            '211.24.94.205: 80',
            '35.244.81.72: 80',
            '140.227.66.105: 58888',
            '103.11.102.68: 3128',
            '1.186.40.130: 80',
            '157.90.89.99: 3128',
            '51.91.182.143: 80',
            '157.230.53.4: 8080',
            '167.172.184.166: 40065',
            '140.227.62.35: 58888',
            '125.25.40.37: 8080',
            '59.124.224.180: 4378',
            '111.68.40.15: 8080',
            '46.101.173.102: 80',
            '140.227.63.136: 58888',
            '119.15.95.198: 8080',
            '115.85.65.94: 8080',
            '158.101.98.173: 128',
            '185.38.111.1: 8080',
            '182.253.171.31: 8080',		
            '13.114.160.78: 80',
            '217.79.181.109: 443',
            '139.99.76.194: 8080',	
            '91.90.183.234: 8080',
            '149.56.86.231: 80',
            '115.124.115.26: 80',	
            '189.112.111.194: 80']

    
    for i in range(amount):
        RP = random.choice(proxy_list)
        proxies = {
            f"https://": f"{RP}"
        }
        chars = string.ascii_letters + string.digits
        code = ""
        
        for i in range(16):
            code = code + random.choice(chars)

        url = f'https://discord.com/api/v9/entitlements/gift-codes/{code}?with_application=true&with_subscription_plan=true'

        r = requests.get(url, proxies=proxies)
        if 'subcription_plan' in r.text:
            print(f"{white} valid code{green} {code} {white}")
        elif 'access denied' in r.text:
            print(f"{white} bad proxy {yellow} {RP} tried {code} {yellow} {white}")
        else:
            print(f"{white} invalid code{red} {code} {white}")
        
banner()
auto()
