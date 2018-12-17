# Purpose

Periodically publishes the sensorReporter's uptime. Do not use with Homie. 


# Dependencies

None

# Config

```
[Sensor8]
Class = heartbeat.heartbeat.heartbeat
Type = Heartbeat
Connection = MQTT
Poll = 3600000
; The number of milliseconds sensorReporter has been online is published to this destination
Num-Dest = status/heartbeat
Str-Dest = status/hearbeatstr
```
