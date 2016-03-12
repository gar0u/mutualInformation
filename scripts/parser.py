#!/usr/bin/env python3
"""
Docs go here
"""

import sys

# Create a set of dictionary objects 
# to keep track of uniquely observed values
# and assign them a symbol

dictSIP = {}      # Source IP
dictDIP = {}      # Destination IP
dictSPort = {}    # Source port
dictDPort = {}    # Destination port
dictPro = {}      # Protocol
dictPackets = {}  # Number of packets
dictBytes = {}    # Number of bytes
dictFlags = {}    # Flags
dictSTime = {}    # Start Time (not used)
dictDuration = {} # Duration
dictETime = {}    # End Time (not used)
dictSen = {}      # Sen?

# ... and a list of 'streams'
streams = []

# A list of next available symbols  (N.b. this should really be a class...)
dictSIPNextSymbol = 'A'
dictDIPNextSymbol = 'A'
dictSPortNextSymbol = 'A'
dictDPortNextSymbol = 'A'
dictProNextSymbol = 'A'
dictPacketsNextSymbol = 'A'
dictBytesNextSymbol = 'A'
dictFlagsNextSymbol = 'A'
dictSTimeNextSymbol = 'A'
dictDurationNextSymbol = 'A'
dictETimeNextSymbol = 'A'
dictSenNextSymbol = 'A'

try:
    filename = sys.argv[1]
except IndexError:
    print('Usage: ./parser.py [filename]')
    exit()

f = open(filename, 'r')
f.readline()  # Skip the first line, which is headers
for line in f:
    stream = ''
    elements = line.split('|')

    sIP = elements[0].strip()
    dIP = elements[1].strip()
    sPort = elements[2].strip()
    dPort = elements[3].strip()
    pro = elements[4].strip()
    packets = elements[5].strip()
    bytes = elements[6].strip()
    flags = elements[7].strip()
    sTime = elements[8].strip()
    duration = elements[9].strip()
    eTime = elements[10].strip()
    sen = elements[11].strip()            

    # (N.b. These should really be a function)
    # Source IP
    if sIP in dictSIP:
        stream += dictSIP[sIP]
    else:        
        dictSIP.update({sIP:dictSIPNextSymbol})
        dictSIPNextSymbol = chr(ord(dictSIPNextSymbol)+1)            
        stream += dictSIP[sIP]
    # Destination IP
    if dIP in dictDIP:
        stream += dictDIP[dIP]
    else:        
        dictDIP.update({dIP:dictDIPNextSymbol})
        dictDIPNextSymbol = chr(ord(dictDIPNextSymbol)+1)            
        stream += dictDIP[dIP]
    # Source Port
    if sPort in dictSPort:
        stream += dictSPort[sPort]
    else:        
        dictSPort.update({sPort:dictSPortNextSymbol})
        dictSPortNextSymbol = chr(ord(dictSPortNextSymbol)+1)            
        stream += dictSIP[sIP]
    # Destination Port
    if dPort in dictDPort:
        stream += dictDPort[dPort]
    else:        
        dictDPort.update({dPort:dictDPortNextSymbol})
        dictDPortNextSymbol = chr(ord(dictDPortNextSymbol)+1)            
        stream += dictDPort[dPort]
    # Packets
    if packets in dictPackets:
        stream += dictPackets[packets]
    else:        
        dictPackets.update({packets:dictPacketsNextSymbol})
        dictPacketsNextSymbol = chr(ord(dictPacketsNextSymbol)+1)            
        stream += dictPackets[packets]
    # Bytes
    if bytes in dictBytes:
        stream += dictBytes[bytes]
    else:        
        dictBytes.update({bytes:dictBytesNextSymbol})
        dictBytesNextSymbol = chr(ord(dictBytesNextSymbol)+1)            
        stream += dictBytes[bytes]
    # Flages
    if flags in dictFlags:
        stream += dictFlags[flags]
    else:        
        dictFlags.update({flags:dictFlagsNextSymbol})
        dictFlagsNextSymbol = chr(ord(dictFlagsNextSymbol)+1)            
        stream += dictFlags[flags]
    # Start time
    # if sTime in dictSTime:
    #     stream += dictSTime[sTime]
    # else:        
    #     dictSTime.update({sTime:dictSTimeNextSymbol})
    #     dictSTimeNextSymbol = chr(ord(dictSTimeNextSymbol)+1)            
    #     stream += dictSTime[sTime]
    # Duration
    if duration in dictDuration:
        stream += dictDuration[duration]
    else:        
        dictDuration.update({duration:dictDurationNextSymbol})
        dictDurationNextSymbol = chr(ord(dictDurationNextSymbol)+1)            
        stream += dictDuration[duration]
    # End Time
    # if eTime in dictETime:
    #     stream += dictETime[eTime]
    # else:        
    #     dictETime.update({eTime:dictETimeNextSymbol})
    #     dictETimeNextSymbol = chr(ord(dictETimeNextSymbol)+1)            
    #     stream += dictETime[eTime]
    # Sen?
    if sen in dictSen:
        stream += dictSen[sen]
    else:        
        dictSen.update({sen:dictSenNextSymbol})
        dictSenNextSymbol = chr(ord(dictSenNextSymbol)+1)            
        stream += dictSen[sen]

    streams.append(stream)

for stream in sorted(streams):
    print(stream)

print(dictSIP)

