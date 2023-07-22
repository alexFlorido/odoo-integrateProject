from odoo import api, fields, models

class ProjectWizard(models.TransientModel):
    _name = 'spacemission.project.wizard'
    _description = "Wizard: Quick Create Project for Spaceship Missions"

    def _default_mission(self):
        return self.env['spacemission.mission'].browse(self._context.get('active_id'))
    
    project_title = fields.Char(string="Project Title", required=True)
    mission_id = fields.Many2one(comodel_name="spacemission.mission", string='Missions ', required=True, default=_default_mission)
    
    
    def create_project(self):
        project_id = self.env['project.project'].create({
            'name': self.mission_id.name,
            'mission_id': self.mission_id.id,
        })