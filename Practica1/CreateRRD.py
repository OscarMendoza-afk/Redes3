#!/usr/bin/env python

import rrdtool

def crearRRD(host:str):
    ret = rrdtool.create("datosGenerados/agente_"+host+"/RRDagente_"+host+".rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:ifOutUcastPkts:COUNTER:600:U:U", 
                     "DS:ipInReceives:COUNTER:600:U:U",  
                     "DS:icmpOutEchos:COUNTER:600:U:U",  
                     "DS:tcpInSegs:COUNTER:600:U:U",  
                     "DS:udpInDatagrams:COUNTER:600:U:U",  
                     "RRA:AVERAGE:0.5:1:20")

    if ret:
        print (rrdtool.error())