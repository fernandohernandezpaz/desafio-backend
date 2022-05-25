# desafio-backend

## Requerimientos basicos para el sistema operativo
Recomendado realizar pruebas en linux

| Requisito  | Version |
|------------|---------|
| Python     | \>= 3.6 |
| Django     | 3.2     |
| virtualenv | 20.14.1 |


### Paso 1: crear entorno virtual
```
python3 -m venv env
```

### Paso 2: activar entorno virtual
```
source env/bin/activate
```

### Paso 3: instalar requerimientos
```
pip install -r requirements/base.txt
```

### Paso 4: migrar datos de prueba
```
python3 manage.py migrate_data
```

### Paso 5: importar json de postman en la aplicación de Postman
```
./collection_postman/DesafioBackend.postman_collection.json
```
En cada api existe una descripción en la opción de documentación menu lateral superior izquierdo


