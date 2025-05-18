# Calcoli Enigmatici Solver

Questo script Python (`solver.py`) è un risolutore per il **Calcolo Enigmatico**, puzzle della rivista **La settimana enigmistica** (in genere a pag.12).

---

## Come funziona

- L'utente inserisce equazioni in formato: `AB + C = D`
- Le lettere rappresentano cifre uniche da 0 a 9.
- Si possono usare gli operatori: `+`, `-`, `*`, `//` (divisione intera).
- È possibile aggiungere vincoli logici sulle lettere, ad esempio `A = 3`, `B > A`, `C != 0`.
- Il programma cerca tutte le soluzioni che soddisfano equazioni e vincoli.
- Le soluzioni trovate vengono stampate a video e salvate nel file `soluzione.txt`.

---

## Requisiti

- Python 3.x
- Nessuna libreria esterna necessaria.

---

## Uso

Esegui lo script:

```bash
python solver.py
```

Segui le istruzioni a video:

1. Inserisci una o più equazioni nel formato `LEFT OP RIGHT = RESULT` (esempio: `AB + C = D`). Premere invio dopo ogni equazione.
2. Scrivi `fine` quando hai finito di inserire le equazioni.
3. Se vuoi, inserisci vincoli opzionali (es: `A = 3`, `B > A`), uno per riga, poi scrivi `fine`.
4. Il programma avvierà la risoluzione e stamperà le soluzioni trovate.

---

## Formato equazioni accettato

- Termini composti da lettere (maiuscole o minuscole).
- Formato: `LEFT OP RIGHT = RESULT`
- Operatori supportati: `+`, `-`, `*`, `//` (divisione intera).
- Esempio: `AB + CD = CBA`

---

## Vincoli supportati

- Uguaglianze e disuguaglianze tra lettere o con numeri.
- Esempi validi:
  - `A = 3`
  - `B != 0`
  - `C > D`
  - `E <= 5`
  - `F >= G`

---

## Limiti

- Max 10 lettere distinte per problema.
- Il risolutore cerca tutte le soluzioni, ma l'algoritmo può impiegare molto tempo per problemi complessi.
- Le lettere all'inizio di un termine non possono essere assegnate a zero (non si accettano numeri con zeri iniziali).

---

## Output

- Soluzioni stampate a video con la mappatura lettere → cifre.
- Le equazioni con i valori numerici verificati.
- Salvataggio automatico delle soluzioni in `soluzione.txt`.

---

## Licenza

Questo progetto è rilasciato sotto licenza MIT. Vedi il file `LICENSE` per i dettagli.

---

## Contatti / Supporto

Per suggerimenti o problemi, apri una issue nel repository o contatta l'autore.

---

Buon divertimento con i tuoi Calcoli Enigmatici! 🧩

