from odoo import fields, models


class HmsDepartments(models.Model):
    _name = "hms.departments"  # this the name in database

    name = fields.Char(required=True)
    capacity = fields.Integer()
    Is_opened = fields.Boolean()

    # every department have many patient
    patient_ids = fields.One2many(comodel_name='hms.patients', inverse_name='department_id')
    doctor_ids = fields.One2many(comodel_name='hms.doctors', inverse_name='department_id')

