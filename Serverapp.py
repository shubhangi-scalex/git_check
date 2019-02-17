import socket
import pickle
import threading
from threading import Thread


def client_thread(conn, ip, port, max_buffer_size = 5120):
    is_active = True

    while is_active:
        s_name = conn.recv(max_buffer_size)#connection to recive data from client accept upto 1024 bytes
        s_name = s_name.decode()# decode client name
        # client_input =conn.recv(conn, max_buffer_size)
        message = input(str("Me : "))#start chatting
        conn.send(message.encode())#send message
    
        message = conn.recv(max_buffer_size)#massage recive from client 
        message = message.decode()#decode it and print it
        print(s_name, ":", message)#display it

        if "--QUIT--" in s_name:
            print("Client is requesting to quit")
            conn.close()
            print("Connection " + ip + ":" + port + " closed")
            is_active = False
        else:
            pass 


print("\nWelcome to Chat Room\n")
print("Initialising....\n")

s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 1333
ips = []
ports = []
Names = [] 


s.bind((host, port))
print(host, "(", ip, ")\n")


x=1
name = input(str("Enter your name: "))
p = input(str(" Enter How Many Connection you Want to connect: "))

for x in range(1,int(p)):
        s.listen()
        print("\nWaiting for incoming connections...\n")
        conn, addr = s.accept()
        print("Received connection from ", addr[0], "(", addr[1], "),\n")
        s_name = conn.recv(1024)
        s_name = s_name.decode()
        print(s_name, "has connected to the chat room\nEnter [e] to exit chat room\n")
        conn.send(name.encode())
        ips.append(conn)
        ports.append(addr)
        Names.append(s_name)
        print(ips)
        print(ports)
        print(Names)



Choice = input(str("Who u r : "))
choiceto = input(str("which client to connect"))

if Choice in Names:
    print("You want to connect with " + choiceto)
    print()


if Choice in Names:
    for client in Names:
        message = client
        conn.sendall(message.encode())
while True:
        message = input(str("Me : "))
        conn.send(message.encode())
        
        message = conn.recv(1024)
        message = message.decode()
        print(s_name, ":", message)



        # if Choice in Names

        # data_string = pickle.dumps(ips)
        # print(ips)
        # s.send(data_string)

        # '''t =  Thread(target=client_thread, args=(conn, ip, port))
        #      threads.append(t)
        #      t.start()'''  

# message = "POOJA IS GOOD"
# conn.sendall(message.encode())
        

# N = input(int("Enter The "))

# s_name = conn.recv(1024)
# s_name = s_name.decode()
# print(s_name, "has connected to the chat room\nEnter [e] to exit chat room\n")
# # conn.send(name.encode())

# while True:
#     message = input(str("Me : "))
#     conn.send(message.encode())
    
#     message = conn.recv(1024)
#     message = message.decode()
#     print(s_name, ":", message)















