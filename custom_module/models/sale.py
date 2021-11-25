from odoo import models, fields, api, _


class AccountAccount(models.Model):
    _inherit = "sale.order"

    custom_field  = fields.Char(string="Custom Field")