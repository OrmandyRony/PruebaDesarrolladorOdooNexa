{
    'name': 'Sale Order Discount',
    'version': '1.0',
    'summary': 'Extensión de Orden de Venta con Aprobación Basada en Descuento',
    'description': 'Este módulo extiende el modelo sale.order en Odoo para implementar un sistema de aprobación basado en el total de descuento aplicado en la orden.',
    'author': 'Rony Ormandy Ortiz Alvarez',
    'category': 'Sales',
    'version': '1.0.0',
    'depends': ['sale'],
    'data': [
        'views/sale_order_view.xml',
    ],
    'installable': True,
    'application': False,
}
