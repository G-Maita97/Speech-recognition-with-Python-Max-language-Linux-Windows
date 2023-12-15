#!/usr/bin/python3

# Importamos la lib speech_recognition y le asignamos un alias sr para agilizar la escritura
import speech_recognition as sr  

recognizer = sr.Recognizer()
"""
    Al crear una instancia de la clase Recognizer 
    mediante recognizer = sr.Recognizer(), estás 
    creando un objeto Recognizer que puede ser 
    utilizado para realizar operaciones de reconocimiento de voz.

"""

mic = sr.Microphone()
"""
    Se crea una instancia del objeto 
    Microphone. Este objeto Microphone representa el micrófono del 
    sistema y se utiliza para capturar audio del entorno.

"""

with mic as source:
    """
        En este caso, el bloque with se encarga automáticamente 
        de la apertura y cierre del micrófono (mic). Cuando el bloque 
        with se inicia, el micrófono se abre (__enter__), y cuando el 
        bloque with se completa, el micrófono se cierra (__exit__).

        Por otra parte source es el micrófono que se utiliza para 
        escuchar y capturar el audio.

    """
    audio = recognizer.listen(source)
    """
        La variable audio  se encarga de capturar audio utilizando 
        el micrófono (source) y almacenar ese audio en un objeto de 
        tipo AudioData.

        recognizer: Este objeto proporciona métodos para interactuar 
        con motores de reconocimiento de voz (En este caso Google).

        Listen(): Este es un método del objeto Recognizer. Toma como 
        argumento la fuente de audio (source) y captura audio del micrófono. 
        Específicamente, el método listen() escucha el audio del micrófono 
        hasta que detecta un período de silencio, indicando que se ha capturado 
        un segmento de audio. 

    """


texto = recognizer.recognize_google(audio, language = 'ES')
"""
    recognize_google(): Este método del objeto Recognizer, realiza el 
    reconocimiento de voz en el audio proporcionado utilizando el servicio 
    de reconocimiento de voz de Google (toma como argumento el audio capturado y el lenguaje).

    audio: El primer argumento es el audio que se va a reconocer, en este caso, 
    el objeto AudioData capturado previamente.

    language='': El segundo argumento opcional especifica el idioma del audio. 
    En este caso, se establece en 'ES', indicando que el reconocimiento debe realizarse en español.

    texto: contendrá el texto transcribido a partir del audio capturado.
"""


print(f'Gustavo Maita a dicho: {texto}')
"""
    esta línea de código imprime un mensaje en la 
    consola que incluye el mensaje almacenado en la variable texto. 
"""