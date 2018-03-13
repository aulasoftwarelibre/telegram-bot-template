# Hackathon bot 

Ejemplo de bot desplegado en Heroku para el hackathon del Aula de Software Libre de marzo de 2018.


## Instalación

Es imprescindible tener cuenta en Heroku para acelerar la instalación. Para desplegar la aplicación en heroku pulse el siguiente botón:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Cuando _Heroku_ se lo solicite indique el token de su bot. El nombre de la aplicación debe coincidir con el dato solicitado en _HEROKU_APP_NAME_.


## Configuración

Dentro del archivo `__hackathon/__init.py__` se inicializan las variables necesarias para que el bot funcione.

Este archivo exporta principalmente dos variables:

* `bot`: Se debe importar en todos los archivos que quieran hacer uso de la API que ofrece la librería de _pyTelegramBotAPI_.
* `app`: Se debe importar en todos los archivos que quieran hacer uso de la API que ofrece la librería de _Flask_. 

Para configurar las variables que necesitamos en local copiar el archivo siguiente:

```
cp .env.dist .env
```

Hay algunos valores que están en blanco, su valor debe ser el mismo que aparece en Heroku. Los podemos ver dentro de la sección _Setting_ del _backend_ o ejecutando lo siguiente:

```
heroku config
```

## Ejecución

### En local

Para instalarlo en local es necesario tener instalado _python2.7_ y _virtualenv_. Por defecto lo tenemos en Ubuntu.

Para instalar _virtualenv_ hacemos lo siguiente:

```sh
sudo apt-get install virtualenv
```

A continuación necesitamos tener instaladas las herramientas de _Heroku_. En Ubuntu 17.10 se puede hacer con _snap_:

```sh
sudo snap install heroku --classic
```

O podemos seguir [las instrucciones de la web de Heroku](https://devcenter.heroku.com/articles/heroku-cli).



Ejecutar el bot en local desactiva el _webhook_. Para iniciar en modo local ejecutar lo siguiente:

```
heroku local polling
``` 

Si se quiere volver a usar el bot en el servidor, hay que volver a configurar el _webhook_ como dice el apartado anterior.

### En el servidor

Cuando se despliega el proyecto, Heroku lo configura automáticamente. Si fuera necesario volver a ejecutar el webhook ejecutar lo siguiente:

```
heroku run webhook
```

O si tenemos configurado el _.env_:

```
python webhook.py
```

También se puede iniciar dentro del apartado _Resources_ de la web de Heroku.

## Funciones

Dentro del directorio `command` se pueden añadir nuevas funciones, ya sea en los archivos existentes o en archivos nuevos.

Las funciones de _Telegram_, ya sean comandos o expresiones regulares, irán con la anotación correspondiente que permite la librería _pyTelegramBotAPI_.

Para más información, leed la documentación de [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI).

Un template para un nuevo archivo de funciones es el siguiente:

```python
# coding=utf-8
from hackathon import bot


@bot.message_handler(commands=['test'])
def test(message):
    bot.reply_to(message, "Prueba")

```

Es necesario importar el fichero en `command/__init__.py` donde se indica.


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

Un ejemplo de uso se encuentra en `commands/db.py`.


## Referencias

Para obtener APIs abiertas podeís consultar el siguiente repositorio de Github:

* [https://github.com/toddmotto/public-apis](https://github.com/toddmotto/public-apis)
