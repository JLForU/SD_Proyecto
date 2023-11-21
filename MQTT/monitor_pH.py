
# IMPORTS
import paho.mqtt.client as mqtt



# VARIABLES GLOBALES
# Establecer conexión.
client = mqtt.Client()
client.connect ( "localhost" , 1883 )
## Tópico
TOOPICO = "pH"


# MAIN FUNCTION DECLARATION
def main ( ) :

    print ("\n\n")


    # Crear archivo BD.
    function_createFile ( "log" )

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

    mensaje = f"Recibir: {message.payload.decode()}; por medio de '{message.topic}'.\n"
    function_writeFile ( "log" , mensaje )
    print ( mensaje )


def function_createFile ( string_fileName ) :

    print ( "FILE CREATION\n" )

    try :

        inStreamFile_createFile = open ( string_fileName , "x" )
        inStreamFile_createFile.close()
        print ( f"\tThe file '{string_fileName}' was successfully created." )

    except FileExistsError :

        print ( f"\tThe file '{string_fileName}' already exists." )

    except Exception as e :

        print ( f"\tAn error occurred while creating the file: {e}." )

    print ( '\n' )


def function_writeFile ( string_fileName , string_fileContent ) :

    print ( "FILE WRITING\n" )

    try :

        outStreamFile_writeFile = open ( string_fileName , "a" )
        outStreamFile_writeFile.write ( string_fileContent )
        outStreamFile_writeFile.close()
        print ( f"\tThe file '{string_fileName}' was successfully written." )

    except FileNotFoundError :

        print ( f"\tThe file '{string_fileName}' does not exist." )

    except Exception as e :

        print ( f"\tAn error occurred while writing the file: {e}." )

    print ( '\n' )



# MAIN FUNCTION IMPLEMENTATION
if __name__ == "__main__" :
    main()




# To rest -->       
