# Programmieren Grundlagen

Implementiere, teste, visualisiere und dokumentiere einen bekannten und verbreiteten Algorithmus.

Wähle ein Problem aus folgender Liste:

- Sortieren
- Suchen
- Primzahlen bestimmen
- Faktorisierung
- Grösster gemeinsamer Teiler

## Lernziele

Die Studierenden

- können Entwicklungsumgebung und Versionsverwaltung effizient und zielführend einsetzen.
- können bei der Programmierung empirische Mittel anwenden.
- können mit Tests und TDD sicherstellen, dass die entwickelten Programme korrekt funktionieren.
- können Programme sinnvoll dokumentieren.
- können die Wiederholungen und bedingte Ausführung routiniert anwenden.
- können einfachere Algorithmen etwa zum Suchen, Sortieren oder Faktorisieren implementieren.

## Vorgehen

Bearbeite die Aufgabenstellung in der folgenden Reihenfolge.

### Initialisierung

Erstelle ein Projekt auf Github oder Gitlab und klone es in der Entwicklungsumgebung.

Erstelle bei jeder Änderung
sogenannte "[Atomic Commits](https://en.wikipedia.org/wiki/Atomic_commit#Atomic_commit_convention)". Erstelle also
Commits, die nur eine einzelne Änderung umfassen.

### Testing

Schreibe zuerst Tests, die das Problem und dessen Lösung anhand von Beispielen beschreiben.

Zum Beispiel:

```python
# using unittest
a = [3, 0, 12, 8]
b = sort(a)
self.assertEqual(b, [0, 3, 8, 12])
```

### Recherche

Recherchiere, mit welchem Algorithmus das Problem gelöst werden kann.

Halte deine Erkenntnisse nachvollziehbar (d.h. mit genauer Quellenangabe) in einem Markdown Dokument fest. Erstelle ein
Flussdiagramm vom Algorithmus in Mermaid oder PlantUML. Erfasse die Dokumente in Git.

### Implementierung

Implementiere den Algorithmus anhand von Code Beispielen und dem Fluss-Diagramm. Stelle sicher, dass du den Ablauf
verstehst. Halte Erkenntnisse in Markdown Files fest.

### Präsentation

Erstelle anhand der Dokumentation, dem Code und der Visualisierung eine kurze, ansprechende Präsentation und ein
Handout. Präsentiere die Arbeit der Klasse.

## Weitergehende Arbeiten

### Pipeline

Erstelle eine Pipeline welche die Tests automatisch ausführt.

### Komplexitätsanalyse

Untersuche die Komplexität des implementierten Algorithmus mittels belastbaren Messungen, nutze dazu z.B.
"[pytest-benchmark](https://pytest-benchmark.readthedocs.io/en/latest/)". Bestimme anhand der Messungen, zu
welcher [Komplexitätsklasse](https://www.bigocheatsheet.com/) der Algorithmus gehört.

### Visualisierung

Visualisiere den Algorithmus mit [matplotlib](https://matplotlib.org/).


## Bewertung

| Bereich                                                                                                                | Punkte |
|------------------------------------------------------------------------------------------------------------------------|--------|
| Sinnvolle und atomare Commit Messages                                                                                  | 10     |
| Testing: Applikation wird vollständig und sinnvoll getestet                                                            | 10     |
| Recherche: Verständlich und korrekt erläutert (Text und Flussdiagramm), Quellen vorhanden und Aussagen nachvollziehbar | 10     |
| Implementierung                                                                                                        | 10     |
| Präsentation: Verständlich und ansprechend (Präsentation und Handout)                                                  | 10     |
