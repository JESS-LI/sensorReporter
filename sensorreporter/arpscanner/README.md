# Purpose

Calls the arp command to look for the given MAC address.

# Dependencies

None

# Config

```
[Sensor12]
; Scans the ARP cache for the specified MAC address and reports present or not
Class: arpscanner.arpScanner.arpScanner
Name: AWiFiPhone
Address = 00:00:00:11:aa:bb
Connection: MQTT
Destination: State/Presence
Poll: 10
```
