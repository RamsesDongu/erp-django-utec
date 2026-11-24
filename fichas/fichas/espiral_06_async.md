# Ficha de Sistematización — Espiral 6
## ERP Django · Espiral E6: Celery e Integraciones

| Campo | Contenido |
|---|---|
| **Número de espiral** | 6 |
| **Nombre del ciclo** | Celery e Integraciones |
| **Semanas** | W16 – W18 |
| **Responsable** | Ramses Oswaldo Dongu Martinez |
| **Asesor** | MC. Román Fernando López González |

## Tareas realizadas
| # | Tarea | Estado |
|---|---|---|
| 1 | Celery + Redis + Flower instalados y configurados | ✅ |
| 2 | Worker embebido en Render (`start.sh`) | ✅ |
| 3 | Webhook `payment_intent.succeeded` como disparador | ✅ |
| 4 | `django-anymail[resend]` + correos reales | ✅ |
| 5 | `Pedido.correo_enviado` (idempotencia) | ✅ |
| 6 | Templates `confirmacion_pedido` y `alerta_stock` | ✅ |
| 7 | `reporte_ventas_diario` con `annotate` | ✅ |
| 8 | `CELERY_BEAT_SCHEDULE` (crontab y timedelta) | ✅ |
| 9 | Beat embebido en Render | ✅ |
| 10 | Fix `kombu==5.3.7` | ✅ |
| 11 | Acción admin para reenviar confirmación | ✅ |

## Evidencias
- Pruebas: `Ran 174 tests — OK`
- Correo de confirmación y reporte diario recibidos vía Resend.
- Logs de Render: `beat: Starting...` y `celery@... ready`.