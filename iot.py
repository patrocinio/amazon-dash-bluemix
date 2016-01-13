#!/usr/bin/python
import sys, json, datetime
import ibmiotf.device
from ibmiotf.codecs import jsonIotfCodec
import argparse

def mqttpub(cfgFile, dataDic):
    options = ibmiotf.device.ParseConfigFile(cfgFile)
    deviceCli = ibmiotf.device.Client(options)
    print 'Publish data to topic on IoTF'
    myData= dataDic
    myQosLevel=0
    deviceCli.publishEvent(event="status", msgFormat="json", data=myData, qos=myQosLevel)

def buildDict():
    iot_dict = {}
    iot_dict['button'] = 'smartwater'
    return (iot_dict)

def main():
    cfgFile = args.c
    dataDic = buildDict()
    pubpayload = mqttpub(cfgFile, dataDic)

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', required=True, help='Appliance config file')
    args = parser.parse_args()
    main()
