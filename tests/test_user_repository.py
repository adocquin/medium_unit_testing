import pytest
from unittest.mock import create_autospec
from sqlalchemy.orm import Session

from src.user_repository import UserRepository
from src.user import User


@pytest.fixture
def mock_session() -> Session:
    """Pytest fixture to create a mock Session instance."""
    session = create_autospec(Session)
    return session


def test_get_users(mock_session: Session) -> None:
    """Test the get_users method of the UserRepository class."""
    # Create a fake user
    fake_user = User(id=1, name="Alice", age=28)

    # Mock the Session.query() method to return our fake user
    mock_session.query.return_value.all.return_value = [fake_user]

    # Create a UserRepository instance with the mocked session
    user_repository = UserRepository("postgresql://test:test@test/test")
    user_repository.session = mock_session

    # Call the get_users method
    users = user_repository.get_users()

    # Ensure that Session.query() was called with the correct argument
    mock_session.query.assert_called_with(User)

    # Assert that the method returned our fake user
    assert users == [fake_user]
