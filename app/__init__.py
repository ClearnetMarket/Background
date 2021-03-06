from flask import Flask
from flask_sqlalchemy import SQLAlchemy


from flask_mail import Mail
from config import ConfigMain

app = Flask(__name__)
app.config.from_object('ConfigMain')
app.config['SQLALCHEMY_DATABASE_URI'] = ConfigMain.SQLALCHEMY_DATABASE_URI_0
UPLOADED_FILES_DEST_ITEM = ConfigMain.UPLOADED_FILES_DEST_ITEM
UPLOADED_FILES_DEST_USER = ConfigMain.UPLOADED_FILES_DEST_USER


db = SQLAlchemy(app)
mail = Mail(app)



