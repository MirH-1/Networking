# # The idea: in Task 1 we went name → IP. Now we go the other way: IP → name. This is called a reverse DNS lookup.
# import socket
# ip = "8.8.8.8" #Google's public DNS server 
# lookup = socket.gethostbyaddr(ip) # pamietaj its gethostbyaddr()
# name = lookup[0] # result/lookup[0] - gives the name of the first item coming out there
# print(f"The name for {ip} is {name}")




# # 
# import socket
# website = "Google.com"
# ip = socket.gethostbyname(website)
# print(f"The ip address of the {website} is {ip}")



import socket 
ip = "8.8.8.8"
lookup = socket.gethostbyaddr(ip)
whichItem = lookup[0]
print(f"The name of the {ip} is {whichItem}")
