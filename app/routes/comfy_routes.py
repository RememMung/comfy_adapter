from flask import Blueprint, jsonify, request, send_file
from app.auth.check_session import verify_user
import service.getComfyImage as getComfyImage


bp = Blueprint('my_routes', __name__)

@bp.route('/comfy/getImage', methods=['GET'])
def getImage():
    parameter = request.args.get('parameter', default=None, type=list)
    jsessionid = request.cookies.get('JSESSIONID')
    
    # Checking is Session validate
    if not jsessionid:
        return "Cookie Not Found", 400
    
    is_verified, user_data = verify_user(jsessionid)
    
    if not is_verified:
        return "Session Invalidate", 401
    
    
    # TODO run에 propmt 내용 추가후 JSON 변경
    image = getComfyImage.run()
    
    return send_file(image, mimetype='image/png')

    
    
    
        