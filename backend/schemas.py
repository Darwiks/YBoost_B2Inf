from pydantic import BaseModel

class RecipeCreate(BaseModel):
    name: str
    ingredients: str
    steps: str
    country: str
    dish_type: str
    diet: str | None = None

class RecipeOut(RecipeCreate):
    id: int

    class Config:
        from_attributes = True