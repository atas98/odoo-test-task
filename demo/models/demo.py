# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Demo(models.Model):
    _name = 'demo.demo'
    _inherit = ['mail.thread']

    @api.model
    def _get_default_name(self):
        """Generates string for default demo name (with index)

        Returns:
            name (str): default demo name
        """        
        global_demo_count = len(self.env['demo.demo'].search([]).ids)
        next_index = str(global_demo_count) if global_demo_count > 9 else f"0{global_demo_count}"
        return "Demo " + next_index
    
    name = fields.Char(default=_get_default_name)
    customer_id = fields.Many2one('res.partner')
    salesperson_id = fields.Many2one('res.partner')
    lead_id = fields.Many2one('crm.lead', 'demo_ids')
    done_date = fields.Date()
    state = fields.Selection(selection=[("planned", "Planned"),
                                        ("done", "Done"),
                                        ("cancelled", "Cancelled")],
                             default='planned')
    my_demo = fields.Boolean(compute='_compute_my_demo', store=True)

    @api.depends('customer_id', 'salesperson_id')
    def _compute_my_demo(self):
        """Computes my_demo flag that displays if this demo belongs to current user"""
        for r in self:
            r.my_demo = (r.customer_id.id == self.env.user.partner_id.id) or \
                        (r.salesperson_id.id == self.env.user.partner_id.id)
    
    def action_complete(self):
        """Changes state to Done"""
        for r in self:
            r.state = 'done'

    def action_cancel(self):
        """Changes state to Cancelled"""
        for r in self:
            r.state = 'cancelled'