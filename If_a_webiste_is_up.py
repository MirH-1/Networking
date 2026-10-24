import socket 
website = "nataliaturska.com"
port = 443 
try: # means "try to run the intended code below"
    socket.create_connection((website, port), timeout=3) # it knocks the door and gives it at most 3 sec for an answer
    print(f"{website} is UP")
except OSError: # if a network error happened, dont crash, do this instead. 
    print(f"{website} is down and unreachable") # This runs only if something goes wrong.
