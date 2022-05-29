from odoo import fields, models


class HmsLogHistory(models.Model):
    _name = "hms.log.history"  # this the name in database

    created_by = fields.Char()
    name = fields.Char()
    date = fields.Char()
    description = fields.Char()
