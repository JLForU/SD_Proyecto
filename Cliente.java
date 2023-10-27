
// PAQUETE


// IMPORTACIONES
//// Números aleatorios.
import java.util.Random ;
//// JZMQ.
import org.zeromq.ZMQ ;
import org.zeromq.ZMQException ;
import java.nio.charset.Charset ;



/* IMPLEMENTACIÓN DE CLASE ´Cliente´. */

public class Cliente {
	

    // @param args the command line arguments

    public static void main ( String[] args ) {


		while ( true ) {

			String mensaje = funcioon_GenerarParaametros() ;

			String respuesta = funcioon_ClienteZMQ ( mensaje ) ;

			System.out.println ( respuesta ) ;

		}


    }

	public static String funcioon_ClienteZMQ ( String mensaje ) {

		String respuesta = "Sin respuesta..." ;

		try (
			
			ZMQ.Context context = ZMQ.context(1) ;
			ZMQ.Socket socket = context.socket ( ZMQ.REQ ) ;
			
		) {

            socket.connect ( "tcp://localhost:5555" ) ;

			// # (1).
			socket.send ( mensaje.getBytes() , ZMQ.NOBLOCK ) ;
			// # (4).
			respuesta = socket.recvStr ( Charset.defaultCharset() ) ;

		} catch ( ZMQException e ) {

   		     if ( e.getErrorCode() == ZMQ.Error.ETERM.getCode() ) {
   		         // Handle the case where the server has shut down (ETERM error).
   		         System.out.println ( "Server has shut down." ) ;
   		     } else {
   		         // Handle other ZeroMQ-related errors.
   		         System.out.println ( "Error: " + e ) ;
   		     }

   		 } catch ( Exception e ) {
   		     // Handle general exceptions (non-ZeroMQ related).
   		     System.out.println("Error: " + e) ;
   		 }

	return respuesta ;
	}

	public static void funcioon_Esperar ( ) {

		try {
			Thread.sleep(2_000) ;
		} catch ( InterruptedException e ) {
			e.printStackTrace() ;
		}

	}

	public static String funcioon_GenerarParaametros ( ) {

		funcioon_Esperar() ;

		String[] paraametros = {"°F","pH","Mg/L"} ;

		Random random = new Random() ;
		int paraametro = random.nextInt ( 3 ) ;

		int parteEntera = 0 ;
		int parteDecimal = 0 ;
		String dato = new String() ;

		switch ( paraametro ) {

			case 0 :
					parteEntera = 68 + random.nextInt ( 21 ) ;
					parteDecimal = random.nextInt ( 100 ) ;
					dato = Integer.toString(parteEntera) + "." + Integer.toString(parteDecimal) ;
					return ( dato + " " + paraametros[paraametro] ) ;

			case 1 :
					parteEntera = 6 + random.nextInt ( 2 ) ;
					parteDecimal = random.nextInt ( 100 ) ;
					dato = Integer.toString(parteEntera) + "." + Integer.toString(parteDecimal) ;
					return ( dato + " " + paraametros[paraametro] ) ;

			case 2 :
					parteEntera = 2 + random.nextInt ( 9 ) ;
					parteDecimal = random.nextInt ( 100 ) ;
					dato = Integer.toString(parteEntera) + "." + Integer.toString(parteDecimal) ;
					return ( dato + " " + paraametros[paraametro] ) ;

			default :
					return ( "0.0" ) ;

		}

	}


}




//  To rest --->-->->    
