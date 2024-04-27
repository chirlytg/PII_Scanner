# Extensión "PII Scanner"
[![Version](https://img.shields.io/badge/Version-v1.0-green.svg)]()
[![Language](https://img.shields.io/badge/Language-Python-orange.svg)](https://www.python.org/)

Una extensión para Burp que escanea de forma pasiva todos las respuestas HTTP, y en caso de detectar un
documento CPF (Catastro de Persona Física - Brasil) muestra un alerta como output de log de la misma extensión.

Esta extensión detecta literalmente la palabra CPF en el cuerpo de la respuesta entregada.

# Instalación

## Manual

1. Descargue [1.Search_PII.py](1.Search_PII.py) en la máquina a ejecutar
2. Vaya a la pestaña _**Extender > Extensions**_, luego haga click en el botón _**Add**_ button. En la ventana emergente navege hasta la ubucación de **1.Search_PII.py** y haga click en el botón _**Next**_.

## Como usar

Navegue al sitio que desea analizar y en la salida de logs de la extensión en caso de detectar un CPF se mostrará un evento.

![Scanner PII](/images/scanner_pii.png)