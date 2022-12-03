# -*- coding: utf-8 -*-

from odoo import fields, models, api

class AccountJournal(models.Model):
    _inherit ='account.journal'

    suspense_account_id = fields.Many2one(
        comodel_name='account.account', check_company=True, ondelete='restrict', readonly=False, store=True,
        compute='_compute_suspense_account_id',
        help="Bank statements transactions will be posted on the suspense account until the final reconciliation "
             "allowing finding the right account.", string='Suspense Account',
        domain=lambda self: "[('deprecated', '=', False), ('company_id', '=', company_id), \
                                 ('user_type_id.type', 'not in', ('receivable', 'payable'))]")


class AccountMove(models.Model):
    _inherit = "account.move"

    @api.model
    def _get_invoice_in_payment_state(self):
        return 'in_payment'
