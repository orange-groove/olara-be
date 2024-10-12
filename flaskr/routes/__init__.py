from flask import Blueprint
from flaskr.routes.pricing import pricing_bp

routes_bp = Blueprint('api/v1', __name__)

routes_bp.register_blueprint(pricing_bp)
