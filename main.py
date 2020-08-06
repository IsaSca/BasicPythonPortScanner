# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import subprocess

def scan_ports(host_range_start, host_range_end, host_prefix):
	for i in range(int(host_range_start), int(host_range_end)):
		subprocess.call("ping " + host_prefix + str(i))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
	defined_range = input("Please enter your range. For example 192.168.1.0-200\n").split('-')
	end = defined_range.pop(1)
	host_octets = defined_range.pop(0).split(".")
	print(host_octets)
	start = host_octets.pop(3)
	print(host_octets)
	host_prefix = "" + host_octets.pop(0) + "."+ host_octets.pop(0) + "."+ host_octets.pop(0)+"."
	print(host_prefix)
	scan_ports(start, end, host_prefix)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
