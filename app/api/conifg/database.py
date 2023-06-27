from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://platzi:platzi@localhost:5432/tarifa_inteligente")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)