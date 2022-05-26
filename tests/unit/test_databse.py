import sqlalchemy

def test_database_init(app):
    from flaskr.database import init, Base, engine, db_session
    init(app)

    assert Base.__class__ == sqlalchemy.orm.decl_api.DeclarativeMeta
    assert engine.__class__ == sqlalchemy.engine.base.Engine
    assert db_session.__class__ == sqlalchemy.orm.scoping.scoped_session

def test_session_shutdown(app):
    from flaskr.database import init, shutdown_session, db_session
    init(app)
    shutdown_session()

    assert db_session()._is_clean()