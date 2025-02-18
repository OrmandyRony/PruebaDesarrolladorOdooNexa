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

    manual_approved = fields.Boolean(
        string="Aprobado Manualmente", 
        default=False,
        help="Bandera para indicar que la orden fue aprobada manualmente mediante el botón."
    )

    @api.depends('order_line', 'order_line.price_unit', 'order_line.discount', 'order_line.product_uom_qty')
    def _compute_total_descuento(self):
        # Recorremos cada linea de la orden y calculamos el total de descuento
        for order in self:
            total = sum(
                line.price_unit * (line.discount / 100.0) * line.product_uom_qty 
                for line in order.order_line
            )
            order.total_descuento = total

    @api.depends('total_descuento', 'manual_approved')
    def _compute_estado_aprobacion(self):
        for order in self:
            # Si se aprobo manualmente, se marca como 'aprobado' 
            if order.manual_approved:
                order.estado_aprobacion = 'aprobado'
            else:
                order.estado_aprobacion = 'aprobado' if order.total_descuento <= 100 else 'pendiente'

    def action_approve(self):
        """Accion del boton para aprobar manualmente la orden cuando esta pendiente."""
        for order in self:
            if order.estado_aprobacion == 'pendiente':
                order.manual_approved = True
        return True
