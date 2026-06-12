from pydantic import BaseModel

class Task_schema(BaseModel):
    title : str
    description : str
    is_completed : bool = False