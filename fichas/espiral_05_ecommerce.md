# Ficha de Sistematización — Espiral 5
## ERP Django · Espiral E5: E-commerce y Pagos

| Campo | Contenido |
|---|---|
| **Número de espiral** | 5 |
| **Nombre del ciclo** | E-commerce y Pagos |
| **Semanas** | W13 – W15 |
| **Fecha de inicio** | 04/11/2026 |
| **Fecha de cierre** | 08/11/2026 |
| **Responsable** | Ramses Dongu |
| **Asesor** | MC. Román Fernando López González |

## 1. Objetivo del ciclo
Implementar el canal de e-commerce completo: catálogo público filtrable, carrito de compras en sesión, proceso de pago con Stripe y confirmación automática vía webhook con descuento de stock.

## 2. Tareas realizadas

| # | Tarea | Estado | Semana |
|---|---|---|---|
| 1 | App catalogo + django-filter | ✅ | W13 |
| 2 | CatalogoView pública con filtros | ✅ | W13 |
| 3 | Carrito en sesión (5 vistas) | ✅ | W13 |
| 4 | Context processor carrito_info | ✅ | W13 |
| 5 | Templates catálogo + carrito | ✅ | W13 |
| 6 | pip install stripe | ✅ | W14 |
| 7 | CheckoutView con PaymentIntent | ✅ | W14 |
| 8 | Template checkout.html con Stripe.js | ✅ | W14 |
| 9 | pago_exitoso + pago_error | ✅ | W14 |
| 10 | items_snapshot en Pedido + migración 0003 | ✅ | W15 |
| 11 | Webhook endpoint con verificación de firma | ✅ | W15 |
| 12 | Descuento de stock con F() | ✅ | W15 |
| 13 | Tests con mock (Stripe + webhook) | ✅ | W15 |

## 3. Evidencias
- URL catálogo: https://erp-django-utec-e95f.onrender.com/catalogo/
- Webhook Stripe configurado en dashboard
- Tests: Ran 157 tests → OK
- Pedido 'pendiente' → 'pagado' via webhook verificado en /admin/
- Stock decrementado verificado en /admin/productos/

## 4. Criterios de aceptación
| Criterio | Estado |
|---|---|
| GET /catalogo/ sin auth → 200 | ✅ |
| Filtro por nombre/categoría/precio | ✅ |
| Agregar/remover/actualizar carrito | ✅ |
| Tarjeta 4242 → pago exitoso | ✅ |
| Webhook payment_intent.succeeded → Pedido 'pagado' | ✅ |
| Stock decrementado con F() (atómico) | ✅ |
| Firma inválida → 400 | ✅ |
| 157 tests OK | ✅ |

## 5. Problemas encontrados
| Problema | Causa | Solución aplicada |
|---|---|---|
| Webhook devolvía 500 | `stripe` v16 devuelve objetos, no dicts | Se agregó helper `_a_dict()` que usa `.to_dict()` |
| Stripe CLI pedía eventos obligatorios | Nueva versión de la CLI cambió el comportamiento | Se especificaron los eventos con `--events` |

## 6. Lecciones aprendidas
1. El webhook es la fuente de verdad del estado de un pago, no la redirección del navegador.
2. Las expresiones F() son esenciales para evitar race conditions en el stock.
3. Stripe actualiza sus APIs y herramientas con frecuencia; hay que adaptar el código a los tipos de objetos que devuelve.

## 7. Tiempo total invertido
| Categoría | Horas |
|---|---|
| Diseño | 3.0 |
| Implementación | 8.0 |
| Pruebas | 2.0 |
| Documentación | 1.5 |
| **Total Espiral 5** | **14.5** |