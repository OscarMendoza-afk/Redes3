from claseAgente import Agente
import rrdtool
import time
def grafica(agente: Agente, tiempoInicial, tiempoFinal, interfaz:int):
    #Grafica desde el tiempo actual menos diez minutos

    tiempoInicial = time.strptime(tiempoInicial, "%d-%m-%Y %H:%M")
    tiempoInicial = int(time.mktime(tiempoInicial))

    tiempoFinal = time.strptime(tiempoFinal, "%d-%m-%Y %H:%M")
    tiempoFinal = int(time.mktime(tiempoFinal))

    nombre = "datosGenerados/agente_"+agente.host+"/RRDagente_"+agente.host

    ret = rrdtool.graph("datosGenerados/agente_"+agente.host+"/"+"1"+".png",
                        "--start",str(tiempoInicial),
                        "--end",str(tiempoFinal),
                        "--vertical-label=Paquetes",
                        "--title=Paquetes unicast que ha recibido la interfaz\n"+agente.descInterfaces[interfaz-1],
                        "DEF:ifOutUcastPkts="+nombre+".rrd:ifOutUcastPkts:AVERAGE",
                        #"AREA:inoctets#00FF00:Tráfico de entrada",
                        "LINE2:ifOutUcastPkts#4f5bd5:Paquetes unicast recibidos")
    ret = rrdtool.graph("datosGenerados/agente_"+agente.host+"/"+"2"+".png",
                        "--start",str(tiempoInicial),
                        "--end",str(tiempoFinal),
                        "--vertical-label=Paquetes",
                        "--title=Paquetes recibidos a protocolos IPv4.",
                        "DEF:ipInReceives="+nombre+".rrd:ipInReceives:AVERAGE",
                        #"AREA:inoctets#00FF00:Tráfico de entrada",
                        "AREA:ipInReceives#962fbf:Paquetes IPv4")
    ret = rrdtool.graph("datosGenerados/agente_"+agente.host+"/"+"3"+".png",
                        "--start",str(tiempoInicial),
                        "--end",str(tiempoFinal),
                        "--vertical-label=Mensajes",
                        "--title=Mensajes ICMP echo que ha enviado el agente",
                        "DEF:icmpOutEchos="+nombre+".rrd:icmpOutEchos:AVERAGE",
                        #"AREA:inoctets#00FF00:Tráfico de entrada",
                        "AREA:icmpOutEchos#fa7e1e:Mensajes ICMP Enviados")
    ret = rrdtool.graph("datosGenerados/agente_"+agente.host+"/"+"4"+".png",
                        "--start",str(tiempoInicial),
                        "--end",str(tiempoFinal),
                        "--vertical-label=Segmentos",
                        "--title=Segmentos recibidos.",
                        "DEF:tcpInSegs="+nombre+".rrd:tcpInSegs:AVERAGE",
                        #"AREA:inoctets#00FF00:Tráfico de entrada",
                        "LINE2:tcpInSegs#065535:Segmentos recibidos")
    ret = rrdtool.graph("datosGenerados/agente_"+agente.host+"/"+"5"+".png",
                        "--start",str(tiempoInicial),
                        "--end",str(tiempoFinal),
                        "--vertical-label=Datagramas",
                        "--title=Datagramas entregados a usuarios UDP.",
                        "DEF:udpInDatagrams="+nombre+".rrd:udpInDatagrams:AVERAGE",
                        #"AREA:inoctets#00FF00:Tráfico de entrada",
                        "AREA:udpInDatagrams#80aaaa:Datagramas entregados.")