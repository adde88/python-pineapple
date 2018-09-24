from module import Module

class Logging(Module):

    def __init__(self, api):
        super(Logging, self).__init__(api, 'Logging')

    def getSyslog(self):
        """
            Return raw syslog
        """
        return self.request('getSyslog')

    def getDmesg(self):
        """
            Return raw dmesg
        """
        return self.request('getDmesg')

    def getReportingLog(self):
        """
            Return raw reporting log
        """
        return self.request('getReportingLog')

    def getPineapLog(self):
        """
            Return PineAP Log in JSON Format
        """
        return self.request('getPineapLog')

    def clearPineapLog(self):
        """
            Clear PineAP Log
        """
        return self.request('clearPineapLog')

    def getPineapLogLocation(self):
        """
            Return the path where PineAP Log is written
    
            default: /tmp/
        """
        return self.request('getPineapLogLocation')

    def setPineapLogLocation(self, location):
        """
            Update the path where PineAP Log is written

            default: /tmp/
        """
        return self.request('setPineapLogLocation', { 'location': location })
    
    def downloadPineapLog(self):
        """
            Return the download token for PineAP Log
        """
        return self.request('downloadPineapLog')

