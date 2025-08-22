// dream_wizard_screen.dart
// Dream wizard screen UI

// Qui va il wizard per la raccolta del sogno, domande e risposte.
// La logica è simile a quella del tuo script Python, ma con UI Flutter.

import 'package:flutter/material.dart';

class DreamWizardScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // Qui va il wizard per sogno/domande/risposte
    return Scaffold(
      appBar: AppBar(title: Text('Interprete dei sogni')),
      body: Center(child: Text('Wizard sogno')),
    );
  }
}
