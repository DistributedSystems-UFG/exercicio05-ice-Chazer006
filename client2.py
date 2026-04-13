import sys, Ice
import Demo

with Ice.initialize(sys.argv) as communicator:
    base1 = communicator.stringToProxy("SimplePrinter1:tcp -h 127.0.0.1 -p 11000")
    printer1 = Demo.PrinterPrx.checkedCast(base1) [cite: 1]
    
    base_log = communicator.stringToProxy("MeuLogger:tcp -h 127.0.0.1 -p 11000")
    logger = Demo.LoggerPrx.checkedCast(base_log)

    if not printer1 or not logger:
        raise RuntimeError("Proxies inválidos")

    soma = printer1.add(10, 5)
    printer1.printString(f"O resultado da soma eh: {soma}")

    logger.log("Cliente finalizou as operacoes com sucesso.")
