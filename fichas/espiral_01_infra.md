# Ficha Schmelkes — Espiral 1: Infraestructura
## Semana W01 · Sprint 0

**Desarrollador:** Ramses Oswaldo Dongu Martinez
**Fecha:** 2/10/2026

## Tiempo invertido en W01
- Aproximado: 3 horas

## Qué logré
- Entorno portable en USB (Python, pip, virtualenv, Git)
- Scripts iniciar_sesion.bat y finalizar_sesion.bat
- Proyecto Django con 5 apps, subido a GitHub
- 11 tests en verde

## Dificultades que tuve
- solamente la memoria, lo demas con la guia esutvo easy
# Ficha de Sistematización — Espiral 1
## ERP Django · Espiral E1: Infraestructura y Configuración Base
## UTEC Celaya · Técnico en Programación (SEP 3061300006-23)

| Campo | Contenido |
|---|---|
| **Número de espiral** | 1 |
| **Nombre del ciclo** | Infraestructura y Configuración Base |
| **Semanas** | W01 – W03 |
| **Fecha de inicio** | 08/10/2026 |
| **Fecha de cierre** | 12/10/2026 |
| **Responsable** | Ramses Oswaldo Dongu Martinez |
| **Asesor** | MC. Román Fernando López González |

---

## 1. Objetivo del ciclo

Establecer el entorno de desarrollo portable en USB y desplegar el
proyecto Django base en Render.com, de modo que cualquier avance
posterior tenga una URL pública verificable desde el inicio del proyecto.

---

## 2. Tareas realizadas

| # | Tarea | Estado | Tiempo invertido |
|---|---|---|---|
| 1 | Configurar Python 3.11 embeddable en USB | ✅ | h:5m |
| 2 | Instalar pip y virtualenv | ✅ | h:5m |
| 3 | Configurar Git Portable | ✅ | h:10m |
| 4 | Crear scripts iniciar/finalizar sesión | ✅ | h:5m |
| 5 | Crear proyecto Django con 5 apps | ✅ | h:5m |
| 6 | Sistema de templates Fable 5 AzulERP | ✅ | h:5m |
| 7 | Configurar WhiteNoise y estáticos | ✅ | h:2m |
| 8 | Completar settings_prod.py con PostgreSQL | ✅ | h:20m |
| 9 | Crear Procfile, Dockerfile, docker-compose.yml | ✅ | h:10m |
| 10 | Crear render.yaml | ✅ | h:2m |
| 11 | Desplegar en Render.com → URL pública | ✅ | h:60m |
| 12 | Ejecutar Sprint 0 Review y Retrospectiva | ✅ | h:3m |

---

## 3. Evidencias generadas

- [ ] Repositorio GitHub: `https://github.com/tu-usuario/erp-django-utec`
- [ ] URL pública Render: `https://erp-django-utec.onrender.com`
- [ ] Captura de pantalla: `evidencias/espiral_01/render_url.png`
- [ ] Captura de pantalla: `evidencias/espiral_01/manage_check.png`
- [ ] Resultado de tests: `Ran 33 tests in X.XXXs — OK`
- [ ] Commit de cierre:C:\Temp_Workspace_ERP>git log --oneline
080deb9 (HEAD -> main, origin/main) Sprint 0 W03: settings_prod + Procfile + Dockerfile + render.yaml
7799f61 Sprint 0 W02 CIERRE: MVT completo + Fable5 + WhiteNoise + 24 tests OK
d2fd823 Sprint 0 W02: render() + templates Fable5 AzulERP x6 vistas
44650f4 Sprint 0 W01: ficha Schmelkes espiral 1
4677165 Sprint 0 W01: suite de tests de entorno (11 tests OK)
c4bfd30 Sprint 0 W01: entorno portable + proyecto Django base + 5 apps

---

## 4. Criterios de aceptación verificados

| Criterio | ¿Cumplido? | Evidencia |
|---|---|---|
| `manage.py check --deploy` sin warnings críticos | ✅ /  | Captura de terminal |
| URL pública `https://…onrender.com/` → HTTP 200 | ✅ /  | Captura del navegador |
| Repositorio con ≥ 6 commits en rama `main` | ✅ /  | `git log --oneline` |
| 33 tests pasando (W01 + W02 + W03) | ✅ /  | Resultado pytest |
| Ficha Schmelkes E1 completa | ✅ /  | Este documento |

---

## 5. Problemas encontrados y soluciones

| Problema | Causa | Solución aplicada |
|el shell es de paga|pues es de paga|lo hice desde eviroments, y asi pude resolverlo|
| | | |
| | | |

---

## 6. Lecciones aprendidas

1.siempre comprobar que funcione
2.no saltarse pasos
3.coroborar que este bien

---

## 7. Tiempo total invertido

| Categoría | Horas |
|w03|2horas|
| Diseño / planeación |5min|
| Implementación |25min|
| Pruebas |40min|
| Despliegue |40min|
| Documentación |10min|
| **Total Espiral 1** | |

---

## 8. Conexión con el trabajo recepcional

> Esta espiral aporta evidencia para el **Capítulo 4** (Desarrollo),
> sección 4.1 "Espiral 1: Infraestructura", y para el
> **Capítulo 3** (Metodología), subsección "Ciclos del modelo espiral".