import os

from flask import Flask
from todoapp.database import init_app
from todoapp.routes import todo_route
from todoapp.routes import auth_route


def create_app():

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='VeryStrongKey',
        DATABASE=os.path.join(app.instance_path, 'todoapp.sqlite')
    )
    
    os.makedirs(app.instance_path, exist_ok=True)

    init_app(app)
    app.register_blueprint(auth_route.bp)
    app.register_blueprint(todo_route.bp)
    app.add_url_rule("/", view_func=auth_route.register)

    return app