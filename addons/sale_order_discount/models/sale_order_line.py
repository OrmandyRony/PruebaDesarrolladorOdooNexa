from odoo import models, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.model_create_multi
    def create(self, vals_list):
        lines = super(SaleOrderLine, self).create(vals_list)
        for line in lines:
            if line.order_id:
                # Reset de la aprobacion manual al crear nuevas lineas
                line.order_id.manual_approved = False
        return lines

    def write(self, vals):
        res = super(SaleOrderLine, self).write(vals)
        # Si se actualizan campos que afectan al descuento, se resetea la aprobacion manual.
        if any(field in vals for field in ['price_unit', 'discount', 'product_uom_qty']):
            for line in self:
                if line.order_id:
                    line.order_id.manual_approved = False
        return res
