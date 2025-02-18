# PruebaDesarrolladorOdooNexa

## Requerimientos Tecnicos
- Docker

## Analisis 
1. Configuración del modulo en este caso se trabajara con docker
2. Se debe activar el modulo de ventas y la funcionalidad de descuento en Odoo, este debe ser del 17 en adelante
3. Realizaremos el calculo de descuento toral siguiendo la formula price_unit * (discount/100) * product_uom_qty.

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

## Documentación de pruebas
[Documentación de pruebas](https://ormandy.notion.site/Documentaci-n-de-pruebas-165702fd0f3080a58e68e0f0b275b246?pvs=4)
