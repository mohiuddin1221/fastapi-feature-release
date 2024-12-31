from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from config import settings

# Database URL from settings
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

# Create engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={'sslmode': 'require'}  # Ensure SSL connection if required
)

# Use a single instance of MetaData
metadata = MetaData()

# Declarative Base for models
class Base(DeclarativeBase):
    metadata = metadata

# SessionLocal for creating database sessions
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Function to create all tables
def create_tables():
    Base.metadata.create_all(bind=engine)

# Dependency to provide database sessions
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
