"""
   Copyright 2016 Richard Koshak

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

 Script: heartbeat.py
 Author: Rich Koshak
 Date:   October 7, 2016
 Purpose: Sends out a heartbeat message on the polling period

 SR 2.0: Implement the new sensor baseclass.
"""

import sensor
import sys
import time

class heartbeat(sensor.Sensor):
    """Issues a heartbeat message on the polling period"""

    def __init__(self, connections, logger, params):
        """Sets the heartbeat message and destination"""

        super().__init__(logger, params, connections)

        self.numDest = params("Num-Dest")
        self.strDest = params("Str-Dest")
        self.startTime = time.time()
        self.utmsec = 0
        self.utstr = "00:00:00"

        self.logger.info('----------Configuring heartbeat to msec destination {0} and str destinatin {1} with interval {2}'.format(self.numDest, self.strDest, self.poll))
        self.checkState()

    def checkState(self):
        """Calculates and publishes the current state"""
        uptime = int(time.time() - self.startTime)

        self.upmsec = uptime * 1000
       
        sec = uptime % 60
        min = (uptime / 60) % 60
        hr  = (uptime / (60*60)) % 24
        day = uptime / (60*60*24)
        msg = ''

        if day > 0:
          msg += '{0}:'.format(day)
        msg += '{0:02d}:{1:02d}:{2:02d}'.format(int(hr), int(min), int(sec))
        self.utstr = msg

        self.publishState(str(self.upmsec), self.numDest)
        self.publishState(self.utstr, self.strDest)

    def publishCurrState(self):
        """Overrides the parent class implementation, publishes the uptime in msec and as a string"""
        self.publishState(str(self.upmsec), self.numDest)
        self.publishState(self.upstr, self.strDest)
    
    def cleanup(self):
        """Does nothing"""
        pass
