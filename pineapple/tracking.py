from module import Module

class Tracking(Module):
    def __init__(self, api):
        super(Tracking, self).__init__(api, 'Tracking')

    def getScript(self):
        """
            Return contents of user tracking script.

            Default Script contents:

            #!/bin/bash

            echo $MAC
            echo $TYPE # 0 PROBE; 1 ASSOCIATION
            echo $SSID
        """
        return self.request('getScript')

    def setScript(self, script):
        """
            Set script content for user tracking

            Default Script contents:

            #!/bin/bash
            echo $MAC
            echo $TYPE # 0 PROBE; 1 ASSOCIATION
            echo $SSID
        """
        return self.request('saveScript', {'trackingScript': script})

    def getTrackingList(self):
        """
            Return list of macs being tracked
        """
        return self.request('getTrackingList')

    def addMac(self, mac):
        """
            Add mac to Tracking List
        """
        return self.request('addMac', {'mac': mac})

    def removeMac(self, mac):
        """
            Remove mac from tracking list
        """
        return self.request('removeMac', {'mac': mac})

    def clearMacs(self):
        """
            Clear all macs from Tracking
        """
        return self.request('clearMacs')
