import socket
import sys
import json
import threading

class Node:
    def __init__(self,Hostname, Port_number,node_count) -> None:
        self.HostName = Hostname
        self.PortNumber = Port_number
        self.nodeCount= node_count
        self.Node_id = self.HostName[-1]
        self.HostAddress = "127.0.0.1"
        self.Neighbouring_nodes= {}
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.HostAddress, self.PortNumber))
        self.nn = int(input("Enter number of neighbouring nodes : "))
        for i in range(self.nn):
            node_name= input("Enter name of the node: ")
            node_port= int(input("Enter the port number: "))
            self.Neighbouring_nodes[node_name]=node_port

    def Find_node(self,dest_node):
        msg = {
            "src":self.HostName,
            "src_port_number":self.PortNumber,
            "distance":0,
            "visited_nodes":{self.HostName:True},
            "destination":dest_node,
            "path":[self.HostName],
            "ttl":6
        }
        for node in self.Neighbouring_nodes.keys(): # initializing visited nodes 
            msg["visited_nodes"][node]=False
        
        for node in self.Neighbouring_nodes.keys():
            self.send_json(msg,node)
        print("Sourcd Node terminating")
        sys.exit()
        
        


    def send_json(self, msg:dict,node_name:str):
        json_msg = json.dumps(msg)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(("127.0.0.1",self.Neighbouring_nodes[node_name] ))
            s.send(json_msg.encode('utf-8'))
            s.close()

    def handle_client(self,client_socket,address):
        print(f'Connection accepted from {address}')
        try:
            message = client_socket.recv(1024)
            message_str = message.decode('utf-8')
            try:
                message = json.loads(message_str)
                if isinstance(message, dict):
                    message["distance"]+=1
                    message["path"].append(self.HostName)
                    message["visited_nodes"][self.HostName]=True
                    if message["destination"]==self.HostName:
                        print("DESTINATION REACHED")
                        print(f"Message received : {message}")
                    elif message["ttl"] > message["distance"]: # message is  to be terminated or not?
                        for key in self.Neighbouring_nodes.keys():
                            if message["visited_nodes"][key] == False:
                                self.send_json(message,key)
                
            except json.JSONDecodeError:
                print("Incorrect json file")
        except ConnectionResetError:
            print(f"Connection reset by address : {address}")
        client_socket.close()

    def server(self):
        self.server_socket.listen(self.nn)
        print(f"Sever listening on {self.HostAddress}@{self.PortNumber}")
        while True:
            client_socket,address = self.server_socket.accept()
            client_handler = threading.Thread(target=self.handle_client, args=(client_socket, address))
            client_handler.start()
        
if __name__ == "__main__":
    h = input("Enter host name : ")
    p = int(input("Enter the port number : "))
    nn =int(input("Enter the number of nodes in the network : "))
    node = Node(h,p,nn)
    threading.Thread(target=node.server).start()
    d = input("Enter name of destination node : ")
    node.Find_node(d)
    