import sys, Ice
import Demo
 
with Ice.initialize(sys.argv) as communicator:
    base1 = communicator.stringToProxy("SimplePrinter1:tcp -h 127.0.0.1 -p 11000")
    printer1 = Demo.PrinterPrx.checkedCast(base1)
    
    base_log = communicator.stringToProxy("MeuLogger:tcp -h 127.0.0.1 -p 11000")
    logger = Demo.LoggerPrx.checkedCast(base_log)

    if not printer1 or not logger:
        raise RuntimeError("Erro ao conectar nos servidores")

    res_soma = printer1.add(30, 12)
    res_sub  = printer1.sub(100, 45)
    
    printer1.printString(f"Calculado no servidor: Soma={res_soma}, Sub={res_sub}")

    logger.log("O cliente chamou as novas funções matemáticas com sucesso!")
