from flask_restplus import Namespace, Resource, fields

api = Namespace('dogs', description='Dogs related operations',)

dog = api.model('Dog', {
    'id': fields.String(required=True, description='The dog identifier'),
    'name': fields.String(required=True, description='The dog name'),
})

DOGS = [
    {'id': 'baldur', 'name': 'Baldur'},
]

@api.route('/')
class DogList(Resource):
    @api.doc('list_dogs')
    @api.marshal_list_with(dog)
    def options(self):
        '''List all dogs'''
        return DOGS

@api.route('/<id>')
@api.param('id', 'The dog identifier')
@api.response(404, 'Dog not found')
class Dog(Resource):
    @api.doc('get_cat')
    @api.marshal_with(dog)
    def options(self, id):
        '''Fetch a cat given its identifier'''
        for dog in DOGS:
            if dog['id'] == id:
                return dog
        api.abort(404)