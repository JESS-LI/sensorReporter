# Purpose

Implements GPIO sensors, actuators, a Connection, and an example script called when the Connection receives a message.

# Dependencies

None

# Config

```
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

[Sensor9]
; Native Raspberry Pi Library - event handling only
Class = rpiGPIOSensor.rpiGPIOSensor
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
Class = rpiGPIOActuator.rpiGPIOActuator
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
Class = rpiGPIOConn.rpiGPIOConn
Actuator = Actuator1
# First value set pin off and second on. Defaults to OFF,ON
Values = CLOSED,OPEN
```
