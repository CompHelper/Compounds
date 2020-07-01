from flask import Blueprint
from flask_restful import Api

from utils.output import output_json
from . import compound

compound_bp = Blueprint('compound', __name__)
compound_api = Api(compound_bp, catch_all_404s=True)
compound_api.representation('application/json')(output_json)

compound_api.add_resource(compound.CompoundBasic, '/v1_0/compound',
                          endpoint='compound')
compound_api.add_resource(compound.UploadPhoto, '/v1_0/upload',
                          endpoint='photo')
