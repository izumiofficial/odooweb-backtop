from . import models


def post_init_enable_eg_website_back_to_top(env):
    env["ir.config_parameter"].sudo().set_param("eg_website_back_to_top.enable_eg_website_back_to_top", True)
