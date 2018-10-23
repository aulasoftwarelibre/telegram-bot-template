from application import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

# Add new tables here
from model import chat

# Last line
db.create_all()
