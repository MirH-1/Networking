# you find the IP address of the server that hosts their website, not the company itself.
# The idea: computers find each other using IP addresses like 142.250.186.78, but people use names like google.com. 
# DNS is the system that translates names into IP addresses, like a phone book for the internet.


# import socket #Socket is python's built-in toolbox for networking
# website = "www.linklaters.com"
# ip = socket.gethostbyname(website)
# print(f"The IP address of {website} is {ip}")



# import socket
# website = "Google.com"
# ip = socket.gethostbyname(website)
# print(f"The ip address of the {website} is {ip}")


import socket 
website = "Linklaters.com"
ip = socket.gethostbyname(website)
print(f"The IP address of the {website} is {ip}")