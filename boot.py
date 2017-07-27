# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import gc

# configura la rete wifi
import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('Alice-53272409', 'WifiFamigliaManfredi2016')
#demone per la connessione
import webrepl
webrepl.start()
gc.collect()



