#!/usr/bin/env python

import optparse
from mac import change_mac, get_current_mac, save_original_mac, load_original_mac, random_mac

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
    parser.add_option("-r", "--random", action="store_true", help="Generate a random MAC address", dest="random_mac")
    parser.add_option("--restore", action="store_true", help="Restore the original MAC address", dest="restore_mac")

    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    if not options.new_mac and not options.random_mac and not options.restore_mac:
        parser.error("[-] Please specify a MAC Address, use --random for a random MAC, or use --restore to restore the original MAC")

    return options


options = get_arguments()

# If --restore flag is set, restore the original MAC address
if options.restore_mac:
    original_mac = load_original_mac(options.interface)
    if original_mac:
        change_mac(options.interface, original_mac)
        print(f"[+] Restored MAC Address to {original_mac}")
    else:
        print("[-] No original MAC Address to restore")
else:
    save_original_mac(options.interface)

    # If --random flag is set, generate a random MAC address
    if options.random_mac:
        options.new_mac = random_mac()

    current_mac = get_current_mac(options.interface)
    print(f"Current MAC: {str(current_mac)}")

    change_mac(options.interface, options.new_mac)

    current_mac = get_current_mac(options.interface)
    if current_mac == options.new_mac:
        print(f"[+] MAC Address was successfully changed to {current_mac}")
    else:
        print("[-] MAC Address did not change.")
