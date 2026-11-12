
"""
Simulador de sensor de temperatura industrial (Publisher MQTT).
Publica lecturas periódicas hacia un broker público.
"""
# - - - LIBRERIAS IMPORTADAS - - - 
import random # Simula las fluctaciones del sensor 
import time
import paho.mqtt.client as mqtt

# 1. CONFIGURACION DE LA RED Y JERARQUIA 
broker = "test.mosquitto.org" # Servidor central que recibe los mensanjes enviados y los distribuye
topic = "fabrica/planta1/hornoA/temperatura" # Ruta jerarquica que identifica de donde viene el dato

# 2. Inicialización del cliente MQTT y conexión al Broker
cliente = mqtt.Client() # Creamos una instancia de cliente (objeto)
cliente.connect(broker) # Invocamos el metodo .connect() para establecer el puente de comunicacion entre el script y el servidor
                        # Conecta el cliente (publisher) con el broker 

# 3. Bucle de transmision con cierre seguro
# El bloque try/except evita errores cuando frenamos el programa manualmente
try:
    while True: # Ciclo infinito que simula el funcionamiento continuo del sensor 

        # Generacion de la lectura simulada
        temperature = random.uniform(155.0, 165.0) 
        temperature = round(temperature, 2)

        # Publicacion: envia el dato (payload) al topic configurado en el broker
        print(f"Transmitiendo {temperature} al Broker ...")
        cliente.publish(topic, temperature) #.publish(topic (ruta), payload) es el metodo que usa el objeto (cliente/publisher) para enviar el paquete de datos hacia el broker 

        # Frecuencia de muestreo
        time.sleep(2)

except KeyboardInterrupt:
    # Se ejecuta cuando se cierra la conexion manualmente para que no marque error
    print("\nSe detuvo la transmisión.")
    cliente.disconnect()




