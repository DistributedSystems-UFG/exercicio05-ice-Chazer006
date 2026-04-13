import sys, Ice
import Demo
 
class PrinterI(Demo.Printer):
    def __init__(self, t):
        self.t = t
        
    def printString(self, s, current=None):
        print(f"{self.t} {s}")

    def add(self, a, b, current=None):
        return a + b

    def sub(self, a, b, current=None):
        return a - b

class LoggerI(Demo.Logger):
    def log(self, message, current=None):
        print(f"[LOG]: {message}")

with Ice.initialize(sys.argv) as communicator:
    adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", "default -p 11000")
    
    object1 = PrinterI("Object1:")
    adapter.add(object1, communicator.stringToIdentity("SimplePrinter1"))
    
    novo_logger = LoggerI()
    adapter.add(novo_logger, communicator.stringToIdentity("MeuLogger"))
    
    adapter.activate()
    print("Servidor pronto e com novos serviços ativos...")
    communicator.waitForShutdown()
