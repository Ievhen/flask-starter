from sqlalchemy import select
from werkzeug.security import generate_password_hash

from ..extensions import db
from ..models import User
from ..schemes import UserSchema


__all__ = [
    'select_user_by_id',
    'insert_user'
]


def select_user_by_id(user_id:int) -> UserSchema | None:
    query = select(User).where(User.id == user_id)
    result = db.session.execute(query).scalar_one_or_none()
    if result is not None:
        return UserSchema.model_validate(result)
    else:
        return None


def insert_user(user: UserSchema):
    db.session.add(
        User(login=user.login, password=generate_password_hash(user.password))
    )
    db.session.commit()
