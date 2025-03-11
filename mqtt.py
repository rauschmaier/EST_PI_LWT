import paho.mqtt.client as mqtt
import socket
import time

BROKER = "10.30.0.90"  # IP des MQTT-Brokers
CLIENT_ID = f"pi-{socket.gethostname()}"  # Eindeutige ID basierend auf dem Hostnamen
TOPIC_STATUS = f"status/{CLIENT_ID}"
TOPIC_LWT = f"status/{CLIENT_ID}/lwt"

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Versuche, eine Verbindung zu einem bekannten Server herzustellen
        s.connect(('8.8.8.8', 80))  # Google DNS Server
        ip_address = s.getsockname()[0]
    except Exception:
        ip_address = "Unable to get local IP"
    finally:
        s.close()
    return ip_address

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    status_msg = f"Online|{get_local_ip()}"
    client.publish(TOPIC_STATUS, status_msg, retain=True)

client = mqtt.Client(client_id=CLIENT_ID)
client.on_connect = on_connect
client.will_set(TOPIC_LWT, "Offline|Unknown", qos=1, retain=True)  # LWT enthält "Offline" + keine IP

client.connect(BROKER, 1883, 30)


status_msg = f"Online|{get_local_ip()}"
client.publish(TOPIC_STATUS, status_msg, retain=True)
client.loop_forever()
