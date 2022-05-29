from odoo import fields, models


class HmsTags(models.Model):
    _name = "hms.tags"  # this the name in database
    _rec_name = 'tag'

    tag = fields.Char(required=True)

    # every department have many patient
    doctors_ids = fields.Many2many('hms.doctors')
