import os
import re

from flask import Blueprint, redirect, render_template, jsonify, session, request
from sqlalchemy.sql.elements import or_

from App.models import User, House, Area, Facility, HouseImage, Order
from utils import status_code
from utils.functions import is_login
from utils.settings import UPLOAD_DIRS
from App.models import db
house = Blueprint('house',__name__)

@house.route('/myhouse/',methods=['GET'])
def myhouse():
    return render_template('myhouse.html')


'''
获取房源信息
'''
@house.route('/auth_myhouse/',methods=['GET'])
@is_login
def auth_myhouse():

    user = User.query.get(session['user_id'])
    if user.id_card:
        houses = House.query.filter(House.user_id==user.id).order_by(House.id.desc())
        hlist_list = []
        for house in houses:
            hlist_list.append(house.to_dict())
        return jsonify(hlist_list=hlist_list,code=status_code.OK)
    else:
        return jsonify(status_code.MYHOUSE_USER_IS_NOT_AUTH)


@house.route('/newhouse/',methods=['GET'])
@is_login
def newhouse():
    return render_template('newhouse.html')


@house.route('/area_facility/',methods=['GET'])
def area_facility():
    areas = Area.query.all()
    area_list = [area.to_dict() for area in areas]

    facilitys = Facility.query.all()
    facility_list = [facility.to_dict() for facility in facilitys]

    return jsonify(area_list=area_list,facility_list=facility_list)


'''
提交房屋信息
'''
@house.route('/newhouse/',methods=['POST'])
@is_login
def newhouse_post():
    house_dict = request.form.to_dict()
    facility_ids = request.form.getlist('facility')

    house = House()
    house.title = house_dict.get('title')
    house.price = house_dict.get('price')
    house.area_id = house_dict.get('area_id')
    house.address = house_dict.get('address')
    house.room_count = house_dict.get('room_count')
    house.acreage = house_dict.get('acreage')
    house.unit = house_dict.get('unit')
    house.capacity = house_dict.get('capacity')
    house.beds = house_dict.get('beds')
    house.deposit = house_dict.get('deposit')
    house.min_days = house_dict.get('min_days')
    house.max_days = house_dict.get('max_days')
    house.user_id = session['user_id']
    if facility_ids:
        facilitys = Facility.query.filter(Facility.id.in_(facility_ids)).all()
        house.facilities = facilitys
    try:
        house.add_update()
        return jsonify(code=status_code.OK,house_id=house.id)
    except:
        return jsonify(status_code.DATABASE_ERROR)


'''
上传房屋图片
'''
@house.route('/newhouse_img/',methods=['POST'])
@is_login
def newhouse_post_img():
    file_dict = request.files
    if 'house_image' in file_dict:
        image = file_dict.get('house_image')
        house_id = request.form.get('house_id')

        if not re.match(r'^image/.*$',image.mimetype):
            return jsonify(status_code.USER_UPLOAD_IMAGE_IS_ERROR)

        url = os.path.join(UPLOAD_DIRS,image.filename)
        image.save(url)

        house = House.query.get(house_id)
        image_url = os.path.join('/static/upload',image.filename)
        if not house.index_image_url:
            house.index_image_url = image_url
        houseimage = HouseImage()
        houseimage.url = image_url
        houseimage.house_id = house_id
        try:
            houseimage.add_update()
            house.add_update()
            return jsonify(code=status_code.OK,url=image_url)
        except Exception as e:
            return jsonify(status_code.DATABASE_ERROR)

    else:
        return jsonify(status_code.PARAMS_ERROR)


@house.route('/detail/',methods=['GET'])
def detail():
    return render_template('detail.html')


@house.route('/detail/<int:id>/',methods=['GET'])
def house_detail(id):
    house = House.query.get(id)

    facility_list = house.facilities
    facility_dict_list = [facility.to_dict() for facility in facility_list]

    booking = 1
    if 'user_id' in session:
        booking = 2
        if house.user_id == session['user_id']:
            booking = 0

    return jsonify(house=house.to_full_dict(),
                   facility_list=facility_dict_list,
                    booking=booking,
                   code=status_code.OK)


@house.route('/booking/',methods=['GET'])
@is_login
def booking():
    return render_template('booking.html')


@house.route('/index/',methods=['GET'])
def hello():
    return render_template('index.html')


@house.route('/hindex/',methods=['GET'])
def index():
    areas = Area.query.all()
    area_list = [area.to_dict() for area in areas]

    houses = House.query.order_by(House.id.desc()).all()[:5]
    house_list = [house.to_dict() for house in houses]

    user_name = ''
    if 'user_id' in session:
        user= User.query.get(session['user_id'])
        user_name = user.name

    return jsonify(code=status_code.OK,areas=area_list,house_list=house_list,user_name=user_name)


@house.route('/search/',methods=['GET'])
def search():
    return render_template('search.html')


@house.route('/allsearch/',methods=['GET'])
def search_house():
    search_dict = request.args

    area_id = search_dict.get('aid')
    start_data = search_dict.get('sd')
    end_data = search_dict.get('ed')
    sort_key = search_dict.get('sk')

    area_name = Area.query.get(area_id).name if area_id else '位置区域'
    sk = '最新上线'
    house = House.query.filter(House.area_id==area_id) if area_id else  House.query.filter()

    orders1 = Order.query.filter(Order.begin_date>=start_data,Order.end_date<=end_data)
    orders2 = Order.query.filter(Order.begin_date<=end_data,Order.end_date>=end_data)
    orders3 = Order.query.filter(Order.begin_date<=start_data,Order.end_date>=start_data)
    orders4 = Order.query.filter(Order.begin_date<=start_data,Order.end_date>=end_data)
    order_list1 = [o1.house_id for o1 in orders1]
    order_list2 = [o2.house_id for o2 in orders2]
    order_list3 = [o3.house_id for o3 in orders3]
    order_list4 = [o4.house_id for o4 in orders4]
    orders_list = order_list1+order_list2+order_list3+order_list4
    orders_list = list(set(orders_list))
    # orders = Order.query.filter(or_(Order.begin_date<=end_data,Order.end_date>=start_data))

    order_list = [order for order in orders_list]

    houses = house.filter(House.id.notin_(order_list))

    if sort_key:
        if sort_key == 'booking':
            sort_key = House.room_count.desc()
            sk = '入住最多'
        if sort_key == 'price-inc':
            sort_key = House.price.asc()
            sk = '价格 低-高'
        if sort_key == 'price-des':
            sort_key = House.price.desc()
            sk = '价格 高-低'
        if sort_key == 'new':
            sort_key = House.id.desc()
    else:
        sort_key = House.id.desc()

    houses = houses.order_by(sort_key)
    house_dict_list = [house.to_full_dict() for house in houses]

    areas = Area.query.all()
    area_list = [area.to_dict() for area in areas]

    return jsonify(code=status_code.OK,house_list=house_dict_list,area_list=area_list,aname=area_name,sk=sk)


