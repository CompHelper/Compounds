from datetime import datetime

from . import db


class Compound(db.Model):
    __tablename__ = 'compound_basic'

    class STATUS:
        ENABLE = 1
        DISABLE = 0

    id = db.Column('compound_id', db.Integer, primary_key=True, doc='化合物ID')
    cas = db.Column(db.String(20), unique=True, doc='CAS')
    cname = db.Column('chinese_name', db.String(255), doc='中文名字')
    ename = db.Column('english_name', db.String(255), doc='英文名字')
    Mf = db.Column('Molecular_formula', db.String(255), doc='分子式')
    Mw = db.Column('Molecular_weight', db.String(255), doc='分子量')
    photo = db.Column('Structural_formula', db.String(128), doc='头像')
    status = db.Column(db.Integer, default=1, doc='状态，是否可用')
    create_time = db.Column(db.DateTime, default=datetime.now, doc='创建时间')
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, doc='更新时间')


class CompoundProfile(db.Model):
    __tablename__ = 'compound_profile'

    id = db.Column('compound_id', db.Integer, primary_key=True, doc='化合物ID')
    Mp = db.Column('Melting_point', db.String(20), unique=True, doc='熔点')
    Bp = db.Column('Boiling_point', db.String(20), doc='沸点')
    density = db.Column(db.String(20), doc='密度')
    Ri = db.Column('Refractive_index', db.String(50), doc='折射率')
    Fp = db.Column('Flash_point', db.String(20), doc='闪点')
    Sd = db.Column('Steam_density', db.String(128), doc='蒸汽密度')
    Sc = db.Column('Storage_conditions', db.String(128), doc='存储条件')
    form = db.Column(db.String(128), doc='形态')
    color = db.Column(db.String(128), doc='颜色')
    Solubility = db.Column('Solubility', db.String(128), doc='溶解性')
    Sensitivity = db.Column('Sensitivity', db.String(128), doc='敏感性')
    Sp = db.Column('Special_properties', db.String(128), doc='特殊性质')
    create_time = db.Column(db.DateTime, default=datetime.now, doc='创建时间')
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, doc='更新时间')
