import itertools

def word_to_number(word, mapping):
    return int("".join(str(mapping[c]) for c in word))

def parse_constraint(raw):
    raw = raw.replace(" ", "").upper()
    allowed_ops = ['==', '!=', '>=', '<=', '>', '<', '=']
    for op in allowed_ops:
        if op in raw:
            parts = raw.split(op)
            if len(parts) == 2:
                left, right = parts[0], parts[1]
                if op == "=":
                    op = "=="
                return f'mapping["{left}"] {op} {right if right.isdigit() else f"mapping[\'{right}\']"}'
    raise ValueError("Vincolo non valido. Usa: A=1, B>C, C!=3 ecc.")

def format_constraint_readable(raw):
    raw = raw.replace(" ", "").upper()
    for op in ['==', '!=', '>=', '<=', '>', '<', '=']:
        if op in raw:
            parts = raw.split(op)
            if len(parts) == 2:
                left, right = parts
                return f"{left} {op if op != '==' else '='} {right}"
    return raw  # fallback

def main():
    open("soluzione.txt", "w").close()

    print("💡 Benvenuto al risolutore di Calcoli Enigmatici con Vincoli!")
    print("Inserisci le equazioni nel formato tipo: AB + C = D")
    print("Supportati: +, -, *, // (divisione intera)")
    print("Scrivi 'fine' per terminare l'inserimento.\n")

    equations = []
    letters = set()

    while True:
        eq = input("👉 Inserisci equazione: ").strip()
        if eq.lower() == "fine":
            break
        try:
            parts = eq.split()
            if len(parts) != 5 or parts[3] != '=':
                print("⚠️  Formato non valido. Usa: LEFT OP RIGHT = RESULT")
                continue
            left, op, right, _, result = parts
            equations.append((left.upper(), op, right.upper(), result.upper()))
            letters.update(set(left.upper() + right.upper() + result.upper()))
        except Exception as e:
            print(f"Errore nell'inserimento: {e}")

    # 👉 Sezione vincoli
    vincoli_raw = []
    vincoli = []
    answer = input("\n🔧 Vuoi inserire vincoli aggiuntivi? (s/n): ").strip().lower()
    if answer in ("s", "si", "sì"):
        print("👉 Inserisci vincoli (es: a = 0, b > a, c != 3). Scrivi 'fine' per terminare.")
        while True:
            v = input("🧠 Vincolo: ").strip()
            if v.lower() == "fine":
                break
            try:
                vincoli.append(parse_constraint(v))
                vincoli_raw.append(format_constraint_readable(v))
            except ValueError as e:
                print(f"⚠️ {e}")

    if len(letters) > 10:
        print("❌ Troppe lettere diverse! Max 10.")
        return

    letters = sorted(list(letters))
    print(f"\n🔠 Lettere coinvolte: {', '.join(letters)}")
    if vincoli_raw:
        print(f"🔒 Vincoli attivi: {', '.join(vincoli_raw)}")
    print("🔄 Inizio risoluzione...\n")

    num_attempts = 0
    num_solutions = 0
    debug = False

    for perm in itertools.permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        num_attempts += 1

        if any(mapping[term[0]] == 0 for eq in equations for term in (eq[0], eq[2], eq[3])):
            continue

        try:
            if not all(eval(expr, {}, {"mapping": mapping}) for expr in vincoli):
                continue
        except:
            continue

        valid = True
        for left, op, right, result in equations:
            try:
                lval = word_to_number(left, mapping)
                rval = word_to_number(right, mapping)
                res = word_to_number(result, mapping)

                if op == "+" and lval + rval != res:
                    valid = False
                    break
                elif op == "-" and lval - rval != res:
                    valid = False
                    break
                elif op == "*" and lval * rval != res:
                    valid = False
                    break
                elif op == "//":
                    if rval == 0 or lval // rval != res or lval % rval != 0:
                        valid = False
                        break
            except:
                valid = False
                break

        if valid:
            num_solutions += 1
            output = []
            output.append(f"\n=== ✅ Soluzione #{num_solutions} ===")
            output.append("🔢 Mappatura lettere → cifre:")
            for l in letters:
                output.append(f"  {l} = {mapping[l]}")
            output.append("\n📐 Equazioni verificate:")
            for left, op, right, result in equations:
                lval = word_to_number(left, mapping)
                rval = word_to_number(right, mapping)
                res = word_to_number(result, mapping)
                output.append(f"  {lval} {op} {rval} = {res}")
            if vincoli_raw:
                output.append(f"\n📌 Vincoli usati: {', '.join(vincoli_raw)}")
            output.append("-" * 40)

            result_text = "\n".join(output)
            print(result_text)

            with open("soluzione.txt", "a") as f:
                f.write(result_text + "\n")

    if num_solutions == 0:
        print("❌ Nessuna soluzione trovata.")
    else:
        print(f"\n✅ Totale soluzioni trovate: {num_solutions}")
    print(f"🔁 Tentativi eseguiti: {num_attempts}")

if __name__ == "__main__":
    main()
