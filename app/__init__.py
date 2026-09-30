from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register Blueprints here
    # app.register_blueprint(hello_world_bp)

    return app