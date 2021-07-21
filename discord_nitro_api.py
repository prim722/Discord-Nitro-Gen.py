import requests
import json
import time
import os
import random
import threading
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

def menu():
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
        RP = proxy_list
        RP = random.choice(RP)
        proxies = {
            f"https://": f"{RP}"
            }
        base_link = "https://www.discord.gift/"
        check_base_link1 = "https://discord.com/api/v9/entitlements/gift-codes/"
        check_base_link2 = "?with_application=true&with_subscription_plan=true"

        p1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                    "A", "B", "C", "D", "E", "F", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "x", "y", "Z",
                    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",]

        p2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                    "A", "B", "C", "D", "E", "F", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "x", "y", "Z",
                    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",]

        p3 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                    "A", "B", "C", "D", "E", "F", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "x", "y", "Z",
                    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",]

        p4 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                    "A", "B", "C", "D", "E", "F", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "x", "y", "Z",
                    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",]

        p5 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                    "A", "B", "C", "D", "E", "F", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "x", "y", "Z",
                    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",]

        p6 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                    "A", "B", "C", "D", "E", "F", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "x", "y", "Z",
                    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",]

        p7 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                    "A", "B", "C", "D", "E", "F", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "x", "y", "Z",
                    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",]

        p8 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                    "A", "B", "C", "D", "E", "F", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "x", "y", "Z",
                    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",]
        p9 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                    "A", "B", "C", "D", "E", "F", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "x", "y", "Z",
                    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",]

        p10 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                    "A", "B", "C", "D", "E", "F", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "x", "y", "Z",
                    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",]

        p11 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                    "A", "B", "C", "D", "E", "F", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "x", "y", "Z",
                    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",]

        p12 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                    "A", "B", "C", "D", "E", "F", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "x", "y", "Z",
                    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",]

        p13 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                    "A", "B", "C", "D", "E", "F", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "x", "y", "Z",
                    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",]

        p14 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                    "A", "B", "C", "D", "E", "F", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "x", "y", "Z",
                    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",]

        p15 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                    "A", "B", "C", "D", "E", "F", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "x", "y", "Z",
                    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",]

        p16 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                    "A", "B", "C", "D", "E", "F", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "x", "y", "Z",
                    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",]

        p1 = random.choice(p1)
        p2 = random.choice(p2)
        p3 = random.choice(p3)
        p4 = random.choice(p4)
        p5 = random.choice(p5)
        p6 = random.choice(p6)
        p7 = random.choice(p7)
        p8 = random.choice(p8)
        p9 = random.choice(p9)
        p10 = random.choice(p10)
        p11 = random.choice(p11)
        p12 = random.choice(p12)
        p13 = random.choice(p13)
        p14 = random.choice(p14)
        p15 = random.choice(p15)
        p16 = random.choice(p16)

        code = base_link + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16
        url = f'https://discord.com/api/v9/entitlements/gift-codes/{code}?with_application=true&with_subscription_plan=true'

        r = requests.get(url, proxies=proxies)
        if 'subcription_plan' in r.text:
            print(f"{white} valid code{green} {code} {white}")
        elif 'access denied' in r.text:
            print(f"{white} bad proxy {yellow} {RP} tried {code} {yellow} {white}")
        else:
            print(f"{white} invalid code{red} {code} {white}")
        
menu()
auto()