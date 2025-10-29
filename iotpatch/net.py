import ssl
import paho.mqtt.client as mqtt

def mqtt_secure_connect(broker, port, cert=None, key=None):
    """Establish MQTT connection with or without TLS."""
    client = mqtt.Client()
    if cert and key:
        client.tls_set(certfile=cert, keyfile=key, tls_version=ssl.PROTOCOL_TLSv1_2)
    elif port == 8883:
        client.tls_set(tls_version=ssl.PROTOCOL_TLSv1_2)  # system CA
    client.connect(broker, port, keepalive=60)
    return client
