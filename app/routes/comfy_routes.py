from flask import Blueprint, jsonify, request, send_file
from app.auth.check_session import verify_user
import app.service.getComfyImage as getComfyImage


bp = Blueprint('my_routes', __name__)

@bp.route('/comfy/getImage', methods=['POST'])
def getImage():
    parameter_list = request.get_json()['parameter']
    parameter = ','.join(parameter_list)
    image = getComfyImage.run(parameter)
    if image == None:
        return "Image Generation Failed", 400
    print("resresres")
    return send_file(image, mimetype='image/png')

    
    
    
        