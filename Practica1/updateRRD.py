from claseAgente import Agente
import time
import rrdtool
from getSNMP import consultaSNMP
import logging

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] (%(threadName)-s) %(message)s')

def update(agente: Agente, interfaz: int):
    logging.info("Monitorizando para el host "+agente.host+" e interfaz "+str(interfaz))
    ifOutUcastPkts = 0
    ipInReceives = 0
    icmpOutEchos = 0
    tcpInSegs = 0
    udpInDatagrams = 0

    while 1:

        ifOutUcastPkts = int(
            consultaSNMP(agente.comunidad, agente.host,
                         "1.3.6.1.2.1.2.2.1.17."+str(interfaz), agente.puerto, agente.version))
        ipInReceives = int(
            consultaSNMP(agente.comunidad, agente.host,
                         "1.3.6.1.2.1.4.3.0", agente.puerto, agente.version))
        icmpOutEchos = int(
            consultaSNMP(agente.comunidad, agente.host,
                         "1.3.6.1.2.1.5.21.0", agente.puerto, agente.version))
        tcpInSegs = int(
            consultaSNMP(agente.comunidad, agente.host,
                         "1.3.6.1.2.1.6.10.0", agente.puerto, agente.version))
        udpInDatagrams = int(
            consultaSNMP(agente.comunidad, agente.host,
                         "1.3.6.1.2.1.7.1.0", agente.puerto, agente.version))

        valor = "N:" + str(ifOutUcastPkts) + ':' + \
            str(ipInReceives)+":"+str(icmpOutEchos)+":" + \
            str(tcpInSegs)+":"+str(udpInDatagrams)
        
        rrdtool.update("datosGenerados/agente_"+agente.host+"/RRDagente_"+agente.host+".rrd", valor)
        rrdtool.dump("datosGenerados/agente_"+agente.host+"/RRDagente_"+agente.host+".rrd", "datosGenerados/agente_"+agente.host+"/RRDagente_"+agente.host+".xml")
        time.sleep(1)
