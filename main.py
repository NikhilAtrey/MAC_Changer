import argparse
from mac import MAC_Changer

def main():
    # Set up the argument parser with -i and -m as flags
    parser = argparse.ArgumentParser(description="MAC Address Changer")
    parser.add_argument("-i", "--interface", required=True, help="Network interface to change the MAC address (e.g., eth0)")
    parser.add_argument("-m", "--mac", required=True, help="New MAC address to set (e.g., 00:11:22:22:22:33)")

    # Parse the arguments
    args = parser.parse_args()

    # Create an instance of MAC_Changer
    mc = MAC_Changer()

    # Display current MAC
    current_mac = mc.get_MAC(args.interface)
    print(f"Current MAC: {current_mac}")

    # Change to new MAC
    updated_mac = mc.change_mac(args.interface, args.mac)
    print(f"Updated MAC: {updated_mac}")

if __name__ == "__main__":
    main()
