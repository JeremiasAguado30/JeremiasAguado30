# Pescando 🐟

Aplicación web en Flask para detectar URLs potencialmente maliciosas usando **heurísticas** (sin modelos de IA complejos en V1).

## Objetivo

Analizar una URL y devolver:

- **Score de riesgo** (0 a 100)
- **Clasificación**: Seguro, Sospechoso o Alto Riesgo
- **Razones detectadas** para explicar el resultado

## Estructura

```text
phishing-detector/
├── app.py
├── analyzer.py
├── features.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── requirements.txt
└── README.md
```

## Requisitos

- Python 3.10+

## Instalación y ejecución

1. Crear y activar entorno virtual:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecutar la app:

```bash
python app.py
```

4. Abrir en navegador:

```text
http://localhost:5000
```

## Reglas heurísticas implementadas

- Longitud de URL
- Uso de IP en lugar de dominio
- Presencia de `@`
- Cantidad de subdominios
- Cantidad de guiones `-`
- Uso de HTTPS
- Presencia de palabras sospechosas (`login`, `verify`, etc.)
- Uso de acortadores (`bit.ly`, `tinyurl.com`, etc.)
- Patrón extra: `//` dentro del path

## Clasificación

- **0–29** → Seguro
- **30–59** → Sospechoso
- **60–100** → Alto Riesgo

## Notas de portafolio

- Código modular (extracción de features separada del motor de scoring).
- Fácil de extender con nuevas reglas.
- Incluye validación mínima y manejo de errores de entrada.
