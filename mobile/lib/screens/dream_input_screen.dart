import 'package:flutter/material.dart';

class DreamInputScreen extends StatefulWidget {
  final Function(String) onDreamSubmitted;
  const DreamInputScreen({required this.onDreamSubmitted, super.key});

  @override
  State<DreamInputScreen> createState() => _DreamInputScreenState();
}

class _DreamInputScreenState extends State<DreamInputScreen> {
  final TextEditingController _controller = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Descrivi il tuo sogno')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            TextField(
              controller: _controller,
              maxLines: 5,
              decoration: InputDecoration(
                labelText: 'Che sogno hai fatto?',
                border: OutlineInputBorder(),
              ),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              child: Text('Avanti'),
              onPressed: () {
                if (_controller.text.isNotEmpty) {
                  widget.onDreamSubmitted(_controller.text);
                }
              },
            ),
          ],
        ),
      ),
    );
  }
}