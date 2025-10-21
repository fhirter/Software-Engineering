# Gruppenarbeit "Datenvernetzung in DB und Web"

Die Studierenden entwickeln eine REST-API für einen Datenstamm ihrer Wahl.

Es sollen für mindestens einen Datensatz sämtliche CRUD-Operationen (Create, Read, Update, Delete) implementiert werden.
Read soll auf der ganzen Collection und auf einzelnen Datensätzen möglich sein.

Die API soll die REST-Prinzipien vollständig umsetzen:

- **Zustandslosigkeit**
- **Caching**: Cache Header werden korrekt gesetzt
- Uniform Interface
    - **Identification of Resources**
    - **Manipulation of Resources through Representations**: Die Daten sind in JSON und XML verfügbar.
    - **Self-Descriptive Messages**: Korrekte Verwendung von HTTP-Methoden
    - **Hypermedia as the Engine of Application State:** Verwandte Ressourcen werden in den Daten verlinkt.

## Dokumentation

### Git-Repository und Code

Die Arbeit soll direkt im Git-Repository dokumentiert werden. Dazu soll eine Git-Plattform
wie [Github](https://github.com/), [Gitlab](https://gitlab.com/) oder
[Codeberg](https://codeberg.org/) verwendet werden.

Die einzelnen Commits sollen atomar sein, also jeweils nur eine kleine Änderung beinhalten und mit verständlichen
Commit-Messages versehen sein.

Der Code soll klar strukturiert und verständlich sein.

### README

In einer Datei README.md im Wurzelverzeichnis werden folgende Punkte dokumentiert:

- Kurze Anleitung, wie die Applikation in Betrieb genommen wird
- Erläuterung, welche Anforderung die Applikation erfüllen soll und inwiefern diese erfüllt sind. Insbesondere soll auch
  erläutert werden, wie die REST-Prinzipien umgesetzt wurden.

### Verwendung von KI

Es gelten die Regeln zur [Verwendung von KI in Arbeiten](../../VerwendungVonKIinArbeiten.md).

## Abgabe

Per **E-Mail** wird ein **Link zu einem Git-Repo** geschickt. Wenn das Repository privat ist, muss der Dozent eingeladen
werden.

## Bewertungsraster

| Bewertungspunkte                                        | Punkte |
|---------------------------------------------------------|--------|
| REST: Zustandslosigkeit                                 | 5      |
| REST: Caching                                           | 5      |
| REST: Identification of Resources                       | 5      |
| REST: Manipulation of Resources through Representations | 10     |
| REST: Self-Descriptive Messages                         | 10     |
| REST: Hypermedia as the Engine of Application State     | 10     |
| Vollständigkeit CRUD                                    | 10     |
| Verständlichkeit Code und Commit-Messages               | 10     |
| Dokumentation (README)                                  | 10     |