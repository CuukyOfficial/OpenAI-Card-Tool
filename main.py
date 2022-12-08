import openai

def get_input():
    # Liste zur Speicherung der Eingabe
    input_lines = []

    # Schleife, die solange läuft, bis der Benutzer eine leere Eingabe macht
    while True:
        # Eingabe vom Benutzer abfragen
        user_input = input()

        # Überprüfen, ob die Eingabe leer ist
        if not user_input:
            break

        # Die Eingabe zur Liste hinzufügen
        input_lines.append(user_input)

    # Die Liste als String zurückgeben
    return "\n".join(input_lines)


if __name__ == '__main__':
    # API-Key für OpenAI setzen
    openai.api_key = "your api key"

    # Vorlage für die Prompt-Nachricht
    prompt_template = "Erstelle mir bitte deutsche Karteikarten im csv Dateiformat. Das bedeutet, dass auf jeder " \
                      "Karteikarte eine Frage gefolgt von einem ';' und dann die Antwort dazu kommen soll. Schreibe " \
                      "die Karteikarten zu dem folgenden Text: \n\n {0}"

    # Endlosschleife zur wiederholten Abfrage von Benutzereingaben
    while True:
        print("Schreibe Nachricht:")

        # Eingabe vom Benutzer abfragen
        user_input = get_input()

        # Nachricht für die OpenAI-API generieren
        prompt_message = prompt_template.format(user_input)

        print("Compiling...")

        # Vervollständigung mit OpenAI anfordern
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt_message,
            max_tokens=1000,
            temperature=1
        )

        # Antwort von OpenAI in cards-Variable speichern
        cards = response.choices[0].text

        # Liste der Zeichen, die ersetzt werden sollen
        replace_chars = [("Frage; ", ""), ("Antwort; ", ""), ("Frage: ", ""), ("Antwort: ", ""), ("\n\n", "\n")]

        # Schleife zum Durchlaufen der Zeichen in replace_chars
        for old, new in replace_chars:
            # Zeichen ersetzen
            cards = cards.replace(old, new)

        # Überprüfen, ob die Antwort mit einem Semikolon beginnt
        if not cards.startswith(";"):
            # Antwort in die Datei /Users/julianheines/Downloads/anki.csv schreiben
            with open("your_file_name.csv", 'a') as f:
                f.write(cards)
            print("Geschrieben")
