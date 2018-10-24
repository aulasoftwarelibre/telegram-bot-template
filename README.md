# Hackathon bot

Ejemplo de bot desplegado en Heroku para el hackathon del Aula de Software Libre.

## Instalación en el servidor

Es imprescindible tener cuenta en Heroku para acelerar la instalación. Para desplegar la aplicación en heroku pulse el siguiente botón:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Cuando _Heroku_ se lo solicite indique el token de su bot. El nombre de la aplicación debe coincidir con el dato solicitado en _HEROKU_APP_NAME_.

Una vez _Heroku_ termine de desplegar la aplicación, el bot estaré listo para ser usado.

## Instalación en local

Si bien podemos tener el entorno de producción en _Heroku_, también tendremos un entorno de desarrollo donde ir probando nuestro bot. Es importante no compartir el mismo token del bot de producción con el que se tenga en desarrollo. Se recomienda que cada miembro del equipo se cree un bot de desarrollo propio.

## Configuración

Dentro del archivo `__application/__init.py__` se inicializan las variables necesarias para que el bot funcione.

Este archivo exporta principalmente dos variables:

* `bot`: Se debe importar en todos los archivos que quieran hacer uso de la API que ofrece la librería de _pyTelegramBotAPI_.
* `app`: Se debe importar en todos los archivos que quieran hacer uso de la API que ofrece la librería de _Flask_. 

Para configurar las variables que necesitamos en local copiar el archivo siguiente:

    cp .env.dist .env

Editar el archivo _.env_ y configuramos el _token_ de nuestro _bot_. El resto de variables se puede dejar como están.

## Ejecución

### En local

Para instalarlo en local es necesario tener instalado _python2.7_ o _python3.x_ y _virtualenv_. Python viene instalado por defecto en cualquier distribución, pero _virtualenv_ es probable que no.

Para instalar _virtualenv_ en _Debian_/_Ubuntu_ hacemos lo siguiente:

```sh
sudo apt-get install virtualenv
```

Una vez instalados vamos a instalar las dependencias e iniciar el entorno virtual de python:

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

Ahora para iniciar el bot, todo lo que debemos hace es ejecutar el archivo _main.py_.

    python main.py

Siempre debemos hacerlo en una consola con el entorno virtual cargado.

## Funciones

Dentro del directorio `application` se pueden añadir nuevas funciones, ya sea en los archivos existentes o en archivos nuevos.

Las funciones de _Telegram_, ya sean comandos o expresiones regulares, irán con la anotación correspondiente que permite la librería _pyTelegramBotAPI_.

Para más información, leed la documentación de [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI).

Un template para un nuevo archivo de funciones es el siguiente:

```python
# coding=utf-8
from application import bot


@bot.message_handler(commands=['test'])
def test(message):
    bot.reply_to(message, "Prueba")

```

Es necesario importar ese nuevo fichero en `application/__init__.py` donde se indica (al final del archivo). El orden es importante, porque la primera orden que coincida es la que se ejecuta.

## Base de datos

En local se crea un archivo en `/tmp/flask_app.db` con la base de datos en sqlite. En remoto, se crea en una base de datos de postgresql proporcionada por Heroku.

### Esquema

Dentro del directorio `model` se ha creado una clase dentro del archivo `chat.py` que sirve de ejemplo para crear tablas dentro de la aplicación.

Para más información, leed la documentación de [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/)

Un template para una nueva clase es el siguiente:

```python
from model import db

class Tabla(db.Model):
    ___table__name = 'tabla'
    id = db.Column(db.Integer, primary_key=True)
    
    # Métodos get/set
```

Es necesario importar el fichero en `model/__init__.py` donde se indica.

### Clase Chat

Se adjunta una clase Chat que permite almacenar valores en una tabla. Se puede indicar el chat asociado al dato (chat), el nombre del dato (key) y su valor (value). Si se quiere un dato que exista para cualquier chat se puede usar como identificador de chat el 0 (cero).

Un ejemplo de uso se encuentra en `application/db.py`.


## Referencias

Para obtener APIs abiertas podeís consultar el siguiente repositorio de Github:

* [https://github.com/toddmotto/public-apis](https://github.com/toddmotto/public-apis)
