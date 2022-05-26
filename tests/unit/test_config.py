def test_default_config():
    from flaskr.config import Default

    assert Default.DEBUG == False
    assert Default.TESTING == False
    assert Default.SQLALCHEMY_TRACK_MODIFICATIONS == False


def test_production_config():
    from flaskr.config import Production
    assert Production.SECRET_KEY
    assert Production.JWT_SECRET_KEY
    assert hasattr(Production, 'SQLALCHEMY_DATABASE_URI')


def test_development_config():
    from flaskr.config import Development
    assert Development.DEBUG
    assert Development.SECRET_KEY == 'dev'
    assert Development.JWT_SECRET_KEY == 'dev'
    assert Development.SQLALCHEMY_DATABASE_URI
