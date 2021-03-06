import rpyc
from const import *

class Client:
  print(f"Iniciando conexão com servidor de diretórios de raiz ip: {SERVERDIRRAIZ} e porta: {PORTDIRRAIZ}")
  
  conn = rpyc.connect(SERVERDIRRAIZ, PORTDIRRAIZ) # Connect to the server
  
  print(f"Fazendo busca de outros servidores de diretórios")
  
  # cenario teste DerpartamentoVendas
  
  print(f"Fazendo busca no servidor de diretórios DerpartamentoVendas")
  DepVendas  =  conn.root.exposed_lookup(SERVER_DEPVENDA_NAME)
  print(f"Conectando ao servirdor de diretórios DerpartamentoVendas com ip:{DepVendas[0]} e porta:{DepVendas[1]}")
  connDepVendas = rpyc.connect(DepVendas[0], DepVendas[1])
  
  print(f"Fazendo busca no servidor de diretórios DerpartamentoVendas do servidor CalcServer")
  depVendasCalcServer  =  connDepVendas.root.exposed_lookup(SERVER_CALCSERVER_NAME)

  print(f"Conectando ao CalcServer do servirdor de diretórios DerpartamentoVendas com ip:{depVendasCalcServer[0]} e porta:{depVendasCalcServer[1]}")
  CalcServerDepVendas  =  rpyc.connect(depVendasCalcServer[0], depVendasCalcServer[1])
  
  print(f"somando valore do CalcServer do servirdor de diretórios DerpartamentoVendas, valor A: 1 valor B: 2 Resultado: {CalcServerDepVendas.root.exposed_soma(1,2)} ")
  print(f"subtraindo valore do CalcServer do servirdor de diretórios DerpartamentoVendas, valor A: 4 valor B: 5 Resultado: {CalcServerDepVendas.root.exposed_sub(4,5)} ")
  print(f"multiplicando valore do CalcServer do servirdor de diretórios DerpartamentoVendas, valor A: 56 valor B: 28 Resultado: {CalcServerDepVendas.root.exposed_mult(56,28)} ")
  print(f"dividindo valore do CalcServer do servirdor de diretórios DerpartamentoVendas, valor A: 10 valor B: 1000 Resultado: {CalcServerDepVendas.root.exposed_div(10,100)} ")
  
  print(f"Fazendo busca no servidor de diretórios DerpartamentoVendas do servidor ValueServer")  
  depVendasValueServer  =  connDepVendas.root.exposed_lookup(SERVER_VALUESERVER_NAME)

  print(f"Conectando ao ValueServer do servirdor de diretórios DerpartamentoVendas com ip:{depVendasValueServer[0]} e porta:{depVendasValueServer[1]}")
  ValueServerDepVendas  =  rpyc.connect(depVendasValueServer[0], depVendasValueServer[1])
  
  print(f"Concatenando valor 'Deu certo' ValeuServer do servirdor de diretórios DerpartamentoVendas")
  ValueServerDepVendas.root.exposed_append("Deu certo")
  print(f"Concatenando valor 'DerpartamentoVendas' ValeuServer do servirdor de diretórios DerpartamentoVendas")
  ValueServerDepVendas.root.exposed_append("DerpartamentoVendas")
  print(f"Retornando valores ValeuServer do servirdor de diretórios DerpartamentoVendas")
  print(ValueServerDepVendas.root.exposed_value())
  
  print(f"Fazendo busca no servidor de diretórios DerpartamentoVendas do servidor HourServer")
  depVendasHourServer  =  connDepVendas.root.exposed_lookup(SERVER_HOURSERVER_NAME)
  
  print(f"Conectando ao HourServer do servirdor de diretórios DerpartamentoVendas com ip:{depVendasHourServer[0]} e porta:{depVendasHourServer[1]}")
  HourServerDepVendas  =  rpyc.connect(depVendasHourServer[0], depVendasHourServer[1])
  
  print(HourServerDepVendas.root.exposed_hourNow(f"{conn.root.get_service_name()}:{connDepVendas.root.get_service_name()}"))

  # cenario teste DepartamentoRH
  print(f"Fazendo busca no servidor de diretórios DepartamentoRH")
  DepRH  =  conn.root.exposed_lookup(SERVER_DEPRH_NAME)
  print(f"Conectando ao servirdor de diretórios DerpartamentoVendas com ip:{DepRH[0]} e porta:{DepRH[1]}")
  connDepRH = rpyc.connect(DepRH[0], DepRH[1])

  print(f"Fazendo busca no servidor de diretórios DepartamentoRH do servidor CalcServer")
  depRhCalcServer  =  connDepRH.root.exposed_lookup(SERVER_CALCSERVER_NAME)

  print(f"Conectando ao CalcServer do servirdor de diretórios DepartamentoRH com ip:{depRhCalcServer[0]} e porta:{depRhCalcServer[1]}")
  CalcServerDepRh  =  rpyc.connect(depRhCalcServer[0], depRhCalcServer[1])
  
  print(f"somando valore do CalcServer do servirdor de diretórios DepartamentoRH, valor A: 1 valor B: 2 Resultado: {CalcServerDepRh.root.exposed_soma(1,2)} ")
  print(f"subtraindo valore do CalcServer do servirdor de diretórios DepartamentoRH, valor A: 4 valor B: 5 Resultado: {CalcServerDepRh.root.exposed_sub(4,5)} ")
  print(f"multiplicando valore do CalcServer do servirdor de diretórios DepartamentoRH, valor A: 56 valor B: 28 Resultado: {CalcServerDepRh.root.exposed_mult(56,28)} ")
  print(f"dividindo valore do CalcServer do servirdor de diretórios DepartamentoRH, valor A: 10 valor B: 1000 Resultado: {CalcServerDepRh.root.exposed_div(10,100)} ")
  
  print(f"Fazendo busca no servidor de diretórios DepartamentoRH do servidor ValeuServer do servidor de diretórios DerpartamentoVendas")  
  depRhValueServer  =  connDepRH.root.exposed_lookup(f"{SERVER_DEPVENDA_NAME}:ValueServer")

  print(f"Conectando ao ValueServer do servirdor de diretórios DerpartamentoVendas atraves do DepartamentoRH com ip:{depRhValueServer[0]} e porta:{depRhValueServer[1]}")
  ValueServerDepRh  =  rpyc.connect(depRhValueServer[0], depRhValueServer[1])
  
  print(f"Concatenando valor 'Deu certo' ValueServer do servirdor de diretórios DepartamentoRH")
  ValueServerDepRh.root.exposed_append(f"Deu certo")
  print(f"Concatenando valor 'DepartamentoRH com  DerpartamentoVendas' ValueServer do servirdor de diretórios DepartamentoRH")
  ValueServerDepRh.root.exposed_append(f"DepartamentoRH com  DerpartamentoVendas")
  print(f"Retornando valores ValueServer do servirdor de diretórios DepartamentoRH com DerpartamentoVendas")
  print(ValueServerDepRh.root.exposed_value())
    
  print(f"Fazendo busca no servidor de diretórios DepartamentoRH do servidor HourServer")
  depRhHourServer  =  connDepRH.root.exposed_lookup(SERVER_HOURSERVER_NAME)
  
  print(f"Conectando ao HourServer do servirdor de diretórios DepartamentoRH com ip:{depRhHourServer[0]} e porta:{depRhHourServer[1]}")
  HourServerDepRh  =  rpyc.connect(depRhHourServer[0], depRhHourServer[1])
  print(HourServerDepVendas.root.exposed_hourNow(f"{conn.root.get_service_name()}:{connDepRH.root.get_service_name()}"))
