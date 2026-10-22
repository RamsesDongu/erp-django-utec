# Ficha de Sistematización — Espiral 3
## ERP Django · Espiral E3: CRUD Web y Autenticación

| Campo | Contenido |
|---|---|
| **Semanas** | W07 – W09 |
| **Fecha de cierre** | 21/10/2026 |
| **Responsable** | Ramses Dongu |

## 1. Objetivo del ciclo
Implementar la interfaz web completa del ERP con vistas de lectura/escritura, formularios validados, autenticación y RBAC.

## 2. Evidencias
- URL pública: https://erp-django-utec-e95f.onrender.com
- Login: /accounts/login/
- Tests: Ran 108 tests → OK
- Grupos: Gerente / Vendedor / Almacen

## 3. Criterios de aceptación
| Criterio | Estado |
|---|---|
| GET /productos/ sin login → solo lectura | ✅ |
| Vendedor en /productos/eliminar/ → 403 | ✅ |
| 108 tests acumulados OK | ✅ |