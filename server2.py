import sys, Ice
import Demo

class PrinterI(Demo.Printer):
    def __init__(self, t):
        self.t = t
        
    def printString(self, s, current=None):
        print(f"{self.t} {s}") [cite: 2]

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
    adapter.add(object1, communicator.stringToIdentity("SimplePrinter1")) [cite: 2]
    
    logger_obj = LoggerI()
    adapter.add(logger_obj, communicator.stringToIdentity("MeuLogger"))
    
    adapter.activate() [cite: 2]
    print("Servidor rodando...")
    communicator.waitForShutdown() [cite: 2]
