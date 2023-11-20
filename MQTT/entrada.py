
# IMPORTACIONES #
import paho.mqtt.client as mqtt



# VARIABLES GLOBALES #
cliente = mqtt.Client()
TOOPICO = "entrada"


#
# DECLARACIÓN DE SENSOR DE ENTRADA #
#
def main ( ) :

    print ("\n\n\n\n")


    # Establecer conexión.
    cliente.connect ( "localhost" , 1883 )

    # Recibir mensaje, especificando un tópico.
    cliente.subscribe ( "centro" )
    cliente.on_message = on_message

    # Control de mensajes.
    try :

        # Escuchar.
        cliente.loop_start()

        # Enviar mensajes.
        while ( True ) :
            funcioon_publicar()

    except KeyboardInterrupt :

        pass

    # Establecer desconexión.
    cliente.disconnect()

    # MENSAJE DE EJECUCIÓN EXITOSA.
    funcioon_mensajeDesconexioon()


    print ("\n\n\n\n")



# OTRAS FUNCIONES #
def on_message ( client , userdata , message ) :

    mensaje = message.payload.decode()

    print ( f"\n\nMensaje: '{mensaje}' desde '{message.topic}'." )


def funcioon_publicar ( ) :

    pregunta = input ( f"{TOOPICO}: " )

    if pregunta == "1" :
        # Enviar mensaje por medio de un tópico.
        cliente.publish ( TOOPICO , pregunta )


def funcioon_mensajeDesconexioon ( ) :

    print ( "\n\nSensor de entrada apagado." )



# IMPLEMENTACIÓN DE FUNCIÓN MAIN #
if __name__ == "__main__" :
    main()




# To rest -->       
