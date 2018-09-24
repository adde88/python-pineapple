from module import Module

class Filters(Module):
    def __init__(self, api):
        super(Filters, self).__init__(api, 'Filters')

    def getSSIDMode(self):
        """
            Return SSID Mode
                Allow or Deny
        """
        return self.request('getSSIDData')

    def getClientMode(self):
        """
            Return Client Mode
                Allow or Deny
        """
        return self.request('getClientMode')

    def getSSIDFilters(self):
        """
            Return SSID Filters from DB
        """
        return self.request('getSSIDFilters')

    def getClientFilters(self):
        """
            Return Client Filters from DB
        """
        return self.request('getClientFilters')

    def getClientData(self):
        """
            Return array of mode and clientFilters
        """
        return self.request('getClientData')

    def getSSIDData(self):
        """
            Return array of mode and ssidFilters
        """
        return self.request('getSSIDData')

    def toggleClientMode(self, mode):
        """
            Toggle Client Mode
                Allow or Deny are valid values.
                Case Sensitive
        """
        return self.request('toggleClientMode', {'mode': mode})

    def toggleSSIDMode(self, allow):
        """
            Toggle SSID Mode
                Allow or Deny are valid values
                Case Sensisitve
        """
        return self.request('toggleSSIDMode', {'mode': mode})

    def addClient(self, mac):
        """
            Add Client by Mac to Filters
        """
        return self.request('addClient', {'mac': mac})

    def removeClient(self, mac):
        """
            Remove Client by Mac from Filters
        """
        return self.request('removeClient', {'mac': mac})

    def addSSID(self, ssid):
        """
            Add SSID to Filters
        """
        return self.request('addSSID', {'ssid': ssid})

    def removeSSID(self, ssid):
        """
            Remove SSID from Filters
        """
        return self.request('removeSSID', {'ssid': ssid})
