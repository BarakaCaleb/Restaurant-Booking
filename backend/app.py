from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object('instance.config.Config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

from routes import *

if __name__ == '__main__':
    app.run(debug=True)

