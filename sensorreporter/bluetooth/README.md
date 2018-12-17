# Purpose

Performs periodic scans for given Bluetooth devices.

# Dependencies

bluez, python-bluez for standard scanning
bluepy for BTLE scanning

# Config

```
[Sensor2]
Class = bluetooth.bluetoothScanner.btSensor
Address = F8:F1:B6:3C:4A:FA
Destination = BluetoothItem
Connection = REST
; Needs to be greater than 1 if using the RSSI mode, 25 if using the LOOKUP mode.
Poll = 2
; Uses signal strength to detect presence of devices
Mode = RSSI
; RSSI - Maximum count for near/far readings
Max = 20
; RSSI - How many near counts before declaring device present
Near = 3
; RSSI - How many far counts before declaring device absent
Far = 15

[Sensor3]
Class = bluetooth.bluetoothScanner.btSensor
Address = E8:E0:A5:2B:39:E9
Connection = MQTT
Destination = sensor4/topic
Poll = 25
Mode = LOOKUP

; Scan for Bluetooth LE devices like an Gigaset G-tag. Scns for presence.
; Does not read any values of the device
[Sensor4]
Class = bluetooth.bluetoothScanner.btSensor
Address = A1:B2:C3:D4:E5:F6
Connection = MQTT
Destination = switch/topic
Mode = BTLE
; How often the values are published. Must be higher than ScanTimeout
Poll = 10
; Scans for x seconds before it validates if the given address is found.
ScanTimeout = 3
; Keyword if the device is found. Could be any value. If option is not set and
; empty the default published value is "ON"
ON = home
; Keyword if the device is NOT found. Could be any value. If option is not set
; and empty the default published value is "OFF"
OFF = away
```
