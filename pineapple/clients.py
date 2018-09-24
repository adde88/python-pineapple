from module import Module

class Clients(Module):
    def __init__(self, api):
        super(Clients, self).__init__(api, 'Clients')

    def getClientData(self):
        """
            Return List of Clients
        """
        return self.request('getClientData')

    def kickClient(self, mac):
        """
            Kick a client by mac address
        """
        return self.request('kickClient', {'mac': mac})

