from flask import Flask, render_template
from dotenv import load_dotenv
import os
from models import db

load_dotenv()

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_default_secret_key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///site.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

from routes.auth import auth_bp
app.register_blueprint(auth_bp)


if __name__ == '__main__':
    app.run(debug=True)