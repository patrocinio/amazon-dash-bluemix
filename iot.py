#!/usr/bin/python
import sys, json, datetime
import ibmiotf.device
from ibmiotf.codecs import jsonIotfCodec
import argparse

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

def main():
    cfgFile, datFile = args.c, args.f
    dataDic = getVarFromFile(datFile)
    pubpayload = mqttpub(cfgFile, dataDic)

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', required=True, help='Appliance config file')
    parser.add_argument('-f', required=True, help='Appliance data file - path and filename')
    args = parser.parse_args()
    main()
