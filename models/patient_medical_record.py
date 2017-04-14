# -*- coding: utf_8 -*-
from datetime import datetime
from openerp import models, fields, api, _
# from openerp.exceptions import Warning as UserError


class medical_record_patient(models.Model):
    _name = 'medical.patient'
    _inherit = 'medical.patient'

    medical_record = fields.Text(string='Medical Record')
    medical_record_history = fields.Text(
        string='Medical Record', store=True, readonly=True)

    def _add_medical_record(self):
        self.ensure_one()
        if not self.medical_record_history:
            self.medical_record_history = ''
        self.medical_record_history += "\n{} - {}\n{}".format(
            datetime.now().strftime('%d/%m/%Y %H:%M'), self.env.user.name,
            self.medical_record)
        self.medical_record = ''
