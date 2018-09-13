import requests
import json
import urllib
from . import __version__

API_URL = 'http://172.16.42.1:1471/api/'

class API(object):
    def __init__(self, apiToken, url = None):
        super(API, self).__init__();
        self.apiToken = apiToken
        self.url = url if url else API_URL
        self.userAgent = 'Pynapple ' + __version__
        self.headers = {'User-Agent': self.userAgent, 'Content-Type': 'application/json', 'Accept': 'application/json,'}
    def request(self, type, module, action, args = None):
        requestObject = {'apiToken': self.apiToken, type: module, 'action': action}
        if args:
            requestObject.update(args)
        payload = json.dumps(requestObject)
        resp = requests.post(self.url, data=payload, headers=self.headers)
        try:
			# Update for latest firmware: 
			# 		The latest firmware puts 6 junk chars in the beginning of the json stream
			# 		Filtering that out.
            return json.loads(resp.text[6:])
        except ValueError as e:
            print("Error decoding: %".format(repr(resp.text)))
            print e

    def download(self, dFile):
        """
            Download a file by token. Just returning text instead of json as a just in case.
            Easy to handle by just grabbing the response object and hitting it with json.loads
                -- This was added to be able to download recon scans but I'm sure someone else might have another use for it
        """
        requestObject = {'apiToken': self.apiToken, 'download': dFile }
        resp = requests.get(self.url, requestObject)
        return resp.text

