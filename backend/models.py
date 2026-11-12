from sqlalchemy import Column, Integer, String, Text
from database import Base

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    ingredients = Column(Text)
    steps = Column(Text)
    country = Column(String, index=True)
    dish_type = Column(String, index=True)   # entrée, plat, dessert
    diet = Column(String, index=True)        # végétarien, sans gluten...