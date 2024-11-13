import subprocess
import re
import random

def random_mac():
    """Generate a random MAC address with a fixed OUI (Organizationally Unique Identifier)."""
    oui = "00:16:3e"  # Fixed OUI
    random_bytes = [random.randint(0x00, 0x7f) for _ in range(3)]  # Random bytes
    random_mac_address = oui + ":{:02x}:{:02x}:{:02x}".format(*random_bytes)
    return random_mac_address


def change_mac(interface, new_mac):
    print(f"[+] Changing MAC Address for {interface} to {new_mac}")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    ifconfig_result = ifconfig_result.decode("utf-8")
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read the MAC address.")
        return None


def save_original_mac(interface):
    original_mac = get_current_mac(interface)
    if original_mac:
        with open(f"{interface}_original_mac.txt", "w") as file:
            file.write(original_mac)
        print(f"[+] Saved original MAC address: {original_mac}")


def load_original_mac(interface):
    try:
        with open(f"{interface}_original_mac.txt", "r") as file:
            original_mac = file.read().strip()
        return original_mac
    except FileNotFoundError:
        print(f"[-] No original MAC address found for {interface}")
        return None
