# Übung III

## Lernziele

Die Studierenden

- wissen wie ein Programm einer höheren Programmiersprache in Maschinencode übersetzt wird
- kennen die Eigenschaften der aktuell wichtigsten Programmiersprachen und deren Anwendungsgebiete
- wissen, dass die hohe Komplexität von Systemen grosse Herausforderungen mit sich bringen
- können Programme mit einfachen Deployment-Pipelines automatisiert überprüfen
- können die Strukturierungswerkzeuge Funktionen, Klassen und Module korrekt anwenden.
- können Datentypen korrekt wählen.

## Aufgabenstellung

Erstelle eine einfache Web-Applikation.

- Erstelle einen einfachen Webserver mit der `net/http` Package.
- Erstelle eine Homepage, welche eine Willkommensnachricht anzeigt.
- Erstelle einen API Endpoint `/api/v1/quotes`, welcher zufällige Zitate zurückgibt.

Strukturiere deinen Code sinnvoll mit Packages und Funktionen.

Beschreibe die Funktionalität zuerst mit Tests mit der `net/http/httptest` Package.

Schreibe für die einzelnen Funktionen vor der Implementierung Unit-Tests.

Führe die Tests mit Github Actions in einer Deployment-Pipeline aus.

Mögliche Erweiterungen:

- Speichere die Zitate in einer Datenbank
- Ermögliche das Hinzufügen von Zitaten
- Deploye die Applikation automatisch

## Dokumentation

Halte das Vorgehen, die Erkenntnisse und offene Fragen in einer README.md Datei fest.

### Präsentation

Erstelle anhand der Dokumentation, dem Code und der Visualisierung eine kurze (max 5min) und ansprechende Präsentation. 

Im Anschluss gibt es eine kurze Frage und Feedbackrunde (5min).

## Bewertung

| Bereich         | Beschreibung                                                                                  | Punkte |
|-----------------|-----------------------------------------------------------------------------------------------|--------|
| Implementierung | Sinnvolle Strukturierung, Deployment Pipeline führt Tests aus                                 | 10     |
| Testing         | Applikation wird vollständig und sinnvoll getestet                                            | 10     |
| Dokumentation   | Vorgehen,Erkenntnisse, offene Fragen sind festgehalten, sinnvolle und atomare Commit Messages | 10     |
| Präsentation    | Verständlich und ansprechend (Präsentation und Handout), Zeit eingehalten                     | 10     |

## Abgabe

Link zum Repository bis Sonntag Abend in der im Semesterprogramm angegebenen Woche.
