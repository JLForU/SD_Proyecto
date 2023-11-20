
# IMPORTACIONES #
import paho.mqtt.client as mqtt



# VARIABLES GLOBALES #
cliente = mqtt.Client()
TOOPICO = "puerta"


#
# DECLARACIÓN DE PUERTA #
#
def main ( ) :

    print ("\n\n\n\n")


    # Establecer conexión.
    cliente.connect ( "localhost", 1883)

    # Recibir mensaje, especificando un tópico.
    cliente.subscribe ( "centro" )
    cliente.on_message = on_message

    # Control de mensajes.
    try :

        # Escuchar.
        cliente.loop_forever()

    except KeyboardInterrupt :

        pass

    # Establecer desconexión.
    cliente.disconnect()

    # MENSAJE DE EJECUCIÓN EXITOSA.
    funcioon_mensajeDesconexioon()


    print ("\n\n\n\n")



# OTRAS FUNCIONES #
def on_message ( client , userdata , message ) :

    print ( f"Mensaje: '{message.payload.decode()}' desde '{message.topic}'." )


def funcioon_mensajeDesconexioon ( ) :

    print ( "\n\nPuerta apagada." )



# IMPLEMENTACIÓN DE FUNCIÓN MAIN #
if __name__ == "__main__" :
    main()




# To rest -->       
