
# IMPORTS
import paho.mqtt.client as mqtt



# VARIABLES GLOBALES
# Establecer conexión.
client = mqtt.Client()
client.connect("localhost", 1883)
## Tópico
TOOPICO = "OD"


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
def on_message(client, userdata, message):
    print(f"Recibir: {message.payload.decode()}; por medio de '{message.topic}'.")



# MAIN FUNCTION IMPLEMENTATION
if __name__ == "__main__" :
    main()




# To rest -->       
