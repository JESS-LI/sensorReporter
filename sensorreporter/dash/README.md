# Purpose

Uses network sniffing to watch for ARP packets from Dash buttons.

# Dependencies

scapy and sensorReporter must run as root.

# Config

```
[Sensor5]
Class = dash.dash.dash
Connection = MQTT
; One Address/Destination pair per button, start with 1, increment numbers
; Mac address
Address1 = 12:34:56:78:90:12
Destination1 = actuators/bounty
Address2 = 21:09:87:65:43:21
Destination2 = actuators/tide
; -1 means this sensor doesn't need to use the main polling thread, it polls on
; its own
Poll = -1
```
