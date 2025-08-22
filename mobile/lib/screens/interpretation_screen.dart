import 'package:flutter/material.dart';

class InterpretationScreen extends StatelessWidget {
  final String interpretation;
  const InterpretationScreen({required this.interpretation, super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Interpretazione')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: SingleChildScrollView(
          child: Text(interpretation, style: TextStyle(fontSize: 18)),
        ),
      ),
    );
  }
}