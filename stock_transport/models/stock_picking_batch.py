from odoo import api,fields, models

class StockPickingBatch(models.Model):
    _inherit = "stock.picking.batch"

    # dock = fields.Many2one()
    vehicle = fields.Many2one("fleet.vehicle", string = "Vehicle")
    vehicle_category = fields.Many2one("fleet.vehicle.model.category", string = "Vehicle Category")
    dock = fields.Many2one("dock.model", string="Dock")
    weight = fields.Integer(compute="_compute_weight", string = "Weight", store=True)
    volume = fields.Integer(compute="_compute_volume", string = "Volume", store=True)
    transfers = fields.Integer(compute="_compute_transfers", string = "Transfer", store=True)
    lines = fields.Integer(compute="_compute_lines", string = "Line", store=True)


    @api.depends('move_ids')
    def _compute_weight(self):
        for record in self:
            current_weight = 0
            for move_id in record.move_ids:
                current_weight = current_weight + move_id.product_qty*move_id.product_id.weight

            if record.vehicle_category.max_weight > 0:
                record.weight = (current_weight/record.vehicle_category.max_weight)*100
            else:
                record.weight = 0

            if record.weight > 100:
                record.weight = 100

    @api.depends('move_ids')
    def _compute_volume(self):
        for record in self:
            current_volume = 0
            for move_id in record.move_ids:
                current_volume = current_volume + move_id.product_qty*move_id.product_id.volume

            if record.vehicle_category.max_volume > 0:
                record.volume = (current_volume/record.vehicle_category.max_volume)*100
            else:
                record.volume = 0

            if record.volume > 100:
                record.volume = 100


    @api.depends('picking_ids')
    def _compute_transfers(self):
        for record in self:
            curr = len(record.picking_ids)
            record.transfers = curr

    @api.depends('move_line_ids')
    def _compute_lines(self):
        for record in self:
            curr = len(record.move_line_ids)
            record.lines = curr

    @api.depends('weight', 'volume')
    def _compute_display_name(self):
        super()._compute_display_name()
        for record in self:
            record.display_name = record.name + f": ({record.weight}, {record.volume})"
        return True
