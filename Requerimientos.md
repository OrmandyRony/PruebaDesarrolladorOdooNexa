# 📌 Extensión de Orden de Venta con Aprobación Basada en Descuento

## 📋 Objetivo
Este módulo extiende el modelo `sale.order` en Odoo para implementar un sistema de aprobación basado en el total de descuento aplicado en la orden.

## ✨ Funcionalidades

### 1️⃣ Cálculo del Total Descuento
- Se agrega un campo computado y almacenado `total_descuento` en `sale.order`.  
- Se calcula sumando el descuento aplicado en cada línea de la orden:  

  ```math
  descuento_línea = price_unit × (discount / 100) × product_uom_qty
  ```

  ```math
  total_descuento = ∑ descuento_línea
  ```

### 2️⃣ Estado de Aprobación Automático
- Se agrega el campo `approval_state` con valores:  
  - `"aprobado"`: Si `total_descuento ≤ 100`.
  - `"pendiente"`: Si `total_descuento > 100`.
- Este estado se recalcula automáticamente cuando cambian `price_unit`, `discount` o `product_uom_qty`.

### 3️⃣ Aprobación Manual
- Se añade un botón en la vista de formulario que permite aprobar órdenes en estado `"pendiente"`.

## 🛠️ Uso
1. Crear una orden de venta con líneas de producto que incluyan descuentos.
2. Guardar la orden y verificar el campo `total_descuento`.
3. Revisar el estado de aprobación:
   - Si `total_descuento ≤ 100`, la orden se aprueba automáticamente.
   - Si `total_descuento > 100`, la orden queda pendiente.
4. En caso de estado `"pendiente"`, presionar el botón **"Aprobar"** en la vista de formulario para cambiar el estado a `"aprobado"`.

## 🧪 Casos de Prueba
✅ **Caso 1:** Orden con total de descuento **≤ 100**  
   - Resultado esperado: Estado `"aprobado"` automáticamente.

✅ **Caso 2:** Orden con total de descuento **> 100**  
   - Resultado esperado: Estado `"pendiente"`, con opción de aprobación manual.

✅ **Caso 3:** Cambio en `discount`, `price_unit` o `product_uom_qty` después de la aprobación  
   - Resultado esperado: El estado de aprobación se recalcula automáticamente.

---


## 📌 Requisitos Técnicos
- Utiliza el decorador `@api.depends` para gestionar la dependencia y el recálculo del campo `total_descuento` cuando cambien `price_unit`, `discount` o `product_uom_qty` en las líneas de la orden.
- La actualización automática del campo `approval_state` debe ocurrir cuando se recalcule el `total_descuento`.
- El módulo debe seguir **buenas prácticas** en cuanto a la estructura y organización de un módulo de Odoo (archivos, nomenclatura, etc.).

## 📦 Entrega
### 📜 Código del Módulo
El candidato debe entregar un módulo completo que incluya:
- Archivos necesarios para **extender el modelo** y definir la vista con el botón de acción.
- Código **organizado y estructurado** siguiendo las mejores prácticas de Odoo.
- Todos los commits se deben realizar a un repositorio el cual sea accesible para evaluar, en caso se hace privado agregar a este usuario 

### 📖 Documentación Breve
Se debe incluir un README (o comentarios en el código) con:
- 📌 **Explicación del flujo de trabajo** y el razonamiento detrás de las decisiones de diseño.
- ✅ **Instrucciones para probar la funcionalidad implementada**.
- 🚀 **Posibles mejoras** o casos límite considerados (ejemplo: qué ocurre si se modifica una línea después de la aprobación).

## 🔍 Puntos Clave a Evaluar
### 🎯 **Claridad en el Diseño**
- Se valorará la forma en que se estructura la solución y se documenta el razonamiento detrás de cada parte del código.

### 🔄 **Uso Correcto de las Dependencias**
- El candidato debe demostrar comprensión en el uso de `@api.depends` para recalcular el campo `total_descuento` correctamente.

### 🔘 **Implementación Funcional del Botón**
- La acción del botón debe ser clara y permitir cambiar manualmente el estado de la orden cuando sea necesario.

### 🏗️ **Simplicidad y Robustez**
- Aunque la tarea es de nivel medio, se valorará la capacidad de pensar en casos especiales o mejoras sin sobrecomplicar la solución.

---
📌 **Autor:** Pablo Arriola 
📅 **Última actualización:** 2025-02-14