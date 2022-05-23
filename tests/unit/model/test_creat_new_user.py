from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from tests.util import get_unique_email

def test_create_new_user(app):
    email = get_unique_email()
    password = '123'

    from flaskr.model.user import User

    session = UnifiedAlchemyMagicMock()
    user = User(email=email, password=password)
    session.add(user)
    session.commit()
    result = session.query(User).first()

    assert result == user