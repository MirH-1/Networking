import socket
def check_port(host, port): # I create a function that is going to check the host and the port
    try: # we try the intended code below, it tries to connect
        socket.create_connection((host, port), timeout =1) 
        return True # runs if the connection worked - the door is open
    except OSError:  # it cathces a an error
        return False # means the door is closed 

host = "127.0.0.1"
port = "8000"

if check_port(host, port):
    print(f"port{port} on host {host} is OPEN")
else: 
    print(f"port {port} on {host} is Closed") 

