from pydantic import BaseModel as BaseSchema
from pydantic import ConfigDict
from flask_login import UserMixin


class UserSchema(UserMixin, BaseSchema):
    model_config = ConfigDict(from_attributes=True)

    id: int | None = None
    login: str
    password: str
