<!-- headingDivider: 2 -->

# Organisatorisches

## Lernziele I

Die Studierenden kennen die Methoden der objektorientierten Programmierung und können diese anwenden.
Sie sind in der Lage, mittelgrosse, vollständig objektorientierte, grafische Anwendungen zu implementieren, testen und dokumentieren.

## Lernziele II

Die Studierenden
- kennen die Konzepte Kapselung, Vererbung, Polymorphie, dynamisches Binden, abstrakte Klassen und generische Programmierung und können diese in einfachen Beispielen anwenden. 
- können den Kontrollfluss eines Programmes mit Ausnahmebehandlung verstehen und die Vorteile erläutern.
- kennen die SOLID - Prinzipien und können sie in eigenen Worten erklären.
- kennen die verschiedenen Testarten und können einfache Unit-Tests selber schreiben.

## Lernziele II
Die Studierenden
- kennen das Vorgehen beim Test Driven Development und kennen die Bedeutung von Refactoring und Testing als integralen Teil der Softwareentwicklung.
- kennen das Vorgehen sowie Vor- und Nachteile des Pair-Programming.
- können eine GUI-Applikation entwickeln. Sie können dabei gängige objektorientierte Konzepte anwenden und den Code sinnvoll strukturieren.
- wissen, worauf sie bei der Auswahl eines Frameworks achten müssen.

## Unterlagen
- [github.com/fhirter](https://github.com/fhirter/ObjektorientierteProgrammierung)
- Literatur.pdf
- OneNote Klassennotizbuch

## Ratschlag
- Wenn du etwas nicht verstehst, frage! Dumme Fragen sind nur die, die nicht gestellt werden.

# Einstieg

## Design
"Any sufficiently advanced technology is indistinguishable from magic."

-- Arthur C. Clarke

## Softwareentwickler:innen bauen Maschinen
- Unsere Maschinen können nicht angefasst werden: Sie sind nicht materiell
- Wir sprechen von Programmen oder Systemen (Software)
- Um eine Softwaremaschine laufen zu lassen brauchen sie eine physische Maschine: den Computer (Hardware)

## Computer
- Computer sind universelle Maschinen. Sie führen die Programme aus, die wir ihnen füttern.
- Die einzigen Grenzen sind unsere Vorstellungskraft
- Gute Nachricht
  - Dein Computer macht genau das, was man ihm sagt.
  - Er macht es sehr schnell.
- Schlechte Nachricht
  - Dein Computer macht genau das, was man ihm sagt.
  - Er macht es sehr schnell.

## Programme erstellen und laufen lassen
![w:500px](Images/create_and_run_programs.png)

## Programme erstellen und laufen lassen
![w:10000px](Images/create_and_run_programs2.png)

## Programme erstellen und laufen lassen
![w:800px](Images/create_and_run_programms3.png)

## Verbreitete Mythen und Entschuldigungen
- «Computer sind intelligent»
  - Fakt: Computer sind weder intelligent noch dumm. Sie führen Programme aus, die von Menschen entwickelt wurden. 
  - Diese Programme bilden die Intelligenz ihrer Autoren ab. 
  - Die grundlegenden Computeroperationen sind elementar (Speichere diesen Wert, Addiere diese beiden Zahlen...)
- «Der Computer ist abgestürzt»
- [«Der Computer erlaubt das nicht»](https://youtu.be/0n_Ty_72Qds)
- «Der Computer hat ihren Datensatz verloren»
- [how to never write bug - Fireship.io](https://youtu.be/X3jw1JVNdPE)

## Software schreiben ist herausfordernd
- Programme können «abstürzen»
- Programme, die nicht «abstürzen» funktionieren nicht zwangsläufig richtig.
- Fehlerhafte Programme können Menschen töten, (medizinische Geräte, Luftfahrt) → Boeing 737 MCAS
- Ariane5 Rakete, 1996: $10 Milliarden verloren aufgrund eines Programmfehlers.
- Programmierer sind veranwortlich für das korrekte Funktionieren der Programme
- Das Ziel dieses Fachs ist, nicht nur programmieren zu lernen, sondern gut programmieren zu lernen.

## Grundsätzliche Organisation
<!-- Bild -->

## Computer
- Computer sind universelle Maschinen, sie führen Programme aus, die wir ihnen "füttern"
<!-- Bild -->

## Informationen und Daten
- Information ist das, was wir Menschen wollen und verstehen, z.B. ein Lied oder einen Text
  - Interpretation von Daten für Menschen
- Daten bezeichnet, wie dies im Computer gespeichert wird, z.B. als MP3 Datei.
  - Ansammlung von Symbolen in einem Computer

## Informationen und Daten
- Daten werden gespeichert
- Eingabegeräte produzieren Daten aus Informationen
- Ausgabegeräte produzieren Informationen aus Daten
<!-- Bild -->

## Wo ist das Programm?
- Stored-program computer: Das Programm ist im Speicher
  - „ausführbare Daten“
- Ein Programm kann in verschiedenen Formen im Speicher auftreten:
  - Quellcode / Sourcecode: durch Menschen lesbare Form (Programmiersprache)
  - Maschinencode: Ausführbar durch Computer
- Compiler / Interpreter transformieren von Sourcecode zu Maschinencode
- Der Computer findet das Programm im Speicher und führt es aus.

## Software Engineering
Software sollte folgende Merkmale haben:
- Korrekt: Machen, was es sollte!
- Erweiterbar: Einfach zu ändern sein!
- Lesbar: durch Menschen!
- Wiederverwertbar: Das Rad nicht neu erfinden!
- Robust: Korrekt auf Fehler reagieren!
- Sicher: Angreifer abwehren!

## Software schreiben ist herausfordernd
- Es ist schwierig, das Programm korrekt zu schreiben 
- Trial-and-error ist ineffizient

## Software schreiben macht Spass
- Entwickle deine eigene Maschine!
- Kreativität und Vorstellungsvermögen kann ausgelebt werden!
- Programme retten leben und machen die Welt besser!

# Entwicklungswerkzeuge
## Programmiersprachen
![w:1000px](Images/TiobeIndex.png)
[Tiobe Index](https://www.tiobe.com/tiobe-index/)
[God-Tier Developer Roadmap](https://www.youtube.com/watch?v=pEfrdAtAmqk)

## C
- 1972, Dennis Ritchie, Bell Labs
- Kompiliert
- Imperativ, Stukturiert
- statisch Typisiert
- Grosse Verbreitung in Betriebssystemen und Embedded
- Sehr schnell und effizient

## C++
- 1985, Bjarne Stroustrup, Bell Labs
- Kompiliert
- Objektorientiert
- Erweiterung von C
- Schnell und effizient
- Hochkomplex
- Grosse Verbreitung in Betriebssystemen, Desktop Applikationen, Games, Datenbanken, Interpreter

## Java
- 1995, James Gosling, Sun Microsystems
- Kompiliert / Virtuelle Maschine (Plattformunabhängigkeit)
- Objektorientiert
- statisch Typisiert
- Grosses angebot an Bibliotheken und Werkzeugen 
- Einfache Syntax

## C#
- 2000, Anders Hejlsberg, Microsoft
- Kompiliert
- Objektorientiert
- statisch Typisiert
- Game Entwicklung (Unity), Microsoft Ökosystem

## Python
- 1991, Guido van Rossum, Centrum Wiskunde & Informatica
- Interpretiert
- Objektorientiert
- dynamische Typisierung
- Einfache Syntax, schlanke Programme, wenig Ballast
- Grosses Angebot an Bibliotheken und Werkzeugen

## PHP
- 1995, Rasmus Lerdorf
- Interpretiert
- Objektorientiert
- dynamische Typisierung
- Im Web weit verbreitet (Backend)

## JavaScript / TypeScript
- 1995, Brendan Eich, Netscape
- Interpretiert
- Objektorientiert (Prototypenbasiert)
- dynamische Typisierung
- statische Typisierung mit TypeScript, 2014, Microsoft
- Hohe Verbreitung im Web (Frontend und Backend)

## Rust
- 2015, Graydon Hoare, Mozilla
- Kompiliert
- Objektorientiert, nebenläufig
- statische Typisierung
- Keine Garbage Collection
- Sicher, Nebenläufig
- Seit 2022 im Linux Kernel verwendet

## Go
- 2012, Rob Pike / Ken Thompson / Robert Griesemer, Google
- Kompiliert
- Objektorientiert, nebenläufig
- statische Typisierung
- Keine Vererbung
- Effizienz, Lesbarkeit / DX, Networking, Multiprocessing

## Energy, Time, Memory Comparison
![w:500px](Images/EnergyTimeMemoryComparision.png)

## Entwicklungsumgebungen
![w:1200px](Images/IDEs.png)

## Entwicklungsumgebungen
### Eclipse
- JavaScript/TypeScript, C/C++, PHP, Rust etc
- Open Source 

### Microsoft Visual Studio
- VB, C, C++, C##, SQL, TypeScript, Python, HTML, JavaScript, CSS
- Closed Source

---

### Microsoft Visual Studio Code
- JavaScript, TypeScript, HTML, CSS, etc
- Open Source, Proprietär, frei

### JetBrains
- Java, Kotlin, Groovy, Scala, JavaScript, TypeScript, C (CLion), PHP (PHPStorm), Ruby (RubyMine), Python (PyCharm), iOS (AppCode), Android (AndroidStudio), C## (Rider)
- Teilweise OpenSource (Community Version)

## Jetbrains PyCharm
![w:800px](Images/PyCharm.png)

## Debugging
![w:800px](Images/Debugging.png)

## Versionsverwaltung Basics
- Protokollierung von Änderungen
- Wiederherstellung von alten Ständen
- Archivierung
- Koordinierung des gemeinsamen Zugriffs 
- Entwicklungszweige (Branches) -> [Don’t Branch!](https://www.youtube.com/watch?v=v4Ijkq6Myfc)

## Moderne Versionsverwaltung
- [CI/CD](https://www.redhat.com/cms/managed-files/ci-cd-flow-desktop_edited_0.png)
- [GitOps](https://www.atlassian.com/git/tutorials/gitops)
- [Infrastructure as Code](https://en.wikipedia.org/wiki/Infrastructure_as_code)
- Documentation as Code 
  - [Markdown](https://www.markdownguide.org/)
  - [MKDocs](https://www.mkdocs.org/) 
  - [PlantUML](https://plantuml.com/de/)
- Everything as Code

## Git
- Fast jede Funktion arbeitet lokal
- Git stellt Integrität sicher
- Git fügt im Regelfall nur Daten hinzu
- [Download](https://git-scm.com/downloads)
![w:800px](https://git-scm.com/book/en/v2/images/snapshots.png)
[Was ist Git](https://git-scm.com/book/de/v2/Erste-Schritte-Was-ist-Git%3F)

## Die drei Zustände
- Modified
- Staged
- Committed
![w:800px](https://git-scm.com/book/en/v2/images/areas.png)


## Arbeiten mit Git
### Initialisieren
- Auf Github oder Gitlab ein leeres Projekt erstellen
- [Dieses Projekt lokal klonen](https://git-scm.com/docs/git-clone) `git clone`
- User name setzen: `git config user.name <name>`

---

### Arbeitsablauf
- [Lokales Repository aktualisieren](https://git-scm.com/docs/git-pull) `git pull origin`
- Source Dateien erstellen oder editieren
- [Änderungen zum Staging Area hinzufügen](https://git-scm.com/docs/git-add) `git add <directory>` (z.B. ".")
- [Änderungen im Repository festhalten](https://git-scm.com/docs/git-commit) `git commit -m "<message>"` (z.B. "change data type")
- [Lokales Repository aktualisieren](https://git-scm.com/docs/git-pull) `git pull <remote>` (z.B. "origin")
  - Mit Rebase bleibt die History aufgeräumter: `git pull --rebase`
- [Änderungen auf Github/Gitlab/Bitbucket laden](https://git-scm.com/docs/git-push) `git push <remote> <branch>` (z.B. "origin main")

## CI/CD mit Git
- Tests und Linter werden bei Commit automatisch ausgeführt und Commit ggf. abgelehnt.
- Mit Tags werden Releases markiert. [semantic versioning](https://semver.org/).
- Das neuste Release wird automatisch deployed.
- [Changelogs werden automatisiert anhand der Git Messages generiert](https://medium.com/agoda-engineering/automating-versioning-and-releases-using-semantic-release-6ed355ede742)


## Commit Messages
- [Your Git Commit History Should Read Like a History Book](https://betterprogramming.pub/your-git-commit-history-should-read-like-a-history-book-heres-how-7f44d5df1801)
```
feat(logging): added logs for failed signups
fix(homepage): fixed image gallery
test(homepage): updated tests
docs(readme): added new logging table information
```

## PyCharm Git Integration
![w:600px](Images/GitIntegration.png)

---
![](Images/GitIntegration2.png)

## Ressourcen
- [Cheatsheet](https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet)
- [Atlassian Tutorials](https://www.atlassian.com/git/tutorials/what-is-version-control)
- [Git Tutorials](https://git-scm.com/book/de/v2/Erste-Schritte-Was-ist-Git%3F)
- [Simulationstool](https://learngitbranching.js.org/)

# Klassen und Objekte
## Eine Klasse: eine Software Maschine
<!-- bild? -->

## Was ist ein Objekt?
Es gibt verschiedene Arten von Objekten:
- “physische Objekte”: bilden physische Objekte ab, z.B. eine Ampel oder ein Auto
- “abstrakte Objekte”: Beschreiben abstrakte Dinge aus der modelierten Welt, z.B. eine Route oder eine Himmelsrichtung
- “Softwareobjekte”: Reine Softwareelemente, z.B.“Datenstrukturen wie Arrays oder Listen
- Ein grosser Vorteil der objektorientierten Programmierung ist, dass die Software anhand der «echten» Welt modeliert werden kann.

## Was ist ein Objekt?
- Ein Objekt besitzt Daten → Eigenschaften / Felder
- Ein Objekt kann Operationen ausführen → Funktionen / Methoden 

Ein Objekt kann Operationen ausführen und dazu auf seine Daten zugreifen und diese ändern.

## Methoden
- Entspricht dem Begriff "Funktion" der strukturierten Programmierung
- Eine Operation, die von Objekten ausgeführt werden kann.
- Abfragen, Befehle
- Name der Methode kann, mit Einschränkungen, frei gewählt werden.
- Eine Methode von einem Objekt wird in den meisten Sprachen mit dem `.` aufgerufen: `<objekt>.<methode> 

## Methoden
- Methoden können Argumente haben:
  - primaryStage.setTitle("Ampelsteuerung");
- Mehrere Argumente werde durch Komma getrennt:
  - primaryStage.add(crossroadController, 1100, 900);
- Weniger Argumente sind übersichtlicher! (Faustregel: Max. 3)

## Ein Objekt hat eine Schnittstelle (Interface)
![w:1000px](Images/Interface.png)

## Ein Objekt hat eine Implementierung
![w:800px](Images/InterfaceImplementation.png)

# Abstraktion
- Ein Objekt kann verwendet werden, ohne die Implementierung der Methoden zu kennen.
- Die Implementierungsdetails sind abstrahiert

## Kapselung
- Grundsätzlich sind alle Felder (Daten) privat, d.h. nur für das eigene Objekt zugänglich.
- Diese Felder stellen den Zustand (State) des Objekts dar.
- Zugriff auf Felder wird mit Methoden gewährt (sogenannte Setter und Getter, z.B. setColor(), getSize()
- Es werden nur die nötigen Methoden zugänglich gemacht.
- Die Programmiersprache stellt den Zugriffsschutz sicher.

## Objektorientierung: Geschichte
- Untergruppe der imperativen Programmierung (Abfolge von Befehlen)
- Ursprung: Simula67, Oslo, 60er Jahre
- Kaum verbreitet in den 70er Jahren
- Smalltalk (Xerox PARC, 1970s) machte OOP Populärer

---

- Grosser Verbreitung in den 90er Jahren
- Die meisten heute verbreiteten Sprachen sind objektorientiert: Objective C, C++, Java, C#, Python, Kotlin, Go, JavaScript, uvm
- Heute das meistverbreitete Konzept der Softwareentwicklung
- Andere Programmierparadigmen:
  - Imperative Programmierung
    - Strukturierte Programmierung
    - Prozedurale Programmierung
  - Deklarative Programmierung
    - funktionale Programmierung

## Syntaktische Struktur einer Klasse
```
class Vehicle:                                 # Class Name
    def __init__(self, brand, model, type):    # Constructor
        self.brand = brand
        self.model = model
        self.type = type
        self.gas_tank_size = 14
        self.fuel_level = 0

    def fuel_up(self):                          # Method declaration
        self.fuel_level = self.gas_tank_size    # Method implementation
        print('Gas tank is now full.')

    def drive(self):
        print(f'The {self.model} is now driving.')

```

## Klasse
- Jedes Objekt gehört zu einer Klasse, welche die zur Verfügung stehenden Methoden und Felder definiert.
- Eine Klasse ist eine Beschreibung von Laufzeit-Objekten, welche dieselben Eigenschaften und Methoden besitzen.
- Eine Klasse ist eine Kategorie von Dingen
- Ein Objekt ist eines von diesen Dingen

## Objekte
Wenn ein Objekt O ein Objekt der Klasse C ist:
- O ist ein Exemplar von C
- O ist eine Instanz von C
![](Images/Baum.png)

## Objekte und Klassen
- Klassen existieren nur im Source Code
  - Bauplan für konkrete Objekte
- Objekte existieren nur zur Laufzeit

---

- Ein zentraler Aspekt der Softwareentwicklung ist das Bilden von sinnvollen Klassen für die Aufgabenstellung (Softwarearchitektur, OOD)
- Das Schreiben der Details wird Implementierung genannt.

## Interface (de: Schnittstelle)
- Die Schnittstelle (engl. interface) ist der Teil eines Systems, welcher der Kommunikation dient.
- Der Begriff stammt ursprünglich aus der Naturwissenschaft [...]. Er beschreibt bildhaft die Eigenschaft eines Systems als Black Box, von der nur die „Oberfläche“ sichtbar ist, und daher auch nur darüber eine Kommunikation möglich ist. [...]
- Daneben bedeutet das Wort „Zwischenschicht“: Für die beiden beteiligten Boxes ist es ohne Belang, wie die jeweils andere intern mit den Botschaften umgeht, und wie die Antworten darauf zustande kommen.

![w:100px](Images/HDMI_Interface.png)

## Interfaces
- User interface: Wenn die Clients Menschen sind
  - GUI: Graphical User Interface
  - Text interfaces, command line interfaces.
- Program interface: Wenn die Clients Software sind
  - API: Application Program Interface

## API
- Eine Schnittstelle gibt an, welche Methoden vorhanden sind oder vorhanden sein müssen.
- Zusätzlich zu dieser syntaktischen Definition sollten Vorbedingungen und Nachbedingungen der verschiedenen Methoden definiert werden.
- Heute werden dazu in der Regel automatisierte Tests geschrieben.
- Es kann auch in der Dokumentation festgehalten werden.

## Schnittstellen definieren
- Nicht jede Methode ist für jeden möglichen Parameter geeignet
- Lösungen:
  - immer: gute Wahl der Bezeichner
  - möglichst immer: Tests
  - Einschränkung durch Datentyp
  - wenn nötig: Kommentare: JavaDoc
  - falls erforderlich: Exceptions

## Javadoc
![w:800px](Images/Javadoc.png)

## UML Klassendiagramm
![](Images/class.png)
[PlantUML](https://www.plantuml.com/)

## UML Klassendiagramm
![](Images/classRelationsUML.png)

## PlantUML
```
@startuml
class Konto {
    bezeichnung
    saldo()
    einzahlen(betrag)
}

class Kunde {
}

class Privatkunde {
    vorname
    nachname
}

class Geschäftskunde {
    firmenname
}

class Adresse {
}

Kunde <|-- Privatkunde
Kunde <|-- Geschäftskunde

Privatkunde "0..*" -- "1" Adresse
Geschäftskunde "0..*" -- "1" Adresse

Konto "1..*" -- "1..*" Kunde
@enduml
```

# Moderne Softwareentwicklung

## Software Engineering
![Margareth Hamilton](Images/MargarethHamilton.png) ![Apollo Guidance Computer](Images/ApolloGuidance.png)

## Kundenorientierung
**Software soll den Kunden Mehrwert bringen**
- Software soll stabil laufen
- Neue Features sollten schnell umgesetzt und nutzbar sein
- Softwaresysteme werden immer komplexer

## Teamarbeit
- Mehrere Personen arbeiten am selben Softwareprojekt
- Versionsverwaltung wird verwendet (Git, SVN)
- Konflikte entstehen und sind aufwendig

## Lösungen
- Kleine Arbeitspakete iterativ und inkrementell
- Kurzer Feedbackloop
- Komplexität reduzieren
- Hohe Qualität

## Alles hängt zusammen
- Hohe Qualität reduziert Komplexität
- Hohe Qualität kürzt den Feedbackloop durch schnelle Entwicklung
- Kleine Arbeitspakete kürzen den Feedbackloop
- Kleine Arbeitspakete reduzieren Komplexität
- ...

## Manifesto for Agile Software Development
* Individuals and interactions over processes and tools
* Working software over comprehensive documentation
* Customer collaboration over contract negotiation
* Responding to change over following a plan

https://agilemanifesto.org/

## Iteratives und inkrementelles Arbeiten
![w:800px Mona Lisa](Images/MonaLisa.png)

## Iterationen
![Iterations](Images/Iterations.png)

## Kurzer Feedbackloop: CI/CD
![img.png](Images/CICD.png)

## CI / CD
- Ziel: Releases werden vereinfacht
- Time to market ist kürzer, neue Features sind sofort verfügbar
- Durch automatisierte deployments ist der Aufwand initial höher, anschliessend jedoch sehr klein
- Nur möglich mit automatisierten Tests

# Testing

## Kosten von Defekten
![w:800px Testing](Images/Testing.png)

## Kosten von Defekten
![w:800px Testing ideal](Images/Testing_ideal.png)

## Pair Programming
![Pair Programming](Images/PairProgramming.png)

## Test Driven Development (TDD)
Following 3 Drawings from Growing Object-Oriented Software by Nat Pryce and Steve Freeman.

---

![bg fit](Images/tdd-simple.svg)

---

![bg fit](Images/listening-to-tests.svg)

---

![bg fit](Images/tdd-with-acceptance-tests.svg)


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

## Testpyramide
![w: 800px Testpyramide](Images/Testpyramide.png)

---

![w:700px TestingPyramid](Images/TestingPyramid)

## Testing: AAA
- Arrange: Set up your data
- Act: Execute code under Test
- Assert: Verify that the result ist correct

## Testing: Further Reading
- [How to write clear and robust unit tests: the dos and don'ts](https://levelup.gitconnected.com/how-to-write-clear-and-robust-unit-tests-the-dos-and-donts-5021c097d041)
- [The Real Value of Testing](https://drpicox.medium.com/the-real-reason-to-do-testing-6f12b410dde3)


## Extreme Programming
![Extreme Programming](Images/ExtremeProgramming.png)

## Embrace Change
![EmbraceChange](Images/EmbraceChange.png)

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

## Record
- Einfachste Anordnung von Daten
- Zeile in Datenbank / Tabelle
- struct in C ![](Images/struct.png)
- Datenobjekte
- Python: `tup1 = ('physics', 'chemistry', 1997, 2000)`


## Set
- Anordnung von Elementen
- keine Duplikate
- keine definierte Ordnung
- testen, ob Teil des Sets
- Python: `thisset = {"apple", "banana", "cherry"}`

## List
- Definierte Ordnung
- Elemente hinzufügen und entfernen
- Element mit einem Index abrufen
- Duplikate möglich
- Python: 
  - `list2 = [1, 2, 3, 4, 5, 6, 7 ];`
  - Zugriff: `list1[0]`, `list1[1:5]`

## Map

- Schlüssel / Wert Paare
- Hinzufügen, Entfernen, Ändern, Abrufen
- Assiozatives Array, Lookup Table, Dictionary
- Python: Dictionaries (hash map)
  - Erstellen: `dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}`
  - Zugriff: `dict['Name']`

## Queue

- FIFO: First In, First Out
- Warteschlange, Pipe
![](Images/queue.png)

## Stack
- LIFO: Last In, First Out
- push: Neues Element speichern
- pop: Letztes Element abrufen und entfernen
- Stapelspeicher, Kellerspeicher
![](Images/stack.png)

## Stack

![](Images/ProgramStack.png)


## Tree
![](Images/Tree.png)

## Konkrete Datenstrukturen
- Array
- Graph

## Big O Natation

![](Images/BigO.png)

## Komplexität von Algorithmen
- O(1): Operation dauert immer gleich lange, unabhängig von der Anzahl der Elemente 
- O(n): Operation ist linear abhängig von der Anzahl der Elemenente (Je mehr Elemente in der Liste, desto länger dauert die Operation) 
- [Big O Cheatsheet](https://www.bigocheatsheet.com/)

## Speicher und Rechenaufwand
![img_1.png](Images/Complexity.png)

# Objektorientierte Prinzipien

## Vererbung
![](Images/Inheritance.png)

## Vererbung
- Generalisierung / Spezialisierung
- Polymorphismus
- Dynamisches Binden

## Vererbung

Eine Klasse ist ein Modul:
- Eine Sammlung von Funktionalität (Methoden)
- Kapselung (nicht alle Funktionalität ist sichtbar)

Eine Klasse ist ein Datentyp:
- Beschreibt die Art einer Objektinstanz
- Kann bei Variablen, Methoden oder Feldern verwendet werden

## Vererbung

- Eine neue Klasse kann als Erweiterung oder Spezialisierung einer existierenden Klasse beschrieben werden.
- `Bar` erbt von `Foo`
  - Modul: Alle Funktionalität von `Foo` steht in `Bar` zur Verfügung
  - Typ: Immer wenn eine Instanz von `Foo` benötigt wird, wird eine Instanz von `Bar` akzeptiert
- Oder umgekehrt: Eine neue Klasse kann eine existierende Klasse generalisieren

## Vererbung

![](Images/InheritanceUML.png)
```
@startuml
Foo : equals()
Bar : size()

Foo <|-- Bar
@enduml
```

## Vererbung: Terminologie

`Bar` erbt von `Foo`
- `Bar` ist eine Kindklasse/'child' von `Foo`
- `Bar` ist eine Unterklasse/'Subclass' von `Foo`
- `Bar` ist eine von `Foo` abgeleitete Klasse
- `Foo` ist die Elternklasse/'parent' von `Bar`
- `Foo` ist die 'superclass' von `Bar`
- `Foo` ist die 'base class' von `Bar`

## Vererbung in Python
```
class Robot:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hi, I am " + self.name)


class PhysicianRobot(Robot):
    def say_hi(self):
        print("Everything will be okay!")
        print(self.name + " takes care of you!")
        
r2d2 = Robot("r2d2")
james = PhysicianRobot("James")
james.say_hi()
r2d2.say_hi()
```

## Vererbung: Beispiel I
![img.png](Images/InheritanceExample.png)

## Vererbung: Beispiel II
![img.png](Images/InheritanceExample2.png)

## Liskovsches Substitutionsprinzip
"Subtype Requirement: Let ϕ ( x ) be a property provable about objects x of type T. Then ϕ ( y ) should be true for objects y of type S where S is a subtype of T."

S ist ein Untertyp von T. Ein Objekt des Typs S sollte sich, wo ein Objekt vom Typ T erwartet wird, gleich verhalten wie ein Objekt des Typs T.

## Polymorphismus

- Bis jetzt war bei einer Zuweisung der Ausdruck rechts immer vom gleichen Typ wie das Ziel links: `ziel = ausdruck`
- Mit Polymorphismus kann der Ausdruck rechts auch eine Unterklasse vom Typ des Ziels sein.
- Das gilt auch bei Argumenten von Methoden
- Variablen, Felder und Parameter von Methoden sollten möglichst einen allgemeinen Datentyp haben (Interface)

## Dynamisches Binden
Es können mehrere Methoden mit demselben Namen existieren:
- Durch Vererbung
- Durch verschiedene Methodensignaturen (unterschiedliche Anzahl oder Typen der Argumente)

Bei einem Methodenaufruf wird immer die bestgeeignete Methode ausgewählt.

## Bindung und Typen
Für einen Methodenaufruf `x.f()`:
- Statische Typisierung: Es gibt mindestens eine Version der Methode f
- Dynamische Typisierung: Während der Laufzeit wird geprüft ob f existiert
- Dynamische Bindung: Jeder Aufruf verwendet die best passende Version von f
→ Methode des Objekts, nicht des Typs

## Vererbung: Coupling
Durch Vererbung werden zwei Klassen sehr eng gekoppelt (coupling).
Sie sind dadurch stark voneinander abhängig. Das kann bei Änderungen zu Problemen führen.

## Vererbung: Zusammenfassung
- Datentypen können gruppiert und geordnet werden
- Neue Klassen können Bestehende erweitern
- Dynamisches Binden: Automatische Auswahl der korrekten Methode


# Grundlegende O-O Prinzipien

- Vererbung
- Polymorphismus
- Dynamische / statische Bindung
- Dynamische / statische Typisierung
- Generische Programmierung

# SOLID Principles

## Single Responsibility Principle
- "A module should be responsible to one, and only one, actor." The term actor refers to a group (consisting of one or more stakeholders or users) that requires a change in the module.
- "A class should have only one reason to change"
[wikipedia](https://en.wikipedia.org/wiki/Single-responsibility_principle)

## Open Closed Principle
"Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification."
[wikipedia](https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle)

## Liskov's Substitution Principle

## Interface Segregation Principle

# Clean Code
[https://cleancoders.com/](https://cleancoders.com/)
[Clean Code: A Handbook of Agile Software Craftsmanship](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882)

## Bezeichner

> There are only two hard things in Computer Science: cache invalidation and naming things.
-- Phil Karlton

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

# Design Patterns
Gang of Four:
Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides (1995): Design Patterns, Elements of Reusable Object-Oriented Software, Addison-Wesley

Fowler, Martin (2002): Patterns of Enterprise Application Architecture, Addison-Wesley

Hohpe, Gregor; Woolf, Bobby (2003): Enterprise Integration Patterns: Designing, Building, and Deploying Messaging Solutions, Addison-Wesley

## Observer
![w:400px](Images/observer_class_diagram.png) ![w:400px](Images/observer_sequence_diagram.png)

# Computer Hardware

## Moore's Law
![](Images/MooresLaw.png)

## Alan Touring
- *1912 - †1954
- Turing- maschine / Entscheidungsproblem
- Begründer der «Computer Science»
- WWII: Massgeblich am Knacken der deutschen Enigma Verschlüsselung beteiligt
- Turing Test
- Verfolgt und «therapiert» wegen Homosexualität
- Vermutlich Selbstmord
- The Imitation Game, Benedict Cumberbatch

## Turing Maschine
Die Turingmaschine hat ein Steuerwerk, in dem sich das Programm befindet, und besteht außerdem aus 
- einem unendlich langen Speicherband mit unendlich vielen sequentiell angeordneten Feldern.
- einem programmgesteuerten Lese- und Schreibkopf, der sich auf dem Speicherband feldweise bewegen und die Zeichen verändern kann.
- Turing bewies, dass solch ein Gerät in der Lage ist, „jedes vorstellbare mathematische Problem zu lösen, sofern dieses auch durch einen Algorithmus gelöst werden kann“. 

## Turing Vollständigkeit
«Exakt ausgedrückt bezeichnet Turing-Vollständigkeit in der Berechenbarkeitstheorie die Eigenschaft einer Programmiersprache oder eines anderen logischen Systems, sämtliche Funktionen berechnen zu können, die eine universelle Turingmaschine berechnen kann.» 
(https://de.wikipedia.org/wiki/Turing-Vollst%C3%A4ndigkeit)

## Halteproblem

- «Das Halteproblem beschreibt die Frage, ob die Ausführung eines Algorithmus zu einem Ende gelangt.
- Obwohl das für viele Algorithmen leicht beantwortet werden kann, konnte der Mathematiker Alan Turing beweisen, dass es keinen Algorithmus gibt, der diese Frage für alle möglichen Algorithmen und beliebige Eingaben beantwortet.»
- (https://de.wikipedia.org/wiki/Halteproblem)
- Wir Programmieren müssen sicherstellen, dass unsere Programme nicht unabsichtlich endlos weiterlaufen!

## Von-Neumann-Architektur
- Befehle werden aus einer Zelle des Speichers gelesen und dann ausgeführt.
- Normalerweise wird dann der Inhalt des Befehlszählers um Eins erhöht.
- Es gibt einen oder mehrere Sprung-Befehle, die den Inhalt des Befehlszählers um einen anderen Wert als +1 verändern.
- Es gibt einen oder mehrere Verzweigungs-Befehle, die in Abhängigkeit vom Wert eines Entscheidungs-Bit den Befehlszähler um Eins erhöhen oder einen Sprung-Befehl ausführen

## paralleler Bus

## Intel 4004, 1971
![](Intel4004.png)

## Arithmetic Logic Unit (ALU)
Mindestens:
- Addition
- Negation
- Konjunktion (AND)
Zusätzlich (Auwahl):
- Subtraktion
- Vergleich
- Multiplikationen
- Division
- Oder-Verknüpfung
- Exklusiv-Oder-Verknüpfung
- Rechts-, Linksshift
- Links- und Rechtsrotation- 

## ALU
![](Images/ALU.png)

## Einfache n-Bit ALU
![](Images/ALU2.png)
![](Images/ALU3.png)

## Carrie-Look-Ahead-Addierer
![](Images/Adder.png)

## CMOS Gatter
![](Images/Gates.png)

## Control Unit (CU)
![](Images/control_unit.png)

## AMD Zen 3
![img_1.png](Images/amd_zen_3.png)

## Apple M1
![img_2.png](Images/apple_m1.png)

## Maschinensprache (1. Generation)
![img_3.png](Images/Machine_Code.png)

## Assembler (2. Generation)
![img_4.png](Images/Assembler.png)

## statische Typisierung
- Zur Laufzeit hat jedes Objekt einen (Daten)typ
- Im Programmtext hat jeder Ausdruck einen Typ → Der Typ ist zum Zeitpunkt der Kompilierung bekannt
- Vorteile
  - Fehler können früher erkannt werden
  - Effizientere Programme, da keine Typprüfung während der Laufzeit
  - Mehr Optimierungsmöglichkeiten durch Compiler
- statisch typisierte Sprachen: Java, Kotlin, C#, C, Go, Rust
![](Images/staticTyping.png)

## dynamische Typisierung

- Zur Laufzeit hat jedes Objekt einen Typ
- Der Typ wird zur Laufzeit geprüft
- Duck Typing: 
- “When I see a bird that walks like a duck and swims like a duck and quacks like a duck, I call that bird a duck.” 
- Vorteile
  - Einfachere Programmierung
- Durch Typehints kann die IDE uns bei der Entwicklung dennoch unterstützen
  - `def greeting(name: str) -> str:`
- dynamisch typisierte Sprachen: PHP, Python, Ruby, JavaScript
