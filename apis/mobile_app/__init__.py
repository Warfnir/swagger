from flask import Blueprint
from flask_restplus import Api
from .staging import api as ns2

blueprint2 = Blueprint('blueprint2', __name__,static_folder='templates')

api2 = Api(blueprint2)
api2.add_namespace(ns2, path='/prefix/of/ns2')
