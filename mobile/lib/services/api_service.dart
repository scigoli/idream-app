// api_service.dart
// API service for mobile app

// Qui andrai a mettere la logica per chiamare il backend FastAPI (ad esempio, invio sogno, ricezione domande, invio risposte).
import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  final String baseUrl;
  final String? authToken; // Token Firebase, da passare nelle richieste

  ApiService({required this.baseUrl, this.authToken});

  Future<List<String>> getQuestions(String dream) async {
    final response = await http.post(
      Uri.parse('$baseUrl/questions'),
      headers: {
        'Content-Type': 'application/json',
        if (authToken != null) 'Authorization': 'Bearer $authToken',
      },
      body: jsonEncode({'sogno': dream}),
    );
    if (response.statusCode == 200) {
      final data = jsonDecode(response.body);
      // Assumendo che il backend restituisca {"domande": [...]}
      return List<String>.from(data['domande']);
    } else {
      throw Exception('Errore nel recupero delle domande');
    }
  }

  Future<String> getInterpretation(String dream, List<Map<String, String>> answers) async {
    final response = await http.post(
      Uri.parse('$baseUrl/interpretation'),
      headers: {
        'Content-Type': 'application/json',
        if (authToken != null) 'Authorization': 'Bearer $authToken',
      },
      body: jsonEncode({
        'sogno': dream,
        'risposte': answers,
      }),
    );
    if (response.statusCode == 200) {
      final data = jsonDecode(response.body);
      // Assumendo che il backend restituisca {"interpretazione": "..."}
      return data['interpretazione'];
    } else {
      throw Exception('Errore nel recupero dell\'interpretazione');
    }
  }
}