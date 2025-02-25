import colorama
from colorama import Fore, Style, init


init(autoreset=True)


def print_banner():
    print(Fore.CYAN + Style.BRIGHT + r"""
    ╔════════════════════════════════════════════╗
    ║         IP LOOKUP TOOL by Zeliro           ║
    ╚════════════════════════════════════════════╝
    """)

def print_ip_info(data):
    print(Fore.YELLOW + Style.BRIGHT + "\n[+] Informations sur l'IP :\n")
    print(Fore.CYAN + f"  ➤ IP: {data.get('ip', 'N/A')}")
    print(Fore.CYAN + f"  ➤ Hostname: {data.get('hostname', 'N/A')}")
    print(Fore.CYAN + f"  ➤ Ville: {data.get('city', 'N/A')}")
    print(Fore.CYAN + f"  ➤ Région: {data.get('region', 'N/A')}")
    print(Fore.CYAN + f"  ➤ Pays: {data.get('country', 'N/A')}")
    print(Fore.CYAN + f"  ➤ Localisation: {data.get('loc', 'N/A')}")
    print(Fore.CYAN + f"  ➤ Organisation: {data.get('org', 'N/A')}")
    print(Fore.CYAN + f"  ➤ Code Postal: {data.get('postal', 'N/A')}")
    print(Fore.CYAN + f"  ➤ Fuseau horaire: {data.get('timezone', 'N/A')}\n")

def ip_lookup(ip):
    url = f"http://ipinfo.io/{ip}/json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print_ip_info(data)
        else:
            print(Fore.RED + "[!] Impossible de récupérer les informations.")
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"[!] Erreur : {str(e)}")

def main():
    print_banner()
    ip = input(Fore.GREEN + Style.BRIGHT + "Entrez une adresse IP : ")
    print(Fore.YELLOW + "[*] Recherche en cours...\n")
    ip_lookup(ip)
    print(Fore.MAGENTA + Style.BRIGHT + r"""
    ╔════════════════════════════════════════╗
    ║      Recherche terminée, merci !       ║
    ╚════════════════════════════════════════╝
    """)

    
    input(Fore.GREEN + "\nAppuyez sur Entrée pour fermer...")

if __name__ == "__main__":
    main()
