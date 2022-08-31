# Tad Proceso
# De cada proceso se conoce el nombre, tipo de proceso, tamaño, prioridad, fecha y hora de la última modificación.

def crearProceso():
    #Crea un proceso vacio
    pro=["","","","","","",""]
    return pro

def cargarProceso(pro, nom, id, tipo, tam, pri, fecha, hora):
    #Carga los datos de un proceso:
    pro[0]=nom                      #nombre
    pro[1]=id                       #id unico
    pro[2]=tipo                     #tipo
    pro[3]=tam                      #tamanio
    pro[4]=pri                      #prioridad
    pro[5]=fecha                    #fecha
    pro[6]=hora                     #hora

def verNom(pro):
    #Retorna el nombre de un proceso
    return pro[0]

def verId(pro):
    #Retorna el id de un proceso
    return pro[1]

def verTipo(pro):
    #Retorna el tipo de proceso
    return pro[2]

def verTam(pro):
    #Retorna el tamanio de un proceso
    return pro[3]

def verPri(pro):
    #Retorna la prioridad de un proceso
    return pro[4]

def verFecha(pro):
    #Retorna la fecha de un proceso
    return pro[5]

def verHora(pro):
    #Retorna la hora de un proceso
    return pro[6]

def modNom(pro, nNom):
    #Modifica el nombre de un proceso
    pro[0] = nNom

def modId(pro, nId):
    #Modifica el id de un proceso
    pro[1] = nId

def modTipo(pro, nTipo):
    #Modifica el tipo de proceso
    pro[2] = nTipo

def modTam(pro, nTam):
    #Modifica el tamanio de un proceso
    pro[3] = nTam

def modPri(pro, nPri):
    #Modifica la prioridad de un proceso
    pro[4] = nPri

def modFecha(pro, nFecha):
    #Modifica la fecha de un proceso
    pro[5] = nFecha

def modHora(pro, nHora):
    #Modifica la hora de un proceso
    pro[6] = nHora

def asignarProceso(pro1, pro2):
    #Asigna datos de un proceso en otro (datos de pro2 pasan a pro1)
    modNom(pro1, verNom(pro2))
    modTipo(pro1, verTipo(pro2))
    modTam(pro1, verTam(pro2))
    modPri(pro1, verPri(pro2))
    modFecha(pro1, verFecha(pro2))
    modHora(pro1, verHora(pro2))