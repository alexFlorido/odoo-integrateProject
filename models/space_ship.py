from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Spaceship(models.Model):
    _name = "spacemission.spaceship"
    _desciption = "Space Ship info"

    name = fields.Char(string="Name", required=True)
    active = fields.Boolean(string="Active", default=True)
    # En este campo de tipo Selection dentro el array de selection todos los campos deben ir con comillas simples
    type = fields.Selection(string="Type", 
                            selection=[
                                ('freighter', 'Freighter'),
                                ('transport', 'Transport'),
                                ('scout_ship', 'Scout_ship'),
                                ('fighter', 'Fighter')
                                 ], copy=False)
    model = fields.Char(string="Model")
    build_date = fields.Date(string="Build Date")
    captain = fields.Char(string="Captain Name")
    required_crew = fields.Integer(string="Required Crew", default="3")
    length = fields.Float(string="Leght", digits="12,2", required=True)
    width = fields.Float(string="Width", digits="12,2", required=True)
    height = fields.Float(string="Height", digits="12,2")
    engine_number = fields.Char(string="Engine Number")
    fuel_type = fields.Selection(string="Fueltype", 
                            selection=[
                                ('solid_fuel', "Solid Fuel"),
                                ('liquid_fuel', "Liquid Fuel"),
                                 ], copy=False)
    max_weight = fields.Float(string="Max Weight", digits="12,2")

    mission_ids = fields.One2many(comodel_name="spacemission.mission", string="Mission", inverse_name="spaceship_id")

    fuel_capacity = fields.Float(string="Fuel Capacity", digits="12,2", compute="_compute_fuel_capacity_and_n_of_engines")
    n_engines = fields.Integer(string="Number of Engines", compute="_compute_fuel_capacity_and_n_of_engines")
    security_features =  fields.Text()




    @api.constrains('width','length')
    def _check_length(self):
        for spaceship in self:
            if (spaceship.width > spaceship.length):
                raise ValidationError('The width of the ship can not be more longer than the lenght.')
            
    @api.depends("type")
    def _compute_fuel_capacity_and_n_of_engines(self):
        for record in self:
            if(record.type == "freighter"):
                record.fuel_capacity = 125000
                record.n_engines = 4
            elif(record.type == "transport"):
                record.fuel_capacity = 70000
                record.n_engines = 4
            elif(record.type == "scout_ship"):
                record.fuel_capacity = 85000
                record.n_engines = 3
            else:
                record.fuel_capacity = 25000
                record.n_engines = 2


   