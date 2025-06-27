from services.config import AppSettings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

settings = AppSettings()

engine = create_engine(
    settings.dburl
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()