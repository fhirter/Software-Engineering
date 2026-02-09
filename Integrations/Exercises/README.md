# Übung Publish / Subscribe mit MQTT

Erstelle einen MQTT-REST Adapter. Dieser soll anhand von MQTT-Nachrichten die Daten einer REST-API aktualisieren.

Nutze dafür die ["Items-API" aus den Beispielen](../Examples/REST) oder die API aus der Gruppenarbeit. Die Beispiel-API
erwartet folgende Daten:

```json
{
  "id": 1,
  "name": "Item 1",
  "description": "First item"
}
```

Löse die Aufgabe ohne KI, um einen möglichst grossen Lerneffekt zu erzielen. 

Halte deine Erkenntnisse schriftlich fest.

1. Installiere ["Eclipse Mosquitto"](https://mosquitto.org/)
2. Starte den Mosquitto MQTT Server mit `mosquitto -p 1883 -v` falls er nicht schon läuft.
3. Starte den MQTT-Client in [mqtt_client.py](mqtt_client.py) oder abonniere in einem zweiten Terminal auf ein Topic mit
   `mosquitto_sub -h localhost -p 1883 -t 'items' -v`
4. Veröffentliche in einem dritten Terminal zum Test eine Nachricht mit cURL. Analysiere die Ausgabe in den drei
   Terminals bzw in der Ausgabe des Python-MQTT-Clients.

```bash
curl -v -X PUBLISH 'mqtt://localhost:1883/items' \
  -H 'Content-Type: application/json' \
  -d '{"id":1,"name":"Item 1","description":"First item"}'
```

5. Implementiere nun den REST Adapter mit der `requests` Bibliothek. Der Adapter soll
    - neue Items Einträge erstellen, falls sie nicht vorhanden sind, bzw.
    - bestehende Einträge aktualisieren, falls sie schon vorhanden sind und geändert wurden.

