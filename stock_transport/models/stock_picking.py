from odoo import api,fields, models

class fleetCategory(models.Model):
    _inherit = "stock.picking"

    shipping_volume = fields.Integer(string = "Volume for shipping", compute = "_compute_shipping_volume")


    @api.depends('move_ids')
    def _compute_shipping_volume(self):
        for record in self:
            curr = 0
            for move_id in record.move_ids:
                curr = curr + move_id.product_qty*move_id.product_id.volume
            record.shipping_volume = curr
