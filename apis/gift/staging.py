from flask_restplus import Namespace, Resource, fields

api = Namespace('staging', description='Stagings related operations')

staging = api.model('Staging', {
    'id': fields.String(required=True, description='The staging identifier'),
    'name': fields.String(required=True, description='The staging name'),
})

STAGING = [
    {'id': 'felix', 'name': 'Felix'},
]

@api.route('/')
class CatList(Resource):
    @api.doc('list_cats')
    @api.marshal_list_with(staging)
    def options(self):
        '''List all cats'''
        return STAGING

@api.route('/<id>')
@api.param('id', 'The cat identifier')
@api.response(404, 'Cat not found')
class Staging(Resource):
    @api.doc('get_staging')
    @api.marshal_with(staging)
    def options(self, id):
        '''Fetch a cat given its identifier'''
        for staging in STAGING:
            if staging['id'] == id:
                return staging
        api.abort(404)