from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.tools import date_utils


class Mission(models.Model):
    _name = "spacemission.mission"
    _description = "Mission Info"

    name = fields.Char(string="Mission Tittle")

    mission_number =  fields.Char(string="Mission Number",
                                  default="M0000", copy=False, required=True, readonly=True)
    
    spaceship_id = fields.Many2one(comodel_name="spacemission.spaceship", string="Space Ship", ondelete="cascade", required=True)
    crew_ids = fields.Many2many(comodel_name="res.partner", string="Space Ship Crew")
    
    release_date = fields.Datetime(string='Release Date', required=True)
    return_date = fields.Datetime(string='Return Date', required=True)
    duration = fields.Integer(string="Space Mission Duration", compute="_compute_mission_duration", inverse="_inverse_mission_duration", readonly=False)

    spaceship_model = fields.Char(related="spaceship_id.model", readonly=True)
    spaceship_required_crew = fields.Char(related="spaceship_id.required_crew", readonly=True)

    
    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('mission_number', ('S0000')) == ('S0000'):
                vals['mission_number'] = self.env['ir.sequence'].next_by_code('mission.number')
        return super().create(vals_list)
    

    @api.constrains('release_date', 'return_date')
    def _check_end_date(self):
        for mission in self:
            if(mission.release_date > mission.return_date):
                raise ValidationError('The end date can not be before the start date.')

    @api.depends('release_date', 'return_date')
    def _compute_mission_duration(self):
        for record in self:
            if record.release_date and record.return_date:
                record.duration = (record.return_date - record.release_date).days + 1

    def _inverse_mission_duration(self):
        for record in self:
            if record.release_date and record.duration:
                record.return_date = date_utils.add(record.release_date, days=record.duration-1)