
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
TOOPICO = "pH"


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



# MAIN FUNCTION IMPLEMENTATION
if __name__ == "__main__" :
    main()




# To rest -->       
