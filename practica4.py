import datetime
from time import ctime
import ntplib
import os

server="time-e-g.nist.gov"

x= datetime.datetime.now()

print("t1 = %s" % x)

ntp_client=ntplib.NTPClient()
respuesta=ntp_client.request(server)
ac_hour=datetime.datetime.strptime(ctime(respuesta.tx_time), "%a %b %d %H:%M:%S %Y")

y= datetime.datetime.now()
print("t2 = %s" % y)
print("tiempo del servidor = %s" % ac_hour)

ajuste=(y-x)/2

print("tiempo de ajuste = %s" % ac_hour)

reloj=ac_hour+ajuste

print("hora nueva del sistema = %s" % ac_hour)

os.system('date --set "%s"' %reloj)
