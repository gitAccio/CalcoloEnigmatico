# Calcoli Enigmatici - Web App

Questo progetto fornisce uno strumento web per risolvere il **Calcolo Enigmatico** de **La Settimana Enigmistica** con equazioni e vincoli opzionali.

---

## Come usare

1. **Inserisci le equazioni** nel box “Equazioni”, una per riga, nel formato:

   ```
   AB + CD = EFG
   A + B = D
   ```

2. **Inserisci vincoli opzionali** nel box “Vincoli opzionali”, uno per riga, ad esempio:

   ```
   A = 3
   B > A
   C != 0
   ```

3. Premi il bottone **“Risolvi”**.

4. I risultati appariranno nel riquadro sotto, con tutte le soluzioni trovate (fino a un massimo di 50).

---

## Limiti e note

- Massimo 10 lettere diverse per problema.
- Supportati operatori: `+`, `-`, `*`, `//` (divisione intera).
- Vincoli con operatori: `=`, `==`, `!=`, `<`, `>`, `<=`, `>=`.
- Le soluzioni rispettano tutti i vincoli e le equazioni.
- Per problemi complessi, il calcolo può richiedere qualche secondo.

---

## Struttura

- `index.html`: pagina web con interfaccia e logica JavaScript.
- Nessuna dipendenza esterna, tutto client-side.


## Licenza

Questo progetto è rilasciato sotto licenza MIT. Vedi il file `LICENSE` per i dettagli.
