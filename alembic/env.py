from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from uvicorn import Config
import sys
from os.path import dirname, abspath
from config import settings
from database import Base
from feature.models import Base as FeatureBase
from campus.models import Base as CampusBase


# Add the path to the directory where config.py is located
sys.path.insert(0, dirname(dirname(abspath(__file__))))

# Import the DATABASE_URL from config.py

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
target_metadata = FeatureBase.metadata
target_metadata = CampusBase.metadata
config = context.config

# Interpret the config file for Python logging.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Set the database URL directly from config.py

db_url_escaped = settings.DATABASE_URL.replace('%', '%%')
config.set_main_option('sqlalchemy.url',db_url_escaped)


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()


