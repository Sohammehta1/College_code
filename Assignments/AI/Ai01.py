import socket
import threading
import json
import sys
import time

class Node:
    
    def __init__(self, port_no, hostN,node_count):
        self.portNum = port_no
        self.hostName = hostN
        self.hostAddress = "127.0.0.1"
        self.neighbour_nodes = {}
        self.node_id = int(self.hostName[-1])
        self.node_count = node_count
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.hostAddress, self.portNum))
        self.n = int(input("Enter number of neighbours: "))
        for i in range(self.n):
            name = input("Enter neighbour hostname: ")
            nport = int(input("Enter neighbour port number: "))
            self.neighbour_nodes[name] = nport
        for key in self.neighbour_nodes.keys():
            print(key, " : ", self.neighbour_nodes[key])

    def send_json(self,key,msg):
        serialized_msg = json.dumps(msg)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(("127.0.0.1",self.neighbour_nodes[key]))
            s.send(serialized_msg.encode('utf-8'))
            s.close()
    
    def Find_node(self,dest):
        msg = {
            "src" : self.portNum,
            "src_name" : self.hostName,
            "dest_name" : dest,
            "ttl" : 6,
            "visited_nodes" : {},
            "distance": 0,
            "path":[self.hostName]
        }
        for i in range(self.node_count):
            msg["visited_nodes"]["node"+str(i+1)]=0
        msg["visited_nodes"][self.hostName] = 1

        for key in self.neighbour_nodes.keys():
            if msg["visited_nodes"][key] ==0:
                self.send_json(key,msg)
        print("Source node terminating .....")
        sys.exit()


        
            
    def handle_client(self, client_socket, address):
            print(f"Accepted connection from {address}")
            try:
                message_bytes = client_socket.recv(1024)
                message_str = message_bytes.decode('utf-8')

                try:
                    message = json.loads(message_str)
                    if isinstance(message, dict):
                        print("Hello")
                        message["distance"] += 1
                        message["visited_nodes"][self.hostName] = 1
                        if self.hostName == message["dest_name"]:
                            print("Message from source has arrived:")
                            print(message)
                            
                            # msg =  str(message["distance"])
                            # self.ping(message["src_name"], msg)

                        elif message["distance"] < message['ttl']:
                            message["path"].append(self.hostName)
                            for key in self.neighbour_nodes.keys():
                                if message["visited_nodes"][key] == 0:
                                    self.send_json(key, message)
                    else:
                        print(f"Received message from {address}: {message_str}")
                except json.JSONDecodeError:
                    print(f"Invalid JSON received from {address}: {message_str}")
                client_socket.close()
            except ConnectionResetError:
                print(f"Connection reset by {address}")
               

            print(f"Connection with {address} closed")

        

    def ping(self,dest,msg):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect(("127.0.0.1",dest))
                msg = msg.encode('utf-8')
                s.sendall(msg)
                s.close()
                data = s.recv(1024)
                
                
    def server(self):
        self.server_socket.listen(self.n)
        print(f"Server listening on {self.hostName}:{self.portNum}")
        while True:
            client_socket, address = self.server_socket.accept()
            # Create a new thread to handle the client
            client_handler = threading.Thread(target=self.handle_client, args=(client_socket, address))
            client_handler.start()
            
if __name__ == "__main__": # Server starts only when script is directly run, not when module is imported.
    p = int(input("Enter port number: "))
    n = input("Enter host name: ")
    nd = Node(p, n,4)
    threading.Thread(target=nd.server).start()  # Start server in a separate thread

    dest = input("Enter the name of destination you want to find : ")
    nd.Find_node(dest)
    

       
