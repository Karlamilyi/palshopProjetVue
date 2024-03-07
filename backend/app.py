from flask import Flask
from middleware import configure_middlewares
from routes.catalogRoutes import catalogRoutes
from routes.homeRoutes import homeRoutes
from routes.loginRoutes import loginRoutes


app = Flask(__name__)

# Register middleware
configure_middlewares(app)


# Register routes
app.register_blueprint(catalogRoutes)
app.register_blueprint(homeRoutes)
app.register_blueprint(loginRoutes)


if __name__ == "__main__":
    app.run(debug=True)
