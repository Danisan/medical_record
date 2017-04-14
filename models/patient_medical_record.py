# -*- coding: utf_8 -*-
from datetime import datetime
from openerp import models, fields, api, _
# from openerp.exceptions import Warning as UserError


class medical_record_patient(models.Model):
    _name = 'medical.patient'
    _inherit = 'medical.patient'

    medical_record = fields.Text(string='Medical Record')
    medical_record_history = fields.Text(
        string='Medical Record', store=True,
        readonly=True)

    # @api.multi
    # @api.depends('medical_record')
    # def _add_medical_record(self):
    #     for x in self:
    #         if not x.medical_record_history:
    #             x.medical_record_history = ''
    #         x.medical_record_history += "\n{} - {}\n{}".format(
    #             datetime.now().strftime('%d/%m/%Y %H:%M'), self.env.user.name,
    #             x.medical_record)
    #         x.medical_record = ''

    @api.onchange('medical_record')
    def _add_medical_record(self):
        x = self
        if not x.medical_record_history:
            x.medical_record_history = ''
        x.medical_record_history += "\n{} - {}\n{}".format(
            datetime.now().strftime('%d/%m/%Y %H:%M'), self.env.user.name,
            x.medical_record)
        x.medical_record = ''
