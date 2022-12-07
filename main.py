import os
import openai

test = "Schreibe mir bitte deutsche Karteikarten im csv Dateiformat. Das bedeutet, dass die Frage " \
       "der Karte gefolgt von einem ';' und dann die Antwort kommen soll. Die Karteikarten sollen Fragen zu folgendem " \
       "Text stellen: \n\n {0}"

openai.api_key = os.getenv("OPENAI_API_KEY")

while True:
    userInput = input("Gib den Text an, von welchem die AI Karteikarten generieren soll:")
    print(test.format(userInput))

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=test.format(userInput),
        max_tokens=1000
    )

    f = open("cards.csv", 'a')
    f.write(response.choices[0].text)
    f.close()
