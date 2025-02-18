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

    @api.depends('order_line', 'order_line.price_unit', 'order_line.discount', 'order_line.product_uom_qty')
    def _compute_total_descuento(self):
        for order in self:
            total = sum(
                line.price_unit * (line.discount / 100.0) * line.product_uom_qty 
                for line in order.order_line
            )
            order.total_descuento = total