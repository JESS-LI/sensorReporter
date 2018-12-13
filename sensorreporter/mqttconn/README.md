# Purpose

Implements a two-way MQTT connection that can be used to publish (sensors, actuator results) and subscribe (sensors) to MQTT topics.

# Dependencies

paho-mqtt

# Config

```
[Connection1]
Class = mqttConn.mqttConnection
Name = MQTT
Client = sensorReporter
User = user
Password = password
Host = host
Port = 1883
Keepalive = 60
; Topic to listen on, when any message is received, the current state of all
; are published to their respective topics.
Topic = sensors/getUpdate
; The MQTT broker will publish the following message on the following topic
; when the client disconnects (cleanly or crashes)
LWT-Topic = status/sensor-reporters
LWT-Msg = mqttReporter is dead
; If TLS is yes the connection will be encrypted, the Certificate is expected to be in
; ./certs/ca.crt"
TLS = NO
```
