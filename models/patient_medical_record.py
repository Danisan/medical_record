# -*- coding: utf_8 -*-
from datetime import datetime
from openerp import models, fields, api, _
# from openerp.exceptions import Warning as UserError


class medical_record_patient(models.Model):
    _name = 'medical.patient'
    _inherit = 'medical.patient'

    medical_record = fields.Text(string='Medical Record')
    medical_record_history = fields.Text(
        string='Medical Record', compute='_add_medical_record', store=True,
        readonly=True)

    @api.multi
    @api.depends('medical_record')
    def _add_medical_record(self):
        for x in self:
            x.medical_record_history += "\n{} - {}\n{}".format(
                datetime.now(), x.company_id.user_id.name, x.medical_record)
            x.medical_record = False
