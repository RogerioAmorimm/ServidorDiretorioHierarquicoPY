import rpyc
import socket
from const import * #-
from rpyc.utils.server import ThreadedServer
 
class CalcServer(rpyc.Service):

  def exposed_soma(self, valorA, valorB):
    
    print(f"Somando valores: {valorA} e {valorB}")
   
    return valorA + valorB
  def exposed_sub(self, valorA, valorB):
    
    print(f"Subtraindo valores: {valorA} e {valorB}")
   
    return valorA - valorB

  def exposed_mult(self, valorA, valorB):
    
    print(f"Multiplicando valores: {valorA} e {valorB}")
   
    return valorA * valorB

  def exposed_div(self, valorA, valorB):
    
    print(f"Dividindo valores: {valorA} e {valorB}")
   
    return valorA / valorB
           
if __name__ == "__main__":
  print(f"Criaando server {SERVER_CALCSERVER_NAME}") 
  server = ThreadedServer(CalcServer, port = PORT_CALCSERVER)
  print(f"Conectando ao Server de diretório DerpartamentoVendas")  
  conn_serverDepVenda = rpyc.connect(SERVER_DEPVENDA,PORT_DEPVENDA)
  print(f"Conectando ao Server de diretório DepartamentoRH")  
  conn_serverDepRh = rpyc.connect(SERVER_DEPRH,PORT_DEPRH)
  print(f"Obtendo ipadress da {SERVER_CALCSERVER_NAME}")  
  ipAdress = socket.gethostbyname(socket.gethostname())
  print(f"Registrando no Server de diretório DerpartamentoVendas") 
  conn_serverDepVenda.root.exposed_register(SERVER_CALCSERVER_NAME,ipAdress,PORT_CALCSERVER)
  print(f"Registrando no Server de diretório DepartamentoRH") 
  conn_serverDepRh.root.exposed_register(SERVER_CALCSERVER_NAME,ipAdress,PORT_CALCSERVER)
  server.start()

