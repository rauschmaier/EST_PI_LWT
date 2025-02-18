# ESP PI-Status Anzeige

Dieses Projekt ermöglicht es, den Status von Raspberry Pi Geräten (in deinem Fall ESP) über MQTT zu verfolgen und auf einer Web-Seite anzuzeigen.

## Webserver

Der Webserver wird auf der IP-Adresse `10.30.0.90` und Port `3000` gehostet und dient als Benutzeroberfläche, um die aktuellen Statusinformationen der Raspberry Pi-Geräte darzustellen.

Die Statusinformationen werden über MQTT-Nachrichten auf bestimmten Topics abonniert und live auf der Webseite aktualisiert. Der Status jedes Geräts (z.B. "Online" oder "Offline") sowie dessen IP-Adresse wird angezeigt.

### MQTT-Topic:
Der Webserver abonniert das MQTT-Topic `status/#`, um alle Status-Nachrichten von Geräten zu empfangen. Jede Nachricht besteht aus dem Status des Geräts und der IP-Adresse im Format `Status|IP`.

## Implementierung auf dem Raspberry Pi (ESP):

### 1. Abhängigkeiten installieren

Installiere die benötigten Python-Pakete auf deinem Raspberry Pi mit:

```bash
sudo apt update
sudo apt install python3-paho-mqtt python3-flask
```
### 3. Anlegen des Python-Skripts
Speichern Sie das Python-Skript m̀qtt.py`auf dem PI

### 2. Automatischen Start von mqtt.py beim Systemstart konfigurieren

Um `mqtt.py' automatisch beim Start des Raspberry Pi im Hintergrund auszuführen, kannst du einen Systemd Service einrichten.
**Schritte zur Einrichtung eines Systemd-Services:**
1. Erstelle eine neue Service-Datei für mqtt.py.
   ```bash
   sudo nano /etc/systemd/system/mqtt-client.service
   ```
2. Füge den folgenden Inhalt in die Datei ein:
   ```ini
     [Unit]
    Description=MQTT Client für Raspberry Pi Status
    After=network.target
    
    [Service]
    ExecStart=/usr/bin/python3 /path/to/your/mqtt.py
    WorkingDirectory=/path/to/your/
    User=pi
    Restart=always
    StandardOutput=inherit
    StandardError=inherit
    
    [Install]
    WantedBy=multi-user.target
   ```
   - Ersetze `/path/to/your/mqtt.py` mit dem tatsächlichen Pfad zu deiner mqtt.py-Datei.
Stelle sicher, dass der Benutzer pi über die notwendigen Berechtigungen verfügt.
3. Lade die Service-Dateien neu, um den neuen Service zu registrieren.
  ```bash
  sudo systemctl daemon-reload
  ```
4. Aktiviere den Service, damit er beim Booten automatisch startet.
  ```bash
  sudo systemctl enable mqtt-client.service
  ```
5. Starte den Service sofort.
  ```bash
  sudo systemctl start mqtt-client.service
  ```
### 4. Zugriff auf die Status-Seite

Nach dem Start des Servers kannst du die Status-Seite im Schulnetz unter 10.30.0.90:3000` erreichen, die die Daten der Raspberry Pi-Geräte in Echtzeit anzeigt. Beachte, dass der PI hiezu ebenfalls im Schulnetz sein muss.
