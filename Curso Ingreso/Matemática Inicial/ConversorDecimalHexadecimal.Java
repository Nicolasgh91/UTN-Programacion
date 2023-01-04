import java.util.Scanner;

public class ConversorDecimalHexadecimal {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Introduce un número decimal: ");
        int decimal = sc.nextInt();

        // Almacenamos el resultado en una cadena de caracteres
        String hexadecimal = "";

        // Repetimos el proceso de división mientras el cociente sea mayor que 0
        while (decimal > 0) {
            // Añadimos el resto de la división entre 16 a la cadena
            int resto = decimal % 16;
            // Si el resto es mayor o igual que 10, añadimos la letra correspondiente
            if (resto >= 10) {
                hexadecimal = (char)('A' + (resto - 10) ) + hexadecimal;
            } else {
                hexadecimal = resto + hexadecimal;
            }
            // Actualizamos el valor de decimal al cociente de la división entre 16
            decimal = decimal / 16;
        }

        System.out.println("El número hexadecimal es: " + hexadecimal);
    }
}
