// main.dart
// Entry point for Flutter mobile app

// Questo è il punto di ingresso dell’app Flutter.
// Qui puoi avviare la schermata di login o il wizard.

import 'package:flutter/material.dart';
import 'screens/login_screen.dart';

void main() {
  runApp(const IdreamApp());
}

class IdreamApp extends StatelessWidget {
  const IdreamApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Interprete dei sogni',
      home: LoginScreen(),
    );
  }
}