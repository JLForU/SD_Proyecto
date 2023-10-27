
// PAQUETE


// IMPORTACIONES
import java.rmi.NotBoundException ;
import java.rmi.RemoteException ;
import java.rmi.registry.LocateRegistry ;
import java.rmi.registry.Registry ;
import java.rmi.server.UnicastRemoteObject ;



/* IMPLEMENTACIÓN DE CLASE ´Servidor´. */

public class Servidor extends UnicastRemoteObject implements InterfazServidor {
    

    //// CONSTRUCTOR ////
    protected Servidor ( ) throws RemoteException {

        System.out.println ( "Iniciando Servidor..." ) ;

    }
        
    //// IMPLEMENTACIÓN DE FUNCIÓN "MAIN". ////
    public static void main ( String[] args ) {

        
        try {

            Servidor S = new Servidor() ;
            
            Registry registry = LocateRegistry.createRegistry ( 1090 ) ;
            registry.rebind ( "Servidor" , S ) ;
            System.out.println ( "Objeto -server- Registrado en el RMI" ) ;
        
        } catch ( RemoteException e ) {

            System.out.println ( "Error: " + e ) ; 

        }


    }

    public String responderMensaje ( String mensaje ) throws RemoteException {

		System.out.println ( mensaje ) ;

		return ( "Recibido " + mensaje ) ;

    }


}




// FIN DE ARCHIVO.

