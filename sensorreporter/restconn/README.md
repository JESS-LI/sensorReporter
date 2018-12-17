# Purpose

One way Connection that can publish sensor readings directly to a REST API. 
This Connection has been tested with openHAB.

# Dependencies

requests

# Config

```
[Connection2]
Class = restconn.restConn.restConnection
Name = REST
URL = http://localhost:8080/rest/items/
```
