// Cliente/app/network/java/ClienteFactory.java

package app.network.java;

import java.util.Random;

public class ClienteFactory {

    private static final String[] NOMES = {
            "João Silva", "Maria Souza", "Carlos Lima",
            "Ana Costa", "Pedro Santos"
    };

    public static Cliente criarClienteFake() {

        Random r = new Random();

        int id = r.nextInt(999);

        String nome = NOMES[r.nextInt(NOMES.length)];
        String email = nome.toLowerCase().replace(" ", ".") + "@email.com";

        return new Cliente(id, nome, email);
    }
}