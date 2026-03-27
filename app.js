const ALLOWED_FREQUENCIES = {
  FM_Radio_Local: 95.1,
  Control_Acceso_IT: 433.92,
};

const TOLERANCE_MHZ = 0.1;

const whitelistEl = document.getElementById("whitelist");
const eventsBodyEl = document.getElementById("events-body");
const formEl = document.getElementById("event-form");
const messageEl = document.getElementById("form-message");
const refreshBtn = document.getElementById("refresh-btn");

const kpiTotal = document.getElementById("kpi-total");
const kpiOk = document.getElementById("kpi-ok");
const kpiAlert = document.getElementById("kpi-alert");

for (const [name, freq] of Object.entries(ALLOWED_FREQUENCIES)) {
  const li = document.createElement("li");
  li.textContent = `${name}: ${freq} MHz`;
  whitelistEl.appendChild(li);
}

function checkCompliance(freqMhz) {
  for (const [name, allowed] of Object.entries(ALLOWED_FREQUENCIES)) {
    if (Math.abs(freqMhz - allowed) < TOLERANCE_MHZ) {
      return { compliant: true, detail: `Autorizada: ${name}` };
    }
  }
  return {
    compliant: false,
    detail: "ALERTA: Frecuencia No Identificada / Posible Fuga",
  };
}

function formatDate(iso) {
  return new Date(iso).toLocaleString("es-ES", {
    dateStyle: "short",
    timeStyle: "medium",
  });
}

function renderEvents(events) {
  eventsBodyEl.innerHTML = "";

  const total = events.length;
  const ok = events.filter((e) => e.status === "Compliant").length;
  const alert = total - ok;

  kpiTotal.textContent = String(total);
  kpiOk.textContent = String(ok);
  kpiAlert.textContent = String(alert);

  for (const event of events) {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td>${formatDate(event.timestamp)}</td>
      <td>${event.frequency.toFixed(3)}</td>
      <td>${event.power_db.toFixed(2)}</td>
      <td><span class="tag ${event.status === "Compliant" ? "ok" : "alert"}">${event.status}</span></td>
      <td>${event.detail}</td>
      <td>${event.action_taken || "Sin acción"}</td>
    `;
    eventsBodyEl.appendChild(tr);
  }
}

async function loadEvents() {
  messageEl.textContent = "";
  const res = await fetch("/api/events");
  if (!res.ok) {
    messageEl.textContent = "No se pudieron cargar eventos desde la API.";
    return;
  }
  const data = await res.json();
  renderEvents(data.events || []);
}

formEl.addEventListener("submit", async (e) => {
  e.preventDefault();
  messageEl.textContent = "Enviando...";

  const frequency = Number(document.getElementById("frequency").value);
  const power = Number(document.getElementById("power").value);
  const action_taken = document.getElementById("action_taken").value;

  const compliance = checkCompliance(frequency);
  const payload = {
    frequency,
    power_db: power,
    status: compliance.compliant ? "Compliant" : "Non-Compliant",
    detail: compliance.detail,
    action_taken,
  };

  const res = await fetch("/api/events", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });

  if (!res.ok) {
    messageEl.textContent = "Error al guardar el evento.";
    return;
  }

  messageEl.textContent = "Evento registrado correctamente.";
  formEl.reset();
  await loadEvents();
});

refreshBtn.addEventListener("click", loadEvents);

const snippet = `import requests
from datetime import datetime

payload = {
    "frequency": center_freq / 1e6,
    "power_db": max_power,
    "status": "Compliant" if is_compliant else "Non-Compliant",
    "detail": msg,
    "action_taken": "Alerta SOC enviada" if not is_compliant else "Sin acción"
}

requests.post("https://TU-PROYECTO.vercel.app/api/events", json=payload, timeout=5)
print("Evento enviado", datetime.utcnow().isoformat())`;

document.getElementById("python-snippet").textContent = snippet;

loadEvents();
