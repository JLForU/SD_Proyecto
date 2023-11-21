
# IMPORTS
## Tiempo
import time
## Random
import random
## Protocolo
import paho.mqtt.client as mqtt



# VARIABLES GLOBALES
## Establecer conexión.
client = mqtt.Client()
client.connect("localhost", 1883)
## Tópico
TOOPICO = "OD"


# MAIN FUNCTION DECLARATION
def main ( ) :

    print ("\n\n")


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
        time.sleep ( tiempo )

        # Dato.
        dato = str ( funcioon_generarDato() )
        client.publish ( TOOPICO , dato )

        print ( f"Enviar: {dato}; por medio de {TOOPICO}." )


def funcioon_generarDato ( ) :

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



# MAIN FUNCTION IMPLEMENTATION
if __name__ == "__main__" :
    main()




# To rest -->       
