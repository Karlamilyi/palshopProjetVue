from flask import Blueprint

routes_blueprint = Blueprint("routes", __name__)

from .catalogRoutes import catalogRoutes
from .homeRoutes import homeRoutes

routes_blueprint.register_blueprint(catalogRoutes)
routes_blueprint.register_blueprint(homeRoutes)