from odoo import fields, models


class HmsDoctors(models.Model):
    _name = "hms.doctors"  # this the name in database
    _rec_name = 'first_name'

    first_name = fields.Char(required=True)
    Last_name = fields.Char(required=True)
    image = fields.Binary()  # for images

    # every department have many patient
    department_id = fields.Many2one('hms.departments')
    tags_ids = fields.Many2many('hms.tags')
    is_department_open = fields.Boolean(related='department_id.Is_opened')
