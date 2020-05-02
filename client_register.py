# This is the code that visits the warehouse.
import sys
import Pyro4
import Pyro4.util
from client import Resource_Machine

sys.excepthook = Pyro4.util.excepthook
nameserver=Pyro4.locateNS(host="192.168.0.105", port=9090)
uri=nameserver.lookup("example.warehouse")
warehouse = Pyro4.Proxy(uri)

this_machine = Resource_Machine()
this_machine.register(warehouse)
this_machine.list_resources(warehouse)
