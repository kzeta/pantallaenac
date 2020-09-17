# Pantalla para enac
## Componentes a instalar

```sh
sudo apt-get install libglib2.0-dev libudev-dev libusb-1.0-0-dev libx11-dev libxrandr-dev libdrm-dev
sudo pip install omxplayer-wrapper
sudo pip install pathlib
sudo pip install psutil

```


## Datos de la Raspberry

Obtener el ID
 ```python
 def getserial():
  # Extract serial from cpuinfo file
  cpuserial = "0000000000000000"
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
        cpuserial = line[10:26]
    f.close()
  except:
    cpuserial = "ERROR000000000"

  return cpuserial
  ```
