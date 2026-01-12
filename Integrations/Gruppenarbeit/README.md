# Gruppenarbeit "Datenvernetzung in DB und Web"

Die Studierenden entwickeln eine REST-API für einen Datenstamm ihrer Wahl.

Es sollen für mindestens einen Datensatz sämtliche CRUD-Operationen (Create, Read, Update, Delete) implementiert werden.
Read soll auf der ganzen Collection und auf einzelnen Datensätzen möglich sein.

Die API soll die REST-Prinzipien vollständig umsetzen:

- **Zustandslosigkeit**: Es werden serverseitig keine Daten zwischen den Requests gespeichert.
- **Caching**: Cache Header werden korrekt gesetzt
- Uniform Interface
    - **Identification of Resources**
    - **Manipulation of Resources through Representations**: Die Daten sind in JSON verfügbar.
    - **Self-Descriptive Messages**: Korrekte Verwendung von HTTP-Methoden
    - **Hypermedia as the Engine of Application State:** Verwandte Ressourcen werden in den Daten verlinkt.

Die Daten sollen in einer relationalen Datenbank persistiert werden.

Mit automatisierten Tests soll das korrekte Funktionieren sichergestellt werden.

## Dokumentation

### Git-Repository und Code

Die Arbeit soll direkt im Git-Repository dokumentiert werden. Dazu soll eine Git-Plattform
wie [Github](https://github.com/), [Gitlab](https://gitlab.com/) oder
[Codeberg](https://codeberg.org/) verwendet werden.

### README

In einer Datei README.md im Wurzelverzeichnis werden folgende Punkte dokumentiert:

- Kurze Anleitung, wie die Applikation in Betrieb genommen wird
- Erläuterung, welche Anforderung die Applikation erfüllen soll und inwiefern diese erfüllt sind. Insbesondere soll auch
  erläutert werden, wie die REST-Prinzipien umgesetzt wurden.

### Verwendung von KI

Es gelten die Regeln zur [Verwendung von KI in Arbeiten](../../Readings/BerichteSchreiben/VerwendungVonKIinArbeiten.md).

## Abgabe

Per **E-Mail** wird ein **Link zu einem Git-Repo** geschickt. Wenn das Repository privat ist, muss der Dozent eingeladen
werden.

## Bewertungsraster

| Bewertungspunkte                                        | Punkte |
|---------------------------------------------------------|--------|
| REST: Zustandslosigkeit                                 | 5      |
| REST: Caching                                           | 5      |
| REST: Identification of Resources                       | 5      |
| REST: Manipulation of Resources through Representations | 5      |
| REST: Self-Descriptive Messages                         | 10     |
| REST: Hypermedia as the Engine of Application State     | 10     |
| Datenbank: Daten werden persistiert                     | 10     |
| Testing: API wird vollständig getestet                  | 10     |
| Vollständigkeit CRUD                                    | 10     |
| Dokumentation (README)                                  | 10     |