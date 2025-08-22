// login_screen.dart
// Login screen UI

// Qui va la schermata di login (Google/email).
// In seguito integrerai Firebase Auth.

import 'package:flutter/material.dart';

class LoginScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // Qui va integrato Firebase Auth
    return Scaffold(
      appBar: AppBar(title: Text('Login')),
      body: Center(child: Text('Schermata di login')),
    );
  }
}
