# Documentación del Proyecto - Preprocesamiento Ciencia de Datos

**Autor:** Lesly Carrasco  
**Curso:** Cultura Digital y Sociedad - Tercer Semestre  
**Institución:** Universidad Nacional de Chimborazo  
**Fecha:** 11 de Mayo de 2026


## 1. Introducción

### 1.1 Objetivo del Proyecto

Implementar técnicas básicas de preprocesamiento de datos utilizando Python, Pandas y Scikit-learn, aplicando control de versiones con Git y GitHub para la gestión colaborativa del proyecto. El objetivo principal es limpiar, transformar y preparar un conjunto de datos para su posterior análisis o aplicación de algoritmos de machine learning.

### 1.2 Funcionalidades Implementadas

El script de preprocesamiento incluye las siguientes funcionalidades:

- **Eliminación de datos duplicados:** Remoción de filas repetidas en el dataset
- **Manejo de valores nulos:** Imputación de datos faltantes utilizando la media de las columnas numéricas
- **Conversión de variables categóricas:** Transformación de texto a formato numérico mediante One-Hot Encoding (get_dummies)
- **Normalización de datos:** Escalado de variables numéricas al rango [0, 1] usando MinMaxScaler
- **Generación de dataset procesado:** Exportación del resultado final a archivo CSV


## 2. Comandos Git Utilizados

### 2.1 Configuración Inicial del Repositorio

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/Less0miu/preprocesamiento-ciencia-datos.git
git push -u origin main´

Propósito: Inicializar el repositorio local, realizar el primer commit y conectarlo con el repositorio remoto en GitHub.

## 2.2 Creación y Gestión de Ramas

```bash
git checkout -b feature-preprocesamiento
```

### Propósito

Crear una rama de desarrollo llamada `feature-preprocesamiento` para trabajar en nuevas funcionalidades sin afectar la rama principal `main`.


## 2.3 Agregar y Confirmar Cambios

```bash
git add .
git commit -m "Ejecución exitosa del preprocesamiento de datos"
```

### Propósito

- `git add .` → Añade todos los archivos modificados al área de staging.
- `git commit` → Crea un snapshot del proyecto con un mensaje descriptivo.

## 2.4 Subir Cambios al Repositorio Remoto

```bash
git push origin feature-preprocesamiento
```

### Propósito

Subir la rama local `feature-preprocesamiento` al repositorio remoto en GitHub para su revisión y posterior fusión.


## 2.5 Actualizar Rama Main

```bash
git checkout main
git pull origin main
```

### Propósito

Cambiar a la rama principal y sincronizarla con los cambios fusionados desde el repositorio remoto.


## 2.6 Eliminar Rama Después del Merge

```bash
git branch -d feature-preprocesamiento
```

### Propósito

Eliminar la rama de desarrollo local una vez que ha sido fusionada exitosamente con `main`, manteniendo el repositorio limpio.

# 3. Automatización con GitHub Actions

## 3.1 Workflow Configurado

El archivo:

```plaintext
.github/workflows/python-app.yml
```

implementa un sistema de Integración Continua (CI) utilizando GitHub Actions.

Este workflow automatiza las siguientes tareas:

- Clonado automático del repositorio
- Configuración del entorno de Python
- Instalación automática de dependencias
- Ejecución del script `preprocesamiento.py`
- Verificación del correcto funcionamiento del proyecto

El workflow se ejecuta automáticamente cada vez que se realiza un `push` a las ramas configuradas del repositorio.


## 3.2 ¿Qué Hace GitHub Actions?

### Trigger (Activación)

El workflow se ejecuta automáticamente cuando:

- Se realiza un push a las ramas `main` o `feature-preprocesamiento`
- Se actualiza el repositorio remoto


### Entorno de Ejecución

GitHub Actions:

- Utiliza una máquina virtual Ubuntu
- Configura automáticamente Python
- Ejecuta el proyecto en un entorno limpio


### Proceso Automatizado

El workflow realiza automáticamente:

1. Clonado del repositorio
2. Instalación de dependencias
3. Configuración de Python
4. Ejecución del script `preprocesamiento.py`


### Resultado

- Workflow exitoso: el proyecto se ejecuta sin errores
- Workflow fallido: existen errores en el código o dependencias


## 3.3 Beneficios de GitHub Actions

- Detección temprana de errores
- Automatización de pruebas
- Validación continua del proyecto
- Mejora de calidad del código
- Integración continua profesional

```yaml
name: Preprocesamiento CI

on:
  push:
    branches: [ main, feature-preprocesamiento ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.14'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pandas scikit-learn numpy
    
    - name: Run preprocesamiento.py
      run: python preprocesamiento.py
```

### Explicación del Workflow

- `on:` → Define cuándo se ejecutará el workflow.
- `push:` → Ejecuta el workflow al subir cambios al repositorio.
- `pull_request:` → Ejecuta validaciones automáticas en Pull Requests.
- `runs-on:` → Define el sistema operativo utilizado.
- `actions/checkout:` → Clona automáticamente el repositorio.
- `setup-python:` → Configura el entorno de Python.
- `Install dependencies:` → Instala las librerías necesarias.
- `Run preprocesamiento.py:` → Ejecuta automáticamente el script principal del proyecto.

## 3.2 ¿Qué Hace GitHub Actions?

### Trigger (Activación)

El workflow se ejecuta automáticamente cuando:

- Se realiza un `push` a las ramas `main` o `feature-preprocesamiento`
- Se crea o actualiza una Pull Request


### Entorno de Ejecución

GitHub Actions:

- Utiliza una máquina virtual con Ubuntu (Linux)
- Configura automáticamente Python 3.14


### Proceso Automatizado

El workflow realiza automáticamente las siguientes tareas:

1. Instala o actualiza `pip`
2. Instala las dependencias:
   - `pandas`
   - `scikit-learn`
   - `numpy`
3. Ejecuta el script `preprocesamiento.py`


### Resultado

- Si el script se ejecuta sin errores → Workflow exitoso (verde)
- Si existen errores → Workflow fallido (rojo)


## 3.3 Beneficios de GitHub Actions

### Detección temprana de errores

Permite identificar problemas antes de fusionar cambios al proyecto principal.


### Validación automática

Asegura que el código funcione correctamente en un entorno limpio y automatizado.


### Calidad del código

Ayuda a mantener buenas prácticas y estándares profesionales de desarrollo.


### Ahorro de tiempo

Reduce la necesidad de realizar pruebas manuales repetitivas durante el desarrollo del proyecto.