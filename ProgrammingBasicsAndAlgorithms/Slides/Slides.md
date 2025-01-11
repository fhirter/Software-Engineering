---
headingDivider: 3
auto-scaling: true
paginate: true
---

# Einstieg

## Softwareentwickler:innen bauen Maschinen

- Unsere Maschinen können nicht angefasst werden: Sie sind nicht materiell
- Wir sprechen von Programmen oder Systemen (Software)
- Um eine Softwaremaschine laufen zu lassen brauchen sie eine physische Maschine: den Computer (Hardware)

## Computer

- Computer sind universelle Maschinen. Sie führen die Programme aus, die wir ihnen füttern.
- Der Computer findet das Programm im Speicher und führt es aus.
- Die einzigen Grenzen sind unsere Vorstellungskraft

![w:400px](Images/ComputerBasic.png)

## Computer

- Gute Nachricht
    - Dein Computer macht genau das, was man ihm sagt.
    - Er macht es sehr schnell.
- Schlechte Nachricht
    - Dein Computer macht genau das, was man ihm sagt.
    - Er macht es sehr schnell.

## Programme erstellen und laufen lassen

![w:600px](Images/AProgrammerAUser.png)

## Programme erstellen und laufen lassen

![w:600px](Images/ManyProgrammersManyUsers.png)

## Programme erstellen und laufen lassen

![w:600px](Images/ManyProgrammersManyUsersUsingComputers.png)

## Software sollte folgende Merkmale haben:

- **Korrekt**: Machen, was es sollte.
- **Erweiterbar**: Einfach zu ändern sein.
- **Lesbar**: durch Menschen.
- **Wiederverwertbar**: Das Rad nicht neu erfinden.
- **Robust**: Korrekt auf Fehler reagieren.
- **Sicher**: Angreifer abwehren.

## Software schreiben ist herausfordernd

- Programme können «abstürzen»
- Programme, die nicht «abstürzen» funktionieren nicht zwangsläufig richtig.
    - [Ariane5 Rakete, 1996](https://www.youtube.com/watch?v=PK_yguLapgA)
- Fehlerhafte Programme können Menschen töten (medizinische Geräte, Luftfahrt).
    - [Boeing 737 MCAS](https://www.youtube.com/watch?v=H2tuKiiznsY)
- Programmierer sind verantwortlich für das korrekte Funktionieren der Programme.
- Das Ziel dieses Fachs ist, nicht nur programmieren zu lernen, sondern gut programmieren zu lernen.

## Software schreiben macht Spass

- Entwickle deine eigene Maschine!
- Kreativität und Vorstellungsvermögen kann ausgelebt werden!
- Programme retten leben und machen die Welt besser!

# Entwicklungswerkzeuge

## Programmiersprachen

![w:1000px](Images/TiobeIndex.png)
[Tiobe Index](https://www.tiobe.com/tiobe-index/)
[God-Tier Developer Roadmap](https://www.youtube.com/watch?v=pEfrdAtAmqk)

---

| Name       | Veröffentlichung |                 | Typisierung | Paradigmen  (imperativ sind alle) |
|------------|------------------|-----------------|-------------|-----------------------------------|
| C          | 1972             | Kompiliert      | statisch    | strukturiert                      |
| C++        | 1985             | Kompiliert      | statisch    | objektorientiert                  |
| Python     | 1991             | Interpretiert   | dynamisch   | strukturiert, objektorientiert    |
| JavaScript | 1995             | Interpretiert   | dynamisch   | objektorientiert                  |
| PHP        | 1995             | Interpretiert   | dynamisch   | strukturiert, objektorientiert    |
| Java       | 1995             | Kompiliert (VM) | statisch    | objektorientiert                  |
| C#         | 2000             | Kompiliert      | statisch    | objektorientiert                  |

---

| Name | Veröffentlichung |            | Typisierung | Paradigmen                                 |
|------|------------------|------------|-------------|--------------------------------------------|
| Go   | 2012             | Kompiliert | statisch    | strukturiert, objektorientiert             |
| Rust | 2015             | Kompiliert | statisch    | strukturiert, funktional, objektorientiert |

--- 

| Name       | Eigenschaften                                                                                                 |
|------------|---------------------------------------------------------------------------------------------------------------|
| C          | Sehr schnell und effizient                                                                                    |
| C++        | Schnell und effizient, hochkomplex                                                                            |
| Java       | Virtuelle Maschine (Plattformunabhängig), grosses Angebot an Bibliotheken und Werkzeugen, einfache Syntax    |
| C#         |                                                                                                               |
| Python     | Einfache Syntax, grosses Angebot an Bibliotheken und Werkzeugen                                               |
| JavaScript | Relativ performant, grosse Verbreitung, enorme Auswahl an Bibliotheken und Werkzeugen, Leistungsfähige Syntax |
| PHP        | Für Webanwendungen optimiert, gute und bewährte Frameworks                                                    |

---

|      | Eigenschaften                                                                        |
|------|--------------------------------------------------------------------------------------|
| Go   | Komposition statt Vererbung, Effizienz, Lesbarkeit / DX, Networking, Multiprocessing |
| Rust | Keine Garbage Collection, sicher, nebenläufig, seit 2022 im Linux Kernel verwendet   |

---

|            | Anwendungsgebiet                                                         |
|------------|--------------------------------------------------------------------------|
| C          | Betriebssystemen und Embedded                                            |
| C++        | Betriebssystemen, Desktop Applikationen, Games, Datenbanken, Interpreter |
| Java       | Enterprise Umfeld                                                        |
| C#         | Game Entwicklung (Unity), Microsoft Ökosystem, Enterprise Umfeld         |
| Python     | Wissenschaften, Machine Learning, Big Data, Einsteiger, Automation       |
| JavaScript | Web Frontend und Backend                                                 |
| PHP        | Web                                                                      |

---

|      | Anwendungsgebiet                                                                      |
|------|---------------------------------------------------------------------------------------|
| Go   | Web Backend, Tooling, DevOps                                                          |
| Rust | Betriebssystemen, Desktop Applikationen, Games, Datenbanken, Interpreter, Web Backend |

### Energy, Time, Memory Comparison

![w:500px](Images/EnergyTimeMemoryComparision.png)

## Entwicklungsumgebungen

![w:1200px](Images/IDEs.png)

### Eclipse

- JavaScript/TypeScript, C/C++, PHP, Rust etc
- Open Source

### Microsoft Visual Studio

- VB, C, C++, C##, SQL, TypeScript, Python, HTML, JavaScript, CSS
- Closed Source

### Microsoft Visual Studio Code

- JavaScript, TypeScript, HTML, CSS, etc
- Open Source, Proprietär, frei

### JetBrains

- Java, Kotlin, Groovy, Scala, JavaScript, TypeScript, C (CLion), PHP (PHPStorm), Ruby (RubyMine), Python (PyCharm), iOS (AppCode), Android (AndroidStudio), C## (Rider)
- Teilweise OpenSource (Community Version)

### Jetbrains PyCharm

![w:800px](Images/PyCharm.png)

### Debugging

![w:800px](Images/Debugging.png)

## Versionsverwaltung

- Protokollierung von Änderungen
- Wiederherstellung von alten Ständen
- Archivierung
- Koordinierung des gemeinsamen Zugriffs
- Entwicklungszweige (Branches) -> [Don’t Branch!](https://www.youtube.com/watch?v=v4Ijkq6Myfc)

### Moderne Versionsverwaltung

- [CI/CD](https://www.redhat.com/cms/managed-files/ci-cd-flow-desktop_edited_0.png)
- [GitOps](https://www.atlassian.com/git/tutorials/gitops)
- [Infrastructure as Code](https://en.wikipedia.org/wiki/Infrastructure_as_code)
- Documentation as Code
- Everything as Code

### [Git](https://git-scm.com/downloads)

- Fast jede Funktion arbeitet lokal -> Repository wird repliziert
- Optimistic Locking
- Git stellt Integrität sicher
- [Git fügt im Regelfall nur Daten hinzu](https://git-scm.com/book/de/v2/Erste-Schritte-Was-ist-Git%3F)
- Snapshots statt Unterschiede
  ![w:800px](https://git-scm.com/book/en/v2/images/snapshots.png)

### Die drei Zustände

- Modified
- Staged
- Committed
  ![w:800px](https://git-scm.com/book/en/v2/images/areas.png)

### Arbeiten mit Git

#### Initialisieren

- Auf Github oder Gitlab ein leeres Projekt erstellen
- [Dieses Projekt lokal klonen](https://git-scm.com/docs/git-clone) `git clone`
- User name setzen: `git config user.name <name>`

---

#### Arbeitsablauf

- [Lokales Repository aktualisieren](https://git-scm.com/docs/git-pull) `git pull origin`
- Source Dateien erstellen oder editieren
- [Änderungen zum Staging Area hinzufügen](https://git-scm.com/docs/git-add) `git add <directory>` (z.B. ".")
- [Änderungen im Repository festhalten](https://git-scm.com/docs/git-commit)
  `git commit -m "<message>"` (z.B. "change data type")
- [Lokales Repository aktualisieren](https://git-scm.com/docs/git-pull) `git pull <remote>` (z.B. "origin")
    - Mit Rebase bleibt die History aufgeräumter: `git pull --rebase`
- [Änderungen auf Github/Gitlab/Bitbucket laden](https://git-scm.com/docs/git-push) `git push <remote> <branch>` (z.B. "
  origin main")

### PyCharm Git Integration

![w:600px](Images/GitIntegration.png)

---

![](Images/GitIntegration2.png)

### Conventional Commits

- Die Commit History (`git log`) sollte sich idealerweise wie ein Buch lesen
- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) sind spezifizieren die Struktur von Commits
- Dies macht die Art der Änderung klarer
- Damit können Versionen und Changelogs automatisch erstellt werden
- Mit Tags werden Releases markiert. [semantic versioning](https://semver.org/).

```
feat: allow provided config object to extend other configs

BREAKING CHANGE: `extends` key in config file is now used for extending other config files
```

### Git Ressourcen

- [Cheatsheet](https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet)
- [Atlassian Tutorials](https://www.atlassian.com/git/tutorials/what-is-version-control)
- [Git Tutorials](https://git-scm.com/book/de/v2/Erste-Schritte-Was-ist-Git%3F)
- [Simulationstool](https://learngitbranching.js.org/)

### Plattformen: Github / Gitlab

- Git Server
- CI/CD Plattform
- Issue Tracking / Projektmanagement
- Dokumentation
- Webhosting
- Release Management

---

#### Issue Tracking

![img.png](Images/GitlabIssueBoard.png)

# Testing

## Kosten von Defekten

![cost_of_defects.svg](Images/cost_of_defects.svg)

## Pair Programming

![Pair Programming](Images/PairProgramming.png)

## Test Driven Development (TDD)

- Test First: Fokus auf die Problemstellung und Schnittstelle
- Nur eigenen Code testen. Datenbanken, APIs oder Libraries werden nur im Rahmen von Integrationstests aufgerufen.
- Tests geben eine Rückmeldung zum Code: Wenn Code schwierig zu testen ist, sollte er vermutlich anders strukturiert werden.
- [Humble Object](https://martinfowler.com/bliki/HumbleObject.html): Code, der schwierig zu testen ist in einem minimalen Objekt isolieren

---

![bg fit](Images/tdd-simple.svg)

---

![bg fit](Images/listening-to-tests.svg)

---

![bg fit](Images/tdd-with-acceptance-tests.svg)

---

Drei Abbildungen aus: Growing Object-Oriented Software by Nat Pryce and Steve Freeman

## Testpyramide

![TestPyramid.svg](Images/TestPyramid.svg)

- Akzeptanztests stellen sicher, dass die Applikation die Kundenkriterien erfüllt.
- Unit-Tests stellen sicher, dass einzelne Programmteile wie von den Entwicklern beabsichtigt funktionieren
- Integrationstests sind optional

## Testing: AAA

- **Arrange**: Set up your data
- **Act**: Execute code under Test
- **Assert**: Verify that the result is correct

```python
# Unit Under Test
from ProgrammingBasicsAndAlgorithms.Exercises.Basics.Solutions.sort import sort
# Testing Library
import unittest


# Test suite
class TestSort(unittest.TestCase):
    # Test
    def test_sort(self):
        a = [3, 0, 12, 8]  # Arrange
        b = sort(a)  # Act
        self.assertEqual(b, [0, 3, 8, 12])  # Assert
```

## FIRST

- Fast: Tests should run quickly to encourage frequent execution.
- Isolated: Each test should run independently and not depend on other tests or external systems.
- Repeatable: Tests should produce the same results every time, regardless of the environment.
- Self-validating: Tests should have clear pass/fail outcomes without manual inspection.
- Timely: Write tests when the code is fresh, ideally before or during implementation.

## IDE Integration

![img.png](Images/PycharmTestIntegration.png)

## Testing: Further Reading

- [How to write clear and robust unit tests: the dos and don'ts](https://levelup.gitconnected.com/how-to-write-clear-and-robust-unit-tests-the-dos-and-donts-5021c097d041)
- [The Real Value of Testing](https://drpicox.medium.com/the-real-reason-to-do-testing-6f12b410dde3)

# Dokumentation (as Code)

- Geeignet für Versionverwaltung
- Kein Kontextwechsel für Dokumentation

## Markdown

```markdown
## Markdown

- Triviale Syntax
- Sehr zukunftssicher
- Syntax-highlight für Code
- Automatisierbar
- Sehr hohe Verbreitung
```

### Markdown Tools

- [Documents](https://dillinger.io/)
- [Github](https://docs.github.com/de/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github)
- [Gitlab](https://docs.gitlab.com/ee/user/markdown.html)
- [Websites](https://gohugo.io/)
- [Notes](https://obsidian.md/)
- Books
- [Documentation](https://www.mkdocs.org/)
- [etc etc etc](https://www.markdownguide.org/tools/)

### Markdown Basic Syntax

![](Images/MarkdownBasicSyntax.png)
[Markdown](https://www.markdownguide.org/)

### Markdown Renderer

- [Dokumentationswebsites mit MKDocs](https://www.mkdocs.org/)
- [Slides mit Marp](https://marp.app/)
- [Websites mit Hugo](https://gohugo.io/)

### Diagramme in Markdown

-[Mermaid](https://mermaid.js.org/)

# CI / CD

## CI/CD mit Git

- Tests und Linter werden bei Commit automatisch ausgeführt und Commit ggf. abgelehnt.
- Das neuste Release wird automatisch deployed.

#### Gitlab CI/CD Plattform

![img.png](../../Architecture/Slides/Images/GitlabPipelines.png)

# Algorithmen und Datenstrukturen

## Containerdatenstrukturen

- Enthalten andere Objekte («items»)
- Grundsätzliche Operationen:
    - Elemente hinzufügen
    - Elemente entfernen
    - Ein Element suchen
    - Über alle Elemente iterieren
- Verschiedene Implementationen unterscheiden sich
    - Welche Operationen möglich sind
    - Wie schnell diese sind
    - Wie der Speicher ausgenutzt wird

## Konkrete Datenstrukturen

### Array

![w:400px](Images/Array.svg)

### Graph

![w:600px](Images/Graphs.svg)

## Abstrakte Datenstrukturen

### Record

- Einfachste Anordnung von Daten
- Zeile in Datenbank / Tabelle
- Datenobjekte

```C
// C
struct date {
  int year;
  int month;
  int day;
}
```

```python
# python
tup1 = ('physics', 'chemistry', 1997, 2000)
```

### Set

- Anordnung von Elementen
- keine Duplikate
- keine definierte Ordnung
- testen, ob Teil des Sets

```python
# python
thisset = {"apple", "banana", "cherry"}
```

### List

- Definierte Ordnung
- Elemente hinzufügen und entfernen
- Element mit einem Index abrufen
- Duplikate möglich

```python
# python
list2 = [1, 2, 3, 4, 5, 6, 7]
first_item = list2[0]  # select first item
list2[1:5]  # select items 2 to 6
```

### Map

- Schlüssel / Wert Paare
- Hinzufügen, Entfernen, Ändern, Abrufen
- Assoziatives Array, Lookup Table, Dictionary

```python
# python
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Name']  # Zara
```

### Queue

- FIFO: First In, First Out
- Warteschlange, Pipe
  ![](Images/queue.png)

### Stack

- LIFO: Last In, First Out
- push: Neues Element speichern
- pop: Letztes Element abrufen und entfernen
- Stapelspeicher, Kellerspeicher
  ![](Images/stack.png)

---

![](Images/ProgramStack.png)

## Tree

![w:600px](Images/Tree.png)

---

![w:600px](Images/tree_example.png)

## Komplexität von Algorithmen

### Speicher und Rechenaufwand von Datenstrukturen

![Complexity.png](Images/Complexity.png)

### Big O Notation

![w:400px](Images/BigO.png) [Big O Cheatsheet](https://www.bigocheatsheet.com/)

- O(1): Operation dauert immer gleich lange, unabhängig von der Anzahl der Elemente
- O(n): Operation ist linear abhängig von der Anzahl der Elemente (Je mehr Elemente in der Liste, desto länger dauert die Operation)

### Alternative Big O Notation

|         |          |
|---------|----------|
| O(1)    | O(yeah)  |
| O(logn) | O(nice)  |
| O(n)    | O(k)     |
| O(n^2)  | O(my)    |
| O(2^n)  | O(no)    |
| O(n!)   | O(mg)    |
| O(n^n)  | O(sh*t!) |

https://quanticdev.com/algorithms/primitives/alternative-big-o-notation/

# Dependencies

## Herausforderungen

- Verschiedene Projekte benötigen verschiedene Versionen der gleichen Bibliothek
- Sicherheitslücken müssen erkannt und behoben werden
- Neue Funktionalität sollte geladen werden können
- Builds sollten reproduzierbar sein

## Lösung: Packetmanager

- Python: PIP
- NodeJS: NPM
- PHP: Composer
- Go: go get
- Rust: cargo
- Java: Maven

## Paketmanager

- Laden von Bibliotheken `pip install pip-audit`
- Aktualisierungen  `pip install --upgrade <package-name>`
- Dependency Checks: `pip-audit`, `npm audit`
- Dependencies werde pro Projekt festgehalten
    - Python: requirements.txt, virtual env
    - JS: package.json, node_modules
    - GO: go.mod

## Requirements.txt

```bash
pip freeze > requirements.txt  # generate
pip install - r requirements.txt  # load
```

```requirements
click == 8.1.3
ghp-import == 2.1.0
importlib-metadata == 4.11.4
Jinja2 == 3.1.2
joblib == 1.2.0
Markdown == 3.3.7
```

## Semantic Versioning

> Auf Grundlage einer Versionsnummer von MAJOR.MINOR.PATCH werden die einzelnen Elemente folgendermaßen erhöht:

> 1. MAJOR wird erhöht, wenn API-inkompatible Änderungen veröffentlicht werden,
> 2. MINOR wird erhöht, wenn neue Funktionalitäten, die kompatibel zur bisherigen API sind, veröffentlicht werden, und
> 3. PATCH wird erhöht, wenn die Änderungen ausschließlich API-kompatible Bugfixes umfassen.

> Außerdem sind Bezeichner für Vorveröffentlichungen und Build-Metadaten als Erweiterungen zum MAJOR.MINOR.
> PATCH-Format verfügbar.

https://semver.org/lang/de/

## Tipps

- Abhängigkeiten Automatisiert auf Updates und Sicherheitslücken testen
- Versionen immer "pinnen": `3.2.1`, ~~`^3.2.1`~~,  ~~`3`~~
- Vorsicht bei indirekten Abhängigkeiten!

## Container

Applikation wird mitsamt ihren Abhängigkeiten in einen "Container" gepackt.

```Dockerfile
FROM node:20

ARG ENVIRONMENT="development"

WORKDIR /usr/src/app

COPY backend /usr/src/app
RUN rm /usr/src/app/lib
COPY lib /usr/src/app/lib

RUN npm ci --verbose

EXPOSE 8080

CMD ./setup-ci.sh
```

# Clean Code

[https://cleancoders.com/](https://cleancoders.com/)
[Clean Code: A Handbook of Agile Software Craftsmanship](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882)

## Bezeichner

> There are only two hard things in Computer Science: cache invalidation and naming things.
> -- Phil Karlton

## Bezeichner

- Zweck erkennbar
- Keine Falschinformation
- Unterscheidbar
- Aussprechbar
- Suchbar
- Klassen: Nomen
- Methoden: Verben
- Länge dem Scope entsprechend

## Funktionen

- Kurz!
- Machen nur etwas
- Keine Nebenwirkungen
- Höchstens 3 Parameter
- Don't Repeat Yourself

## Kommentare

- Code sollte selbsterklärend sein
- Informativ
- Absicht erklären
- Erläuterung
- Warnung
- Todo

# Refactoring

## Why Should You Refactor?

* Refactoring Improves the Design of Software
* Refactoring Makes Software Easier to Understand
* Refactoring Helps You Find Bugs
* Refactoring Helps You Program Faster

## When Should You Refactor?

* [The Rule of Three](https://en.wikipedia.org/wiki/Rule_of_three_(computer_programming))
* Refactor When You Add Functionality
* Refactor When You Need to Fix a Bug
* Refactor As You Do a Code Review


# Fehlerbehandlung

- Exceptions, die im normalen Programmablauf auftreten können (z.B. Fehlerhafter User Input, Netzwerkverbindung offline) müssen gefangen und behandelt werden.
- Exceptions aufgrund von einem Programmierfehler sollten nicht gefangen werden.
- Code für die Fehlerbehandlung sollte möglichst vom Code der Funktionalität getrennt werden.

## Geworfene Exceptions

```python
try:
    foo()  ## method that might raise an exception
except:
## handle exception
```

```python
raise Exception('<error message>')
```

## Fehler als Rückgabewert

- Exceptions können es schwierig machen, den Programmablauf nachzuvollziehen, weil Exceptions den normalen Programmablauf unterbrechen.
- In Go müssen Fehler als Rückgabewert explizit angegeben werden.
- Die kann mit Fehlertypen auch in den meisten anderen Sprachen erreicht werden

```go
swagger, err := api.GetSwagger()
if err != nil {
    fmt.Fprintf(os.Stderr, "Error loading swagger spec\n: %s", err)
    os.Exit(1)
}
```

```go
func Sqrt(f float64) (float64, error) {
    if f < 0 {
        return 0, errors.New("math: square root of negative number")
    }
    // implementation
}
```

### Fehler als Rückgabewert in Python

```python
def return_value():
    return 'foo', None


def test_return_value(self):
    value, error = return_value()
    self.assertIsNotNone(value)
    self.assertIsNone(error)


def return_error():
    return None, Exception('something went wrong')


def test_return_error(self):
    value, error = return_error()
    self.assertIsNotNone(error)
    self.assertIsNone(value)
```

