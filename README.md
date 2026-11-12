# Simulación de Telemetría IIoT con MQTT y Python

Prueba de Concepto (PoC) de una arquitectura **Publicador/Suscriptor (Pub/Sub)** aplicada al monitoreo industrial de temperatura en tiempo real utilizando el protocolo **MQTT**.

## Descripción y Arquitectura

El proyecto simula el flujo de datos entre un activo de planta y una consola de control centralizada, desacoplando al emisor del receptor mediante un Broker público:

* **`horno1.py` (Publisher):** Simula un sensor industrial de temperatura que genera lecturas continuas (entre 155.0 °C y 165.0 °C) y las transmite cada 2 segundos hacia el broker `test.mosquitto.org` bajo el tópico jerárquico `fabrica/planta1/hornoA/temperatura`.
* **`monitor.py` (Subscriber):** Consola central que se suscribe al tópico del horno y escucha la red de forma pasiva. Utiliza programación orientada a eventos (*callbacks*) para decodificar y mostrar cada *payload* entrante en tiempo real, evitando el consumo innecesario de recursos por *polling*.

## Conceptos Técnicos Aplicados

* **Protocolo MQTT (IIoT):** Transmisión liviana de telemetría mediante jerarquía de tópicos sobre TCP/IP.
* **Programación Orientada a Objetos (POO):** Instanciación y manejo de métodos de red a través de la clase `mqtt.Client`.
* **Arquitectura Orientada a Eventos:** Uso de funciones *callback* (`on_message`) disparadas asincrónicamente ante la llegada de paquetes binarios y decodificación UTF-8.
* **Cierre Seguro (Graceful Shutdown):** Manejo de excepciones (`KeyboardInterrupt`) para liberar el socket de red limpiamente al detener los scripts.

## Requisitos e Instalación

1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/josefina-sureda/mqtt-telemetry-poc.git](https://github.com/josefina-sureda/mqtt-telemetry-poc.git)
   cd mqtt-telemetry-poc