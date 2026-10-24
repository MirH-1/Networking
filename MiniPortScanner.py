import socket
def check_port(host, port):
    try: 
        connection = socket.create_connection((host, port), timeout = 1)
        connection.close() # hangs up after checking
        return True 
    except OSError:
        return False

host = "127.0.0.1"
open_ports = []

for port in range(7900, 8011):
        if check_port(host, port):
            open_ports.append(port)

print(f"Scanned ports 7900 to 8010 on {host}")
print(f"Open ports: {open_ports}")



