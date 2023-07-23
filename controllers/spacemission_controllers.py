from odoo import http


class SpaceMission(http.Controller):
    @http.route("/spacemission/", auth="public", website=True)
    def index(self, **kw):
        return "Hello World"

    @http.route("/spacemission/mission/", auth="public", website=True)
    def missions(self, **kw):
        missions = http.request.env["spacemission.mission"].search([])
        return http.request.render(
            "space_mission.mission_website",
            {
                "missions": missions,
            },
        )

    
