import montyhall

vecesJugadas = 1000
vecesGanadasCambiando = 0
vecesGanadasSinCambiar = 0

for i in range(vecesJugadas):
    if montyhall.montyHall(True):
        vecesGanadasCambiando += 1
    if montyhall.montyHall(False):
        vecesGanadasSinCambiar += 1

print(f"Al jugar {vecesJugadas} veces, se ganaron {vecesGanadasCambiando} veces al cambiar y {vecesGanadasSinCambiar} veces al no cambiar")
    
