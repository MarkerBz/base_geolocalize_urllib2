# -*- coding: utf-8 -*-
from odoo import api, models
import urllib2
import odoo.addons.base_geolocalize.models.res_partner as original_code


class ResPartner(models.Model):
    _inherit = "res.partner"
    
    @api.multi
    def geo_localize(self):
        # monkey patching
        original_code.urllib = urllib2
        # call original method
        return super(ResPartner, self).geo_localize()
