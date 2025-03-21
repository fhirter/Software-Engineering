---
headingDivider: 3
auto-scaling: true
paginate: true
---

# Einstieg

## Softwaredebakel

#### VBS

- [Schweizer Armee ohne krisensichere Logistik bis 2035](https://www.srf.ch/news/schweiz/militaerische-it-projekte-schweizer-armee-ohne-krisensichere-logistik-bis-2035)

- [Armee-Debakel: 300-Millionen-Projekt seit Monaten suspendiert](https://www.srf.ch/news/schweiz/neue-luftraumueberwachung-armee-debakel-300-millionen-projekt-seit-monaten-suspendiert)

#### Kantonsverwaltung

- [Wegen fehlerhafter Software braucht es mehr Haftplätze](https://www.srf.ch/news/schweiz/it-probleme-im-kanton-bern-wegen-fehlerhafter-software-braucht-es-mehr-haftplaetze)

#### Polizei

- [Berner Polizisten beklagen sich über die neue IT](https://www.inside-it.ch/berner-polizisten-beklagen-sich-ueber-die-neue-it-20220722)

#### Crowdstrike

- [Der Tag, an dem die IT weltweit verrückt spielte – ein Überblick](https://www.srf.ch/news/international/crowdstrike-softwarefehler-der-tag-an-dem-die-it-weltweit-verrueckt-spielte-ein-ueberblick)

## Kundenorientierung

**Software soll den Kunden Mehrwert bringen**

- Software soll stabil laufen
- Neue Features sollten schnell umgesetzt und nutzbar sein
- Softwaresysteme werden immer komplexer

---

![w:1000px](Images/when-the-cloud-leaves-the-datacenter-530836-1.jpg){ width=50% }

## Anforderungen an moderne Software

---

- Hohe Verfügbarkeit
- Skalierbarkeit
- Im Katastrophenfall sollen die Systeme schnell wiederhergestellt werden können
- Soll funktionieren, auch wenn Teile des Systems Offline sind (Resilienz)
- Kostengünstig
- Einfach
- Updates müssen einfach eingespielt werden können

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

> Software engineering is the application of an empirical, scientific approach to finding efficient, economic solutions
> to practical problems in software

(Farley, 2022, S.4)

> The goal of software architecture is to minimize the human resources required to build and maintain the required
> system

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

![w:500px](Images/Wissenspiramide.png)

(Richards, 2021, S.29)

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

- **Kein Branching**, alle Änderungen werden von allen Teammitgliedern **mehrmals täglich
  ** in den Master Branch eingecheckt.
- Dieser Branch ist **jederzeit lauffähig**
- Dadurch werden die **Releases vereinfacht**
- Eine sehr hohe, **automatische Testabdeckung** ist zwingend

### Continuous Deployment

- Ziel: **Releases werden vereinfacht**
- **Time to market ist kürzer**, neue Features sind sofort verfügbar
- Durch automatisierte Deployments ist der Aufwand initial höher, anschliessend jedoch sehr klein
- **Higher quality**, **Better products**
- Kaum mehr Release-Stress, **Happier teams**

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

# Kommunikation

## Domain Driven Design

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

## Architectural Decision Records

```markdown
# <!-- short title, representative of solved problem and found solution -->

## Context and Problem Statement

## Considered Options

## Decision Outcome

### Consequences
```

- https://github.com/adr/madr/blob/4.0.0/template/adr-template-bare-minimal.md
- https://github.com/adr/madr/blob/4.0.0/template/adr-template-bare.md

### Templates

- Nygard: https://github.com/joelparkerhenderson/architecture-decision-record/blob/main/locales/en/templates/decision-record-template-by-michael-nygard/index.md
- MADR: https://github.com/adr/madr/blob/4.0.0/template/adr-template.md

### Tools

- https://github.com/npryce/adr-tools
- https://github.com/opinionated-digital-center/pyadr

# Komplexität

## Modularity & Separation of Concerns

## Testing

> The hardest single part of building a software system is deciding precisely what to build.

– Fred Brooks, The mythical man-month

---

![w:800px](Images/BDD.png)
https://cucumber.io/docs/bdd/

## Cohesion & Coupling

![img_1.png](Images/High_cohesion_loose_coupling.png)

## Abstraction

# Architekturen

## Schichtenarchitektur

![w:400px](Images/LayeredArchitecture.svg)

## Ports and Adapters

![w:500px](Images/ports-and-adapters-architecture.svg)
[growing-object-oriented-software.com](https://www.martinfowler.com/microservices/)

## Traditional Monolithic Design

![](Images/traditional_monolithic_design.png)

## Schichtenarchitektur im Client Server Modell

![w:1000px](Images/client_server_II.png)

## Microservices

- Maximale Skalierbarkeit
- Einzelne Services können von **kleinen[^1]** Teams **unabhängig entwickelt und deployed** werden
- Bessere Wart- und Erweiterbarkeit
- Unterschiedliche Technologien können eingesetzt werden
- Kommunikation nicht trivial
- Höhere Wahrscheinlichkeit eines Ausfalls
- **Hohe Komplexität**

[martinfowler.com/articles/microservices.html](https://www.martinfowler.com/articles/microservices.html)
[^1]: ["We try to create teams that are no larger than can be fed by two pizzas"](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/two-pizza-teams.html)

## Monolith First

- Vorsicht vor [Cargo-Kult](https://de.wikipedia.org/wiki/Cargo-Kult): Amazon, Google, Meta etc. haben heute andere
  Herausforderungen als Startups
- Technologien oder Architekturen wählen, "weil Google macht das auch so" ist ein schlechter Grund
  ![w:500px](Images/route_to_microservices.png)
  [martinfowler.com/bliki/MonolithFirst.html](https://www.martinfowler.com/bliki/MonolithFirst.html)

## Event Driven Architecture

## Reactive Systems

![w:1000px](Images/reactive-traits.svg)

## Fallstudie

![w:1000px](Images/CaseStudyDashboard.png)

# Cloud Computing

> The entire history of software engineering is that of the rise in levels of abstraction.

-- Grady Booch

---

![w:800px](Images/PizzaAsAService.png)

## Abstractions

![w:1000px](Images/Abstractions.png)
(VanSteen, 2017, S. 30)

## XaaS

![w:1000px](Images/XaaS.png)

## What is a Cloud Native application?

A "cloud native" application, like all native species, has adapted and evolved to be maximally efficient in its
environment: the cloud.

The cloud is a harsher environment for applications than those of the past, in particular, than the idealistic
environment of a dedicated single node system.

In the cloud, an application becomes distributed. Thus, it is forced to be resilient to hardware/network
unpredictability and unreliability, i.e., from varying performance to all-out failure.

https://www.reactiveprinciples.org/cloud-native/index.html

---

The bad news is that ensuring responsiveness and reliability in this harsh environment is difficult.

The good news is that the applications we build after embracing this environment better match how the real world
actually works.

This in turn, provides better experiences for our users, whether humans or software.

https://www.reactiveprinciples.org/cloud-native/index.html

---

The constraints of the cloud environment, that make up the "cloud operating model," include:

- Applications are limited in the ability to scale vertically on commodity hardware which typically leads to having many
  isolated autonomous services (often called microservices).
- All inter-service communication takes place over unreliable networks.
- You must operate under the assumption that the underlying hardware can fail or be restarted or moved at any time.
- The services need to be able to detect and manage failure of their peers—including partial failures.
- Strong consistency and transactions are expensive. Because of the coordination required, it is difficult to make
  services that manage data available, performant, and scalable.

---

Therefore, a Cloud Native application is designed to leverage the cloud operating model. 

It is predictable, decoupled from the infrastructure, right-sized for capacity, and enables tight collaboration 
between development and operations.

It can be decomposed into loosely-coupled, independently-operating services that are resilient from failures, driven by
data, and operate intelligently across geographic regions.

---

While Cloud Native applications always have a clean separation of state and compute, there are two major classes of
Cloud Native applications: stateful and stateless.

Each class addresses and excels in a different set of use-cases;
non-trivial modern Cloud Native applications are usually a combination and composition of the two.

# Quellen

Farley, 2022
: David Farley (2022): Modern Software Engineering: Doing What Works to Build Better Software Faster, Addison-Wesley

Martin, 2018
: Robert C. Martin (2018): Clean Architecture: A Craftman's Guide to Software Structure and Design, Prentice Hall

Richards, 2021
: Mark Richards, Neal Ford (2021): Handbuch moderner Softwarearchitektur: Architekturstile, Patterns und Best Practices,
O'Reilly, 978-3-96009-149-3
