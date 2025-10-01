from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from app.config import config


DATABASE_URL = URL.create(
    drivername='postgresql+psycopg2',
    host=config.DB_HOST,
    port=config.DB_PORT,
    username=config.DB_USER,
    password=config.DB_PASS,
    database=config.DB_NAME,
)

engine = create_engine(DATABASE_URL)
LocalSession = sessionmaker(bind=engine)
Base = declarative_base()


def initial_db():
    from app.models.user import User
    from app.models.post import Post
    from app.models.comment import Comment

    Base.metadata.create_all(engine)
