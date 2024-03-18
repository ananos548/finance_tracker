from pydantic import BaseModel


class CategorySchema(BaseModel):
    id: int
    title: str


class CategorySchemaAdd(BaseModel):
    title: str


class ExpenseSchema(BaseModel):
    id: int
    source: str
    amount: int
    category_id: int
    user_id: int

    class Config:
        from_attributes = True


class ExpenseSchemaAdd(BaseModel):
    source: str
    amount: int
    category_id: int
