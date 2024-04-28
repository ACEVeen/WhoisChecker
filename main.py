from colorama import *
import requests
import json
import sys

init(autoreset=True)

print(f"""{Fore.RED}
 █     █░ ██░ ██  ▒█████   ██▓  ██████
▓█░ █ ░█░▓██░ ██▒▒██▒  ██▒▓██▒▒██    ▒
▒█░ █ ░█ ▒██▀▀██░▒██░  ██▒▒██▒░ ▓██▄   
░█░ █ ░█ ░▓█ ░██ ▒██   ██░░██░  ▒   ██▒
░░██▒██▓ ░▓█▒░██▓░ ████▓▒░░██░▒██████▒▒
░ ▓░▒ ▒   ▒ ░░▒░▒░ ▒░▒░▒░ ░▓  ▒ ▒▓▒ ▒ ░
  ▒ ░ ░   ▒ ░▒░ ░  ░ ▒ ▒░  ▒ ░░ ░▒  ░ ░
  ░   ░   ░  ░░ ░░ ░ ░ ▒   ▒ ░░  ░  ░ 
    ░     ░  ░  ░    ░ ░   ░        ░ 

{Fore.BLUE}@author ACE Veen ~ www.imhatimi.org
{Fore.BLUE}Usage: python3 main.py <DOMAIN>
""")

domain = sys.argv[1]
api_url = f"https://rdap.verisign.com/com/v1/domain/{domain}"

req = requests.get(api_url)
data = req.json()

print(f"{Fore.YELLOW}Domain Information:")
print(f"Name: {data['ldhName']}")
print(f"Registry Domain ID: {data['handle']}")
print(f"Domain Status: {data['status'][0]}")
print("Nameservers:")
for nameserver in data["nameservers"]:
    print(f"- {nameserver['ldhName']}")
print("\n")

print(f"{Fore.YELLOW}Events:")
for event in data["events"]:
    print(f"Action: {event['eventAction']}")
    print(f"Date: {event['eventDate']}")
