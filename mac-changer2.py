import subprocess
import optparse

def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface for change")
    parser.add_option("-m", "new_mac", dest="new_mac", help="new mac addres you want")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("please specify an interface, use --help for more help")
    elif not options.new_mac:
        parser.error("please specify a new mac, use --help for more help")
    return options

def mac_changer(interface, new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    print("[+] MAC address for " + interface + "changed to " + new_mac)



options = get_argument()
mac_changer(options.interface, options.new_mac)


