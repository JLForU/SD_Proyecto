
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
TOOPICO = "T"


# MAIN FUNCTION DECLARATION
def main ( ) :

    print ("\n\n")


    # Publicar cada cierto tiempo.
    funcioon_publicar()
    # Establecer desconexión.
    client.disconnect()
    

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



# MAIN FUNCTION IMPLEMENTATION
if __name__ == "__main__" :
    main()




# To rest -->       
