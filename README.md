# 👋 Hola, soy @JeremiasAguado30

Soy entusiasta de la ciberseguridad y estoy construyendo un perfil orientado al **análisis de malware** y la **respuesta a incidentes**.

## 🔬 Enfoque profesional
- 🧠 **Intereses:** reverse engineering, threat intelligence, DFIR y análisis estático/dinámico.
- 🌱 **Actualmente aprendiendo:** Windows internals, Linux malware basics, YARA y reglas Sigma.
- 🤝 **Abierto a colaborar en:** laboratorios CTF, writeups técnicos y proyectos de detección.

## 🧪 Laboratorio de análisis de malware (uso ético)
> Todo el trabajo se realiza en entornos aislados (VMs), sin ejecutar muestras fuera de laboratorio y con fines educativos/defensivos.

## 🐍 Herramienta Python: `malware_analyzer.py`
Creé una utilidad de **triage estático offline** para iniciar análisis de muestras de forma rápida y defensiva.

### ¿Qué hace?
1. Calcula hashes (`MD5`, `SHA1`, `SHA256`).
2. Estima entropía Shannon del archivo.
3. Detecta tipo básico de archivo (PE, ELF, ZIP, PDF).
4. Extrae strings imprimibles.
5. Busca IOCs en strings (`URLs`, `IPs`, dominios comunes).
6. Intenta parsear metadatos básicos de PE (arquitectura, secciones, timestamp).

### Uso
```bash
python3 malware_analyzer.py <ruta_muestra>
python3 malware_analyzer.py <ruta_muestra> --json
```

### Ejemplo
```bash
python3 malware_analyzer.py README.md --json
```

## 📂 Contenido que estaré publicando
- Writeups de análisis de muestras (sanitizados).
- Reglas YARA comentadas.
- Cheatsheets de reversing y hunting.
- Notas de hardening y monitoreo.

## 📫 Contacto
- Puedes abrir un issue o conectar conmigo por GitHub.

## ⚡ Meta 2026
Publicar análisis consistentes, mejorar la calidad técnica de los reportes y aportar valor real a la comunidad blue team.
