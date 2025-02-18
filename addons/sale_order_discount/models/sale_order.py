from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # Definimos un campo nuevo para almacenar el total de descuento aplicado en la orden
    total_descuento = fields.Float(
        string="Total Descuento",
        compute="_compute_total_descuento", 
        store=True,
        help="Suma del descuento aplicado en cada línea: price_unit * (discount/100) * product_uom_qty."
    )

    estado_aprobacion = fields.Selection(
        [
            ('aprobado', 'Aprobado'),
            ('pendiente', 'Pendiente')
        ],
        string="Estado de Aprobación", 
        compute="_compute_estado_aprobacion", 
        store=True,
        help="Estado de aprobación basado en el total de descuento y/o aprobación manual."
    )    

    @api.depends('order_line', 'order_line.price_unit', 'order_line.discount', 'order_line.product_uom_qty')
    def _compute_total_descuento(self):
        for order in self:
            total = sum(
                line.price_unit * (line.discount / 100.0) * line.product_uom_qty 
                for line in order.order_line
            )
            order.total_descuento = total

    @api.depends('total_descuento')
    def _compute_estado_aprobacion(self):
        for order in self:
            order.estado_aprobacion = 'aprobado' if order.total_descuento <= 100 else 'pendiente'
