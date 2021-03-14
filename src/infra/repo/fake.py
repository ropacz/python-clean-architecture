from src.infra.config import DbConnectionHandler
from src.infra.entities import Users


class FakerRepo:
    """ A simple Repository """

    @classmethod
    def insert_user(cls):
        """ Something """
        with DbConnectionHandler() as db_connection:
            try:
                new_user = Users(name="Programador", password="Rodrigo")
                db_connection.session.add(new_user)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
