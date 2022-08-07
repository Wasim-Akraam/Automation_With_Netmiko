import ipaddress

ip_obj=ipaddress.IPv4Network('10.10.10.0/24')

print(ip_obj.with_netmask)
print(ip_obj.with_prefixlen)
print(ip_obj.hostmask)
print(ip_obj.netmask)
print(ip_obj.network_address)
print(ip_obj.num_addresses)


for ip in ip_obj.hosts():
    print(ip)
