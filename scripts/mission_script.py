from xmlrpc import client
url='http://localhost:8069'
db='test1'
username='alexflorido0897@gmail.com'
password='admin'

common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
print(common.version())

uid = common.authenticate(db, username, password, {})
print(uid)

models =  client.ServerProxy("{}/xmlrpc/2/object".format(url))
model_access = models.execute_kw(db, uid, password,
                                 'spacemission.spaceship', 'check_access_rights',
                                 ['write'], {'raise_exception': False})
print(model_access)

spaceships = models.execute_kw(db, uid, password,'spacemission.spaceship', 'search_read',[[['type','in',['freighter','transport','scout_ship']]]])
print(spaceships)

spaceship = models.execute_kw(db, uid, password, 'spacemission.spaceship', 'search', [[['name','=','Kia102']]])
print(spaceship)

mission_field = models.execute_kw(db, uid, password,'spacemission.mission', 'fields_get', [], {'attributes': ['string', 'type', 'required']})
print(mission_field)

new_mission = models.execute(db, uid, password,
                             'spacemission.mission', 'create',
                             [
                                 {
                                     'spaceship_id': spaceship[0],
                                     'duration': 5,
                                 }
                             ])
print(new_mission)