
// PAQUETE


// IMPORTACIONES
//// JZMQ.
import org.zeromq.ZMQ ;
import java.nio.charset.Charset ;



/* IMPLEMENTACIÓN DE CLASE ´Servidor´. */

public class Servidor {
    

    //// IMPLEMENTACIÓN DE FUNCIÓN "MAIN". ////
    public static void main ( String[] args ) {

        
		while ( true ) {

	        funcioon_ServidorZMQ() ;

		}
		

    }

	public static void funcioon_ServidorZMQ ( ) {

		try (
			
			ZMQ.Context context = ZMQ.context(1) ;
			ZMQ.Socket socket = context.socket ( ZMQ.REP ) ;
			
		) {

            socket.bind ( "tcp://localhost:5555" ) ;

			// # (2).
			String mensajeRecibido = socket.recvStr ( Charset.defaultCharset() ) ;
			System.out.println ( mensajeRecibido ) ;
			// # (3).
			String mensajeEnviado = "Recibido " + mensajeRecibido ;
			socket.send ( mensajeEnviado.getBytes() , ZMQ.NOBLOCK ) ;

		} catch ( Exception e ) {

			System.out.println ( "Error: " + e ) ;

		}

	}


}




// FIN DE ARCHIVO.

