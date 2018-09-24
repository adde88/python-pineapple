from module import Module

class Recon(Module):
    def __init__(self, api):
        super(Recon, self).__init__(api, 'Recon')
    def getScanStatus(self, scanId, scanType):
        """ This method is deprecated but left in for compatibility with older firmware """
        return self.request('getScanStatus', {'scan': {'scanID': scanId, 'scanType': scanType}})
    def startScan(self, scanType, scanDuration):
        """ This method is deprecated but left in for compatibility with older firmware """
        return self.request('startScan', {'scanType': scanType, 'scanDuration': scanDuration})
    def startNormalScan(self, scanType, scanDuration):
        """ Start a Normal Scan
            Scan Type: 
                0 - 2.4 Ghz
                1 - 5 Ghz
                2 - Both
        """
        return self.request('startNormalScan', {'scanType': scanType, 'scanDuration': scanDuration})
    def startLiveScan(self, scanType, scanDuration):
        """ Start a Live Scan
            Scan Type:
                0 - 2.4 Ghz
                1 - 5 Ghz
                2 - Both
        """
        return self.request('startLiveScan', { 'scanType': scanType, 'scanDuration': scanDuration})
    def checkPineAPDaemon(self):
        """ Errors on return but added to mirror recon api """
        return self.request('checkPineAPDaemon')
    def startPineAPDaemon(self):
        """ Start Pine AP Daemon """
        return self.request('startPineAPDaemon')
    def getScans(self):
        """ Return a list of Scans """
        return self.request('getScans')
    def downloadResults(self, scanId):
        """ Download Scan Results by ID 
                Basically a limited stub right now,
                Pending rewrite of Pineapple module to download data
        """
        return self.request('downloadResults', { 'scanId': scanId })
    def removeScan(self, scanId):
        """ Delete a scan by ID """
        return self.request('removeScan', { 'scanId': scanId})
    def getCurrentScanID(self):
        """ Return ID of Current Scan """
        return self.request('getCurrentScanID')
    def stopScan(self):
        """ Stop currently running scan 
                Note: This is not by scan ID but rather just currently running scan
        """
        return self.request('stopScan')
    def loadResults(self, scanId):
        return self.request('loadResults', { 'scanId': scanId })

