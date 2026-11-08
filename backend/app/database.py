from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.config import get_settings


class Base(DeclarativeBase):
    pass


settings = get_settings()


engine: Engine = create_engine(
    settings.database_url,
    echo=settings.debug,
    pool_pre_ping=True,
)


SessionLocal = sessionmaker[Session](
    bind=engine,
    expire_on_commit=False,
)


def get_session() -> Generator[Session, None, None]:
    with SessionLocal() as session:
        yield session


def init_database() -> None:
    Base.metadata.create_all(bind=engine)