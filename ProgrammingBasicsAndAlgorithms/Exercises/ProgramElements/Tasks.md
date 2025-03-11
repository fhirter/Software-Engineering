# Übung Programmelemente

## Lernziele

Die Studierenden

- können die Wiederholungen und bedingte Ausführung routiniert anwenden.
- können die Strukturierungswerkzeuge Funktionen, Klassen und Module korrekt anwenden.
- können Datentypen korrekt wählen.

## Aufgabenstellung

Schreibe einen Algorithmus, der Daten mit einem Mittelwert aggregiert. So soll etwa das Array `[5,5,4,4,3,3,2,2]` bei
einer Fenstergrösse von 2 auf `[5,4,3,2]` reduziert werden. Bei einer Fenstergrösse von 4 soll entsprechend `[4.5, 2.5]`
zurückgegeben werden. Siehe auch [beiliegenden Test](./Solution/logic/mean_test.go).

Erweitere das Programm anschliessend um weitere Aggregierungsfunktionen: "Min", "Max", "Median".

Schreibe ein CLI user interface:

`go run . mean 5 5 4 4 3 3 2 2 -w 2`
`go run . min 5 5 4 4 3 3 2 2 -w 2`
`go run . max 5 5 4 4 3 3 2 2 -w 2`
`go run . median 5 5 4 4 3 3 2 2 -w 2`

Versuche den Programmcode möglichst sauber zu strukturieren!

Für ein Beispiel, wie die Bibliothek "Cobra" für CLI Programme verwendet werden kann, siehe
das [Beispielprogramm](Solution).