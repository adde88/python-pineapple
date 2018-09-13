# python-pineapple
WiFi pineapple API Wrapper written in python

## Documentation
Documentation is a work in progress. It may not be complete for a while, but I believe the code to be very readable and if you do know python it shouldn't be too hard to figure out.
Some hints:
- All modules have the same name they do on the pineapple (all lower case). To see what a module can do just run `help(fruit.getModule(modulename))`
- To find out more about the WiFi Pineapple API itself, set `debug = True` when instantiating your `Pineapple()`s and it will log the HTTP requests it makes
- Read the WiFi Pineapple php source located on your pineapple at `/pineapple/modules/$modulename/api/module.php` as well as the corresponding python files in this project

## Examples:
##### Instantiate a Pineapple object:
<pre>
API_TOKEN = "xxxxxxxxxx..."
from pineapple import *
fruit = pineapple.Pineapple(API_TOKEN)
</pre>
##### Add a notification:
<pre>
fruit.getModule("notifications").addNotification("test")
</pre>
##### Start PineAP
<pre>
fruit.getModule("pineap").enable()
</pre>
##### Deauth/dissasoc the clients `73:65:62:6b:69:6e` and `6e:65:73:67:69:61` from the bssid `6e:74:64:69:63:6b` 5 times on channel 1
<pre>
fruit.getModule("pineap").deauth('6e:74:64:69:63:6b', ['73:65:62:6b:69:6e', '6e:65:73:67:69:61'], 5, 1)
</pre>
##### Get SSID Pool
<pre>
p = fruit.getModule("pineap").getSSIDPool()
</pre>
Returns a dict. The pool is on the key "ssidPool" separated by newlines. To get a quick list, do the following:
<pre>
ssids = p['ssidPool'].split('\n')
</pre>
##### Download Scans
Some support for download files via token was added to api and recon
<pre>
fruit.getModule("recon").downloadResults(1)
</pre>
Will return a dict with key "download" and a unique download token for the results of Scan ID 1. So knowing that,
you can call api.download now to get the results
<pre>
myScan = fruit.api.download(fruit.getModule("recon").downloadResults(1)['download'])
</pre>
myScan will be the raw file text. In the case of a recon scan, it is json. So you can make it more usable with json.loads(myScan)
*To generate API tokens, use the [API Tokens](https://github.com/735tesla/Pineapple-API-Tokens-Module/) module*
