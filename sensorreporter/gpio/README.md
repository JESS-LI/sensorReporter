# Purpose

Implements GPIO sensors, actuators, a Connection, and an example script called when the Connection receives a message.

# Dependencies

None

# Config

```
[Sensor9]
; Native Raspberry Pi Library - event handling only
Class = gpio.rpiGPIOSensor.rpiGPIOSensor
Pin = 4
Connection = MQTT
Destination = sensor2/topic
PUD = DOWN
; Allows the pin to be initialized to a known state - UP/DOWN defaults to DOWN
InitialState = UP
; EventDetection - RISING/FALLING/BOTH
EventDetection = BOTH
; Optional custom script called when an event occurs
StateCallback = switchLed
; Optional free form args for above script - can identify actuator for example by section name
StateCallbackArgs = Actuator1,Actuator2
Poll = -1

[Actuator1]
Class = gpio.rpiGPIOActuator.rpiGPIOActuator
; The chosen connection must support a register(path, handler) method the actuators can call
; to receive specific incoming messages. See mqttConn.py for an example
; restConnection is not supported.
Connection = MQTT
Pin = 17
Topic = actuators/actuator1
; When true set the pin to LOW for half a second then set it to HIGH when any message is received 
; on Topic
; Otherwise if the message is "ON" set the pin to HIGH, if the message is "OFF: set the pub to LOW.
Toggle = True
Poll = 0

[Connection3]
Name = PinConn
Class = gpio.rpiGPIOConn.rpiGPIOConn
Actuator = Actuator1
# First value set pin off and second on. Defaults to OFF,ON
Values = CLOSED,OPEN
```
