# Purpose

Executes a shell command on command (Actuator) or periodically (Sensor). 

# Dependencies

None

# Config

```
[Sensor3]
; Sensor that executes the configured script or program and publishes the restults to the destination
Class = exec.execSensor.execSensor
Type = Exec
Connection = MQTT
Poll = 30
Script = ./iphone.sh 123.45.56.8 fe:dc:ba:98:76:54
Destination = scripts/presence/iphone/results

[Actuator2]
Class = exec.execActuator.execActuator
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
