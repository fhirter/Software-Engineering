# Übung Programmelemente

## Lernziele

Die Studierenden

- Können die Wiederholungen und bedingte Ausführung routiniert anwenden.
- Können die Strukturierungswerkzeuge Funktionen, Klassen und Module korrekt anwenden.
- Können Datentypen korrekt wählen.

## Aufgabenstellung

Schreibe einen Algorithmus, der Daten mit einem Mittelwert aggregiert. So soll etwa das Array `[5,5,4,4,3,3,2,2]` bei
einer Fenstergrösse von 2 auf `[5,4,3,2]` reduziert werden. Bei einer Fenstergrösse von 4 soll entsprechend `[4.5, 2.5]`
zurückgegeben werden. Siehe auch [beiliegenden Test](mean_test.go).

Erweitere das Programm anschliessend um wählbare Aggregierungsfunktionen: "Min", "Max" und "Mean".

Schreibe ein CLI user interface mit cobra (https://github.com/spf13/cobra)

`go get -u github.com/spf13/cobra@latest`