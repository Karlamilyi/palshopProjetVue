from flask import Flask
from middleware import configure_middlewares
from error import configure_error_handlers
from routes.catalogRoutes import catalogRoutes
from routes.homeRoutes import homeRoutes
from routes.loginRoutes import loginRoutes


app = Flask(__name__)

# Initialize database connection

# Register middleware
configure_middlewares(app)

# Register error handlers
configure_error_handlers(app)


# Register routes
app.register_blueprint(catalogRoutes)
app.register_blueprint(homeRoutes)
app.register_blueprint(loginRoutes)


if __name__ == "__main__":
    app.run(debug=True)
