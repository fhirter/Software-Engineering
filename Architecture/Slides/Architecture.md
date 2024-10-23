<!-- headingDivider: 3 -->

# Einstieg

## Softwaredebakel

#### VBS

- [Schweizer Armee ohne krisensichere Logistik bis 2035](https://www.srf.ch/news/schweiz/militaerische-it-projekte-schweizer-armee-ohne-krisensichere-logistik-bis-2035)

- [Armee-Debakel: 300-Millionen-Projekt seit Monaten suspendiert](https://www.srf.ch/news/schweiz/neue-luftraumueberwachung-armee-debakel-300-millionen-projekt-seit-monaten-suspendiert)

#### Kantonsverwaltung
 
- [Wegen fehlerhafter Software braucht es mehr Haftplätze](https://www.srf.ch/news/schweiz/it-probleme-im-kanton-bern-wegen-fehlerhafter-software-braucht-es-mehr-haftplaetze)

#### Crowdstrike

- [Der Tag, an dem die IT weltweit verrückt spielte – ein Überblick](https://www.srf.ch/news/international/crowdstrike-softwarefehler-der-tag-an-dem-die-it-weltweit-verrueckt-spielte-ein-ueberblick)

## Kundenorientierung

**Software soll den Kunden Mehrwert bringen**

- Software soll stabil laufen
- Neue Features sollten schnell umgesetzt und nutzbar sein
- Softwaresysteme werden immer komplexer

## Teamarbeit

**Mehrere Personen arbeiten am selben Softwareprojekt**

- Versionsverwaltung wird verwendet (Git, SVN)
- Konflikte entstehen und sind aufwendig

## Ab 1961: Margaret Hamilton, Apollo Guidance Computer

![h:300px](Images/MargarethHamilton.png) ![w:400px](Images/ApolloGuidance.png)

## 2001: Manifesto for Agile Software Development

* Individuals and interactions over processes and tools
* Working software over comprehensive documentation
* Customer collaboration over contract negotiation
* Responding to change over following a plan

https://agilemanifesto.org/

## Software Engineering / Software Architecture

> Software engineering is the application of an empirical, scientific approach to finding efficient, economic solutions to practical problems in software

(Farley, 2022, S.4)

> The goal of software architecture is to minimize the human resources required to build and maintain the required system

(Martin, 2018)

Übergang zwischen Software Entwicklung und Software Architektur ist fliessend

## Learning

- Iteratives und inkrementelles Arbeiten
- Feedback
- Empirisches und experimentelles Arbeiten

(vgl. Farley, 2022, S.4)

## Managing Complexity

- Modularity & Separation of Concerns
- Cohesion & Coupling
- Abstraction

(vgl. Farley, 2022, S.5)

## Production Is Not Our Problem

- Softwareentwicklung ist meistens Kreativarbeit
- Die Herausforderung der "Produktion" existiert kaum

## Space X Starship

[How Not to Land an Orbital Rocket Booser, 2017](https://www.youtube.com/watch?v=bvim4rsNHkQ)
[WOW! Watch SpaceX Catch A Starship Booster In Air, 2024](https://www.youtube.com/watch?v=NpjLfUoiT_w)

Finanzierung: **ca 3 Mrd. Dollar**

Apollo-Programm: 1958 bis 1969, inflationsbereinigt: **163 Mrd. Dollar** (ohne Mercury und Gemini)

# Lernen

## Iteratives und inkrementelles Arbeiten

![w:800px Mona Lisa](Images/MonaLisa.png)

## Iterationen

![Iterations](Images/Iterations.png)

## Embrace Change

![EmbraceChange](Images/EmbraceChange.png)

### Extreme Programming

![Extreme Programming](Images/ExtremeProgramming.png)


## Feedback 

### CI/CD

![img.png](Images/CICD.png)

### Continuous Integration

- Kein Branching, alle Änderungen werden von allen Teammitgliedern mehrmals täglich in den Master Branch eingecheckt.
- Dieser Branch ist jederzeit lauffähig
- Dadurch werden die Releases vereinfachen
- Eine sehr hohe, automatische Testabdeckung ist zwingend

### Continuous Delivery

- Ziel: Releases werden vereinfacht
- Time to market ist kürzer, neue Features sind sofort verfügbar
- Durch automatisierte deployments ist der Aufwand initial höher, anschliessend jedoch sehr klein
- Higher quality
- Lower costs
- Better products
- Happier teams

### Principles

- Build quality in
- Work in small batches
- Computers perform repetitive tasks, people solve problems
- Relentlessly pursue continuous improvement
- Everyone is responsible

https://www.continuousdelivery.com/

[Modern Software Engineering](https://www.amazon.com/Modern-Software-Engineering-Discipline-Development/dp/0137314914)

### Deployment Pipelines

![w:800px](Images/Deployment_Pipeline_Tradeoffs.jpeg)
(Jez Humble, David Farley (2010): Continuous Delivery)

---

![w:800px](Images/Deployment_Pipeline.jpeg)
(Jez Humble, David Farley (2010): Continuous Delivery)

---

![w:1000px](Images/GitlabPipelines.png)

--- 

- [Youtube: Continous Delivery - Deployment Pipelines](https://www.youtube.com/watch?v=x9l6yw1PFbs&list=PLwLLcwQlnXBzhxIXSbtDPX78zYTgvST0B)
- Jez Humble, David Farley (2010): Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment
  Automation, Addison-Wesley Signature Series (Fowler)


## Empirisches und experimentelles Arbeiten

## Domain Driven Design

# Kommunikation

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

## C4 Model

![img.png](Images/C4Overview.png)
https://c4model.com/

----

![img.png](Images/C4-overview.png)

----

![img.png](Images/C4Abstractions.png)

# Komplexität

## Modularity & Separation of Concerns

## Cohesion & Coupling

![img_1.png](Images/High_cohesion_loose_coupling.png)

## Abstraction

## Testing

### Kosten von Defekten

![cost_of_defects.svg](Images/cost_of_defects.svg)

### Pair Programming

![Pair Programming](Images/PairProgramming.png)

### Test Driven Development (TDD)

- Test First: Fokus auf die Problemstellung und Schnittstelle
- Nur eigenen Code testen. Datenbanken, APIs oder Libraries werden nur im Rahmen von Integrationstests aufgerufen.
- Tests geben eine Rückmeldung zum Code: Wenn Code schwierig zu testen ist, sollte er vermutlich anders strukturiert
  werden.
- [Humble Object](https://martinfowler.com/bliki/HumbleObject.html): Code, der schwierig zu testen ist in einem
  minimalen Objekt isolieren

---

![bg fit](Images/tdd-simple.svg)

---

![bg fit](Images/listening-to-tests.svg)

---

![bg fit](Images/tdd-with-acceptance-tests.svg)

---

Drei Abbildungen aus: Growing Object-Oriented Software by Nat Pryce and Steve Freeman

### Testpyramide

![TestPyramid.svg](Images/TestPyramid.svg)

### Testing: AAA

- Arrange: Set up your data
- Act: Execute code under Test
- Assert: Verify that the result ist correct

### IDE Integration

![height:500px](Images/TestRunner.png)

### Testing: Further Reading

- [How to write clear and robust unit tests: the dos and don'ts](https://levelup.gitconnected.com/how-to-write-clear-and-robust-unit-tests-the-dos-and-donts-5021c097d041)
- [The Real Value of Testing](https://drpicox.medium.com/the-real-reason-to-do-testing-6f12b410dde3)

### Why Should You Refactor?

* Refactoring Improves the Design of Software
* Refactoring Makes Software Easier to Understand
* Refactoring Helps You Find Bugs
* Refactoring Helps You Program Faster

### When Should You Refactor?

* [The Rule of Three](https://en.wikipedia.org/wiki/Rule_of_three_(computer_programming))
* Refactor When You Add Functionality
* Refactor When You Need to Fix a Bug
* Refactor As You Do a Code Review

## Architekturen


### Schichtenarchitektur

![w:600px](Images/LayeredArchitecture.svg)

### Ports and Adapters

![w:500px](Images/ports-and-adapters-architecture.svg)
[growing-object-oriented-software.com](https://www.martinfowler.com/microservices/)

### Traditional Monolithic Design

![](Images/traditional_monolithic_design.png)

### Schichtenarchitektur im Client Server Modell

![](Images/client_server_II.png)

### Microservices

![img_2.png](../../Slides/Images/microservices.png)
[martinfowler.com/articles/microservices.html](https://www.martinfowler.com/articles/microservices.html)

### Microservices

- Maximale Skalierbarkeit
- Einzelne Services können von **kleinen[^1]** Teams **unabhängig entwickelt und deployed** werden
- Bessere Wart- und Erweiterbarkeit
- Unterschiedliche Technologien können eingesetzt werden
- Kommunikation nicht trivial
- Höhere Wahrscheinlichkeit eines Ausfalls
- **Hohe Komplexität**

[^1]: ["We try to create teams that are no larger than can be fed by two pizzas"](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/two-pizza-teams.html)

### Monolith First

- Vorsicht vor [Cargo-Kult](https://de.wikipedia.org/wiki/Cargo-Kult): Amazon, Google, Meta etc. haben heute andere
  Herausforderungen als Startups
- Technologien oder Architekturen wählen, "weil Google macht das auch so" ist ein schlechter Grund
  ![w:600px](Images/route_to_microservices.png)
  [martinfowler.com/bliki/MonolithFirst.html](https://www.martinfowler.com/bliki/MonolithFirst.html)

# Quellen

Farley, 2022
: David Farley (2022): Modern Software Engineering: Doing What Works to Build Better Software Faster, Addison-Wesley

Martin, 2018
: Robert C. Martin (2018): Clean Architecture: A Craftman's Guide to Software Structure and Design, Prentice Hall
