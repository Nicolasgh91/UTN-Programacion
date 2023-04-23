import java.util.Scanner;

public class ConversorDecimalBinario {
    public static void main(String[] args) {

            Scanner sc = new Scanner(System.in);
            System.out.print("Introduce un número decimal: ");
            int decimal = sc.nextInt();

            // Almacenamos el resultado en una cadena de caracteres
            String binary = "";

            // Repetimos el proceso de división mientras el cociente sea mayor que 0
            while (decimal > 0) {
                // Añadimos el resto de la división entre 2 a la cadena
                binary = decimal % 2 + binary;
                // Actualizamos el valor de decimal al cociente de la división entre 2
                decimal = decimal / 2;
            }

            System.out.println("El número binario es: " + binary);
    }
}
