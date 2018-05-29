OK = 200
SUCCESS = {'code':200,'msg':'请求成功'}
DATABASE_ERROR = {'code':900,'msg':'数据库请求失败'}
PARAMS_ERROR = {'code':901,'msg':'参数错误'}

# 用户模块
USER_REGISTER_PARAMS_ERROR = {'code':1000,'msg':'注册信息参数错误'}
USER_REGISTER_MOBLIE_ERROR = {'code':1001,'msg':'注册手机号码不符合规则'}
USER_REGISTER_MOBLIE_IS_EXSITS = {'code':1002,'msg':'注册手机号码已注册'}
USER_REGISTER_PASSWORD_IS_ERROR = {'code':1003,'msg':'注册密码不一致'}
USER_LOGIN_IS_NOT_EXSIST = {'code':1004,'msg':'用户不存在'}
USER_LOGIN_PASSWORD_IS_ERROR = {'code':1005,'msg':'用户密码错误'}

USER_UPLOAD_IMAGE_IS_ERROR = {'code':1006,'msg':'上传图片不符合标准'}
USER_UPLOAD_NAME_IS_EXSITS = {'code':1007,'msg':'用户名已存在'}

USER_AUTH_ID_CART_ERROR = {'code':1008,'msg':'身份证号不符合规则'}

# 房屋模块
MYHOUSE_USER_IS_NOT_AUTH = {'code':2000,'msg':'用户没有实名认证'}

# 订单模块
ORDER_START_TIME_GT_END_TIME = {'code':2001,'msg':'开始时间大于结束时间'}