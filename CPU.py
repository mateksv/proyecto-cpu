#   ENTREGA: 11 DE JUNIO 2021
#   GRUPO 15: GIMENEZ NAZARENO 31194 - SANCHEZ VIAMONTE MATEO 31035
#   Se tiene una Cola de procesos que necesitan ocupar la CPU. De cada proceso se conoce el nombre,
#   tipo de proceso, tamaño, prioridad, fecha y hora de la última modificación. Se deberá desarrollar
#   una aplicación, utilizando los TADs que crea necesarios. Se desea tener un menú con los siguientes
#   puntos:
#   a) Encolar proceso.
#   b) Modificar la prioridad del proceso.
#   c) Desencolar proceso. 
#   d) Listado de procesos.
#   e) Dado un determinado mes, modificar la prioridad de los procesos a baja.
#   f) Eliminar los procesos cuyo tipo sea igual al ingresado.
#   g) Generar una cola con aquellos procesos cuya última modificación se encuentre entre dos horas dadas.

# IMPORTO LAS LIBRERIAS
import UTILIDADES, TAD_COLA, TAD_PROCESO, time
from UTILIDADES import *
from TAD_COLA import *
from TAD_PROCESO import *

# CREO UNA COLA PARA INGRESARLE LOS PROCESOS
cola = crearCola()
# CREO UNA COLA AUXILIAR
colaAux = crearCola()
# CREO UNA COLA AUXILIAR 2
colaAux2 = crearCola()
# CREO LA LISTA
lista=[]

# MENU
def menu():
    clear()
    print("==="*20)
    print(" "*20 + "<<< MENU DEL CPU >>>" + " "*20)
    print("==="*20)
    print("a) Encolar proceso.")
    print("b) Modificar la prioridad del proceso.") 
    print("c) Desencolar proceso.") 
    print("d) Listado de procesos.") 
    print("e) Modificar la prioridad de los procesos a baja.")
    print("f) Eliminar los procesos cuyo tipo sea igual al ingresado.")
    print("g) Generar una cola con aquellos procesos cuya última \n   modificación se encuentre entre dos horas dadas.")
    print("==="*20)
    print("0) Finalizar ejecucion.")
    print("==="*20)
    res = input("---> ")
    return res.lower() #Retorna el valor en minuscula

# ENCOLAR PROCESO
def puntoA():
    clear()
    titulo = " >> ENCOLAR PROCESO >>"       #
    l = len(titulo)                         #
    print("="*l)                            # Titulo
    print(titulo)                           #
    print("="*l)                            #

    pro = crearProceso() #Creo un proceso nuevo

    id = codNumRand(5)
    nom = input("Nombre: ")
    #tipo = input("Tipo: ").capitalize()
    #tam = input("Tamaño: ")
    #nom = codMayusRand(8)
    tipo = "Prueba"
    tam =  str(random.randint(5, 3000)) + " Mb"
    #pri = input("Prioridad: ").capitalize() #.capitalize: la primera letra es mayuscula, el resto no
    pri = "Alta"
    fecha = time.strftime("%d/%m/%Y", time.localtime()) #Utilizo la libreria 'time'
    hora = time.strftime("%H:%M:%S", time.localtime())  #Utilizo la libreria 'time'

    cargarProceso(pro, nom, id, tipo, tam, pri, fecha, hora) #Cargo los datos del proceso
    encolar(cola, pro) #Encolo el proceso

# MODIFICO PRIORIDAD DE PROCESO
def puntoB():
    
    clear()
    titulo = " >> MODIFICAR PRIORIDAD DE PROCESO >>"
    l = len(titulo)
    print("="*l)
    print(titulo)
    print("="*l)

    idPro = input("Ingrese el id del proceso: ") #Ingreso dato para buscar

    clear()
    print("="*l)
    print(titulo)
    print("="*l)

    cambio=0
    for i in range(0, tamanio(cola)):   #Busco dentro de la cola el dato
        a = desencolar(cola)    #Desencolo proceso

        if verId(a) == idPro: #Si coincide con el dato ingresado por el usuario:
            cambio=1 

            print("Nombre del proceso: " + verNom(a))
            print("Id: " + verId(a))
            print("Pioridad actual: " + verPri(a))

            nPri = input("Ingrese la nueva prioridad: ").capitalize()   #Cargo la nueva prioridad
            modPri(a, nPri) #Modifico la prioridad del proceso
            nFecha = time.strftime("%d/%m/%Y", time.localtime()) #Utilizo la libreria 'time'
            nHora = time.strftime("%H:%M:%S", time.localtime())  #Utilizo la libreria 'time'
            modFecha(a, nFecha)
            modHora(a, nHora)
            

        encolar(colaAux, a) #Encolo proceso en 'colaAux' para no perder los datos
    
    copiarCola(cola, colaAux)   #Paso los datos de 'colaAux' a 'cola'
    colaAux.clear() #Limpio la 'colaAux' para poder volver a usarla

    if cambio == 1:
        print("Modificacion realizada con exito.")
    else:
        print("No se pudo encontrar el proceso con id: ", idPro)

    input()

# DESENCOLAR
def puntoC():
    clear()
    titulo = " >> DESENCOLAR >>"
    l = len(titulo)
    print("="*l)
    print(titulo)
    print("="*l)
    
    co = desencolar(cola)
    #print(co)
    print("Nombre:", verNom(co))
    print("Id:", verId(co))
    print("Tipo:", verTipo(co))
    print("Tamanio:", verTam(co))
    print("Prioridad:", verPri(co))
    print("Ultima modificacion:", verFecha(co), "a las", verHora(co), "hs")
    print("==="*16)
        
    input()

# LISTADO DE PROCESOS ACTUALES
def puntoD():
    clear()
    titulo = " >> LISTADO DE PROCESOS ACTUALES >>"
    l = len(titulo)
    print("="*l)
    print(titulo)
    print("="*l)

    for i in range(0, tamanio(cola)):   
        fl = desencolar(cola)    #Desencolo proceso

        lista.append(fl)    #Meto los los datos de la cola en una lista
        encolar(colaAux, fl) #Encolo proceso en 'colaAux' para no perder los datos
    copiarCola(cola, colaAux)   #Paso los datos de 'colaAux' a 'cola'
    colaAux.clear() #Limpio la 'colaAux' para poder volver a usarla

    for i in range(0, len(lista)):  #Imprime los datos de la lista
        print("Nombre:", verNom(lista[i]))
        print("Id:", verId(lista[i]))
        print("Tipo:", verTipo(lista[i]))
        print("Tamaño:", verTam(lista[i]))
        print("Prioridad:", verPri(lista[i]))
        print("Ultima modificacion:", verFecha(lista[i]), "a las", verHora(lista[i]), "hs")
        print("==="*16) 
    lista.clear()
    input()

# MODIFICAR PRIORIDAD DE LOS PROCESOS A BAJA
def puntoE():
    clear()
    titulo = " >> MODIFICAR PRIORIDAD DE LOS PROCESOS A BAJA >>"
    l = len(titulo)
    print("="*l)
    print(titulo)
    print("="*l)

    aux=1
    while aux!=0:
        print("Ingrese el mes de los procesos a modificar.")
        op = input("---> ").capitalize()
        if op == "Enero":
            op="01"
            aux=0
        elif op == "Febrero":
            op="02"
            aux=0
        elif op == "Marzo":
            op="03"
            aux=0
        elif op == "Abril":
            op="04"
            aux=0
        elif op == "Mayo":
            op="05"
            aux=0
        elif op == "Junio":
            op="06"
            aux=0
        elif op == "Julio":
            op="07"
            aux=0
        elif op == "Agosto":
            op="08"
            aux=0
        elif op == "Septiembre":
            op="09"
            aux=0
        elif op == "Octubre":
            op="10"
            aux=0
        elif op == "Noviembre":
            op="11"
            aux=0
        elif op == "Diciembre":
            op="12"
            aux=0
        else:
            print("Vuelve a ingresar los datos.")

    for i in range(0, tamanio(cola)):
        c = desencolar(cola)
        mes = verFecha(c).split("/") # dia/mes/año
        if op == mes[1]:
            nPri = "Baja"
            modPri(c, nPri)
            nFecha = time.strftime("%d/%m/%Y", time.localtime()) #Utilizo la libreria 'time'
            nHora = time.strftime("%H:%M:%S", time.localtime())  #Utilizo la libreria 'time'
            modFecha(c, nFecha)
            modHora(c, nHora)
            print("Proeso #" + str(i+1) + " completado.")
        encolar(colaAux, c)
    print("Cambios realizados con exito.")
    copiarCola(cola, colaAux)   #Paso los datos de 'colaAux' a 'cola'
    colaAux.clear() #Limpio la 'colaAux' para poder volver a usarla


    input()

# ELIMINO PROCESOS DEL MISMO TIPO QUE EL INGRESADO
def puntoF():
    clear()
    titulo = " >> ELIMINO PROCESOS DEL MISMO TIPO QUE EL INGRESADO >>"
    l = len(titulo)
    print("="*l)
    print(titulo)
    print("="*l)

    print("Que tipo de procesos queres eliminar?")
    tip = input("---> ").capitalize()
    for i in range(0, tamanio(cola)):

        c = desencolar(cola)

        if verTipo(c) != tip:
            encolar(colaAux, c)
        else:
            print("Proceso eliminado")

    copiarCola(cola, colaAux)   #Paso los datos de 'colaAux' a 'cola'
    colaAux.clear() #Limpio la 'colaAux' para poder volver a usarla
    input()

# GENERO UNA COLA CON PROCESOS CUYA ULTIMA MODIFICACION SE ENCUENTRA ENTRE DOS HORAS DADAS
def puntoG():
    titulo = " >> GENERAR COLA CUYA ULTIMA MODIFICACION SE ENCUENTRA ENTRE DOS HORAS DADAS >>"
    l = len(titulo)

    correcto = 0
    while correcto!=6:
        try:
            correcto = 0

            clear()
            print("="*l)
            print(titulo)
            print("="*l)

            print("Ingrese las dos horas en formato [HORA:MIN:SEG]")
            h1 = input("Hora 1: ")
            h2 = input("Hora 2: ")
            lish1 = h1.split(':') 
            lish2 = h2.split(':')
            
            if len(h1)!=8 or len(h2)!=8:
                print("Ha ocurrido un error, el formato no es el pedido.")
                print("Vuelva a intentarlo. Presione cualquier tecla.")
                #print("Len1: ", len(h1))
                #print("Len2: ", len(h2))
                input()
            elif h1 == h2:
                print("Ha ocurrido un error, la 'Hora 1' no puede ser igual a la 'Hora 2'")
                print("Vuelva a intentarlo. Presione cualquier tecla.")
                input()
            elif h2 < h1:
                print("Ha ocurrido un error, la 'Hora 1' no puede ser mayor que la 'Hora 2'")
                print("Vuelva a intentarlo. Presione cualquier tecla.")
                input()
            else:
                for i in range(0, len(lish1)):
                    try:
                        if int(lish1[i]) >= 00 and int(lish1[i]) <= 59 and int(lish1[0]) <= 23:
                            correcto +=1       #Si todo va bien correcto=+3
                    except Exception as ex:
                        print(">>>>> ERROR >>>>>", ex)

                for i in range(0, len(lish2)):
                    try:
                        if int(lish2[i]) >= 00 and int(lish2[i]) <= 59 and int(lish2[0]) <= 23:
                            correcto +=1
                    except Exception as ex:
                        print(">>>>> ERROR >>>>>", ex)

                if correcto !=6:
                    print("Ha ocurrido un error, el formato no es el pedido.")
                    print("\nVuelva a intentarlo. Presione cualquier tecla.")
                    print("Verif=", correcto)
                    input()
        except Exception as ex:
            print(">>>>> ERROR >>>>>", ex)
            input()            
    
    verif = 0
    for i in range(0, tamanio(cola)):
        c = desencolar(cola)
        #hr = str(verHora(c))
        if verHora(c) >= h1 and verHora(c) <= h2:
            encolar(colaAux, c)
            verif = 1
        encolar(colaAux2, c)

    copiarCola(cola, colaAux2)
    colaAux2.clear()

    if verif == 1:
        for i in range(0, tamanio(colaAux)):    
            c = desencolar(colaAux)
            print("Nombre:", verNom(c))
            print("Id:", verId(c))
            print("Tipo:", verTipo(c))
            print("Tamaño:", verTam(c))
            print("Prioridad:", verPri(c))
            print("Ultima modificacion:", verFecha(c), "a las", verHora(c), "hs")
            print("==="*16) 
    else:
        print("Ha ocurrido un error: no existen elementos entre esas horas.")
        if  len(h1) or len(h2) != 8:
            print("Tambien es posible que haya ingresado mal el formato de la hora.")

    input()

# MODULO PRINCIPAL
def main():
    t_ini = time.time()
    op = "1"
    while op!="0":
        op = menu()
        if op == "a":
            puntoA()
        elif op == "b":
            puntoB()
        elif op == "c":
            puntoC()
        elif op == "d":
            puntoD()
        elif op == "e":
            puntoE()
        elif op == "f":
            puntoF()
        elif op == "g":
            puntoG()
        elif op == "0":
            print("\nFin de la ejecucion...")
            t_fin = time.time()
            t_total = time.strftime("%H:%M:%S", time.gmtime(t_fin-t_ini))
            print("Tiempo total de ejecucion: " + t_total)
            print("Programa por:")
            print(" >> Gimenez Nazareno >>")
            print(" >> Sanchez Viamonte Mateo >>")

# EJECUCION DEL MODULO MAIN
main()

# Entrega 1: 17/05
# Entrega 2: 31/05
