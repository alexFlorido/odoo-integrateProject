from . import fields, models

class Spaceship(models.Model):
    _name = "spaceship.spaceship"
    _desciption = "Space Ship info"

    name = fields.Char(string="Name", required=True)
    active = fields.Boolean(string="Active", default=True)
    type = fields.Selection(string="Type", 
                            selection=[
                                ('freighter', "Freighter"),
                                ('transport', "Transport"),
                                ('scout_ship', "Scout_ship"),
                                ('fighter', "Fighter")
                                 ], copy=False)
    model = fields.Char(string="Model")
    build_date = fields.Date(string="Build Date")
    captain = fields.Char(string="Captain Name")
    required_crew = fields.Integer(string="Required Crew", default="3")
    length = fields.Float(string="Leght", digits="12,2")
    width = fields.Float(string="Width", digits="12,2")
    height = fields.Float(string="Height", digits="12,2")
    engine_number = fields.Char(string="Engine Number")
    fuel_type = fields.Selection(string="Fueltype", 
                            selection=[
                                ('solid_fuel', "Solid Fuel"),
                                ('liquid_fuel', "Liquid Fuel"),
                                 ], copy=False)
    max_weight = fields.Float(string="Max Weight", digits="12,2")