# -*- coding: utf-8 -*-

from odoo import models, fields, api


class EmailTracker(models.Model):
    _inherit = 'crm.lead'

    email_from = fields.Char('Email', help="Email address of the contact", track_visibility='onchange', index=True)
