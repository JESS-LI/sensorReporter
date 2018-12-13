# Purpose

Executes a shell command on command (Actuator) or periodically (Sensor). 

# Dependencies

subprocess32 if running on Python2

None if running on Python 3

# Config

```
[Sensor7]
; DHT22 Sensor
Class = DHTSensor.DHTSensor
Sensor = DHT22
Pin = 27
; Either Advanced or Simple
Mode = Advanced
; Round temperature with one digit
PressionTemp = 1
; Round humidity to zero digits
PressionHum = 0
; Select C or F units - defaults to C if not specified
Scale = C
Connection = MQTT
Destination = sensor7/dht22
Poll = 10

[Actuator2]
Class = execActuator.execActuator
Type = Exec
; Actuators only support MQTT at this time
; The content of messages are added as arguments to the command
; Use NA for no arguments
; Arguments that include ';', '|', or '\' are ignored
Connection = MQTT
Poll = 0
; Arguments with ';', '|', and '\' will be ignored
Command = /bin/systemctl restart plexmediaserver.service
CMDTopic = scripts/restartplex
; The output string from the command is posted to the below topic.
; If the command returned a non-zero exit code, "ERROR" is published
ResultTopic = scripts/restartplex/results
```
