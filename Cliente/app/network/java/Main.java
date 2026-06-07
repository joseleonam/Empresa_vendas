// Cliente/app/network/java/Main.java
package app.network.java;

import java.io.IOException;
import java.util.*;

public class Main {

    static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws Exception {

        Cliente cliente = ClienteFactory.criarClienteFake();

        while (true) {

            System.out.println("\n=== SISTEMA DE VENDAS JAVA ===");
            System.out.println("Cliente ID: " + cliente.id);
            System.out.println("1 - Listar produtos");
            System.out.println("2 - Buscar produtos");
            System.out.println("3 - Comprar produtos");
            System.out.println("4 - Calcular total");
            System.out.println("5 - Buscar pedido");
            System.out.println("0 - Sair");

            System.out.print("Escolha: ");
            String op = scanner.nextLine();

            switch (op) {

                case "1" -> {
                    limparTela();
                    System.out.println("\n=== PRODUTOS ===");
                    System.out.println(ClienteAPI.listarProdutos());
                }

                case "2" -> {
                    System.out.print("IDs (ex: 1,2,3): ");
                    List<Integer> ids2 = parseIds(scanner.nextLine());
                    limparTela();
                    System.out.println("\n=== RESULTADO ===");
                    System.out.println(ClienteAPI.buscarProdutos(ids2));
                }

                case "3" -> {
                    System.out.print("IDs (ex: 1,2,3): ");
                    List<Integer> ids3 = parseIds(scanner.nextLine());
                    limparTela();
                    System.out.println("\n=== COMPRA ===");
                    System.out.println(ClienteAPI.comprarProdutos(cliente, ids3));
                }

                case "4" -> {
                    System.out.print("IDs (ex: 1,2,3): ");
                    List<Integer> ids4 = parseIds(scanner.nextLine());
                    limparTela();
                    System.out.println("\n=== TOTAL ===");
                    System.out.println(ClienteAPI.calcularTotal(ids4));
                }

                case "5" -> {
                    limparTela();
                    System.out.println("\n=== MEUS PEDIDOS ===");

                    String pedidos = ClienteAPI.buscarPedido(cliente.id);

                    if (pedidos.startsWith("\"") && pedidos.endsWith("\"")) {
                        pedidos = pedidos.substring(1, pedidos.length() - 1);
                    }

                    pedidos = pedidos.replace("\\n", "\n");

                    if (pedidos.contains("status")) {
                        System.out.println(pedidos);
                    } else {
                        System.out.println(pedidos);
                        System.out.println("-".repeat(40));
                    }
                }

                case "0" -> {
                    System.out.println("Saindo...");
                    return;
                }

                default -> System.out.println("Opção inválida");
            }
        }
    }

    private static List<Integer> parseIds(String input) {
        String[] parts = input.split(",");
        List<Integer> ids = new ArrayList<>();

        for (String p : parts) {
            ids.add(Integer.valueOf(p.trim()));
        }
        return ids;
    }

    private static void limparTela() {
        try {
            if (System.getProperty("os.name").contains("Windows")) {
                new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
            } else {
                System.out.print("\033[H\033[2J");
                System.out.flush();
            }
        } catch (IOException | InterruptedException e) {
            System.out.println("\n".repeat(5));
        }
    }
}