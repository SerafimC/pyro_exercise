import psutil
import socket

class Resource_Machine():
    def __init__(self):
        self.hostname = socket.gethostname()  
        self.ip_address = socket.gethostbyname(self.hostname) 
        self.memory_usage = psutil.virtual_memory()[2]
        self.cpu_usage = psutil.cpu_percent()

    def register(self, warehouse):
        warehouse.register({
            "hostname": self.hostname,
            "ip_address": self.ip_address,
            "memory_usage": self.memory_usage,
            "cpu_usage": self.cpu_usage
        })
        print("Register complete!")

    def list_resources(self, warehouse):
        print(warehouse.list_contents())

