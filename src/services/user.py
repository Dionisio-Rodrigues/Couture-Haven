from src.models.user import User
from src.models.dao import BaseDAO

base_dao = BaseDAO(User)

get_user_by_username = lambda username: base_dao.get_by(conditions={"username": username})
save_user = lambda user: (
    base_dao.save(instance=user) or user
    if not (
            base_dao.get_by(conditions={"username": user.username}, exception_id=user.id) and
            base_dao.get_by(conditions={"username": user.username}, exception_id=user.id).first()
    )
    else None
)
