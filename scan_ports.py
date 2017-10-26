# coding: utf-8

import socket
from multiprocessing.dummy import Pool as ThreadPool

def main():
    global host_ip
    host = input("Enter a host to scan:")
    exit_port = int(input("Enter exit_port:"))
    processes_num = int(input("Enter processes num:"))
    host_ip = socket.gethostbyname(host)
    ports = []
    print ('-' * 60)
    print ('Please wait, scanning host ', host_ip)
    print ('-' * 60)
    socket.setdefaulttimeout(0.5)
    for i in range(1,exit_port):
        ports.append(i)
    pool = ThreadPool(processes = processes_num)
    results = pool.map(scan_port,ports)
    pool.close()
    pool.join()
    print ('port scan end')

def scan_port(port):
    try:
        s = socket.socket(2,1)
        res = s.connect_ex((host_ip,port))
        if res == 0:
            print ('Port {}: OPEN'.format(port))
        s.close()
    except Exception as e:
        print (str(e.message))

if __name__ == '__main__':
    main()
