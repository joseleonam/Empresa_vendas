// Cliente/app/network/java/cliente.api.java
package app.network.java;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.List;
import java.util.stream.Collectors;

public class ClienteApi {

    private static final String BASE_URL = "http://localhost:8000";

    private static final HttpClient client =
            HttpClient.newHttpClient();

    // 🔹 LISTAR PRODUTOS
    public static String listarProdutos()
            throws IOException, InterruptedException {

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(BASE_URL + "/produtos"))
                .GET()
                .build();

        HttpResponse<String> response =
                client.send(
                        request,
                        HttpResponse.BodyHandlers.ofString()
                );

        return response.body();
    }

    // 🔹 BUSCAR PRODUTOS
    public static String buscarProdutos(
            List<Integer> ids
    ) throws IOException, InterruptedException {

        String idsStr = ids.stream()
                .map(String::valueOf)
                .collect(Collectors.joining(","));

        HttpRequest request = HttpRequest.newBuilder()
                .uri(
                        URI.create(
                                BASE_URL +
                                "/produtos/buscar?ids=" +
                                idsStr
                        )
                )
                .GET()
                .build();

        HttpResponse<String> response =
                client.send(
                        request,
                        HttpResponse.BodyHandlers.ofString()
                );

        return response.body();
    }

    // 🔹 COMPRAR PRODUTOS
    public static String comprarProdutos(
            String clienteJson,
            List<Integer> ids
    ) throws IOException, InterruptedException {

        String idsJson = ids.stream()
                .map(String::valueOf)
                .collect(Collectors.joining(","));

        String payload =
                "{"
                + "\"cliente\":"
                + clienteJson
                + ","
                + "\"ids\":["
                + idsJson
                + "]"
                + "}";

        HttpRequest request =
                HttpRequest.newBuilder()
                        .uri(
                                URI.create(
                                        BASE_URL +
                                        "/compras"
                                )
                        )
                        .header(
                                "Content-Type",
                                "application/json"
                        )
                        .POST(
                                HttpRequest.BodyPublishers
                                        .ofString(payload)
                        )
                        .build();

        HttpResponse<String> response =
                client.send(
                        request,
                        HttpResponse.BodyHandlers.ofString()
                );

        return response.body();
    }

    // 🔹 CALCULAR TOTAL
    public static String calcularTotal(
            List<Integer> ids
    ) throws IOException, InterruptedException {

        String idsJson = ids.stream()
                .map(String::valueOf)
                .collect(Collectors.joining(","));

        String payload =
                "{"
                + "\"ids\":["
                + idsJson
                + "]"
                + "}";

        HttpRequest request =
                HttpRequest.newBuilder()
                        .uri(
                                URI.create(
                                        BASE_URL +
                                        "/total"
                                )
                        )
                        .header(
                                "Content-Type",
                                "application/json"
                        )
                        .POST(
                                HttpRequest.BodyPublishers
                                        .ofString(payload)
                        )
                        .build();

        HttpResponse<String> response =
                client.send(
                        request,
                        HttpResponse.BodyHandlers.ofString()
                );

        return response.body();
    }
}