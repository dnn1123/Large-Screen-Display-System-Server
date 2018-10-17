#coding=utf-8
from flask import Blueprint, jsonify,request
from . import response
import sys
from webapp.models import p_city_manager,db

reload(sys)
sys.setdefaultencoding('utf8')

c_manager_blueprint = Blueprint(
    'c_manager',
    __name__,
    url_prefix="/c_manager"
)

@c_manager_blueprint.route('/get_by_city',methods=('GET', 'POST'))
def num_by_city():
    data=db.session.query(p_city_manager.City,db.func.count('*').label("dcount")).group_by(p_city_manager.City).all()
    city_list = []
    value_list = []
    for i in data:
        city_list.append(i[0])
        value_list.append(i[1])
    return response(jsonify({"property": "p_manager_distribution_by_major_city","city_list": city_list,
                             "value_list": value_list}))


@c_manager_blueprint.route('/get_by_edu_city',methods=('GET', 'POST'))
def num_by_education_city():
    city = request.args.get('city')
    if city == 'null':
        data = db.session.query(p_city_manager.Education, db.func.count('*').label("dcount")).group_by(p_city_manager.Education).all()
    else:
        data = db.session.query(p_city_manager.Education, db.func.count('*').label("dcount")).filter(
            p_city_manager.City == city).group_by(
            p_city_manager.Education).all()
    education_list = []
    value_list = []
    for i in data:
        education_list.append(i[0])
        value_list.append(i[1])
    return response(jsonify({"property": "p_manager_distribution_by_major_city", "city": city, "education_list": education_list,"value_list":value_list}))


