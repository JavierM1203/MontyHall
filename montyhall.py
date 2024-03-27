import random

def montyHallImpriendo(changeDoor):
    
    puertas = ["Cabra", "Cabra", "Cabra"]
    
    posicionAuto = random.randint(0, 2)
    puertas[posicionAuto] = "Auto"
    print(f"Posición del Auto: {posicionAuto + 1}")
    
    puertaParticipante = random.randint(0, 2)
    print(f"Posición elegida por el participante: {puertaParticipante + 1}")
    
    # Si el participante escogió la puerta donde está el auto, hago que el 
    # presentador escoja al azar una puerta distinta a la del participante
    if puertas[puertaParticipante] == "Auto":
        puertaPresentador = random.randint(0, 2)
        while puertaPresentador == puertaParticipante:
            puertaPresentador = random.randint(0, 2)
    
    # Si el participante no escogió la puerta donde esta el auto, hago que
    # el presentador escoja la puerta donde no está el auto y que sea 
    # distinta a la del participante.
    else:
        for i in range(len(puertas)):
            if i != puertaParticipante and puertas[i] != "Auto":
                puertaPresentador = i        
    
    print(f"Puerta abierta por el presentador: {puertaPresentador + 1}")
    
    # Si el participante quiere cambiar puerta, busco la puerta que no ha sido
    # escogida por el presentador ni por el participante
    if changeDoor == True:
        for i in range(len(puertas)):
            if i != puertaParticipante and i != puertaPresentador:
                puertaParticipante = i
                print(f"El participante ha cambiado a la puerta {puertaParticipante + 1}")
                break
    else:
        print("El participante no ha cambiado de puerta")

    if puertas[puertaParticipante] == "Auto":
        return "El participante ha ganado el auto"
    return "El participante ha perdido"


def montyHall(changeDoor):
    
    puertas = ["Cabra", "Cabra", "Cabra"]
    
    posicionAuto = random.randint(0, 2)
    puertas[posicionAuto] = "Auto"
    
    puertaParticipante = random.randint(0, 2)
    
    if puertas[puertaParticipante] == "Auto":
        puertaPresentador = random.randint(0, 2)
        while puertaPresentador == puertaParticipante:
            puertaPresentador = random.randint(0, 2)
    else:
        for i in range(len(puertas)):
            if i != puertaParticipante and puertas[i] != "Auto":
                puertaPresentador = i        
    
    if changeDoor == True:
        for i in range(len(puertas)):
            if i != puertaParticipante and i != puertaPresentador:
                puertaParticipante = i
                break

    if puertas[puertaParticipante] == "Auto":
        return True
    return False
