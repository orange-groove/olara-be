from flask import Blueprint, jsonify

pricing_bp = Blueprint('pricing_bp', __name__)

@pricing_bp.route('/pricing', methods=['GET'])
def pricing():
    return jsonify({
        "message": "Success",
    }), 200
