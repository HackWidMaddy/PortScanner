from queue import Queue
import threading
import socket


port_dict = {
    7: 'Echo',
    20: 'FTP Data',
    21: 'FTP Control',
    22: 'SSH',
    23: 'Telnet',
    25: 'SMTP',
    53: 'DNS',
    67: 'DHCP Client',
    68: 'DHCP Server',
    69: 'TFTP',
    80: 'HTTP',
    110: 'POP3',
    119: 'NNTP',
    123: 'NTP',
    135: 'RPC',
    137: 'NetBIOS Name Service',
    138: 'NetBIOS Datagram Service',
    139: 'NetBIOS Session Service',
    143: 'IMAP',
    161: 'SNMP',
    162: 'SNMP Trap',
    389: 'LDAP',
    443: 'HTTPS',
    514: 'Syslog',
    636: 'LDAPS',
    873: 'rsync',
    993: 'IMAPS',
    995: 'POP3S',
    1080: 'SOCKS',
    1433: 'Microsoft SQL Server',
    1434: 'Microsoft SQL Server Browser',
    1521: 'Oracle Database',
    1723: 'PPTP',
    3306: 'MySQL',
    3389: 'Remote Desktop Protocol',
    5432: 'PostgreSQL',
    5900: 'VNC',
    8080: 'HTTP Alternate',
}

queue = Queue()
open_port = []

count = 0


target = "172.31.198.130"
def port_scan(port):
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((target,port))
        return True
    except:
        return False
    


def fill_queue(port_list):
    for port in port_list:
        queue.put(port)


def worker():
    global count
    while not queue.empty():
        port = queue.get()
        if port_scan(port):
            if count == 0:
                print("PortNo.            Name")
                count = count + 1
            print(port, "               " ,port_dict[port])
            open_port.append(port)

port_list = range(1,1024)
fill_queue(port_list)

thread_list = []

for t in range(10):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)


for thread in thread_list:
    thread.start()


for thread in thread_list:
    thread.join()



    
print("Open Ports are " , open_port)

            
