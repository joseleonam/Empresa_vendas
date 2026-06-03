// Cliente/app/network/java/main.java

package app.network.java;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

    public static void limparTela() {

        try {

            if (System.getProperty("os.name")
                    .toLowerCase()
                    .contains("windows")) {

                new ProcessBuilder(
                        "cmd",
                        "/c",
                        "cls"
                ).inheritIO().start().waitFor();

            } else {

                new ProcessBuilder(
                        "clear"
                ).inheritIO().start().waitFor();
            }

        } 
        catch (
                IOException
                |InterruptedException
                |NumberFormatException e
        ) {
        System.out.println(
                "Erro: "
                + e.getMessage()
        );
        }
        
    }

        public static String menu(
                Scanner scanner
        ) {

        System.out.println("\n=== SISTEMA DE VENDAS (API/JAVA) ===");

        System.out.println("1 - Listar produtos");
        System.out.println("2 - Buscar produtos");
        System.out.println("3 - Comprar produtos");
        System.out.println("4 - Calcular total");
        System.out.println("0 - Sair");

        System.out.print("Escolha: ");

        return scanner.nextLine();
        }

    public static List<Integer> lerIds(
            Scanner scanner
    ) {

        System.out.print(
                "IDs (ex: 1,2,3): "
        );

        String entrada = scanner.nextLine();

        String[] partes = entrada.split(",");

        List<Integer> ids =
                new ArrayList<>();

        for (String p : partes) {

            ids.add(Integer.valueOf(
                            p.trim()
                    )
            );
        }

        return ids;
    }

    public static void main(
            String[] args
    ) {

        try (Scanner scanner = new Scanner(System.in)) {
            String clienteJson =
                    """
                                    {
                                      "id": 1,
                                      "nome": "Oliver",
                                      "email": "java@email.com"
                                    }
                                    """;
            
            OUTER:
            while (true) {
                String opcao = menu(scanner);
                try {
                    switch (opcao) {
                        case "1" -> {
                            limparTela();
                            System.out.println(
                                    "\n=== PRODUTOS ==="
                            );  System.out.println(
                                    ClienteApi
                                            .listarProdutos()
                            );
                        }
                        case "2" ->                         {
                            List<Integer> ids =
                                    lerIds(scanner);
                            limparTela();
                            System.out.println(
                                    "\n=== RESULTADO ==="
                            );      System.out.println(
                                    ClienteApi
                                            .buscarProdutos(
                                                    ids
                                            )
                            );                             }
                        case "3" ->                         {
                            List<Integer> ids =
                                    lerIds(scanner);
                            limparTela();
                            System.out.println(
                                    "\n=== COMPRA ==="
                            );      System.out.println(
                                    ClienteApi
                                            .comprarProdutos(
                                                    clienteJson,
                                                    ids
                                            )
                            );                             }
                        case "4" ->                         {
                            List<Integer> ids =
                                    lerIds(scanner);
                            limparTela();
                            System.out.println(
                                    "\n=== TOTAL ==="
                            );      System.out.println(
                                    ClienteApi
                                            .calcularTotal(
                                                    ids
                                            )
                            );                             }
                        case "0" -> {
                            System.out.println(
                                    "Saindo..."
                            );  break OUTER;
                        }
                        default -> System.out.println(
                                    "Opção inválida"
                            );
                    }
                }
                catch (
                        IOException
                        |InterruptedException
                        |NumberFormatException e
                ) {
                System.out.println(
                        "Erro: "
                        + e.getMessage()
                );
                }
            }
        }
    }
}