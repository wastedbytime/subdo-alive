import requests

def check_subdomain(subdomain):
    try:
        response = requests.get(f'http://{subdomain}', timeout=5)
        if response.status_code == 200:
            print(f"{subdomain} is alive")
        else:
            print(f"{subdomain} returned status code {response.status_code}")
    except requests.RequestException:
        print(f"{subdomain} is not reachable")

with open('subdomains.txt') as file:
    subdomains = file.readlines()

for subdomain in subdomains:
    check_subdomain(subdomain.strip())
