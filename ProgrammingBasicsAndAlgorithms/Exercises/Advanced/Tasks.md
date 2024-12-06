# Übung II: Fortgeschrittene Algorithmen

Implementiere, teste, dokumentiere einen bekannten und verbreiteten Algorithmus.

Wähle ein deinen Kenntnissen (🤔, 😳, 🤯) entsprechendes Problem aus folgender Liste:

- Sortieren
    - Bubble Sort 🤔
    - Quicksort 😳
    - Mergesort 😳
    - Merge Insertion 😳
- Verschlüsselung
    - RSA 🤯
    - AES 🤯
- Prüfsumme
    - CRC 😳
- Hashing
    - SHA 🤯
    - MD5 🤯
- Kompression:
    - Run Length Encoding 🤯
    - Entropie 🤯
- Routing
    - Dijkstra-Algorithmus 😳
- Clustering
    - DBSCAN 🤯

In Absprache mit dem Dozenten können auch beliebige andere Algorithmen ausgewählt werden.

## Lernziele und Kompetenzen

Alle Lernziele aus Übung [Basics](../Basics/Tasks.md), zusätzlich:

Die Studierenden

- verstehen die Wichtigkeit von Softwarequalität und potenziellen Fehlerquellen für die Nutzer des Systems
- können die Funktionsweise von einfacheren Algorithmen etwa zum Suchen, Sortieren oder Faktorisieren verstehen.
- verstehen die unterschiedliche Komplexität von Algorithmen und können die BigO Notation interpretieren
- kennen die Datenstrukturen Array und Graphen und deren Anwendungen
- können Datenstrukturen korrekt auswählen und verwenden.
- können Wiederholungen und bedingte Ausführung routiniert anwenden.
- können Funktionen korrekt anwenden.

## Vorgehen

Bearbeite die Aufgabenstellung in der folgenden Reihenfolge.

### Initialisierung

Erstelle ein Projekt auf Github oder Gitlab und klone es in der Entwicklungsumgebung.

Erstelle bei jeder Änderung sogenannte "[Atomic Commits](https://en.wikipedia.org/wiki/Atomic_commit#Atomic_commit_convention)".

### Testing

Schreibe zuerst Tests, die das Problem und dessen Lösung anhand von Beispielen beschreiben.

### Recherche

Recherchiere, mit welchem Algorithmus das Problem gelöst werden kann.

Halte deine Erkenntnisse nachvollziehbar (d.h. mit genauer Quellenangabe) in einem Markdown Dokument fest. Erfasse die Dokumente in Git.

### Implementierung

Implementiere den Algorithmus anhand der Recherche. Nutze nur grundlegende Programmstrukturen wie Schleifen, bedingte Ausführung und Funktionen. Verzichte auf komplexe Bibliotheksfunktionen.

Stelle sicher, dass du den Ablauf verstehst. Halte Erkenntnisse in Markdown Files fest.

### Komplexitätsanalyse

Untersuche die Komplexität des implementierten Algorithmus mittels belastbaren Messungen, nutze dazu z.B.
"[pytest-benchmark](https://pytest-benchmark.readthedocs.io/en/latest/)". Bestimme anhand der Messungen, zu welcher [Komplexitätsklasse](https://www.bigocheatsheet.com/) der Algorithmus gehört.

Visualisiere die Messungen (Rechenaufwand in Abhängigkeit der Samplegrösse) mit Matplotlib.

### Präsentation

Erstelle anhand der Dokumentation, dem Code und der Visualisierung eine kurze (max 5min), ansprechende Präsentation und ein Handout. Präsentiere die Arbeit der Klasse.

Im Anschluss gibt es eine kurze Frage und Feedbackrunde.

## Bewertung

| Bereich             | Beschreibung                                                                                                      | Punkte |
|---------------------|-------------------------------------------------------------------------------------------------------------------|--------|
| Testing             | Applikation wird vollständig und sinnvoll getestet                                                                | 10     |
| Recherche           | Verständlich und korrekt erläutert, Quellen vorhanden und Aussagen nachvollziehbar                                | 10     |
| Implementierung     | Nur grundlegende Programmstrukturen, Funktionsweise verständlich erläutert, sinnvolle und atomare Commit Messages | 10     |
| Komplexitätsanalyse | Korrekte und belastbare Messungen, korrekte Komplexitätsklasse, Veständliche Visualisierung                       | 10     |
| Präsentation        | Verständlich und ansprechend (Präsentation und Handout), Zeit eingehalten                                         | 10     |