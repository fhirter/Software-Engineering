# Model View Controller

## Theorie
Schaue das Video "Model View Controller" auf Vimeo (bis 18:52). 
Lies den Abschnitt ["Humble View"](https://martinfowler.com/eaaDev/uiArchs.html#HumbleView).

Notiere dir allfällige Fragen.

## Übung
### Beispiel
Studiere das Beispiel `/Examples/Python/MVC_Observer`. Skizziere die Kommunikation in einem [Sequenzdiagramm](https://plantuml.com/de/sequence-diagram).

### Gruppenarbeit
1. Strukturiere das Klassendiagramm der Gruppenarbeit nach `Model View Controller` bzw `Model View Presenter` sowie dem `Observer`Pattern.
2. Setze die Beziehungen zwischen den Klassen so, dass die View und Model Klassen nicht vom Controller und Model bzw View abhängig sind. Abhängigkeit bedeutet konkret, dass auf Objekte zugegriffen wird. In UML lassen sich Abhängigkeiten mit Pfeilen darstellen. Die Pfeilspitze zeigt jeweils in die Richtung der Abhängigkeit.
3. Definiere die Schnittstellen (Public Methoden) der View und Model Klassen im Klassendiagramm. Versuche Controller und View so schlank wie möglich zu halten. Der View sollte sich nur um die Darstellung kümmern und alle dazu nötigen Informationen vom Controller erhalten. Der Controller sollte nur das Model mit dem View verknüpfen.
4. Schreibe Tests für die Methoden des Models.
5. Implementiere die Methoden für View und Model.

### Abgabe
Schick das Sequenz- und Klassendiagramm und allfällige Fragen an fabian.hirter@edu.teko.ch.