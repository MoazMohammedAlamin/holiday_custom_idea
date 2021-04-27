from odoo import fields, models, api

class holiday(models.Model):
    _inherit = "hr.leave.type"

    state = fields.Selection([
        ('draft','Draft'),
        ('confirm','Confirm'),
        ('approve','Approve'),
    ], string="Status", readonly=True, default='draft')

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_approve(self):
        for rec in self:
            rec.state = 'approve'

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'