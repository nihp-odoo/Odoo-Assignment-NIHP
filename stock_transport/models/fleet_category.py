from odoo import api,fields, models

class fleetCategory(models.Model):
    _inherit = "fleet.vehicle.model.category"

    max_weight = fields.Integer(string = "Max Weight (kg)")
    max_volume = fields.Integer(string = "Max Volumne (m^3)")


    @api.depends('max_weight', 'max_volume')
    def _compute_display_name(self):
        super()._compute_display_name()
        for record in self:
            record.display_name = record.name + f" ({record.max_weight}, {record.max_volume})"
        return True
