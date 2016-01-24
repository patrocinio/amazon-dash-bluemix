#!/usr/bin/python
import sys, json, datetime
import ibmiotf.device
from ibmiotf.codecs import jsonIotfCodec
import argparse
from scapy.all import *

def mqttpub(cfgFile, dataDic):
    options = ibmiotf.device.ParseConfigFile(cfgFile)
    deviceCli = ibmiotf.device.Client(options)
    print 'Publish data to topic on IoTF'
    ts=str(datetime.datetime.now())
    dataDic["ts"]=ts
    deviceCli.connect()
    myData= { "d": dataDic}
    myQosLevel=0
    deviceCli.publishEvent(event="status", msgFormat="json", data=myData, qos=myQosLevel)

def getVarFromFile(fname):
    iot_dict = {}
    with open(fname) as file:
        for line in file:
            print line
            key , val = line.strip().split('=')
            iot_dict[key.strip()] = val.strip()
    return (iot_dict)

def arp_display(pkt):
    if pkt[ARP].op == 1: #who-has (request)
        if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
            if pkt[ARP].hwsrc == '74:c2:46:05:99:37': # SmartWater
                print "smartwater"
                pubpayload = mqttpub(cfgFile, dataDic)
            else:
                print "ARP Probe from unknown device: " + pkt[ARP].hwsrc


def main():
    print sniff(prn=arp_display, filter="arp", store=0, count=10)

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', required=True, help='Appliance config file')
    parser.add_argument('-f', required=True, help='Appliance data file - path and filename')
    args = parser.parse_args()
    cfgFile, datFile = args.c, args.f
    dataDic = getVarFromFile(datFile)
    main()
