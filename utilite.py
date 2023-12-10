from typing import List, Union
from models.users import User

def get_user_by_id(id: int, users: List[User]) -> Union[User, None]:
    for user in users:
        if user.id == id:
            return user
    return None