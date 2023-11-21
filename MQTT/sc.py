
# IMPORTS
import paho.mqtt.client as mqtt



# VARIABLES GLOBALES
# Establecer conexión.
client = mqtt.Client()
client.connect ( "broker.hivemq.com" , 1883 )
## Tópico
TOOPICO = "Alarmas"


# MAIN FUNCTION DECLARATION
def main ( ) :

    print ("\n\n")


    # Recibir mensaje, especificando un tópico.
    client.subscribe ( TOOPICO )
    client.on_message = on_message

    # Esperar más mensajes.
    try :
        client.loop_forever()
    except KeyboardInterrupt :
        # Handle the KeyboardInterrupt gracefully.
        pass

    # Establecer desconexión.
    client.disconnect()


    print ("\n\n")


# OTHER FUNCTIONS
def on_message ( client , userdata , message ) :

    str_mensajeDeLlegada = message.payload.decode()
    #mensajeDeRecibir = f"Recibir: {str_mensajeDeLlegada}; por medio de '{message.topic}'.\n"
    print ( str_mensajeDeLlegada )



# MAIN FUNCTION IMPLEMENTATION
if __name__ == "__main__" :
    main()




# To rest -->       
