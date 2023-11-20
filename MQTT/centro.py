
# IMPORTACIONES #
import datetime
import paho.mqtt.client as mqtt



# VARIABLES GLOBALES #
cliente = mqtt.Client()
TOOPICO = "centro"
booleano_salaHabilitada = True
maaximo_personas = 5
contador_personas = 0


#
# DECLARACIÓN DE CENTRO DE COMANDO #
#
def main ( ) :

    print ("\n\n\n\n")


    # Establecer conexión.
    cliente.connect ( "localhost", 1883)

    # Recibir mensaje, especificando un tópico.
    cliente.subscribe ( "entrada" )
    cliente.subscribe ( "salida" )
    cliente.on_message = on_message

    # Control de mensajes.
    try :

        # Escuchar.
        cliente.loop_start()

        # Evaluar si la sala está habilitada.
        while ( True ) :

            funcioon_evaluarSala()

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
    toopico = message.topic

    print ( f"Recibiendo '{mensaje}' desde '{toopico}'." )

    funcioon_calcularPersonas ( toopico )

    funcioon_monitorear ( mensaje , toopico  )


def funcioon_calcularPersonas ( topico ) :

    global contador_personas
    global booleano_salaHabilitada 

    if ( booleano_salaHabilitada == True ) :
        if ( topico == "entrada" ) :
            contador_personas += 1

    if ( contador_personas > 0 ) :
        if ( topico == "salida" ) :
            contador_personas -= 1


def funcioon_monitorear ( mensaje , toopico ) :

    global contador_personas
    global maaximo_personas

    tiempo = datetime.datetime.now()

    reporte = f"TÓPICO: {toopico}; MENSAJE: {mensaje}; PERSONAS: {contador_personas}; LÍMITE: {maaximo_personas}; TIEMPO: {tiempo}."

    cliente.publish ( "monitor" , reporte )

    archivo = open ( "log" , "a" )
    archivo.write ( reporte+'\n' )
    archivo.close()


def funcioon_publicar ( mensaje ) :

    print ( f"\nEnviando '{mensaje}' para '{TOOPICO}'.\n" )
    cliente.publish ( TOOPICO , mensaje )


def funcioon_evaluarSala ( ) :

    global contador_personas
    global maaximo_personas
    global booleano_salaHabilitada

    booleano_evaluarSala = contador_personas < maaximo_personas

    if ( booleano_evaluarSala != booleano_salaHabilitada ) :

        if ( booleano_salaHabilitada == True ) :
            funcioon_publicar ( "0" )
            booleano_salaHabilitada = False
        else :
            funcioon_publicar ( "1" )
            booleano_salaHabilitada = True


def funcioon_mensajeDesconexioon ( ) :

    print ( "\n\nCentro de comando apagado." )



# IMPLEMENTACIÓN DE FUNCIÓN MAIN #
if __name__ == "__main__" :
    main()




# To rest -->       
