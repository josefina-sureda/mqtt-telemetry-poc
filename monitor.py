"""
Consola de monitoreo central (Subscriber MQTT).
Recibe y muestra en tiempo real las lecturas publicadas por el sensor.
"""

import paho.mqtt.client as mqtt

# 1. CONFIGURACION DE LA RED
# Debe coincidir con el broker y el topic donde publica el sensor horno1.py
broker = "test.mosquitto.org"
topic = "fabrica/planta1/hornoA/temperatura"

# --- 2. FUNCIÓN CALLBACK (PROGRAMACIÓN ORIENTADA A EVENTOS) ---
# Esta función NO se ejecuta al iniciar el script; se dispara automáticamente cada vez que llega un paquete de datos enviados por el publisher
def al_recibir_mensaje(cliente, userdata, mensaje):
    payload = mensaje.payload.decode("utf-8") #MQTT transmite los mensajes en formato binario para ahorrar ancho de banda, .decode("utf-8") traduce los bytes a texto tangible
    print(f"MONITOR CENTRAL - Temperatura en tiempo real: {payload} °C")

# --- 3. INICIALIZACIÓN Y VINCULACIÓN DE EVENTOS ---
cliente = mqtt.Client()
cliente.on_message = al_recibir_mensaje # Le indicamos al cliente qué función debe ejecutar cuando detecte un mensaje que entra

# --- 4. CONEXIÓN, SUSCRIPCIÓN Y ESCUCHA ACTIVA ---
print("Conectando al Broker y esperando datos del horno...")
cliente.connect(broker) #Establece la conexion entre el cliente en modo suscriptor y el Broker
cliente.subscribe(topic) #.suscribe() registra al cliente en el Broker como suscriptor de esa ruta especifica

try:
    cliente.loop_forever() # Cliente es el objeto suscriptor al que el Broker le esta mandando los datos  y .loop_forever() le da la orden de que no cierre el porgrama y deje la conexion de red abierta 
except KeyboardInterrupt: # Detecta que se cerro el programa manualmente 
    print("\nDesconectado del Broker.")
    cliente.disconnect() # El cliente se desconecta del Broker