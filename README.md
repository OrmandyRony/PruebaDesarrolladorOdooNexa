# PruebaDesarrolladorOdooNexa

## Requerimientos Tecnicos
- Docker

## Analisis 
1. Configuración del modulo en este caso se trabajara con docker
2. Se debe activar el modulo de ventas y la funcionalidad de descuento en Odoo, este debe ser del 17 en adelante

## Comenzando
```
docker compose up
```
## Estructura de carpetas

```
addons/
├── sale_order_discount/
    ├── __init__.py
    ├── __manifest__.py
    ├── models/
    │   ├── __init__.py
    │   ├── sale_order.py
    │   └── sale_order_line.py
    ├── views/
    │   └── sale_order_view.xml
    └── README.md

```