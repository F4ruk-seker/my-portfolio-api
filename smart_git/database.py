from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from typing import NoReturn


Base = declarative_base()


class Dependency(Base):
    __tablename__ = 'dependencies'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    version = Column(String(20), default=0)
    as_a_name = Column(String(255), default=None, nullable=True)


# class Session:
#     def __init__(self):
#         self.__engine = create_engine('sqlite:///database.sqlite3')
#         self.__session = self.__open_session()
#
#     def __open_session(self):
#         self.__session = sessionmaker(bind=self.__engine)
#         return self.__session()
#
#     def __add__(self, other):
#         print('atm')
#         if type(other) is list:
#             self.__session.add_all(other)
#         else:
#             self.__session.add(other)
#         return self
#
#     def commit(self) -> NoReturn:
#         self.__session.commit()
#
#     def close(self) -> NoReturn:
#         self.__session.close()

def get_session():
    engine = create_engine('sqlite:///database.sqlite3')
    return sessionmaker(bind=engine)


'''

if __name__ == '__main__':
    session = Session()
    dependency = Dependency(name="ğars")
    session += dependency
    session.commit()
    session.close()

    # Create Table
    # Base.metadata.create_all(engine)

    # start session
    # Session = sessionmaker(bind=engine)

    # session = Session()

    # save
    # session.commit()

    # close session
    # session.close()

'''
