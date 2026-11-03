# Ficha de Sistematización — Espiral 4
## ERP Django · Espiral E4: API REST y Media

| Campo | Contenido |
|---|---|
| **Número de espiral** | 4 |
| **Nombre del ciclo** | API REST y Media |
| **Semanas** | W10 – W12 |
| **Fecha de inicio** | 27/10/2026 |
| **Fecha de cierre** | 03/11/2026 |
| **Responsable** | Ramses Dongu |
| **Asesor** | MC. Román Fernando López González |

---

## 1. Objetivo del ciclo
Exponer el ERP como API REST con DRF, gestionar imágenes de productos
y generar facturas PDF descargables.

## 2. Tareas realizadas

| # | Tarea | Estado | Tiempo |
|---|---|---|---|
| 1 | DRF + authtoken instalado | ✅ W10 | 0:30 |
| 2 | Serializers × 5 entidades | ✅ W10 | 1:00 |
| 3 | API Views × 5 entidades | ✅ W10 | 0:45 |
| 4 | URLs de API + token endpoint | ✅ W10 | 0:30 |
| 5 | 7 tests APIClient | ✅ W10 | 0:30 |
| 6 | ImageField + migración 0002 | ✅ W11 | 0:45 |
| 7 | Validador MIME + tamaño | ✅ W11 | 0:30 |
| 8 | Serializer con imagen_url | ✅ W11 | 0:20 |
| 9 | Admin con preview | ✅ W11 | 0:15 |
| 10 | 8 tests media | ✅ W11 | 0:30 |
| 11 | Vista venta_pdf con xhtml2pdf | ✅ W12 | 1:30 |
| 12 | Template factura_pdf.html | ✅ W12 | 1:00 |
| 13 | 8 tests PDF | ✅ W12 | 0:30 |

## 3. Evidencias
- API pública: `https://erp-django-utec-e95f.onrender.com/api/productos/`
- PDF descargable: `http://127.0.0.1:8000/ventas/1/pdf/`
- Tests: `Ran 131 tests → OK`

## 4. Criterios de aceptación

| Criterio | Estado |
|---|---|
| GET /api/productos/ → 200 JSON | ✅ |
| POST con token → 201 | ✅ |
| ImageField con validador MIME | ✅ |
| PDF descargable con datos completos | ✅ |
| 131 tests acumulados OK | ✅ |

## 5. Problemas encontrados

| Problema | Causa | Solución |
|---|---|---|
| Docker Desktop requiere WSL2 + virtualización | Procesador AMD A8 no soporta virtualización | Fallback a xhtml2pdf (sin Docker) |
| pip install django-allauth actualizó Django 5.x | Requirements.txt sin versión fija | Se fijó `Django==4.2` |

## 6. Lecciones aprendidas
1. Los requisitos de infraestructura (Docker, virtualización) deben verificarse ANTES de la clase.
2. Tener un plan B (xhtml2pdf) es crítico para no perder una semana completa.
3. Los validadores MIME con `filetype` protegen contra archivos disfrazados.

## 7. Tiempo total invertido

| Categoría | Horas |
|---|---|
| Diseño / planeación | 2.0 |
| Implementación | 5.0 |
| Pruebas | 1.5 |
| Documentación | 1.0 |
| **Total Espiral 4** | **9.5** |

## 8. Aprobación

| Rol | Nombre | Fecha | Observaciones |
|---|---|---|---|
| Desarrollador | Ramses Dongu | 03/11/2026 | Ciclo completado con xhtml2pdf |
| **Asesor (PO)** | **MC. Román Fernando López González** | ___/___/_____ | Pendiente revisión |

> ⚠️ **Nota:** la Espiral 4 se cerró con el motor `xhtml2pdf` en lugar de WeasyPrint/Docker, porque el equipo del aula no tiene soporte de virtualización. Esto está documentado como alternativa aceptada en la Guía W12.