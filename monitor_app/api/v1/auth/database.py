"""
This file sets up the database connection for the application 
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from monitor_app.core.config import get_setting 

setting = get_setting()

SQLALCHEMY_DATABASE_URL = (
    f"mysql+pymysql://{setting.db_user}:{setting.db_password}"
    f"@{setting.db_host}:{setting.db_port}/{setting.db_name}"
)
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
