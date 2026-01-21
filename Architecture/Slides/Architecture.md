---
headingDivider: 3
auto-scaling: true
paginate: true
---

# Einstieg

## Internet of Bugs

![w:250px](Images/InternetOfBugs/84464E30-422B-4395-8D63-F728C9A6F549.jpg)![w:250px](Images/InternetOfBugs/Bildschirmfoto%202025-03-04%20um%2009.39.23.png)![w:250px](Images/InternetOfBugs/Bildschirmfoto%202025-03-26%20um%2012.08.26.png)![w:300px](Images/InternetOfBugs/C8BDE622-6528-44EF-A0C4-798622164ACC.jpg)![w:250px](Images/InternetOfBugs/IMG_0276.JPG)![w:250px](Images/InternetOfBugs/IMG_0491.PNG)![w:250px](Images/InternetOfBugs/IMG_0492.JPG)![w:250px](Images/InternetOfBugs/IMG_0531.JPG)![w:250px](Images/InternetOfBugs/IMG_0660.JPG)![w:250px](Images/InternetOfBugs/IMG_0707.JPG)![w:250px](Images/InternetOfBugs/IMG_0790.JPG)![w:250px](Images/InternetOfBugs/IMG_0912.JPG)

---

![w:250px](Images/InternetOfBugs/IMG_1218.jpg)![w:250px](Images/InternetOfBugs/Screenshot%202025-07-09%20at%2021.48.17.png)![w:250px](Images/InternetOfBugs/Screenshot%202025-07-17%20at%2011.21.25.png)
![w:600px](Images/InternetOfBugs/Bildschirmfoto%202025-09-30%20um%2012.11.11.png)

---

- EJPD:
  [Kostenexplosion bei IT-Projekt: Finanzdelegation schlägt Alarm](https://www.srf.ch/news/schweiz/departement-von-beat-jans-kostenexplosion-bei-it-projekt-finanzdelegation-schlaegt-alarm)
- VBS:
  [Schweizer Armee ohne krisensichere Logistik bis 2035](https://www.srf.ch/news/schweiz/militaerische-it-projekte-schweizer-armee-ohne-krisensichere-logistik-bis-2035),
- [Armee-Debakel:300-Millionen-Projekt seit Monaten suspendiert](https://www.srf.ch/news/schweiz/neue-luftraumueberwachung-armee-debakel-300-millionen-projekt-seit-monaten-suspendiert)
- Kantonsverwaltung:
  [Wegen fehlerhafter Software braucht es mehr Haftplätze](https://www.srf.ch/news/schweiz/it-probleme-im-kanton-bern-wegen-fehlerhafter-software-braucht-es-mehr-haftplaetze)
- Polizei:
  [Berner Polizisten beklagen sich über die neue IT](https://www.inside-it.ch/berner-polizisten-beklagen-sich-ueber-die-neue-it-20220722)

### Crowdstrike

![h:400px](Images/Crowdstrike.png)

-- https://www.srf.ch/news/international/crowdstrike-softwarefehler-der-tag-an-dem-die-it-weltweit-verrueckt-spielte-ein-ueberblick

### Google

![h:400px](Images/GCP_Outage.png)

https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW

### AWS 20.10.25

> Between **11:49 PM** PDT on October 19 and 2:24 AM PDT on October 20, we experienced increased error rates and
> latencies for AWS Services in the **US-EAST-1** Region.
> Additionally, services or features that rely on US-EAST-1 endpoints such as **IAM and DynamoDB** Global Tables also
> experienced issues during this time.
> At 12:26 AM on October 20, we identified the trigger of the event as **DNS resolution** issues for the regional
> DynamoDB service endpoints. [...]
> As we continued to work through EC2 instance launch impairments,[...] connectivity issues in multiple services such as
**Lambda, DynamoDB, and CloudWatch**.  [...]
> By **3:01 PM**, all AWS services returned to normal operations. [...]

-- https://health.aws.amazon.com/health/status

---

![h:500px](Images/GitClearStudy.png)

-- https://www.gitclear.com/ai_assistant_code_quality_2025_research

## Ab 1961: Margaret Hamilton, Apollo Guidance Computer

![h:300px](Images/MargarethHamilton.png) ![h:300px](Images/ApolloGuidance.png)

> “I remember thinking, Oh my God, it worked,” the pioneering software engineer tells TIME. “I was so happy. But I was
> more happy about it working than about the fact that we landed.”

-- https://time.com/3948364/moon-landing-apollo-11-margaret-hamilton/

## Anforderungen an (moderne) Software

> - the problems of achieving sufficient reliability in the data systems which are becoming increasingly integrated into
    the central activities of modern society
> - the difficulties of meeting schedules and specifications on large software projects
> - the education of software (or data systems) engineers

-- SOFTWARE ENGINEERING, Report on a conference sponsored by the NATO SCIENCE COMMITTEE, Garmisch, Germany, 7th to 11th
October 1968 http://homepages.cs.ncl.ac.uk/brian.randell/NATO/nato1968.PDF

## Agiles Manifest

* **Individuals and interactions** over processes and tools
* **Working software** over comprehensive documentation
* **Customer collaboration** over contract negotiation
* **Responding to change** over following a plan

2001, https://agilemanifesto.org/

## Anforderungen an Software

**Software soll den Kunden Mehrwert bringen**

- Software soll zuverlässig sein
- Neue Features sollten schnell umgesetzt und nutzbar sein

### Zuverlässigkeit

- Hohe Verfügbarkeit
- Skalierbarkeit
- Im Katastrophenfall sollen die Systeme schnell wiederhergestellt werden können
- Soll funktionieren, auch wenn Teile des Systems Offline sind (Resilienz)
- Kostengünstig
- Einfach
- Updates müssen einfach eingespielt werden können

## Softwarekrise

**Softwaresysteme werden immer komplexer**

> “[The major cause of the software crisis is] that the machines have become several orders of magnitude more powerful!
> To put it quite bluntly: as long as there were no machines, programming was no problem at all; when we had a few weak
> computers, programming became a mild problem, and now we have gigantic computers, programming has become an equally
> gigantic problem.”

-- Edsger Dijkstra: The Humble Programmer https://www.cs.utexas.edu/~EWD/ewd03xx/EWD340.PDF, 1972

## Software Engineering vs Software Architecture vs Software Development

> Software engineering is the application of an empirical, scientific approach to finding efficient, economic solutions
> to practical problems in software

(Farley, 2022, S.4)

> The goal of software architecture is to minimize the human resources required to build and maintain the required
> system

(Martin, 2018)

- Übergang zwischen Software Entwicklung, Software Architektur und Softwareentwicklung ist fliessend.
- Grundsätzlich sollen alle Beteiligten in allen Bereichen bewandert sein.

## Kommunikation

**Mehrere Personen arbeiten am selben Softwareprojekt**

- Fachkräftemangel
- Ausbildung ist sehr herausfordernd
- Wissenstransfer

## Lernen

- Iteratives und inkrementelles Arbeiten
- Feedback
- Empirisches und experimentelles Arbeiten

(vgl. Farley, 2022, S.4)

## Komplexität "managen"

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

# Generative KI

- LLMs können inherent nur durchschnittliche Antworten generieren
- Je nach Fragestellung kann das hilfreich sein oder auch nicht
- Längere generierte Texte scheinen oft auf den ersten Blick sehr gut, bei genauerer Betrachtung aber inhaltsleer,
  inkorrekt und übermässig umfangreich.
- Offensichtlich generierte Texte stossen beim Empfänger oft auf starke Ablehnung.
- Datenschutztechnisch ist die Verwendung von LLMs sehr heikel.

## in der Software-Entwicklung

- Die Kontextfenster sind oft zu klein für Software-Architektur.
- Bei Code werden oft Features implementiert, die nicht gefragt wurden oder übermässig komplizierte Lösungen entworfen.
- Der Nutzen durch die schnelle Code-Generierung wird durch längeres Debugging und Refactoring oft zunichtegemacht.
- Diskutieren von Architekturideen kann sehr hilfreich sein.

## in der Bildung

- Wenn die inhaltliche Korrektheit wichtig ist (was sehr oft der Fall ist), muss der KI-Output vollständig überprüft
  werden.
- Voraussetzung dafür ist ein vollständiges Verstehen des Inhalts.
- In der Ausbildung ist dies meistens nicht der Fall.
- Der Lerneffekt ist gering, echtes Verständnis entsteht, wenn man sich intensiv mit einer Materie auseinandersetzt.
- Um auf dem Arbeitsmarkt erfolgreich zu sein, ist kritisches Denken essenziell.
- Ein Studium ist das ideale Umfeld, dies zu lernen.

vgl. https://www.golem.de/news/produktivitaetssabotage-ki-muell-kostet-unternehmen-millionen-2509-200417.html

## Konkrete Empfehlungen

- KI verwenden für:
    - Analyse von Dokumenten(-sammlungen)
    - Boilerplate-Code
    - Formulierungen und Textkorrektur
    - Entwurf von Lösungsstrategien
- KI nicht verwenden für:
    - Schreiben von ganzen Dokumenten, Arbeiten, E-Mails
    - Schreiben von ganzen Funktionen und Klassen
    - Entwurf von ganzen Architekturen



# Kommunikation

## UML Klassendiagramm

![](Images/class.png)
[PlantUML](https://www.plantuml.com/)

---

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

- Ähnlich wie verschiedene Zoom-Stufen einer Landkarte werden Diagramme mit unterschiedlichem Umfang erstellt:
    - System Context
    - Container
    - Component
    - Code
- Die ersten beiden Diagramme (System Context, Container) sind dabei die wichtigsten, da diese Informationen enthalten,
  die schwer im Code sichtbar sind
- Component und Code Diagramme sind eher selten nötig, da Information, die gut aus dem Code gelesen werden kann dupliziert
  wird.

https://c4model.com/

---

![](Images/C4Overview.png)


### System Context

![w:600px](Images/SystemContext.png)

https://c4model.com/diagrams/system-context

### Container Diagram

![w:600px](Images/Container.png)

### Component Diagram

![w:600px](Images/Component.png)

### Code Diagram

![w:600px](Images/Code.png)

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

- Nygard:
  https://github.com/joelparkerhenderson/architecture-decision-record/blob/main/locales/en/templates/decision-record-template-by-michael-nygard/index.md
- MADR: https://github.com/adr/madr/blob/4.0.0/template/adr-template.md

### Tools

- https://github.com/npryce/adr-tools
- https://github.com/opinionated-digital-center/pyadr


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

![w:800px](Images/Pipeline.png)

---

![w:800px](Images/Deployment_Pipeline_Tradeoffs.jpeg)

(Jez Humble, David Farley (2010): Continuous Delivery)

---

![w:1000px](Images/GitlabPipelines.png)

### Kubernetes

![img.png](Images/Kubernetes.png)

([Wikipedia](https://de.wikipedia.org/wiki/Kubernetes#/media/Datei:Kubernetes.png))

---

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx:1.14.2
          ports:
            - containerPort: 80
```

(https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)

### Quellen

- [Youtube: Continous Delivery - Deployment Pipelines](https://www.youtube.com/watch?v=x9l6yw1PFbs&list=PLwLLcwQlnXBzhxIXSbtDPX78zYTgvST0B)
- Jez Humble, David Farley (2010): Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment
  Automation, Addison-Wesley Signature Series (Fowler)

## Empirisches und experimentelles Arbeiten

> Rule 1. You can't tell where a program is going to spend its time. Bottlenecks occur in surprising places, so don't
> try to second guess and put in a speed hack until you've proven that's where the bottleneck is.
>
> Rule 2. Measure. Don't tune for speed until you've measured, and even then don't unless one part of the code
> overwhelms the rest.
>
> Rule 3. Fancy algorithms are slow when n is small, and n is usually small. Fancy algorithms have big constants.
> Until you know that n is frequently going to be big, don't get fancy. (Even if n does get big, use Rule 2 first.)
>
> Rule 4. Fancy algorithms are buggier than simple ones, and they're much harder to implement. Use simple algorithms
> as well as simple data structures.
>
-- Rob Pike http://www.catb.org/~esr/writings/taoup/html/ch01s06.html

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

# Quellen

Farley, 2022
: David Farley (2022): Modern Software Engineering: Doing What Works to Build Better Software Faster, Addison-Wesley

Martin, 2018
: Robert C. Martin (2018): Clean Architecture: A Craftman's Guide to Software Structure and Design, Prentice Hall

Richards, 2021
: Mark Richards, Neal Ford (2021): Handbuch moderner Softwarearchitektur: Architekturstile, Patterns und Best Practices,
O'Reilly, 978-3-96009-149-3
