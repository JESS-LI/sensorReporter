# Purpose

Performs a network discovery to find the IP address of a given Roku.

# Dependencies

None

# Config

```
[Sensor6]
Class = rokuAddr.rokuAddr
Type = Roku
Connection = MQTT
Poll = 3600000
; Name is the serial number of the device, located on the label on bottom of device and listed on the Roku website
Name1 = XXXXXXXXXXXX
Destination1 = rokus/bedroom
Name2 = XXXXXXXXXXXX
Destination2 = rokus/den
```
