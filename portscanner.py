import socket
from IPy import IP


# checking if the ip address is numeric, or converting the url to ip address
def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)

# function to scan the port
def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        print('[+] Port ' + str(port) + ' is Open')
    except:
        print('[-] Port ' + str(port) + ' is Closed')

        
# specifying the ipaddress
ipaddress = input('[+] Enter Target to Scan: ')
converted_ip = check_ip(ipaddress)

# range of ports to scan
for port in range(1, 100):
    scan_port(converted_ip, port)
