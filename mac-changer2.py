import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="interface for change")
parser.add_option("-m", "new_mac", dest="new_mac", help="new mac addres you want")

(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

print("[+] MAC address for " + interface + "changed to " + new_mac)