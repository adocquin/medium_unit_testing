from src.math_utils import divide
from src.user import User
from src.user_repository import UserRepository


if __name__ == "__main__":
    print(divide(1, 2))
    user_repository: UserRepository = UserRepository(
        "postgresql://postgres:postgres@localhost/postgres"
    )
    users: list[User] = user_repository.get_users()
    for user in users:
        print(user.greet())
