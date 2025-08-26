# Pipeline automatica di test proxy

Questa pipeline serve per eseguire automaticamente i test sui proxy `/proxy/questions` e `/proxy/interpretation` del backend, verificando che funzionino correttamente e che i log vengano generati. È utile per:
- Validare che le API siano raggiungibili e rispondano come previsto
- Tracciare errori e anomalie in modo automatico
- Migliorare la sicurezza e la robustezza del backend

## Come funziona
La pipeline esegue gli script di test definiti in `proxy_test.py` e salva i risultati e i log in `proxy.log`. Può essere integrata in CI/CD oppure lanciata manualmente.

## Come lanciarla manualmente
1. Assicurati che il backend sia avviato e funzionante.
2. Inserisci un token JWT valido (puoi ottenerlo tramite login Google dalla UI).
3. Esegui il comando:

```powershell
python app/proxy_test.py
```

Puoi modificare lo script per inserire il token e i dati di test.

## Come integrarla in CI/CD (GitHub Actions, Azure DevOps, ecc.)
- Aggiungi uno step che lancia `python app/proxy_test.py` dopo il deploy o prima della pubblicazione.
- Verifica che il file `proxy.log` venga salvato come artefatto o analizzato per errori.

## Note di sicurezza
- Non inserire token reali nel codice sorgente o nei file di pipeline.
- Usa variabili d’ambiente o secret manager per gestire i token.

---

Questa pipeline ti aiuta a mantenere il backend sicuro, testato e monitorato in modo automatico. Per personalizzazioni o integrazioni avanzate, consulta la documentazione del tuo sistema CI/CD.
