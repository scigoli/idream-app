import 'package:flutter/material.dart';

class QuestionWizardScreen extends StatefulWidget {
  final List<String> questions;
  final Function(List<Map<String, String>>) onCompleted;
  const QuestionWizardScreen({required this.questions, required this.onCompleted, super.key});

  @override
  State<QuestionWizardScreen> createState() => _QuestionWizardScreenState();
}

class _QuestionWizardScreenState extends State<QuestionWizardScreen> {
  int _currentIndex = 0;
  List<String> _answers = [];

  @override
  void initState() {
    super.initState();
    _answers = List.filled(widget.questions.length, '');
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Rispondi alle domande')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            Text(widget.questions[_currentIndex], style: TextStyle(fontSize: 18)),
            TextField(
              onChanged: (val) => _answers[_currentIndex] = val,
              decoration: InputDecoration(
                labelText: 'Risposta',
                border: OutlineInputBorder(),
              ),
            ),
            SizedBox(height: 20),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                if (_currentIndex > 0)
                  ElevatedButton(
                    child: Text('Indietro'),
                    onPressed: () {
                      setState(() {
                        _currentIndex--;
                      });
                    },
                  ),
                ElevatedButton(
                  child: Text(_currentIndex == widget.questions.length - 1 ? 'Invia' : 'Avanti'),
                  onPressed: () {
                    if (_answers[_currentIndex].isEmpty) return;
                    if (_currentIndex < widget.questions.length - 1) {
                      setState(() {
                        _currentIndex++;
                      });
                    } else {
                      // Fine wizard
                      final result = List.generate(widget.questions.length, (i) => {
                        'question': widget.questions[i],
                        'answer': _answers[i],
                      });
                      widget.onCompleted(result);
                    }
                  },
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}