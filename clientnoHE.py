import socket
import os.path
import datetime
import time
import sys
import csv

if __name__ == '__main__':
    
    HOST = '127.0.0.1'
    PORT = 50001

    sock = socket.socket()
    sock.connect((HOST, PORT))
    print("Alice has started the client")
    
    fn = input("Enter dataset that you wish to store on server Carol:\n")
    
    linecount = len(list(csv.reader(open(fn))))
    sock.send(str(linecount).encode('utf=8'))
    
    for line in open(fn):
        sock.send(line.encode('utf-8'))
        
    query = input("Enter query from among [avg,sum]\n")
    while True:
        if query not in ['avg','sum']:
            fn = input("Invalid input. Enter query from among [avg,add]\n")
        else:
            break
    sock.send(query.encode('utf-8'))
    
    paramter = input("Enter paramter from among [age,income]\n")
    while True:
        if paramter not in ['age','income']:
            fn = input("Invalid input. Enter query from among [age,income]\n")
        else:
            break
    sock.send(paramter.encode('utf-8'))
    
    start_pos = input("Enter number of first entry\n")
    sock.send(str(start_pos).encode('utf-8'))
    end_pos = input("Enter number of final entry\n")
    
    while True:
        if int(end_pos) < int(start_pos) or int(end_pos) > linecount-2:
            end_pos = input("Invalid input. Enter a number between the first entry and number of entries\n")
        else:
            break
        
    start_time = time.time()
    sock.send(str(end_pos).encode('utf-8'))
    result = sock.recv(1024).decode('utf-8')
    end_time = time.time()
    
    time_elapsed = end_time - start_time
    
    print("Reult of query is: ",result)
    print("Time elapsed: ",time_elapsed)
    
    sock.close()
