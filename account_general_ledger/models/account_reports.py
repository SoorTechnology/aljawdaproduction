# -*- coding: utf-8 -*-
import copy
import json
import io
import logging
import lxml.html
import datetime
import ast
from collections import defaultdict
from math import copysign

from dateutil.relativedelta import relativedelta

from odoo.tools.misc import xlsxwriter
from odoo import models, fields, api, _
from odoo.tools import config, date_utils, get_lang
from odoo.osv import expression
from babel.dates import get_quarter_names
from odoo.tools.misc import formatLang, format_date
from odoo.addons.web.controllers.main import clean_action
from odoo.tools.safe_eval import safe_eval

_logger = logging.getLogger(__name__)

class AccountReport(models.AbstractModel):
    _inherit = 'account.report'
    
    def get_html_footnotes(self, footnotes):
        if self._name == 'account.partner.ledger':
            template = self._get_templates().get('account_general_ledger.account_reports_footer_extend', 'account_general_ledger.account_reports_footer_extend')
            rcontext = {'footnotes': footnotes, 'context': self.env.context}
            html = self.env['ir.ui.view'].render_template(template, values=dict(rcontext))
            return html
        else:
            return super(AccountReport, self).get_html_footnotes(footnotes=footnotes)
    