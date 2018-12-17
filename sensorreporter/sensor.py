"""
   Copyright 2018 Richard Koshak

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

 Script:  connection.py
 Author:  Rich Koshak
 Date:    December 16, 2018
 Purpose: Base class for sensorReporter sensors
"""

from abc import ABC, abstractmethod
from configparser import NoOptionError

class Sensor(ABC):
    """Abstract parent class of all sensors."""

    def __init__(self, logger, params, connections):
        """Performs initialization needed by all sensors"""

        self.logger = logger
        self.connections = connections
        self.params = params
        try:
            self.poll = int(params("Poll"))
        except NoOptionError:
            self.logger.warn("No Poll parameter, using -1")
            self.poll = 0
        self.nodename = params("NodeName")
        self.destination = self.nodename
        self.logger.info("Initializing {0}".format(self.nodename))
        

    @abstractmethod
    def checkState(self):
        """Called by the polling thread to read the sensor value(s)"""
        pass

    def publishState(self, data, destination):
        """Iterates through all the registered connections and sends data to the given destination"""
        for conn in self.connections:
            conn.publish(data, destination)

    def publishCurrState(self):
        """Called to publish the sensor's current state"""
        self.publishState(self.state, self.destination)

    @abstractmethod
    def cleanup(self):
        """Called before seneorReporter closes down"""
        pass
