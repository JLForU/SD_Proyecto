
// PAQUETE


// IMPORTACIONES
import java.rmi.NotBoundException;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;



/* IMPLEMENTACIÓN DE CLASE ´Cliente´. */

public class Cliente {
	

    // @param args the command line arguments

    public static void main ( String[] args ) {


		String mensaje = "Hola" ;
		String respuesta = new String() ;

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

		System.out.println ( respuesta ) ;


    }


}




//  To rest --->-->->    
