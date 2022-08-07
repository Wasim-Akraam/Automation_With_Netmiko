import ipaddress
IP=ipaddress.ip_address("192.168.10.1").is_global
print(IP)
IP=ipaddress.ip_address("192.168.10.1").is_multicast
print(IP)
IP=ipaddress.ip_address("192.168.10.1").is_private
print(IP)
IP=ipaddress.ip_address("10.10.10.1").is_global
print(IP)