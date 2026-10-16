# Ficha de Sistematización — Espiral 2
## ERP Django · Espiral E2: Modelado de Datos y ORM
## UTEC Celaya · Técnico en Programación (SEP 3061300006-23)

| Campo | Contenido |
|---|---|
| **Número de espiral** | 2 |
| **Nombre del ciclo** | Modelado de Datos y ORM |
| **Semanas** | W04 – W06 |
| **Fecha de inicio** | 15/10/2026 |
| **Fecha de cierre** | 16/10/2026 |
| **Responsable** | Ramses Dongu |
| **Asesor** | MC. Román Fernando López González |

---

## 1. Objetivo del ciclo

Diseñar, implementar y validar el esquema de base de datos completo del
ERP en Django, garantizando integridad referencial, normalización 3FN y
cobertura de pruebas ≥ 15 tests de modelo.

---

## 2. Tareas realizadas

| # | Tarea | Estado | Tiempo invertido |
|---|---|---|---|
| 1 | Diseño diagrama ER (8 entidades) | ✅ W04 | 1:30 |
| 2 | Normalización 3FN y decisiones de diseño | ✅ W04 | 1:00 |
| 3 | Aprobación del asesor | ✅ W04 | 0:20 |
| 4 | Implementar models.py × 6 apps | ✅ W05 | 1:30 |
| 5 | Ejecutar makemigrations + migrate | ✅ W05 | 0:30 |
| 6 | Registrar en admin.py | ✅ W05 | 0:40 |
| 7 | Agregar validators + clean() | ✅ W06 | 0:30 |
| 8 | Suite de ≥ 15 tests de modelo | ✅ W06 | 0:35 |
| 9 | Instalar django-jazzmin | ✅ W06 | 0:20 |

---

## 3. Evidencias generadas

- [x] Diagrama ER aprobado: `docs/diagramas/diagrama_er.md`
- [x] Imagen exportada: `evidencias/espiral_02/diagrama_er.png`
- [x] Decisiones de diseño: `docs/decisiones_diseno.md`
- [x] Tabla de entidades: `docs/entidades_atributos.md`
- [x] Migraciones: `*/migrations/0001_initial.py` × 5 apps
- [x] Migración adicional: `ventas/migrations/0002_validators_pedido.py`
- [x] Tests: `tests/test_w05_modelos.py` (12 OK) + `tests/test_w06_validadores.py` (17 OK)
- [x] URL producción: `https://erp-django-utec-e95f.onrender.com`
- [x] Admin en producción con Jazzmin: `https://erp-django-utec-e95f.onrender.com/admin/`
- [x] Commit de cierre:
```
3c307cb Sprint 1 CIERRE [M2]: Jazzmin + clean() + 72 tests OK + Ficha Schmelkes E2
```

---

## 4. Criterios de aceptación verificados

| Criterio | ¿Cumplido? | Evidencia |
|---|---|---|
| Diagrama ER aprobado por el asesor | ✅ | Firma en sección 8 |
| `showmigrations` → `[X] 0001_initial` en 5 apps | ✅ | Terminal |
| `[X] 0002_validators_pedido` en ventas | ✅ | Terminal |
| `/admin/` muestra las 8 entidades | ✅ | Captura en producción |
| Tema Jazzmin azul/dorado activo | ✅ | Captura del `/admin/` |
| 72 tests pasando (W01 + W02 + W03 + W04 + W05 + W06) | ✅ | pytest output |
| Precio negativo → `ValidationError` | ✅ | `test_precio_negativo_lanza_validation_error` |
| Correo duplicado → `IntegrityError` | ✅ | `test_correo_duplicado_cliente_lanza_integrity_error` |
| Ficha Schmelkes E2 completa | ✅ | Este documento |

---

## 5. Problemas encontrados y soluciones

| Problema | Causa | Solución aplicada |
|---|---|---|
| Error `Cannot use ImageField because Pillow is not installed` | El campo `ConfiguracionERP.logo` requiere Pillow, que no se instaló en W05 | `pip install Pillow` + actualizar `requirements.txt` |
| Error 500 en `/admin/login/` con "Missing staticfiles manifest entry for vendor/bootswatch" | Jazzmin agregó CSS nuevo, pero el manifest de `collectstatic` era anterior a la instalación | `python manage.py collectstatic --no-input --clear` |
| Warning: `JAZZMIN_UI_TWEAKS['dark_mode_theme'] is deprecated` | La guía usa sintaxis de Jazzmin 2.x, pero se instaló 3.x | Pendiente de limpiar en W07 (no bloquea) |

---

## 6. Lecciones aprendidas

1. Diseñar el ER en papel ANTES de codificar evita tener que refactorizar modelos con FKs ya creadas.
2. Los validators (`MinValueValidator`) y el método `clean()` se ejecutan con `full_clean()`, no con `save()` directo — importante en los tests.
3. Los planes gratuitos de PaaS limitan herramientas (Render Free no tiene Shell), lo que obliga a soluciones creativas como `createsuperuser --noinput` con variables de entorno.
4. Django Admin con Jazzmin transforma la experiencia del usuario final sin escribir una sola vista nueva.

---

## 7. Tiempo total invertido

| Categoría | Horas |
|---|---|
| Diseño / planeación | 3.0 |
| Implementación | 3.0 |
| Pruebas | 1.5 |
| Documentación | 1.5 |
| **Total Espiral 2** | **9.0** |

---

## 8. Aprobación formal del diagrama ER

| Rol | Nombre | Fecha | Observaciones |
|---|---|---|---|
| Desarrollador | Ramses Dongu | 16/10/2026 | Diseño completo, 8 entidades normalizadas a 3FN |
| **Asesor (PO)** | **MC. Román Fernando López González** | 16/10/2026 | **Aprobado ✅** |

> ✅ **La Espiral 2 queda cerrada. El Hito M2 está alcanzado.**