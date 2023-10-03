
// PAQUETE


// IMPORTACIONES
//// Números aleatorios.
import java.util.Random ;
//// Establecer conexión.
import java.rmi.NotBoundException;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;



/* IMPLEMENTACIÓN DE CLASE ´Cliente´. */

public class Cliente {
	

    // @param args the command line arguments

    public static void main ( String[] args ) {


		while ( true ) {

			String mensaje = funcioon_GenerarParaametros() ;

			String respuesta = funcioon_EstablecerConexioon ( mensaje ) ;

			System.out.println ( respuesta ) ;

		}


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

	public static String funcioon_EstablecerConexioon ( String mensaje ) {

		String respuesta = "Sin respuesta..." ;

        try {

            Registry registry = LocateRegistry.getRegistry ( "localhost" , 1090 ) ;

            InterfazServidor servidor = (InterfazServidor) registry.lookup ( "Servidor" ) ;

			respuesta = servidor.responderMensaje ( mensaje ) ;

        } catch ( NotBoundException e ) {

            System.out.println ( "No se encontró el objeto en el registro." ) ;
            System.exit(0) ;

        } catch ( RemoteException e ) {

            System.out.println ( "Error: " + e ) ;
            System.exit(0) ;

        }

	return respuesta ;
	}


}




//  To rest --->-->->    
