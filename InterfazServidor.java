
// PAQUETE


// IMPORTACIONES
import java.rmi.Remote ;



/* DEFINICIÓN DE INTERFAZ ´InterfazServer´. */
public interface InterfazServidor extends Remote {


	public String responderMensaje ( String mensaje ) throws java.rmi.RemoteException ;

    
}

