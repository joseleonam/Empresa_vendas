// Cliente/app/network/java/Cliente.java

package app.network.java;

public class Cliente {
    public int id;
    public String nome;
    public String email;

    public Cliente(int id, String nome, String email) {
        this.id = id;
        this.nome = nome;

        this.email = email;
    }

    public String toJson() {
        return String.format(
            "{\"id\":%d,\"nome\":\"%s\",\"email\":\"%s\"}",
            id, nome, email
        );
    }
}