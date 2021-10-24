# Smashed It!
- [Smashed It!](#smashed-it)
  - [Overview](#overview)
  - [Docker](#docker)
  - [Local (poetry installed)](#local-poetry-installed)

## Overview
- Simple todo app implemented in Python and used for educational/testing purposes
- Flask backend, SQLite and ORM (Flask-SQLAlchemy)

## Docker
```bash
# get container
podman pull adegoodyer/smashed-it-test-app:latest

# run locally
podman run -d --rm -p 8080:5000 --network bridge adegoodyer/smashed-it-test-app

# open browser and visit http://localhost:8080
```

## Local (poetry installed)
```bash
git clone git@github.com:adegoodyer/smashed-it-test-app.git
cd smashed-it-test-app
poetry init
poetry shell
flask run
```
