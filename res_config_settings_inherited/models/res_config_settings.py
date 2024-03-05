from odoo import fields, models

class resConfigSettingsInherited(models.TransientModel):
    _inherit = "res.config.settings"

    module_stock_transport = fields.Boolean("Dispatch Management System")
