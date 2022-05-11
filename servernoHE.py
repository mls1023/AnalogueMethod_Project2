import socket
import os
import sys

if __name__ == '__main__':
    PORT = 50001
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', PORT))
    
    print("Server is Online")
    sock.listen(1)
    
    while True:
        conn, addr = sock.accept()
        print("User Alice has connected to the server" + str(addr))
        
        lc = int(conn.recv(1024).decode('utf-8'))
        linecount = 1
        line = ''
        database = {}
        
        while True:
            if linecount == lc:
                break
            while not line.endswith("\n"):
                line += conn.recv(1).decode('utf-8')
            linecount+=1
            database[line.split(",")[0]] = line.rstrip("\n").split(",")[1:]
            line = ''
            
        line = conn.recv(1024).decode('utf-8')
        database[line.split(",")[0]] = line.rstrip("\n").split(",")[1:]
        
        print("Dataset recieved")
        
        query = conn.recv(1024).decode('utf-8')
        parameter = conn.recv(1024).decode('utf-8')
        start = int(conn.recv(1024).decode('utf-8'))
        end = int(conn.recv(1024).decode('utf-8'))
        
        print("Performing operation",query,"on parameter", parameter,"on entries",start,"to",end)
        
        pos = 2 if parameter == 'age' else 3
        result = 0
        
        for i in range(start,end+1):
            result += float(database[str(i)][pos])
        if query == 'avg':
                result /= (end-start+1)
                
        conn.send(str(result).encode('utf-8'))
        conn.close()
        break
