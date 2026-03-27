# 👋 Hola, soy @Jeremias 
# Cyber Aegis Security - RF Compliance Dashboard

Soy entusiasta de la ciberseguridad y estoy construyendo un perfil orientado al **análisis de malware** y la **respuesta a incidentes**.
Creacion de Aplicación web en **HTML + CSS + JavaScript** preparada para desplegar en **Vercel** y de ciberseguridad.

## 🔬 Enfoque profesional
- 🧠 **Intereses:** reverse engineering, threat intelligence, DFIR y análisis estático/dinámico.
- 🌱 **Actualmente aprendiendo:** Windows internals, Linux malware basics, YARA y reglas Sigma.
- 🤝 **Abierto a colaborar en:** laboratorios CTF, writeups técnicos y proyectos de detección.
Permite:
- Visualizar una lista blanca de frecuencias permitidas.
- Registrar eventos de detección RF de forma manual (simulación).
- Clasificar eventos en `Compliant` o `Non-Compliant`.
- Guardar y consultar eventos vía endpoint `/api/events`.
- Integrar un sensor Python (RTL-SDR) enviando eventos por `POST`.

## 🧪 Laboratorio de análisis de malware (uso ético)
> Todo el trabajo se realiza en entornos aislados (VMs), sin ejecutar muestras fuera de laboratorio y con fines educativos/defensivos.
## Estructura

### Flujo de análisis que estoy documentando
1. **Triage inicial:** hash (SHA256), tipo de archivo, strings relevantes, metadatos.
2. **Análisis estático:** PE headers, imports, empaquetado, IOCs preliminares.
3. **Análisis dinámico controlado:** comportamiento, procesos, red, persistencia.
4. **Detección:** creación de reglas YARA/Sigma e hipótesis MITRE ATT&CK.
5. **Reporte técnico:** hallazgos, evidencia y recomendaciones defensivas.
- `index.html`: interfaz principal.
- `styles.css`: estilos del dashboard.
- `app.js`: lógica de frontend (compliance, tabla y formularios).
- `api/events.js`: API serverless para recibir/consultar eventos.

## 📂 Contenido que estaré publicando
- Writeups de análisis de muestras (sanitizados).
- Reglas YARA comentadas.
- Cheatsheets de reversing y hunting.
- Notas de hardening y monitoreo.
## Despliegue en Vercel

## 📫 Contacto
- Puedes abrir un issue o conectar conmigo por GitHub.
1. Sube este repositorio a GitHub.
2. En Vercel, importa el repositorio.
3. Framework preset: **Other** (sin build command).
4. Deploy.

## ⚡ Meta 2026
Publicar análisis consistentes, mejorar la calidad técnica de los reportes y aportar valor real a la comunidad blue team.
Tambien Crear Aplicaciones. 
