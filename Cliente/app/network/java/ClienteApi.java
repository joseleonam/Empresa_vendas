// Cliente/app/network/java/ClienteApi.java
package app.network.java;

import java.net.URI;
import java.net.http.*;
import java.util.List;

public class ClienteAPI {

    private static final String BASE_URL = "http://localhost:8000";
    private static final HttpClient client = HttpClient.newHttpClient();
    private static String formatarResposta(String response) {

        // Remove aspas externas do JSON stringificado
        if (response.startsWith("\"") && response.endsWith("\"")) {
            response = response.substring(1, response.length() - 1);
        }

        // Converte escapes \n em quebra real de linha
        response = response.replace("\\n", "\n");

        return response;
    }

    public static String listarProdutos() throws Exception {
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(BASE_URL + "/produtos"))
                .GET()
                .build();

        String response = client.send(request, HttpResponse.BodyHandlers.ofString()).body();

         // 🔥 trata o texto retornado
        return formatarResposta(response);
    }

    public static String buscarProdutos(List<Integer> ids) throws Exception {
        String joined = String.join(",", ids.stream().map(String::valueOf).toList());

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(BASE_URL + "/produtos/buscar?ids=" + joined))
                .GET()
                .build();

        String response = client.send(request, HttpResponse.BodyHandlers.ofString()).body();

         // 🔥 trata o texto retornado
        return formatarResposta(response);
    }

    public static String comprarProdutos(Cliente cliente, List<Integer> ids) throws Exception {

        StringBuilder idsJson = new StringBuilder("[");
        for (int i = 0; i < ids.size(); i++) {
            idsJson.append(ids.get(i));
            if (i < ids.size() - 1) idsJson.append(",");
        }
        idsJson.append("]");

        String json = String.format(
            "{\"cliente\":%s,\"ids\":%s}",
            cliente.toJson(),
            idsJson
        );

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(BASE_URL + "/compras"))
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(json))
                .build();

        String response = client.send(request, HttpResponse.BodyHandlers.ofString()).body();

         // 🔥 trata o texto retornado
        return formatarResposta(response);
    }

    public static String calcularTotal(List<Integer> ids) throws Exception {

        StringBuilder json = new StringBuilder("{\"ids\":[");
        for (int i = 0; i < ids.size(); i++) {
            json.append(ids.get(i));
            if (i < ids.size() - 1) json.append(",");
        }
        json.append("]}");

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(BASE_URL + "/total"))
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(json.toString()))
                .build();

        String response = client.send(request, HttpResponse.BodyHandlers.ofString()).body();

         // 🔥 trata o texto retornado
        return formatarResposta(response);
    }

    public static String buscarPedido(int clienteId) throws Exception {

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(BASE_URL + "/pedidos/" + clienteId))
                .GET()
                .build();

        String response = client.send(request, HttpResponse.BodyHandlers.ofString()).body();

         // 🔥 trata o texto retornado
        return formatarResposta(response);
    }
}