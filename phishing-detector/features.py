"""Extracción de características heurísticas para detección de phishing.

Este módulo contiene funciones puras y reutilizables para analizar una URL.
"""

from __future__ import annotations

import ipaddress
import re
from urllib.parse import urlparse

import tldextract

# Evita llamadas de red en entornos restringidos y usa la lista incluida en la librería.
_TLD_EXTRACTOR = tldextract.TLDExtract(suffix_list_urls=None)

SUSPICIOUS_KEYWORDS = {
    "login",
    "verify",
    "update",
    "secure",
    "bank",
    "account",
    "password",
    "confirm",
}

KNOWN_SHORTENERS = {
    "bit.ly",
    "tinyurl.com",
    "t.co",
    "goo.gl",
    "ow.ly",
    "is.gd",
    "buff.ly",
    "adf.ly",
    "shorturl.at",
    "cutt.ly",
    "rebrand.ly",
}


def normalize_url(url: str) -> str:
    """Normaliza entrada de usuario para facilitar parseo.

    - Elimina espacios extremos.
    - Si no hay esquema, agrega https:// por defecto para parsear correctamente.
    """
    clean = url.strip()
    if clean and not re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", clean):
        clean = f"https://{clean}"
    return clean


def is_ip_address(hostname: str) -> bool:
    """Retorna True si hostname es una dirección IP válida."""
    if not hostname:
        return False
    try:
        ipaddress.ip_address(hostname)
        return True
    except ValueError:
        return False


def extract_features(url: str) -> dict:
    """Extrae características de riesgo de una URL.

    Devuelve un diccionario con métricas y banderas utilizadas por el analizador.
    """
    parsed = urlparse(url)
    hostname = parsed.hostname or ""
    path_and_query = f"{parsed.path} {parsed.query}".lower()
    full_lower = url.lower()

    extracted = _TLD_EXTRACTOR(hostname)

    # Subdominios: se consideran partes separadas por '.'
    subdomain_parts = [p for p in extracted.subdomain.split(".") if p]

    # Conteo de palabras sospechosas en toda la URL
    keyword_matches = [kw for kw in SUSPICIOUS_KEYWORDS if kw in full_lower]

    # Detección de acortador de URL
    fqdn = ".".join(part for part in [extracted.domain, extracted.suffix] if part)
    is_shortener = fqdn in KNOWN_SHORTENERS or hostname in KNOWN_SHORTENERS

    return {
        "original_url": url,
        "hostname": hostname,
        "url_length": len(url),
        "has_ip": is_ip_address(hostname),
        "has_at_symbol": "@" in url,
        "subdomain_count": len(subdomain_parts),
        "hyphen_count": hostname.count("-"),
        "is_https": parsed.scheme.lower() == "https",
        "suspicious_keyword_count": len(keyword_matches),
        "suspicious_keywords_found": sorted(keyword_matches),
        "is_shortener": is_shortener,
        "path_has_double_slash": "//" in parsed.path,
        "path_and_query": path_and_query,
    }
