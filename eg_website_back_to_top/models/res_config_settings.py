from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    enable_eg_website_back_to_top = fields.Boolean(string="Website Back to Top",
                                            config_parameter="eg_website_back_to_top.enable_eg_website_back_to_top")
