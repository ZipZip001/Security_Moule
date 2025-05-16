from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from .routes import battle_bp
    app.register_blueprint(battle_bp)

    return app