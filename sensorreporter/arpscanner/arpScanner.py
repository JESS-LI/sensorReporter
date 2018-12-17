"""
   Copyright 2016 Richard Koshak / Lenny Shirley

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

 Script:      arpScanner.py
 Author:      Rich Koshak / Mark Radbourne
 Date:        September 24, 2018
 Purpose:     Grabs the current ARP cache and reports if a specific MAC address is present.

 SR 2.0 Changes: Inherit from Sensor, changed to read the arp table directly instead of 
   calling the arp command.
"""

import sensor
import sys
import os

class arpScanner(sensor.Sensor):
    """Represents a Mac address to search for in arp output"""

    def __init__(self, connections, logger, params):
        """Initializes the ARP scanner"""

        super().__init__(logger, params, connections)

        self.address = params("Address").lower()
		
		# Colons in MAC address mess up openHab MQTT item syntax so convert to dots
        self.destination = self.nodename + '/' + self.address.replace(':', '.')
        self.state = 'UNDEF'

        self.logger.info("----------Configuring arpSensor: Address = " + self.address + " Destination = " + self.destination)

        self.checkState()

    def checkState(self):
        """Detects and publishes any state change"""

        state = 'OFF'
        inf = open('/proc/net/arp')
        try:
            for line in inf:
                if line.split()[3].lower() == self.address:
                    state = 'ON'
                    break        
        finally:
            inf.close()

        if state != self.state:
            self.state = state
            self.publishCurrState()

    def cleanup(self):
        """Does nothing"""
        pass
