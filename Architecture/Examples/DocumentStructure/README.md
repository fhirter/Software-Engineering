# Projektstruktur

In diesem Ordner ist beispielhaft eine Projektstruktur abgelegt und hier erläutert.

## Dokumentation

- `README.md`: Übersicht über das Projekt, erster Einstiegspunkt
- `LICENCE.md`: Lizenz des Projekts, z.B. GPL, MIT oder Apache

Im Ordner `/docs` wird sämtliche weitere Dokumentation abgelegt.

## Konfiguration

> `.gitignore`, `eslint.config.js`, `.dockerignore`, `jest.config.js`

Zahlreiche config files definieren die unterschiedlichen Tools für Versionsverwaltung, Linting, Testing etc.

## Build & Deployment

- `.gitlab-ci.yml`: Definition der Gitlab Build Pipeline
- `Dockerfile`: Build Anleitung für ein Docker-Image
- `package.json`, `package-lock.json`: Auflistung der verwendeten Node Pakete

## Render & build outputs

> `/dist`, `/build`, `/coverage`, 

Verschiedene build tools generieren Output der in diesen Ordnern abgelegt wird.
In `/dist` oder `/build` wird die Applikation nach dem build abgelegt.
In `/coverage` wird der coverage report der Testa abgelegt.
`/node_modules` enthält den Quellcode der Node Pakete.

Diese Ordner werden in der Regel nicht in git verwaltet und sind dazu in `.gitignore` erfasst.

## Source Code

> `/src`

Hier ist der eigentliche Quellcode der Applikation abgelegt.
