#!/usr/bin/python3

import socket
import sys, time
from datetime import datetime

start_time= datetime.now()
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host=["166.104.177.20", "166.104.177.21","166.104.177.22", "166.104.177.23","166.104.177.24", "166.104.177.25","166.104.177.26", "166.104.177.27","166.104.177.28", "166.104.177.29"]
port=[80, 8080]


def portScanner():
    count=0

    for host_now in host:
        for port_now in port:
            if s.connect_ex((host_now,port_now)):
                    print("The IP is ", host_now, "and its ", port_now, "port is closed")
            else:
                    print("The IP is ", host_now, "and its ", port_now, "port is open")
                    count=count+1

    stop_time = datetime.now()
    
    total_time_duration = round((stop_time - start_time).total_seconds(),1)

    print("The number of server that can be my target server(available server) is ", count)

    print("The total duration is ", total_time_duration, "sec")
    
portScanner()
