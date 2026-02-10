# Übung Modularität

## Kompetenzen

Die Studierenden können Architekturen entwerfen, die die Applikation in klar definierte Module gliedert, die in sich
hohe Kohäsion aufweisen ("Cohesion"), loose gekoppelt sind ("Coupling"), klare Zuständigkeiten haben ("Separation of
Concerns"), austauschbar und wartbar sind ("Modularität").

## Aufgaben

Untersucht, wie eure Applikation in Module strukturiert werden kann.

Module sollten klar definierte Zuständigkeiten (Separation of Concerns) und Grenzen haben (Cohesion) sowie möglichst
wenige und einfache Schnittstellen aufweisen (Loose Coupling, Abstraction) damit die einzelnen Module einfach
ausgetauscht und geändert werden können.

Folgende Fragen helfen bei der Modellierung:

- Welche Module sind vorhanden?
- Welche Abhängigkeiten bestehen zwischen den Modulen?
- Wie können die Module strukturiert werden, damit möglichst wenige Abhängigkeiten zwischen ihnen bestehen?
- Welche Zuständigkeiten sind vorhanden? Wie können diese gruppiert werden?

Untersucht, wie ihr dies erreichen könnt und haltet offene Fragen und Abwägungen fest. Dokumentiert die Struktur mit C4
Architekturdiagramme eurer Applikation. Verwendet dazu geeignete Werkzeuge (z.B. diagrams.net, PlantUML, Mermaid,
Papier).
Erstellt zuerst das System Context Diagram und anschliessend laufend die feineren Diagramme.

Stellt am Schluss die Architektur der Klasse mit einer Flipchart oder am Whiteboard vor.

## Siehe Auch

- [Domain Driven Design](DomainDrivenDesign.md) befasst sich extensiv mit der Modellierung von Software-Systemen
- ["Ports & Adapters"](PortsAndAdapters.md) ist eine Architektur mit der sich Systeme modular gestalten
  lassen.