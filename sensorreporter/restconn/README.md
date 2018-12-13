# Purpose

One way Connection that can publish sensor readings directly to a REST API. 
This Connection has been tested with openHAB.

# Dependencies

requests

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
