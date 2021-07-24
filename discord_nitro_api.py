import requests
import os
import random
import string
from colorama import Fore

green = Fore.GREEN
red = Fore.RED
white = Fore.WHITE
yellow = Fore.YELLOW
lmag = Fore.LIGHTMAGENTA_EX

os.system("title Nitro Gen")
os.system("mode 75, 15")

print(f"""
{lmag}███╗   ██╗██╗████████╗██████╗  ████{white}██╗   ██████╗ ███████╗███╗   ██╗
{lmag}████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══█{white}█╗ ██╔════╝ ██╔════╝████╗  ██║
{lmag}██╔██╗ ██║██║   ██║   ██████╔╝██║   █{white}█║ ██║  ███╗█████╗  ██╔██╗ ██║
{lmag}██║╚██╗██║██║   ██║   ██╔══██╗██║   {white}██║ ██║   ██║██╔══╝  ██║╚██╗██║
{lmag}██║ ╚████║██║   ██║   ██║  ██║╚████{white}██╔╝ ╚██████╔╝███████╗██║ ╚████║
{lmag}╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚════{white}═╝   ╚═════╝ ╚══════╝╚═╝  ╚═══╝ {white}
""")

def auto():
    print("    ╔[Amount of codes]")
    amount = int(input(f'    ╚[$]~[>{lmag} '))
    with open(f'proxies.txt', 'r') as f:
        p_list = f.read()
        p_list.split(',')

    for i in range(amount):
        RP = random.choice(p_list)
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
        
auto()
