# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountMoveInherit(models.Model):
    _inherit = 'account.move'

    employee_sales_person_id = fields.Many2one('hr.employee', string='Employee Sales Person',)
