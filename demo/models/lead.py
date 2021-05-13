# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Lead(models.Model):
    _inherit = 'crm.lead'

    demo_ids = fields.One2many('demo.demo', 'lead_id')
    demo_count = fields.Integer(compute='_compute_demo_count')

    @api.depends('demo_ids')
    def _compute_demo_count(self):
        for r in self:
            r.demo_count = len(r.demo_ids.ids)

    def create_new_demo(self):
        """Opens demo form view with filled fields based on selected lead"""
        context = {
            'default_salesperson_id': self.user_id.partner_id.id,
            'default_customer_id': self.partner_id.id,
            'default_lead_id': self.id
        } 
        return {
            'name': 'Demo',
            'view_type': 'form',
            'view_mode': 'form',
            'view_id': False,
            'res_model': 'demo.demo',
            'type': 'ir.actions.act_window',
            'target': 'main',
            'context': context
        }
        
    def open_demos(self):
        """Opens demo tree view for selected lead"""
        return {
            'name': 'Demo',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'view_id': False,
            'res_model': 'demo.demo',
            'type': 'ir.actions.act_window',
            'target': 'main',
            'domain': [('id', 'in', self.demo_ids.ids)]
        }
