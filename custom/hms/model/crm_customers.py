from odoo import fields, models
from odoo.exceptions import UserError


class CrmCustomersInherit(models.Model):
    # _name = 'res.partner'
    _inherit = 'res.partner'

    patient_id = fields.Many2one(comodel_name='hms.patients')

    def unlink(self):
        for rec in self:
            if rec.patient_id:
                raise UserError("You can\'t delete any customer linked to a patient")
            super().unlink()

    @api.constrains('email')
    def check_email(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.fullmatch(regex, self.email):
            raise UserError(f"this {self.email} is Invalid Email")
