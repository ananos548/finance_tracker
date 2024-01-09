from pydantic import BaseModel


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
    user_id: int
