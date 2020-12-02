import os
import sys
import psycopg2
import commands
import ConfigParser
import time

config = ConfigParser.ConfigParser()
config.readfp(open(r'/boot/geko.txt'))

gekoserver = config.get('geko', 'IP_SERVIDOR')
gekobase = config.get('geko', 'BASE_DATOS')
iddispositivo = config.get('geko', 'ID_DISPOSITIVO')
idnet = config.get('geko', 'ETHERNET')

params = {
  'dbname': gekobase,
  'user': 'postgres',
  'password': '123aiculedASD..',
  'host': gekoserver,
  'port': 5432
}

print params

def getMAC(interface):
        # Return the MAC address of interface
        try:
                str = open('/sys/class/net/' + interface + '/address').read()
        except:
                str = "00:00:00:00:00:00"
        return str[0:17]


print commands.getoutput('hostname -I')

while True:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        sql = "select gc13_estado from gc13_dispositivo where gc13_id_dispositivo = %s" % iddispositivo
        cur.execute(sql)

        x = cur.fetchone()[0]

        macdisp = getMAC(idnet)
        ipdisp = commands.getoutput('hostname -I')

        if(x == 2):

                print "debo reiniciar"

                #print sql

                sql = "update gc13_dispositivo set gc13_estado = 3 , gc13_fecha_reporte = now() where gc13_id_dispositivo = %s" % iddispositivo

                cur.execute(sql)
                conn.commit()

client_loop: send disconnect: Connection reset by peer
crosales@KAZETA-PC:~$
                #print sql
        else:
                print "estoy online"

                sql = "update gc13_dispositivo set gc13_estado = 1 , gc13_fecha_reporte = now(), gc13_mac = '%s', gc13_ip = '%s' where gc13_id_dispositivo = %s" % (macdisp,ipdisp,iddispositivo)

                cur.execute(sql)
                conn.commit()

        conn.close()
        time.sleep(1)
