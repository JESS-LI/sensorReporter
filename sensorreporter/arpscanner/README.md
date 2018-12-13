# Purpose

Calls the arp command to look for the given MAC address.

# Dependencies

subprocess23 if running in Pyhton 2

None if running in Python 3

# Config

```
[Sensor12]
; Scans the ARP cache for the specified MAC address and reports present or not
Class: arpScanner.arpScanner
Name: AWiFiPhone
Address = 00:00:00:11:aa:bb
Connection: MQTT
Destination: State/Presence
Poll: 10
```
