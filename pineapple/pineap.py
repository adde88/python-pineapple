import json
from module import Module

class Pineap(Module):
    def __init__(self, api):
        super(Pineap, self).__init__(api, 'PineAP')

        """
            List of Methods this module needs:

            getPool
clearPool
addSSID
addSSIDs
removeSSID
getPoolLocation
setPoolLocation
setPineAPSettings
getPineAPSettings
setEnterpriseSettings
getEnterpriseSettings
detectEnterpriseCertificate
generateEnterpriseCertificate
clearEnterpriseCertificate
clearEnterpriseDB
getEnterpriseData
startHandshakeCapture
stopHandshakeCapture
getHandshake
getAllHandshakes
checkCaptureStatus
downloadHandshake
downloadAllHandshakes
clearAllHandshakes
deleteHandshake
deauth
enable
disable
enableAutoStart
disableAutoStart
downloadPineAPPool
loadProbes
inject
countSSIDs
downloadJTRHashes
downloadHashcatHashes

        """

    def getSSIDPool(self):
        """
            Return raw SSID Pool.

            Note: It's just a \n terminated list
        """
        return self.request('getPool')

    def clearPool(self):
        """
            Clear the SSID Pool
        """
        return self.request('clearPool')

    def addSSID(self, ssid):
        """
            Add SSID to Pool
        """
        return self.request('addSSID', {'ssid': ssid})

    def removeSSID(self, ssid):
        """
            Remove SSID from Pool
        """
        return self.request('removeSSID', {'ssid': ssid})

    def setPineAPSettings(self, settings):
        """
            Set PineAP Settings.
            Hand settings as a Python Dictionary
        """
        self.request('setPineAPSettings', {'settings': json.dumps(settings)})

    def getPineAPSettings(self):
        """
            Get Current PineAP Settings
        """
        return self.request('getPineAPSettings')

    def deauth(self, sta, clients, multiplier, channel):
        """
            Deauth a Client from a Station X times on Y Channel
        
            Args in order: Station, Client, Multiplier, Channel

        """
        multiplier = 10 if multiplier > 10 else multiplier
        return self.request('deauth', {'sta': sta, 'clients': clients, 'multiplier': multiplier, 'channel': channel})

    def enable(self):
        """
            Enable PineAP
        """
        return self.request('enable')

    def disable(self):
        """
            Disable PineAP
        """
        return self.request('disable')

    def saveSettignsAsDefault(self, config = None):
        """
            Hand a config as Python Dictionary.
            Once it updates, save as default
        """
        if config:
            resp = self.setPineAPSettings(config)
            if (resp['error']):
                return resp
        return self.request('saveAsDefault')
