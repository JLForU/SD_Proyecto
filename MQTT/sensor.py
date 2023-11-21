
# IMPORTS
## Parámetros de sistema y salida de programa.
import sys
## Tiempo
import time
from datetime import datetime
## Random
import random
## Protocolo
import paho.mqtt.client as mqtt



# VARIABLES GLOBALES
## Establecer conexión.
client = mqtt.Client()
client.connect ( "broker.hivemq.com" , 1883 )
## Tópico
TOOPICO = None
## Tiempo
TIEMPO = None
## Archivo
ARCHIVO = None


# MAIN FUNCTION DECLARATION
def main ( ) :

    print ("\n\n")


    if ( len(sys.argv) == 4 ) :
        global TOOPICO ; TOOPICO = str ( sys.argv[1] )
        global TIEMPO ; TIEMPO = float ( sys.argv[2] )
        global ARCHIVO ; ARCHIVO = str ( sys.argv[3] )
    else :
        print ( "Se necesita configurar Tópico, Tiempo y Archivo.\n\n" )
        sys.exit()

    try :
        # Publicar cada cierto tiempo.
        funcioon_publicar()
    except KeyboardInterrupt :
        # Establecer desconexión.
        client.disconnect()
        # Handle the KeyboardInterrupt gracefully.
        pass
    

    print ("\n\n")


# OTHER FUNCTIONS
def funcioon_publicar ( ) :

    while ( True ) :

        # Tiempo.
        tiempo = random.random()
        time.sleep ( TIEMPO )

        # Dato.
        dato = str ( funcioon_generarDato() )
        client.publish ( TOOPICO , dato )

        print ( f"Enviar: {dato}; por medio de {TOOPICO}." )


def funcioon_generarDato ( ) :

    if ( TOOPICO == "T" ) :
        return ( funcioon_generarDato_T() )
    elif ( TOOPICO == "pH" ) :
        return ( funcioon_generarDato_pH() )
    elif ( TOOPICO == "OD" ) :
        return ( funcioon_generarDato_OD() )
    elif ( TOOPICO == "Tiempo" ) :
        return ( funcioon_generarDato_Tiempo() )


def funcioon_generarDato_T ( ) :

    nuumeroAleatorio = random.random()

    # Valores correctos.
    if nuumeroAleatorio <= 0.6 and nuumeroAleatorio > 0.4 :

        return random.randint(68,89)

    # Valores fuera de rango.
    elif nuumeroAleatorio <= 0.4 and nuumeroAleatorio > 0.1 :

        if random.random() < 0.5 :
            return random.randint(58,68)
        else :
            return random.randint(89,99)

    # Errores.
    else :

        if random.random() < 0.5 :
            return random.randint(-42,58)
        else :
            return random.randint(99,199)


def funcioon_generarDato_pH ( ) :

    nuumeroAleatorio = random.random()

    # Valores correctos.
    if nuumeroAleatorio <= 0.6 and nuumeroAleatorio > 0.4 :

        return random.uniform(6.0,8.0)

    # Valores fuera de rango.
    elif nuumeroAleatorio <= 0.4 and nuumeroAleatorio > 0.1 :

        if random.random() < 0.5 :
            return random.uniform(5.0,6.0)
        else :
            return random.uniform(8.0,9.0)

    # Errores.
    else :

        if random.random() < 0.5 :
            return random.uniform(-5.0,5.0)
        else :
            return random.uniform(9.0,14.0)


def funcioon_generarDato_OD ( ) :

    nuumeroAleatorio = random.random()

    # Valores correctos.
    if nuumeroAleatorio <= 0.6 and nuumeroAleatorio > 0.4 :

        return random.randint(2,11)

    # Valores fuera de rango.
    elif nuumeroAleatorio <= 0.4 and nuumeroAleatorio > 0.1 :

        if random.random() < 0.5 :
            return random.randint(-3,2)
        else :
            return random.randint(11,16)

    # Errores.
    else :

        if random.random() < 0.5 :
            return random.randint(-13,3)
        else :
            return random.randint(16,26)


def funcioon_generarDato_Tiempo ( ) :

    tiempo = datetime.now()

    minutos = tiempo.minute
    segundos = tiempo.second
    milisegundos = tiempo.microsecond // 1000
    
    total_milisegundos = ( minutos*60*1000 ) + ( segundos*1000 ) + milisegundos

    return ( total_milisegundos )



# MAIN FUNCTION IMPLEMENTATION
if __name__ == "__main__" :
    main()




# To rest -->       
