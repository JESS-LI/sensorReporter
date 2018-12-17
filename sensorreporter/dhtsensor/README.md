# Purpose

Uses the Adafruit DHT library to read a DHT11 or DHT22 temperature/humidity sensor from GPIO.

# Dependencies

Adafruit_DHT library and the user sensorReporter runs as must be a member of the gpio group.

# Config

```
[Sensor7]
; DHT22 Sensor
Class = dhtsensor.DHTSensor.DHTSensor
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
```
