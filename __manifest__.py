{
    'name': "space_mission",
    'summary': """Module to Logistic Handle of a Space Mission""",
    'description': """Module Handle: 
            - Logisctic
            - Space travel ships
            - Crew
            """,
    'license': "OPL-1",
    'author': "alexFlorido",
    'website': 'www.odoo.com',
    'category': "Custom Modules/Space Mission",
    "depends": ['project'] ,
    'data': [
        'security/spaceship_groups.xml',
        'security/ir.model.access.csv',
        'security/spaceship_security.xml',
        'data/mission_data.xml',
        'views/space_ship_menuitems.xml',
        'views/spaceship_views.xml',
        'views/spacemission_views.xml',
        'views/project_views_inherit.xml',
        'wizard/project_wizard_view.xml',
    ],
    'demo': [
        'demo/space_ship_demo.xml',
    ],
    'application': True,
}