"""Motor de scoring para clasificación de URLs potencialmente maliciosas."""

from __future__ import annotations

from features import extract_features, normalize_url


def classify_score(score: int) -> str:
    """Clasifica score en etiqueta de riesgo."""
    if score >= 60:
        return "Alto Riesgo"
    if score >= 30:
        return "Sospechoso"
    return "Seguro"


def analyze_url(user_url: str) -> dict:
    """Analiza una URL con reglas heurísticas.

    Retorna:
      - score (0-100)
      - classification
      - reasons (lista de explicaciones)
      - features (métricas internas útiles para depuración)
    """
    if not user_url or not user_url.strip():
        raise ValueError("Debes ingresar una URL para analizar.")

    normalized_url = normalize_url(user_url)
    features = extract_features(normalized_url)

    # Validación mínima de dominio/host
    if not features["hostname"]:
        raise ValueError("La URL no parece válida: falta el dominio.")

    score = 0
    reasons: list[str] = []

    # 1) Longitud de URL
    if features["url_length"] >= 75:
        score += 10
        reasons.append("URL muy larga (>= 75 caracteres), patrón común en phishing.")

    # 2) Uso de IP en vez de dominio
    if features["has_ip"]:
        score += 25
        reasons.append("Usa una dirección IP en lugar de un dominio legible.")

    # 3) Presencia de @
    if features["has_at_symbol"]:
        score += 20
        reasons.append("Contiene '@', técnica usada para ocultar el destino real.")

    # 4) Subdominios excesivos
    if features["subdomain_count"] >= 3:
        score += 10
        reasons.append("Tiene muchos subdominios, posible intento de suplantación.")

    # 5) Muchos guiones en host
    if features["hyphen_count"] >= 2:
        score += 10
        reasons.append("El dominio contiene múltiples guiones, señal sospechosa.")

    # 6) No HTTPS
    if not features["is_https"]:
        score += 10
        reasons.append("No utiliza HTTPS.")

    # 7) Palabras sospechosas
    if features["suspicious_keyword_count"] >= 3:
        score += 15
        reasons.append(
            "Contiene varias palabras asociadas a phishing: "
            + ", ".join(features["suspicious_keywords_found"])
            + "."
        )
    elif features["suspicious_keyword_count"] > 0:
        score += 8
        reasons.append(
            "Incluye palabras potencialmente sensibles: "
            + ", ".join(features["suspicious_keywords_found"])
            + "."
        )

    # 8) Acortador de URL
    if features["is_shortener"]:
        score += 20
        reasons.append("Utiliza un acortador de URL que oculta el destino final.")

    # 9) Doble slash en path (heurística extra suave)
    if features["path_has_double_slash"]:
        score += 5
        reasons.append("Contiene '//' dentro del path, patrón anómalo.")

    score = min(score, 100)
    classification = classify_score(score)

    if not reasons:
        reasons.append("No se detectaron señales de riesgo relevantes con estas reglas.")

    return {
        "url": normalized_url,
        "score": score,
        "classification": classification,
        "reasons": reasons,
        "features": features,
    }
