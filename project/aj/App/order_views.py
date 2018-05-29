from datetime import datetime
from flask import Blueprint,render_template,request,session,jsonify

from App.models import Order, House
from utils import status_code
from utils.functions import is_login

order = Blueprint('order',__name__)


@order.route('/',methods=['POST'])
@is_login
def order_post():

    order_dict = request.form

    house_id = order_dict.get('house_id')
    start_time = datetime.strptime(order_dict.get('start_time'),'%Y-%m-%d')
    end_time = datetime.strptime(order_dict.get('end_time'),'%Y-%m-%d')

    if not all([house_id,start_time,end_time]):
        return jsonify(status_code.PARAMS_ERROR)

    if start_time > end_time:
        return jsonify(status_code)

    house = House.query.get(house_id)

    order = Order()
    order.user_id = session['user_id']
    order.house_id = house_id
    order.begin_date = start_time
    order.end_date = end_time
    order.house_price = house.price
    order.days = (end_time-start_time).days + 1
    order.amount = order.days * order.house_price

    try:
        order.add_update()
        return jsonify(code=status_code.OK)
    except:
        return jsonify(status_code.DATABASE_ERROR)


@order.route('/order/',methods=['GET'])
@is_login
def orders_get():

    return render_template('orders.html')

@order.route('/orders/',methods=['GET'])
@is_login
def my_orders():
    user_id = session['user_id']
    order_list = Order.query.filter(Order.user_id==user_id)
    order_dict_list = [order.to_dict() for order in order_list]

    return jsonify(code=status_code.OK,orders=order_dict_list)


@order.route('/lorders/',methods=['GET'])
@is_login
def lorders():

    return render_template('lorders.html')


@order.route('/mylorders/',methods=['GET'])
@is_login
def my_lorders():

    user_id = session['user_id']
    houses = House.query.filter(House.user_id==user_id)

    # 第一种
    house_ids = [house.id for house in houses]
    orders = Order.query.filter(Order.house_id.in_(house_ids)).order_by(Order.id.desc())

    # 第二种
    # order_list=[]
    # for house in houses:
    #     orders = house.orders
    #     order_list.append(orders)
    # order_dict_list = [order.to_dict() for order in order_list]

    order_dict_list = [order.to_dict() for order in orders]

    return jsonify(code=status_code.OK,orders=order_dict_list)


@order.route('/order/<int:id>/',methods=['PATCH'])
@is_login
def order_status(id):

    status = request.form.get('status')
    order = Order.query.get(id)
    order.status = status
    if status == 'REJECTED':
        comment = request.form.get('comment')
        order.comment = comment
    try:
        order.add_update()
        return jsonify(code=status_code.OK)
    except:
        return jsonify(status_code.DATABASE_ERROR)
