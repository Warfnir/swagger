from flask_restplus import Namespace, Resource, fields

api = Namespace('master', description='Master related operations',)

master = api.model('Master', {
    'id': fields.String(required=True, description='The master identifier'),
    'name': fields.String(required=True, description='The master name'),
})

MASTER = [
    {'id': 'baldur', 'name': 'Baldur'},
]

@api.route('/')
class DogList(Resource):
    @api.doc('list_master')
    @api.marshal_list_with(master)
    def options(self):
        '''List all masters'''
        return MASTER

@api.route('/<id>')
@api.param('id', 'The master identifier')
@api.response(404, 'Master not found')
class Master(Resource):
    @api.doc('get_cat')
    @api.marshal_with(master)
    def options(self, id):
        '''Fetch a master given its identifier'''
        for master in MASTER:
            if master['id'] == id:
                return master
        api.abort(404)