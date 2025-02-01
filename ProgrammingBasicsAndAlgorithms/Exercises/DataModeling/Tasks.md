# Übung III: Kompilierte Sprachen und Datentypen

## Lernziele

Die Studierenden

- wissen wie ein Programm einer höheren Programmiersprache in Maschinencode übersetzt wird
- kennen die Eigenschaften der aktuell wichtigsten Programmiersprachen und deren Anwendungsgebiete
- können die Strukturierungswerkzeuge Funktionen und Klassen korrekt anwenden.
- können Datentypen korrekt wählen.
- können mit Tests und TDD sicherstellen, dass die entwickelten Programme korrekt funktionieren
- können Programme sinnvoll dokumentieren
- können die Wiederholungen und bedingte Ausführung routiniert anwenden.
- können Datenstrukturen korrekt auswählen und verwenden.

## Aufgabenstellung

Modelliere folgende Daten für ein CRM System in Go:

Ein `Kunde` hat folgende Eigenschaften:

- Eindeutige ID in Form einer UUID
- Kontaktperson
- Adresse

Eine (Kontakt-)`Person` hat folgende Eigenschaften:

- Vorname und Nachname
- Gender
- Telefonnummer
- E-Mail-Adresse

Eine `Adresse` hat folgende Eigenschaften:

- Strasse und Hausnummer
- Postleitzahl
- Ort

Modelliere die Daten zuerst mit einem Klassendiagramm. Überlege dir genau, welche Datentypen geeiget sind.

Schreibe geeignete Tests und implementiere anschliessend die Datenstrukturen.
Sie das beliegende [Beispiel](article.go).

Schreibe eine einfache Suche, die Kunden anhand verschiedener Kriterien wie Adresse oder Kontaktperson findet.

## Dokumentation

Halte das Vorgehen, die Erkenntnisse und offene Fragen in einer README.md Datei fest.

## Weiterführende Aufgaben

Erstelle eine einfache Web-Applikation.

- Erstelle einen einfachen Webserver mit der `net/http` Package.
- Erstelle eine Homepage, welche eine Willkommensnachricht anzeigt.
- Erstelle API Endpoints `/api/v1/persons`, `/api/v1/customers`, `/api/v1/addresses` welche entsprechende Daten zurückgeben (`GET`).
- Ermögliche das Hinzufügen, Löschen und Aktualisieren der Daten.
- Speichere die Daten in einer Datenbank.