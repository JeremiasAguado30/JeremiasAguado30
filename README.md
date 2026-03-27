# Cyber Aegis Security - RF Compliance Dashboard

Aplicación web en **HTML + CSS + JavaScript** preparada para desplegar en **Vercel**.

Permite:
- Visualizar una lista blanca de frecuencias permitidas.
- Registrar eventos de detección RF de forma manual (simulación).
- Clasificar eventos en `Compliant` o `Non-Compliant`.
- Guardar y consultar eventos vía endpoint `/api/events`.
- Integrar un sensor Python (RTL-SDR) enviando eventos por `POST`.

## Estructura

- `index.html`: interfaz principal.
- `styles.css`: estilos del dashboard.
- `app.js`: lógica de frontend (compliance, tabla y formularios).
- `api/events.js`: API serverless para recibir/consultar eventos.

## Despliegue en Vercel

1. Sube este repositorio a GitHub.
2. En Vercel, importa el repositorio.
3. Framework preset: **Other** (sin build command).
4. Deploy.

Vercel detectará automáticamente:
- archivos estáticos (`index.html`, `styles.css`, `app.js`)
- función serverless (`/api/events`)

## Integración con el sensor Python

En tu script RTL-SDR, después de detectar una señal, envía el evento:

```python
import requests

payload = {
    "frequency": center_freq / 1e6,
    "power_db": max_power,
    "status": "Compliant" if is_compliant else "Non-Compliant",
    "detail": msg,
    "action_taken": "Alerta SOC enviada" if not is_compliant else "Sin acción"
}

requests.post("https://TU-PROYECTO.vercel.app/api/events", json=payload, timeout=5)
```

## Nota importante

`api/events.js` usa almacenamiento en memoria para demo. Para producción, conecta una base real
(Supabase, MongoDB Atlas o PostgreSQL) para persistencia permanente.
