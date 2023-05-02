# Practica Python Venv

Este proyecto fue creado con el objetivo de aprender y practicar el uso de entornos virtuales en Python.

Los entornos virtuales son una herramienta esencial en el desarrollo de proyectos en Python, ya que permiten aislar las dependencias de cada proyecto, evitando conflictos entre versiones de paquetes, además de ofrecer un mayor control sobre las dependencias utilizadas.

## Requisitos

- Python 3.x
- Virtualenv (opcional)

## Instalación

- Clona o descarga el repositorio.
- Crea un entorno virtual para el proyecto (recomendado)
- Activa el entorno virtual
- Instala las dependencias con pip

Windows

```sh
  py -m venv env
  env\Scripts\activate
  pip install -r requirements.txt
```

Linux o Mac

```sh
  python3 -m venv env
  env\Scripts\activate
  pip3 install -r requirements.txt
```

## Ejecutar el Juego (Piedra, Papel o Tjera)

```sh
py game/main.py
```

```sh
python3 game/main.py
```

## Crear una Gráfica con Matplotlib

```sh
py charts/main.py
```

```sh
python3 charts/main.py
```

## Hacer una Solicitud HTTP con Requests

```sh
py web-server/main.py
```

```sh
python3 web-server/main.py
```
