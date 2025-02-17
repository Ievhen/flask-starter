from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .models import BaseModel


db: SQLAlchemy = SQLAlchemy(model_class=BaseModel)

migrate: Migrate = Migrate()
