import redis
from flask import current_app

def get_redis_connection():
    return redis.StrictRedis(
        host=current_app.config['REDIS_HOST'],
        port=current_app.config['REDIS_PORT'],
        db=current_app.config['REDIS_DB']
    )

def verify_user(jsessionid):
    r = get_redis_connection()
    user_data = r.get(jsessionid)
    if user_data:
        # 사용자가 인증된 경우
        return True, user_data.decode('utf-8')
    else:
        # 인증 실패
        return False, None