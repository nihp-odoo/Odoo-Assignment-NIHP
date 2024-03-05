from odoo import fields, models

class dockModel(models.Model):
    _name = "dock.model"
    _description = "Dock Model"

    name = fields.Char(string="Dock")
