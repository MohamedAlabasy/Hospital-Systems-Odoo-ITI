from odoo import fields, models, api
from odoo.exceptions import UserError
import re
from datetime import date


class HmsPatients(models.Model):
    _name = "hms.patients"  # this the name in database
    _rec_name = 'first_name'
    # _log_access=False #if I wanted to remove add some additional tables

    # name = fields.Char(required=True,default="anyThing")
    first_name = fields.Char(required=True)
    Last_name = fields.Char(required=True)
    email = fields.Char()
    # birth_date = fields.Datetime()
    birth_date = fields.Date()
    history = fields.Html()
    CR_ratio = fields.Float()
    blood_type = fields.Selection([
        ('A', 'has A antigens on the red blood cells with anti-B antibodies in the plasma'),
        ('B', 'has B antigens with anti-A antibodies in the plasma'),
        ('O', 'has no antigens, but both anti-A and anti-B antibodies in the plasma'),
        ('AB', 'has both A and B antigens, but no antibodies'),
    ])
    PCR = fields.Boolean()
    # image = fields.Image()
    image = fields.Binary()  # for images
    address = fields.Text()
    age = fields.Integer(compute='calc_age', store=True, readonly=True)

    # every department have many patient
    department_id = fields.Many2one('hms.departments')
    is_department_open = fields.Boolean(related='department_id.Is_opened')
    state = fields.Selection([
        ('Undetermined', 'Undetermined'),
        ('Good', 'Good'),
        ('Fair', 'Fair'),
        ('Serious', 'Serious'),
    ], default='Undetermined')

    # @api.onchange("age")
    # def onchange_age(self):
    #     if self.age < 30:
    #         self.CR_ratio = 10.10
    #         self.PCR = True
    #     return {
    #         "warning": {
    #             "title": "age lower than 30",
    #             "message": "You have change you age"
    #         },
    #         # "domain": {
    #         #
    #         # }
    #     }

    def pass_undetermined(self):
        self.state = 'Good'
        patient_history = self.env['hms.log.history'].create({
            'created_by': 'admin',
            'name': f"{self.first_name} {self.Last_name}",
            'date': self.birth_date,
            'description': self.state,
        })
        print(patient_history)

    def pass_good(self):
        self.state = 'Fair'
        patient_history = self.env['hms.log.history'].create({
            'created_by': 'admin',
            'name': f"{self.first_name} {self.Last_name}",
            'date': self.birth_date,
            'description': self.state,
        })
        print(patient_history)

    def pass_fair(self):
        self.state = 'Serious'
        patient_history = self.env['hms.log.history'].create({
            'created_by': 'admin',
            'name': f"{self.first_name} {self.Last_name}",
            'date': self.birth_date,
            'description': self.state,
        })
        print(patient_history)

    def return_undetermined(self):
        self.state = 'Undetermined'
        patient_history = self.env['hms.log.history'].create({
            'created_by': 'admin',
            'name': f"{self.first_name} {self.Last_name}",
            'date': self.birth_date,
            'description': self.state,
        })
        print(patient_history)

    def unlink(self):
        if self.state != 'Undetermined':
            raise UserError("You can\'t delete patient when state isn\'t Undetermined")
        super().unlink()

    @api.constrains('email')
    def check_email(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.fullmatch(regex, self.email):
            raise UserError(f"this {self.email} is Invalid Email")

    @api.depends('birth_date')
    def calc_age(self):
        today = date.today()
        for rec in self:
            rec.age = today.year - rec.birth_date.year

    _sql_constraints = [
        ('duplicate_email', 'UNIQUE(email)', 'This email already exists')
    ]
