from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:1939Enigma**#@localhost:5432/Modelo_RN")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)