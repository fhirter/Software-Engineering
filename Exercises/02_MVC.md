# Exercise Model View Controller

1. Strukturiere das Klassendiagramm der Gruppenarbeit nach `Model View Controller` bzw `Model View Presenter` sowie dem `Observer`Pattern.
2. Setze die Beziehungen zwischen den Klassen so, dass die View und Model Klassen nicht vom Controller und Model bzw View abhängig sind. Abhängigkeit bedeutet konkret, dass auf Objekte zugegriffen wird. In UML lassen sich Abhängigkeiten mit Pfeilen darstellen. Die Pfeilspitze zeigt jeweils in die Richtung der Abhängigkeit.
3. Definiere die Schnittstellen (Public Methoden) der View und Model Klassen im Klassendiagramm. Versuche Controller und View so schlank wie möglich zu halten. Der View sollte sich nur um die Darstellung kümmern und alle dazu nötigen Informationen vom Controller erhalten. Der Controller sollte nur das Model mit dem View verknüpfen.
4. Schreibe Tests für die Methoden des Models.
5. Implementiere die Methoden für View und Model.