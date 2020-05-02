from __future__ import print_function
import Pyro4

@Pyro4.expose
#@Pyro4.behavior(instance_mode="single")
class Warehouse(object):
    def __init__(self):
        self.contents = []

    def list_contents(self):
        return self.contents

    def register(self, element):
        self.contents.append(element)
        if "hostname" in element:
            print(element['hostname'] + "has been registred.")

def main():
    Pyro4.config.HOST = "192.168.0.105"
    Pyro4.Daemon.serveSimple(
            {
                Warehouse: "example.warehouse"
            },
            ns = True   )

if __name__=="__main__":
    main()