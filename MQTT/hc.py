
# IMPORTS
## Parametros por consola y salida de programa.
import sys
## Tiempo
from datetime import datetime
## Protocolo de comunicación.
import paho.mqtt.client as mqtt



# VARIABLES GLOBALES
# Establecer conexión.
client = mqtt.Client()
client.connect ( "localhost" , 1883 )
## Tópico
TOOPICO = "HC"


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

    mensajeDeLlegada = message.payload.decode()
    
    if ( mensajeDeLlegada == "T" or mensajeDeLlegada == "pH" or mensajeDeLlegada == "OD" or mensajeDeLlegada == "Tiempo" ) :

        global TOOPICO
        TOOPICO = mensajeDeLlegada
        client.subscribe ( TOOPICO )
        # Crear archivo BD.
        function_createFile ( "log" )

    else :

        mensajeDeRecibido = f"Recibir: {mensajeDeLlegada}; por medio de '{message.topic}'.\n"
        funcioon_monitorear ( mensajeDeLlegada , mensajeDeRecibido )


def funcioon_monitorear ( mensajeDeLlegada , mensajeDeRecibir ) :

    if ( TOOPICO == "T" ) :

        int_mensajeDeLlegada = int ( mensajeDeLlegada )

        if int_mensajeDeLlegada >= 58 and int_mensajeDeLlegada <= 99 :
            function_writeFile ( "log" , mensajeDeRecibir )
        else :
            client.publish ( "Alarmas" , mensajeDeRecibir )

    elif ( TOOPICO == "pH" ) :

        float_mensajeDeLlegada = float ( mensajeDeLlegada )

        if float_mensajeDeLlegada >= 5.0 and float_mensajeDeLlegada <= 9.0 :
            function_writeFile ( "log" , mensajeDeRecibir )
        else :
            client.publish ( "Alarmas" , mensajeDeRecibir )

    elif ( TOOPICO == "OD" ) :

        int_mensajeDeLlegada = int ( mensajeDeLlegada )

        if int_mensajeDeLlegada >= -3 and int_mensajeDeLlegada <= 16 :
            function_writeFile ( "log" , mensajeDeRecibir )
        else :
            client.publish ( "Alarmas" , mensajeDeRecibir )

    elif ( TOOPICO == "Tiempo" ) :

        # Tiempo menor.
        int_mensajeDeLlegada = int ( mensajeDeLlegada )

        # Tiempo mayor.
        tiempo = datetime.now()
        minutos = tiempo.minute
        segundos = tiempo.second
        milisegundos = tiempo.microsecond // 1000
        total_milisegundos = ( minutos*60*1000 ) + ( segundos*1000 ) + milisegundos

        # TM - Tm
        diferencia = total_milisegundos - int_mensajeDeLlegada

        print ( "Tiempo: " + str(diferencia) )


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
