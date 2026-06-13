from pydantic import BaseModel

class Task_schema(BaseModel):
    title : str
    description : str
    is_completed : bool = False

class TaskResponseSchema(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool
    user_id : int | None = 0