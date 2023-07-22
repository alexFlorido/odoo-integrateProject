from odoo import api, fields, models


class Project(models.Model):
    _inherit = 'project.project'

    mission_id = fields.Many2one(comodel_name="spacemission.mission",
                                 string="Related Mission",
                                 ondelete="set null")
    mission_name = fields.Char(related='mission_id.name', string="Mission Name")
    
    