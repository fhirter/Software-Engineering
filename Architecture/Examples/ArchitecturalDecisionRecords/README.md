# Architecture Decision Records (ADR)

## Tooling

Für diese Beispiele wurde das CLI Programm "adr-tools" verwendet: https://github.com/npryce/adr-tools

Das Verzeichnis wurde mit

```bash
adr init .
```

initialisiert. Dabei wurde der erste ADR automatisch erstellt.

Neue ADRs können mit

```bash
adr new Beschreibung des Entscheides
```

erstellt werden. Anstelle von "Beschreibung des Entscheides" kann ein beliebiger Text verwendet werden.

Um eine Entscheidung, die in einem ADR festgehalten wurde zu ändern wird ein neuer ADR erstellt und der alte mit `–s`
referenziert.
Mit dem folgenden Befehl wird zum Beispiel ADR Nr 9 ersetzt.

```bash
adr new -s 9 Use Rust for performance-critical functionality
```

## Beispiele

Folgende ADRs entstammen einem echten Projekt und dienen hier als Beispiel:

* [1. Record architecture decisions](0001-record-architecture-decisions.md)
* [2. Use Svelte as Frontend Framework](0002-use-svelte-as-frontend-framework.md)
* [3. Use Go as Backend Language](0003-use-go-as-backend-language.md)
* [4. Use Event Sourcing](0004-use-event-sourcing.md)
* [5. define aggregate roots](0005-define-aggregate-roots.md)
* [6. use cloudevents specification](0006-use-cloudevents-specification.md)
* [7. There Can Only Be One Board at a Time](0007-there-can-only-be-one-board-at-a-time.md)
* [8. A Shipment Must Be Completed During One Day](0008-a-shipment-must-be-completed-during-one-day.md)
* [9. Use Google Cloud Run Container Runtime](0009-use-google-cloud-run-container-runtime.md)
* [10. Use Node.js as Backend Language](0010-use-node-js-as-backend-language.md)

## Inhalt

Wie in den Beispielen ersichtlich müssen ADRs nicht besonders ausführlich sein. Eine knappe Dokumentation ist besser
als keine Dokumentation.

In meinen Projekten halte ich ADRs sehr schlank. Weitere Recherche und Dokumentation halte ich in separaten Dokumenten
fest.
