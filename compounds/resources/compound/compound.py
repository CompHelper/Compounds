from flask_restful import Resource
from flask import g, current_app
from sqlalchemy.exc import SQLAlchemyError
from flask_restful.reqparse import RequestParser

from models.compound import Compound, CompoundProfile
from models import db
from utils.oss import AliOss
from utils import parser


class CompoundBasic(Resource):

    def get(self):
        # 校验参数  查询参数
        jp = RequestParser()
        jp.add_argument('page', type=int, location='args', help='This parameter is missing')
        jp.add_argument('size', type=int, location='args', help='This parameter is missing')
        args = jp.parse_args()
        # 数据库 查询
        try:
            comp = Compound.query.filter(Compound.status == 1).paginate(args.page, args.size)
            # 返回结果
            data = []
            for item in comp.items:
                ret = {}
                ret['id'] = item.id
                ret['cas'] = item.cas
                ret['chinese_name'] = item.cname
                ret['english_name'] = item.ename
                ret['Molecular_formula'] = item.Mf
                ret['Molecular_weight'] = item.Mw
                ret['Structural_formula'] = current_app.config['BASE_IMAGE_URL'] + item.photo if item.photo else None
                data.append(ret)
            return data, 200
        except SQLAlchemyError as e:
            current_app.logger.error(e)
            return {'message': 'Select Compound Failure'}, 400

    def post(self):
        # 1 校验参数
        jp = RequestParser()
        jp.add_argument('cas', type=str, required=True, location='json', help='This parameter is missing')
        jp.add_argument('chinese_name', type=str, required=True, location='json', help='This parameter is missing')
        jp.add_argument('english_name', type=str, required=True, location='json', help='This parameter is missing')
        jp.add_argument('Molecular_formula', type=str, required=True, location='json',
                        help='This parameter is missing')
        jp.add_argument('Molecular_weight', type=str, required=True, location='json', help='This parameter is missing')
        args = jp.parse_args()

        try:
            comp = Compound.query.filter_by(cas=args.cas).first()
            if comp:
                return {'message': 'This compound already exists'}, 400
        except SQLAlchemyError as e:
            current_app.logger.error(e)
            return {'message': 'Database query failed'}, 400
        id = current_app.id_worker.get_id()
        try:
            comp = Compound(id=id, cas=args.cas, cname=args.chinese_name, ename=args.english_name,
                            Mf=args.Molecular_formula, Mw=args.Molecular_weight)
            db.session.add(comp)
            db.session.commit()
            return None, 200
        except SQLAlchemyError as e:
            current_app.logger.error(e)
            db.session.rollback()
            return {'message': 'Compound Add Failure'}, 400

    def put(self):
        # 1 校验参数
        jp = RequestParser()
        jp.add_argument('id', type=int, required=True, location='json', help='This parameter is missing')
        jp.add_argument('cas', type=str, required=False, location='json', help='This parameter is missing')
        jp.add_argument('chinese_name', type=str, required=False, location='json', help='This parameter is missing')
        jp.add_argument('english_name', type=str, required=False, location='json', help='This parameter is missing')
        jp.add_argument('Molecular_formula', type=str, required=False, location='json',
                        help='This parameter is missing')
        jp.add_argument('Molecular_weight', type=str, required=False, location='json', help='This parameter is missing')
        args = jp.parse_args()
        try:
            comp = Compound.query.filter_by(id=args.id).first()
            if args.cas:
                comp.cas = args.cas
            if args.chinese_name:
                comp.cname = args.args.chinese_name
            if args.english_name:
                comp.ename = args.english_name
            if args.Molecular_formula:
                comp.Mf = args.Molecular_formula
            if args.Molecular_weight:
                comp.Mw = args.Molecular_weight
            db.session.add(comp)
            db.session.commit()
            return None, 200
        except SQLAlchemyError as e:
            current_app.logger.error(e)
            return {'message': 'Compound Update Failure'}, 400

    def delete(self):
        jp = RequestParser()
        jp.add_argument('id', type=int, required=True, location='json', help='This parameter is missing')
        args = jp.parse_args()

        try:
            comp = Compound.query.filter_by(id=args.id).first()
            comp.status = 0
            db.session.add(comp)
            db.session.commit()
            return None, 200
        except:
            return {'message': 'Compound Delete Failure'}, 400


class CompoundProfile(Resource):

    def get(self):
        jp = RequestParser()
        jp.add_argument('id', type=int, required=True, location='json', help='This parameter is missing')
        args = jp.parse_args()
        try:
            comps = CompoundProfile().query.filter_by(id=args.id).first()
            # 返回结果
            ret = {}
            ret['Melting_point'] = comps.Mp
            ret['Boiling_point'] = comps.Bp
            ret['density'] = comps.density
            ret['Refractive_index'] = comps.Ri
            ret['Flash_point'] = comps.Fp
            ret['Steam_density'] = comps.Sd
            ret['Storage_conditions'] = comps.Sc
            ret['form'] = comps.form
            ret['color'] = comps.color
            ret['Solubility'] = comps.Solubility
            ret['Sensitivity'] = comps.Sensitivity
            ret['Special_properties'] = comps.Sp
            return ret, 200
        except SQLAlchemyError as e:
            current_app.logger.error(e)
            return {'message': 'Select Compound Failure'}, 400

    def post(self):
        jp = RequestParser()
        jp.add_argument('id', type=int, required=False, location='json', help='This parameter is missing')
        jp.add_argument('Melting_point', type=str, required=False, location='json', help='This parameter is missing')
        jp.add_argument('Boiling_point', type=str, required=False, location='json', help='This parameter is missing')
        jp.add_argument('density', type=str, required=False, location='json', help='This parameter is missing')
        jp.add_argument('Refractive_index', type=str, required=False, location='json',
                        help='This parameter is missing')
        jp.add_argument('Flash_point', type=str, required=False, location='json', help='This parameter is missing')
        jp.add_argument('Steam_density', type=str, required=False, location='json', help='This parameter is missing')
        jp.add_argument('Storage_conditions', type=str, required=False, location='json',
                        help='This parameter is missing')
        jp.add_argument('form', type=str, required=False, location='json',
                        help='This parameter is missing')
        jp.add_argument('color', type=str, required=False, location='json', help='This parameter is missing')
        jp.add_argument('Solubility', type=str, required=False, location='json',
                        help='This parameter is missing')
        jp.add_argument('Sensitivity', type=str, required=False, location='json',
                        help='This parameter is missing')
        jp.add_argument('Special_properties', type=str, required=False, location='json',
                        help='This parameter is missing')
        args = jp.parse_args()

        try:
            comps = CompoundProfile(id=args.id, Mp=args.Melting_point, Bp=args.Boiling_point, density=args.density,
                                    Ri=args.Refractive_index, Fp=args.Flash_point, Sd=args.Steam_density,
                                    Sc=args.Storage_conditions,
                                    form=args.form, color=args.color, Solubility=args.Solubility,
                                    Sensitivity=args.Sensitivity, Sp=args.Special_properties)
            db.session.add(comps)
            db.session.commit()
            return None, 200

        except SQLAlchemyError as e:
            current_app.logger.error(e)
            db.session.rollback()
            return {'message': 'CompoundPorfile Add Failure'}, 400


class UploadPhoto(Resource):

    def patch(self):
        rp = RequestParser()
        rp.add_argument('id', type=int, required=True, location='form', help='This parameter is missing')
        rp.add_argument('photo', type=parser.image, required=True, location='files')  # request.files.get('photo')
        args = rp.parse_args()
        image_file, file_type = args.photo
        image_data = image_file.read()
        url, path = AliOss().upload(image_data, file_type)

        try:
            comp = Compound.query.filter_by(id=args.id).first()
            comp.photo = path
            db.session.add(comp)
            db.session.commit()
            return url, 200
        except:
            return {'message': 'Image Upload Failed'}, 400
