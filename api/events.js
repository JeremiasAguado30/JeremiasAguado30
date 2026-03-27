const store = globalThis.__CYBER_AEGIS_STORE__ || [
  {
    timestamp: new Date().toISOString(),
    frequency: 433.92,
    power_db: -24.12,
    status: "Compliant",
    detail: "Autorizada: Control_Acceso_IT",
    action_taken: "Sin acción",
  },
  {
    timestamp: new Date(Date.now() - 600000).toISOString(),
    frequency: 430.11,
    power_db: -18.56,
    status: "Non-Compliant",
    detail: "ALERTA: Frecuencia No Identificada / Posible Fuga",
    action_taken: "Alerta SOC enviada",
  },
];

globalThis.__CYBER_AEGIS_STORE__ = store;

export default async function handler(req, res) {
  if (req.method === "GET") {
    return res.status(200).json({
      events: [...store].sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp)),
    });
  }

  if (req.method === "POST") {
    const { frequency, power_db, status, detail, action_taken } = req.body || {};

    if (
      typeof frequency !== "number" ||
      typeof power_db !== "number" ||
      !status ||
      !detail
    ) {
      return res.status(400).json({ error: "Payload inválido" });
    }

    const event = {
      timestamp: new Date().toISOString(),
      frequency,
      power_db,
      status,
      detail,
      action_taken: action_taken || "Sin acción",
    };

    store.push(event);
    return res.status(201).json({ event });
  }

  return res.status(405).json({ error: "Método no permitido" });
}
